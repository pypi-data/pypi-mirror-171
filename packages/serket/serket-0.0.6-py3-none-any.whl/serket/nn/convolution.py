# this script defines different convolutional layers
# https://arxiv.org/pdf/1603.07285.pdf
# Throughout the code, we use OIHW  as the default data format for kernels. and NCHW for data.

from __future__ import annotations

import functools as ft
import operator as op
from typing import Callable

import jax
import jax.numpy as jnp
import jax.random as jr
import pytreeclass as pytc
from jax.lax import ConvDimensionNumbers

from .utils import (
    _calculate_convolution_output_shape,
    _check_and_return_init_func,
    _check_and_return_input_dilation,
    _check_and_return_input_size,
    _check_and_return_kernel,
    _check_and_return_kernel_dilation,
    _check_and_return_padding,
    _check_and_return_strides,
    _transpose_padding,
)

# ------------------------------ Convolutional Layers ------------------------------ #


@pytc.treeclass
class ConvND:
    weight: jnp.ndarray
    bias: jnp.ndarray

    in_features: int = pytc.nondiff_field()
    out_features: int = pytc.nondiff_field()
    kernel_size: int | tuple[int, ...] = pytc.nondiff_field()
    strides: int | tuple[int, ...] = pytc.nondiff_field()
    padding: str | int | tuple[int, ...] | tuple[tuple[int, int], ...] = pytc.nondiff_field()  # fmt: skip
    input_dilation: int | tuple[int, ...] = pytc.nondiff_field()
    kernel_dilation: int | tuple[int, ...] = pytc.nondiff_field()
    weight_init_func: str | Callable[[jr.PRNGKey, tuple[int, ...]], jnp.ndarray]
    bias_init_func: str | Callable[[jr.PRNGKey, tuple[int]], jnp.ndarray]
    groups: int = pytc.nondiff_field()

    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        strides=1,
        padding="SAME",
        input_dilation=1,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        groups=1,
        ndim=2,
        key=jr.PRNGKey(0),
    ):
        """Convolutional layer.

        Args:
            in_features: number of input features
            out_features: number of output features
            kernel_size: size of the convolutional kernel
            strides: stride of the convolution
            padding: padding of the input
            input_dilation: dilation of the input
            kernel_dilation: dilation of the convolutional kernel
            weight_init_func: function to use for initializing the weights
            bias_init_func: function to use for initializing the bias
            groups: number of groups to use for grouped convolution
            ndim: number of dimensions of the convolution
            key: key to use for initializing the weights

        See: https://jax.readthedocs.io/en/latest/_autosummary/jax.lax.conv.html
        """
        if not isinstance(in_features, int) or in_features <= 0:
            raise ValueError(
                f"Expected `in_features` to be a positive integer, got {in_features}"
            )

        if not isinstance(out_features, int) or out_features <= 0:
            raise ValueError(
                f"Expected `out_features` to be a positive integer, got {out_features}"
            )

        if not isinstance(groups, int) or groups <= 0:
            raise ValueError(f"Expected groups to be a positive integer, got {groups}")

        assert (
            out_features % groups == 0
        ), f"Expected out_features % groups == 0, got {out_features % groups}"

        self.in_features = in_features
        self.out_features = out_features
        self.groups = groups

        self.kernel_size = _check_and_return_kernel(kernel_size, ndim)
        self.strides = _check_and_return_strides(strides, ndim)
        self.input_dilation = _check_and_return_input_dilation(input_dilation, ndim)
        self.kernel_dilation = _check_and_return_kernel_dilation(kernel_dilation, ndim)
        self.padding = _check_and_return_padding(padding, self.kernel_size)
        self.weight_init_func = _check_and_return_init_func(weight_init_func, "weight_init_func")  # fmt: skip
        self.bias_init_func = _check_and_return_init_func(bias_init_func, "bias_init_func")  # fmt: skip

        weight_shape = (out_features, in_features // groups, *self.kernel_size)  # OIHW
        self.weight = self.weight_init_func(key, weight_shape)

        if bias_init_func is None:
            self.bias = None
        else:
            bias_shape = (out_features, *(1,) * ndim)
            self.bias = self.bias_init_func(key, bias_shape)

        self.dimension_numbers = ConvDimensionNumbers(*((tuple(range(ndim + 2)),) * 3))

    def __call__(self, x: jnp.ndarray, **kwargs) -> jnp.ndarray:
        y = jax.lax.conv_general_dilated(
            lhs=jnp.expand_dims(x, 0),
            rhs=self.weight,
            window_strides=self.strides,
            padding=self.padding,
            lhs_dilation=self.input_dilation,
            rhs_dilation=self.kernel_dilation,
            dimension_numbers=self.dimension_numbers,
            feature_group_count=self.groups,
        )

        if self.bias is None:
            return y[0]
        return (y + self.bias)[0]


@pytc.treeclass
class Conv1D(ConvND):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        strides=1,
        padding="SAME",
        input_dilation=1,
        kernel_dilation=1,
        weight_init_func=jax.nn.initializers.glorot_uniform(),
        bias_init_func=jax.nn.initializers.zeros,
        groups: int = 1,
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features=in_features,
            out_features=out_features,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            input_dilation=input_dilation,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            groups=groups,
            ndim=1,
            key=key,
        )


