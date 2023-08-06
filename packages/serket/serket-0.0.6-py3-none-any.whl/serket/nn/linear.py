from __future__ import annotations

from typing import Callable

import jax.numpy as jnp
import jax.random as jr
import pytreeclass as pytc

from .utils import _check_and_return_init_func


@pytc.treeclass
class Linear:
    weight: jnp.ndarray
    bias: jnp.ndarray

    in_features: int = pytc.nondiff_field()
    out_features: int = pytc.nondiff_field()

    def __init__(
        self,
        in_features: int,
        out_features: int,
        *,
        weight_init_func: str | Callable = "he_normal",
        bias_init_func: str | Callable = "ones",
        key: jr.PRNGKey = jr.PRNGKey(0),
    ):
        """Fully connected layer

        Args:
            in_features: number of input features
            out_features: number of output features
            weight_init_func: function to initialize the weight matrix with . Defaults to "he_normal".
            bias_init_func: bias initializer function . Defaults to ones.
            key: Random key for weight and bias initialization. Defaults to jr.PRNGKey(0).

        Examples:
            >>> l1 = Linear(10, 5)
            >>> l1(jnp.ones((3, 10))).shape
            (3, 5)
        """

        self.weight_init_func = _check_and_return_init_func(
            weight_init_func, "weight_init_func"
        )
        self.bias_init_func = _check_and_return_init_func(
            bias_init_func, "bias_init_func"
        )

        self.in_features = in_features
        self.out_features = out_features

        self.weight = self.weight_init_func(key, (in_features, out_features))

        if bias_init_func is None:
            self.bias = None
        else:
            self.bias = self.bias_init_func(key, (out_features,))

    def __call__(self, x: jnp.ndarray, **kwargs) -> jnp.ndarray:
        if self.bias is None:
            return x @ self.weight
        return x @ self.weight + self.bias


@pytc.treeclass
class Bilinear:
    weight: jnp.ndarray
    bias: jnp.ndarray

    in1_features: int = pytc.nondiff_field()
    in2_features: int = pytc.nondiff_field()
    out_features: int = pytc.nondiff_field()

    def __init__(
        self,
        in1_features: int,
        in2_features: int,
        out_features: int,
        *,
        weight_init_func: str | Callable = "he_normal",
        bias_init_func: str | Callable = "ones",
        key: jr.PRNGKey = jr.PRNGKey(0),
    ):
        """Bilinear layer
        see: https://pytorch.org/docs/stable/generated/torch.nn.Bilinear.html

        Args:
            in_features (int): number of input features
            out_features (int): number of output features
            weight_init_func (Callable, optional): . Defaults to jax.nn.initializers.he_normal().
            bias_init_func (Callable, optional): . Defaults to lambdakey.
            key (jr.PRNGKey, optional):  . Defaults to jr.PRNGKey(0).

        Examples:
            >>> b1 = Bilinear(10, 5, 3)
            >>> b1(jnp.ones((3, 10)), jnp.ones((3, 5))).shape
            (3, 3)
        """

        self.in1_features = in1_features
        self.in2_features = in2_features
        self.out_features = out_features

        self.weight_init_func = _check_and_return_init_func(
            weight_init_func, "weight_init_func"
        )
        self.bias_init_func = _check_and_return_init_func(
            bias_init_func, "bias_init_func"
        )

        self.weight = self.weight_init_func(
            key, (in1_features, in2_features, out_features)
        )

        if self.bias_init_func is None:
            self.bias = None
        else:
            self.bias = self.bias_init_func(key, (out_features,))

    def __call__(self, x1: jnp.ndarray, x2: jnp.ndarray, **kwargs) -> jnp.ndarray:
        x = x1 @ self.weight.reshape(-1, self.in2_features * self.out_features)
        x = x2 @ x.reshape(-1, self.out_features)

        if self.bias is None:
            return x
        return x + self.bias


@pytc.treeclass
class Identity:
    """Identity layer"""

    def __call__(self, x: jnp.ndarray, **kwargs) -> jnp.ndarray:
        return x
