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