@pytc.treeclass
class Conv2D(ConvND):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        strides=1,
        padding="SAME",
        input_dilation=1,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        groups: int = 1,
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features=in_features,
            out_features=out_features,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            input_dilation=input_dilation,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            groups=groups,
            ndim=2,
            key=key,
        )


@pytc.treeclass
class Conv3D(ConvND):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        strides=1,
        padding="SAME",
        input_dilation=1,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        groups: int = 1,
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features=in_features,
            out_features=out_features,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            input_dilation=input_dilation,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            groups=groups,
            ndim=3,
            key=key,
        )


# ------------------------------ Transposed Convolutional Layers ------------------------------ #


@pytc.treeclass
class ConvNDTranspose:
    weight: jnp.ndarray
    bias: jnp.ndarray

    in_features: int = pytc.nondiff_field()
    out_features: int = pytc.nondiff_field()
    kernel_size: int | tuple[int, ...] = pytc.nondiff_field()
    padding: str | int | tuple[int, ...] | tuple[tuple[int, int], ...] = pytc.nondiff_field()  # fmt: skip
    output_padding: int | tuple[int, ...] = pytc.nondiff_field()
    strides: int | tuple[int, ...] = pytc.nondiff_field()
    kernel_dilation: int | tuple[int, ...] = pytc.nondiff_field()
    weight_init_func: str | Callable[[jr.PRNGKey, tuple[int, ...]], jnp.ndarray]
    bias_init_func: Callable[[jr.PRNGKey, tuple[int]], jnp.ndarray]
    groups: int = pytc.nondiff_field()

    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        strides=1,
        padding="SAME",
        output_padding=0,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        groups=1,
        ndim=2,
        key=jr.PRNGKey(0),
    ):
        """Convolutional Transpose Layer

        Args:
            in_features : Number of input channels
            out_features : Number of output channels
            kernel_size : Size of the convolutional kernel
            strides : Stride of the convolution
            padding : Padding of the input
            output_padding : Additional size added to one side of the output shape
            kernel_dilation : Dilation of the convolutional kernel
            weight_init_func : Weight initialization function
            bias_init_func : Bias initialization function
            groups : Number of groups
            ndim : Number of dimensions
            key : PRNG key
        """
        if not isinstance(in_features, int) or in_features <= 0:
            raise ValueError(
                f"Expected in_features to be a positive integer, got {in_features}"
            )

        if not isinstance(out_features, int) or out_features <= 0:
            raise ValueError(
                f"Expected out_features to be a positive integer, got {out_features}"
            )

        if not isinstance(groups, int) or groups <= 0:
            raise ValueError(f"Expected groups to be a positive integer, got {groups}")

        assert (
            out_features % groups == 0
        ), f"Expected out_features % groups == 0, got {out_features % groups}"

        self.in_features = in_features
        self.out_features = out_features
        self.groups = groups

        self.kernel_size = _check_and_return_kernel(kernel_size, ndim)
        self.strides = _check_and_return_strides(strides, ndim)
        self.kernel_dilation = _check_and_return_kernel_dilation(kernel_dilation, ndim)
        self.padding = _check_and_return_padding(padding, self.kernel_size)
        self.output_padding = _check_and_return_strides(output_padding, ndim)
        self.weight_init_func = _check_and_return_init_func(weight_init_func, "weight_init_func")  # fmt: skip
        self.bias_init_func = _check_and_return_init_func(bias_init_func, "bias_init_func")  # fmt: skip

        weight_shape = (out_features, in_features // groups, *self.kernel_size)  # OIHW
        self.weight = self.weight_init_func(key, weight_shape)

        if bias_init_func is None:
            self.bias = None
        else:
            bias_shape = (out_features, *(1,) * ndim)
            self.bias = self.bias_init_func(key, bias_shape)

        self.dimension_numbers = ConvDimensionNumbers(*((tuple(range(ndim + 2)),) * 3))

        self.transposed_padding = _transpose_padding(
            padding=self.padding,
            extra_padding=self.output_padding,
            kernel_size=self.kernel_size,
            input_dilation=self.kernel_dilation,
        )

    def __call__(self, x: jnp.ndarray, **kwargs) -> jnp.ndarray:
        y = jax.lax.conv_transpose(
            lhs=jnp.expand_dims(x, 0),
            rhs=self.weight,
            strides=self.strides,
            padding=self.transposed_padding,
            rhs_dilation=self.kernel_dilation,
            dimension_numbers=self.dimension_numbers,
        )

        if self.bias is None:
            return y[0]
        return (y + self.bias)[0]


@pytc.treeclass
class Conv1DTranspose(ConvNDTranspose):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        strides=1,
        padding="SAME",
        output_padding=0,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        groups=1,
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            strides=strides,
            padding=padding,
            output_padding=output_padding,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            groups=groups,
            ndim=1,
            key=key,
        )


