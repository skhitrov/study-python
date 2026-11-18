"""Домашняя работа 1: циклы, последовательности и рассуждения об алгоритмах.

Для каждой задачи:
1. Реализовать функцию без сторонних библиотек.
2. Проверить обычные и граничные случаи.

В задачах используются циклы и списки. В последней задаче нужно обработать
ввод построчно и обратить порядок данных на двух уровнях.

Запуск тестов:
    python hw1.py                  # проверить все функции
    python hw1.py fibonacci        # проверить одну функцию
    python hw1.py --reverse        # запустить reverse на stdin
"""

import sys
from collections.abc import Callable, Sequence


def fibonacci(n: int) -> int:
    """Вернуть n-е число Фибоначчи, где F(0) = 0, F(1) = 1.

    Требования:
    - n — целое неотрицательное число;
    - использовать цикл, не рекурсию и не формулу в замкнутом виде.

    Примеры:
        fibonacci(0) -> 0
        fibonacci(1) -> 1
        fibonacci(7) -> 13
    """
    return -1


def maximum_of_four(
    a: int,
    b: int,
    c: int,
    d: int,
) -> int:
    """Вернуть наибольшее число среди 4х аргументов.

    Примеры:
        maximum_of_four(3, -2, 8, 1) -> 8
        maximum_of_four(5, 5, 2, 0) -> 5
    """
    return -1


def maximum(numbers: list[int]) -> int:
    """Вернуть наибольшее число в непустом списке numbers.

    Примеры:
        maximum([3, -2, 8, 1]) -> 8
        maximum([5, 5, 2]) -> 5
    """
    return -1


def transpose(matrix: list[list[object]]) -> list[list[object]]:
    """Вернуть транспонированную матрицу.

    Предусловие: matrix — непустая прямоугольная матрица.

    Требования:
    - не использовать zip();
    - не изменять исходную матрицу.

    Пример:
        transpose([[1, 2, 3], [4, 5, 6]])
        -> [[1, 4], [2, 5], [3, 6]]
    """
    return []


def reverse_input_lines(lines: list[str]) -> list[str]:
    """Обработать входные строки для задачи на разворот порядка.

    Дана последовательность строк. В каждой строке находится ноль или
    более целых чисел, разделённых пробелами. Нужно получить строки ответа,
    расположив строки в обратном порядке и также развернув числа в каждой
    строке. Пустая входная строка должна остаться пустой строкой ответа.

    Аргумент lines — строки, прочитанные из stdin (с окончаниями строк или
    без них). Верните список строк без символов окончания строки; числа в
    каждой выходной строке разделите одним пробелом. В основной программе
    ввод читается до EOF, поэтому пустая строка не служит сигналом остановки.

    Ограничения: не более 10^6 строк и 10^6 чисел; каждое число — целое.

    Пример:
        Ввод:  ["1 2\\n", "3\\n"]
        Ответ: ["3", "2 1"]

        Ввод:  ["1 2\\n", "\\n", "3\\n"]
        Ответ: ["3", "", "2 1"]
    """
    return [""]


### TESTS ###
# Ниже служебные классы и функции. Если интересно, можно изучать :)


class PublicTests:
    """Простой универсальный запускатель публичных тест-кейсов.

    Каждый кейс имеет вид (input, expected). Для функции с несколькими
    аргументами input задаётся кортежем; для функции с одним аргументом —
    непосредственно этим значением.

    Пример использования:
        PublicTests(FIBONACCI_CASES).check(fibonacci)
    """

    def __init__(self, cases: Sequence[tuple[object, object]]) -> None:
        self.cases = cases

    def check(self, function: Callable[..., object]) -> int:
        for index, (test_input, expected) in enumerate(self.cases, start=1):
            if isinstance(test_input, tuple):
                actual = function(*test_input)
            else:
                actual = function(test_input)
            if actual != expected:
                raise AssertionError(
                    f"Кейс {index}: для {test_input!r} ожидалось {expected!r}, "
                    f"получено {actual!r}"
                )
        return len(self.cases)


FIBONACCI_CASES = [
    (0, 0),
    (1, 1),
    (2, 1),
    (7, 13),
    (10, 55),
]

MAXIMUM_OF_FOUR_CASES = [
    ((3, -2, 8, 1), 8),
    ((5, 5, 2, 0), 5),
    ((-8, -3, -10, -4), -3),
    ((9, 1, 2, 3), 9),
]

MAXIMUM_CASES = [
    ([3, -2, 8, 1], 8),
    ([5, 5, 2], 5),
    ([-8, -3, -10], -3),
    ([4], 4),
]

TRANSPOSE_CASES = [
    ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[7], [8], [9]], [[7, 8, 9]]),
    ([[5]], [[5]]),
]

REVERSE_INPUT_LINES_CASES = [
    (["1 2\n", "3\n"], ["3", "2 1"]),
    (["1 2\n", "\n", "3\n"], ["3", "", "2 1"]),
    (["1   -2  3\n"], ["3 -2 1"]),
    (["\n"], [""]),
    ([], []),
]

PUBLIC_TESTS = {
    "fibonacci": PublicTests(FIBONACCI_CASES),
    "maximum_of_four": PublicTests(MAXIMUM_OF_FOUR_CASES),
    "maximum": PublicTests(MAXIMUM_CASES),
    "transpose": PublicTests(TRANSPOSE_CASES),
    "reverse_input_lines": PublicTests(REVERSE_INPUT_LINES_CASES),
}

PUBLIC_FUNCTIONS: dict[str, Callable[..., object]] = {
    "fibonacci": fibonacci,
    "maximum_of_four": maximum_of_four,
    "maximum": maximum,
    "transpose": transpose,
    "reverse_input_lines": reverse_input_lines,
}


def run_public_tests(function_name: str | None = None) -> None:
    """Запустить публичные тесты одной функции или всех функций."""
    if function_name is not None and function_name not in PUBLIC_TESTS:
        names = ", ".join(PUBLIC_TESTS)
        raise SystemExit(
            f"Неизвестная функция {function_name!r}. Доступны: {names}")

    names_to_run = [function_name] if function_name is not None else list(
        PUBLIC_TESTS)
    for name in names_to_run:
        try:
            passed = PUBLIC_TESTS[name].check(PUBLIC_FUNCTIONS[name])
        except AssertionError as error:
            raise SystemExit(f"Тесты {name}: ОШИБКА — {error}") from None
        print(f"{name}: пройдено кейсов — {passed}")


def main() -> None:
    """По умолчанию проверить все функции; принять имя для выборочного запуска."""
    arguments = sys.argv[1:]
    if arguments == ["--reverse"]:
        output_lines = reverse_input_lines(sys.stdin.readlines())
        for line in output_lines:
            print(line)
    elif len(arguments) <= 1:
        run_public_tests(arguments[0] if arguments else None)
    else:
        raise SystemExit(
            "Использование: python hw1.py [имя_функции | --reverse]")


if __name__ == "__main__":
    main()
