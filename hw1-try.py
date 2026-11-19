import sys
from _collections_abc import Callable, Sequence


def fibonacci(n: int) -> int:
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a


def maximum_of_four(
    a: int,
    b: int,
    c: int,
    d: int,
) -> int:
    if a > b:
        n = a
        print("a maximum")
    else:
        n = b
        print("b is maximum")
    if c > d:
        f = c
        print("c is maximum")
    else:
        f = d
        print("d is maximum")
    if n >= f:
        return n
    else:
        return f