@pytc.treeclass
class Conv2DTranspose(ConvNDTranspose):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        strides=1,
        padding="SAME",
        output_padding=0,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        groups=1,
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            strides=strides,
            padding=padding,
            output_padding=output_padding,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            groups=groups,
            ndim=2,
            key=key,
        )


@pytc.treeclass
class Conv3DTranspose(ConvNDTranspose):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        strides=1,
        padding="SAME",
        output_padding=0,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        groups=1,
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            strides=strides,
            padding=padding,
            output_padding=output_padding,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            groups=groups,
            ndim=3,
            key=key,
        )


# ------------------------------ Depthwise Convolutional Layers ------------------------------ #


@pytc.treeclass
class DepthwiseConvND:
    weight: jnp.ndarray
    bias: jnp.ndarray

    in_features: int = pytc.nondiff_field()  # number of input features
    kernel_size: int | tuple[int, ...] = pytc.nondiff_field()
    strides: int | tuple[int, ...] = pytc.nondiff_field()  # stride of the convolution
    padding: str | int | tuple[tuple[int, int], ...] = pytc.nondiff_field()

    weight_init_func: str | Callable[[jr.PRNGKey, tuple[int, ...]], jnp.ndarray]
    bias_init_func: str | Callable[[jr.PRNGKey, tuple[int]], jnp.ndarray]
    kernel_dilation: int | tuple[int, ...] = pytc.nondiff_field()

    def __init__(
        self,
        in_features,
        kernel_size,
        *,
        depth_multiplier=1,
        strides=1,
        padding="SAME",
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        ndim: int = 2,
        key: jr.PRNGKey = jr.PRNGKey(0),
    ):
        """Depthwise Convolutional layer.

        Args:
            in_features: number of input features
            kernel_size: size of the convolution kernel
            depth_multiplier : number of output channels per input channel
            strides: stride of the convolution
            padding: padding of the input
            weight_init_func: function to initialize the weights
            bias_init_func: function to initialize the bias
            ndim: number of spatial dimensions
            key: random key for weight initialization

        Examples:
            >>> l1 = DepthwiseConvND(3, 3, depth_multiplier=2, strides=2, padding="SAME")
            >>> l1(jnp.ones((3, 32, 32))).shape
            (3, 16, 16, 6)

        Note:
            See :
                https://keras.io/api/layers/convolution_layers/depthwise_convolution2d/
                https://github.com/google/flax/blob/main/flax/linen/linear.py
        """
        if not isinstance(in_features, int) or in_features <= 0:
            raise ValueError(
                f"Expected in_features to be a positive integer, got {in_features}"
            )

        if not isinstance(depth_multiplier, int) or depth_multiplier <= 0:
            raise ValueError(
                f"Expected depth_multiplier to be a positive integer, got {depth_multiplier}"
            )

        self.in_features = in_features
        self.depth_multiplier = depth_multiplier

        self.kernel_size = _check_and_return_kernel(kernel_size, ndim)
        self.strides = _check_and_return_strides(strides, ndim)
        self.input_dilation = _check_and_return_input_dilation(1, ndim)
        self.kernel_dilation = _check_and_return_kernel_dilation(1, ndim)
        self.padding = _check_and_return_padding(padding, self.kernel_size)
        self.weight_init_func = _check_and_return_init_func(weight_init_func, "weight_init_func")  # fmt: skip
        self.bias_init_func = _check_and_return_init_func(bias_init_func, "bias_init_func")  # fmt: skip

        weight_shape = (depth_multiplier * in_features, 1, *self.kernel_size)  # OIHW
        self.weight = self.weight_init_func(key, weight_shape)

        if bias_init_func is None:
            self.bias = None
        else:
            bias_shape = (depth_multiplier * in_features, *(1,) * ndim)
            self.bias = self.bias_init_func(key, bias_shape)

        self.dimension_numbers = ConvDimensionNumbers(*((tuple(range(ndim + 2)),) * 3))

    def __call__(self, x: jnp.ndarray, **kwargs) -> jnp.ndarray:
        y = jax.lax.conv_general_dilated(
            lhs=x[None],
            rhs=self.weight,
            window_strides=self.strides,
            padding=self.padding,
            lhs_dilation=self.input_dilation,
            rhs_dilation=self.kernel_dilation,
            dimension_numbers=self.dimension_numbers,
            feature_group_count=self.in_features,
        )

        if self.bias is None:
            return y[0]
        return (y + self.bias)[0]


