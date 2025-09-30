"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x, y):
    return x * y

def id(x):
    return x

def add(x, y):
    return x + y

def neg(x):
    return -x

def lt(x, y):
    return 1.0 if x < y else 0.0

def eq(x, y):
    return 1.0 if x == y else 0.0

def max(x, y):
    return x if x > y else y

def is_close(x, y):
    return abs(x - y) < 1e-2

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))

def relu(x):
    return x if x > 0 else 0.0

def log(x):
    return math.log(x + 1e-6)

def exp(x):
    return math.exp(x)

def log_back(x, d):
    return d * (1/x)

def inv(x):
    return 1 / x

def inv_back(x, y):
    return -(1 / x ** 2) * y

def relu_back(x, y):
    return y if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(fn):
    def map_func(a):
        return [fn(el) for el in a]

    return map_func

def zipWith(fn):
    def zip_func(a, b):
        return [fn(x, y) for x, y in zip(a, b)]

    return zip_func

def reduce(fn, start):
    def reduce_func(ls):
        res = start
        for el in ls:
            res = fn(res, el)
        return res

    return reduce_func

def negList(a):
    return map(neg)(a)

def addLists(a, b):
    return zipWith(add)(a, b)

def sum(a):
    return reduce(add, 0)(a)

def prod(a):
    return reduce(mul, 1)(a)
