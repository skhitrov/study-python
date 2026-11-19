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


def maximum(numbers: list[int]) -> int:
    max = numbers[0]
    for number in numbers:
        if max <= number:
            max = number
    return max


def transpose(matrix: list[list[object]]) -> list[list[object]]:
    result = []
    column_index = 0
    for item in matrix[0]:
        column = []
        for row in matrix:
            column.append(row[column_index])
        result.append(column)
        column_index = column_index + 1
    return result


def reverse_input_lines(lines: list[str]) -> list[str]:
    result = []
    for line in reversed(lines):
        numbers = line.split()
        numbers.reverse()
        result.append(" ".join(numbers))
    return result