@pytc.treeclass
class DepthwiseConv1D(DepthwiseConvND):
    def __init__(
        self,
        in_features,
        kernel_size,
        *,
        depth_multiplier=1,
        strides=1,
        padding="SAME",
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            kernel_size,
            depth_multiplier=depth_multiplier,
            strides=strides,
            padding=padding,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            ndim=1,
            key=key,
        )


@pytc.treeclass
class DepthwiseConv2D(DepthwiseConvND):
    def __init__(
        self,
        in_features,
        kernel_size,
        *,
        depth_multiplier=1,
        strides=1,
        padding="SAME",
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            kernel_size,
            depth_multiplier=depth_multiplier,
            strides=strides,
            padding=padding,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            ndim=2,
            key=key,
        )


@pytc.treeclass
class DepthwiseConv3D(DepthwiseConvND):
    def __init__(
        self,
        in_features,
        kernel_size,
        *,
        depth_multiplier=1,
        strides=1,
        padding="SAME",
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            kernel_size,
            depth_multiplier=depth_multiplier,
            strides=strides,
            padding=padding,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            ndim=3,
            key=key,
        )


# ------------------------------ SeparableConvND Depthwise Convolutional Layers ------------------------------ #


@pytc.treeclass
class SeparableConvND:
    depthwise_conv: DepthwiseConvND
    pointwise_conv: DepthwiseConvND

    in_features: int = pytc.nondiff_field()
    out_features: int = pytc.nondiff_field()
    depth_multiplier: int = pytc.nondiff_field()
    kernel_size: int | tuple[int, ...] = pytc.nondiff_field()
    strides: int | tuple[int, ...] = pytc.nondiff_field()
    padding: str | int | tuple[tuple[int, int], ...] = pytc.nondiff_field()

    depthwise_weight_init_func: str | Callable[[jr.PRNGKey, tuple[int, ...]], jnp.ndarray]  # fmt: skip
    pointwise_weight_init_func: str | Callable[[jr.PRNGKey, tuple[int, ...]], jnp.ndarray]  # fmt: skip
    pointwise_bias_init_func: str | Callable[[jr.PRNGKey, tuple[int]], jnp.ndarray]

    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        depth_multiplier=1,
        strides=1,
        padding="SAME",
        depthwise_weight_init_func="glorot_uniform",
        pointwise_weight_init_func="glorot_uniform",
        pointwise_bias_init_func="zeros",
        ndim=2,
        key=jr.PRNGKey(0),
    ):
        """Separable convolutional layer.

        Note:
            See:
                https://en.wikipedia.org/wiki/Separable_filter
                https://keras.io/api/layers/convolution_layers/separable_convolution2d/
                https://github.com/deepmind/dm-haiku/blob/main/haiku/_src/depthwise_conv.py

        Args:
            in_features : Number of input channels.
            out_features : Number of output channels.
            kernel_size : Size of the convolving kernel.
            depth_multiplier : Number of depthwise convolution output channels for each input channel.
            strides : Stride of the convolution.
            padding : Padding to apply to the input.
            depthwise_weight_init_func : Function to initialize the depthwise convolution weights.
            pointwise_weight_init_func : Function to initialize the pointwise convolution weights.
            pointwise_bias_init_func : Function to initialize the pointwise convolution bias.
            ndim : Number of spatial dimensions.

        """

        if not isinstance(in_features, int) or in_features <= 0:
            raise ValueError(
                f"Expected in_features to be a positive integer, got {in_features}"
            )

        if not isinstance(out_features, int) or out_features <= 0:
            raise ValueError(
                f"Expected out_features to be a positive integer, got {out_features}"
            )

        if not isinstance(depth_multiplier, int) or depth_multiplier <= 0:
            raise ValueError(
                f"Expected depth_multiplier to be a positive integer, got {depth_multiplier}"
            )

        self.in_features = in_features
        self.out_features = out_features
        self.depth_multiplier = depth_multiplier

        self.kernel_size = _check_and_return_kernel(kernel_size, ndim)
        self.strides = _check_and_return_strides(strides, ndim)
        self.padding = _check_and_return_padding(padding, self.kernel_size)
        self.depthwise_weight_init_func = _check_and_return_init_func(
            depthwise_weight_init_func, "depthwise_weight_init_func"
        )
        self.pointwise_weight_init_func = _check_and_return_init_func(
            pointwise_weight_init_func, "pointwise_weight_init_func"
        )
        self.pointwise_bias_init_func = _check_and_return_init_func(
            pointwise_bias_init_func, "pointwise_bias_init_func"
        )

        self.ndim = ndim

        self.depthwise_conv = DepthwiseConvND(
            in_features=in_features,
            depth_multiplier=depth_multiplier,
            kernel_size=self.kernel_size,
            strides=strides,
            padding=padding,
            weight_init_func=depthwise_weight_init_func,
            bias_init_func=None,  # no bias for lhs
            key=key,
            ndim=ndim,
        )

        self.pointwise_conv = ConvND(
            in_features=in_features * depth_multiplier,
            out_features=out_features,
            kernel_size=1,
            strides=strides,
            padding=padding,
            weight_init_func=pointwise_weight_init_func,
            bias_init_func=pointwise_bias_init_func,
            key=key,
            ndim=ndim,
        )

    def __call__(self, x: jnp.ndarray, **kwargs) -> jnp.ndarray:
        x = self.depthwise_conv(x)
        x = self.pointwise_conv(x)
        return x


@pytc.treeclass
class SeparableConv1D(SeparableConvND):
    """1D separable convolutional layer."""

    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        depth_multiplier=1,
        strides=1,
        padding="SAME",
        depthwise_weight_init_func="glorot_uniform",
        pointwise_weight_init_func="glorot_uniform",
        pointwise_bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            depth_multiplier=depth_multiplier,
            strides=strides,
            padding=padding,
            depthwise_weight_init_func=depthwise_weight_init_func,
            pointwise_weight_init_func=pointwise_weight_init_func,
            pointwise_bias_init_func=pointwise_bias_init_func,
            ndim=1,
            key=key,
        )


@pytc.treeclass
class SeparableConv2D(SeparableConvND):
    """2D separable convolutional layer."""

    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        depth_multiplier=1,
        strides=1,
        padding="SAME",
        depthwise_weight_init_func="glorot_uniform",
        pointwise_weight_init_func="glorot_uniform",
        pointwise_bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            depth_multiplier=depth_multiplier,
            strides=strides,
            padding=padding,
            depthwise_weight_init_func=depthwise_weight_init_func,
            pointwise_weight_init_func=pointwise_weight_init_func,
            pointwise_bias_init_func=pointwise_bias_init_func,
            ndim=2,
            key=key,
        )


@pytc.treeclass
class SeparableConv3D(SeparableConvND):
    """3D separable convolutional layer."""

    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        depth_multiplier=1,
        strides=1,
        padding="SAME",
        depthwise_weight_init_func="glorot_uniform",
        pointwise_weight_init_func="glorot_uniform",
        pointwise_bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            depth_multiplier=depth_multiplier,
            strides=strides,
            padding=padding,
            depthwise_weight_init_func=depthwise_weight_init_func,
            pointwise_weight_init_func=pointwise_weight_init_func,
            pointwise_bias_init_func=pointwise_bias_init_func,
            ndim=3,
            key=key,
        )


# ------------------------------ ConvNDLocal Convolutional Layers ------------------------------ #


@pytc.treeclass
class ConvNDLocal:
    weight: jnp.ndarray
    bias: jnp.ndarray

    in_features: int = pytc.nondiff_field()  # number of input features
    out_features: int = pytc.nondiff_field()  # number of output features
    kernel_size: int | tuple[int, ...] = pytc.nondiff_field()
    in_size: tuple[int, ...] = pytc.nondiff_field()  # size of input
    strides: int | tuple[int, ...] = pytc.nondiff_field()  # stride of the convolution
    padding: str | int | tuple[tuple[int, int], ...] = pytc.nondiff_field()
    input_dilation: int | tuple[int, ...] = pytc.nondiff_field()
    kernel_dilation: int | tuple[int, ...] = pytc.nondiff_field()
    weight_init_func: Callable[[jr.PRNGKey, tuple[int, ...]], jnp.ndarray]
    bias_init_func: Callable[[jr.PRNGKey, tuple[int]], jnp.ndarray]

    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        in_size,
        strides=1,
        padding="SAME",
        input_dilation=1,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        ndim=2,
        key=jr.PRNGKey(0),
    ):
        """Local convolutional layer.

        Args:
            in_features: number of input features
            out_features: number of output features
            kernel_size: size of the convolution kernel
            in_size: size of the input
            strides: stride of the convolution
            padding: padding of the convolution
            input_dilation: dilation of the input
            kernel_dilation: dilation of the convolution kernel
            weight_init_func: weight initialization function
            bias_init_func: bias initialization function
            ndim: number of dimensions
            key: random number generator key
        Note:
            See : https://keras.io/api/layers/locally_connected_layers/
        """

        if not isinstance(in_features, int) or in_features <= 0:
            raise ValueError(
                f"Expected in_features to be a positive integer, got {in_features}"
            )

        if not isinstance(out_features, int) or out_features <= 0:
            raise ValueError(
                f"Expected out_features to be a positive integer, got {out_features}"
            )

        self.in_features = in_features
        self.out_features = out_features

        self.in_size = _check_and_return_input_size(in_size, ndim)
        self.kernel_size = _check_and_return_kernel(kernel_size, ndim)
        self.strides = _check_and_return_strides(strides, ndim)
        self.input_dilation = _check_and_return_input_dilation(input_dilation, ndim)
        self.kernel_dilation = _check_and_return_kernel_dilation(1, ndim)
        self.padding = _check_and_return_padding(padding, self.kernel_size)
        self.weight_init_func = _check_and_return_init_func(
            weight_init_func, "weight_init_func"
        )
        self.bias_init_func = _check_and_return_init_func(
            bias_init_func, "bias_init_func"
        )
        self.dimension_numbers = ConvDimensionNumbers(*((tuple(range(ndim + 2)),) * 3))
        self.out_size = _calculate_convolution_output_shape(
            shape=self.in_size,
            kernel_size=self.kernel_size,
            padding=self.padding,
            strides=self.strides,
        )

        # OIHW
        self.weight_shape = (
            self.out_features,
            self.in_features * ft.reduce(op.mul, self.kernel_size),
            *self.out_size,
        )

        self.weight = self.weight_init_func(key, self.weight_shape)

        bias_shape = (self.out_features, *self.out_size)

        if bias_init_func is None:
            self.bias = None
        else:
            self.bias = self.bias_init_func(key, bias_shape)

    def __call__(self, x: jnp.ndarray, **kwargs) -> jnp.ndarray:
        y = jax.lax.conv_general_dilated_local(
            lhs=x[None],
            rhs=self.weight,
            window_strides=self.strides,
            padding=self.padding,
            filter_shape=self.kernel_size,
            lhs_dilation=self.kernel_dilation,
            rhs_dilation=self.input_dilation,  # atrous dilation
            dimension_numbers=self.dimension_numbers,
        )

        if self.bias is None:
            return y[0]
        return (y + self.bias)[0]


@pytc.treeclass
class Conv1DLocal(ConvNDLocal):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        in_size,
        strides=1,
        padding="SAME",
        input_dilation=1,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            in_size=in_size,
            strides=strides,
            padding=padding,
            input_dilation=input_dilation,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            ndim=1,
            key=key,
        )


@pytc.treeclass
class Conv2DLocal(ConvNDLocal):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        in_size,
        strides=1,
        padding="SAME",
        input_dilation=1,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            in_size=in_size,
            strides=strides,
            padding=padding,
            input_dilation=input_dilation,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            ndim=2,
            key=key,
        )


@pytc.treeclass
class Conv3DLocal(ConvNDLocal):
    def __init__(
        self,
        in_features,
        out_features,
        kernel_size,
        *,
        in_size,
        strides=1,
        padding="SAME",
        input_dilation=1,
        kernel_dilation=1,
        weight_init_func="glorot_uniform",
        bias_init_func="zeros",
        key=jr.PRNGKey(0),
    ):
        super().__init__(
            in_features,
            out_features,
            kernel_size,
            in_size=in_size,
            strides=strides,
            padding=padding,
            input_dilation=input_dilation,
            kernel_dilation=kernel_dilation,
            weight_init_func=weight_init_func,
            bias_init_func=bias_init_func,
            ndim=3,
            key=key,
        )
