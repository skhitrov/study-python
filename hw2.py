"""Домашняя работа 2: включения списков, срезы, изменяемость и ссылки.

Включение списка (list comprehension) строит новый список по правилу:
    [выражение for элемент in последовательность]

Например, [x * x for x in numbers] соответствует циклу:
    squares = []
    for x in numbers:
        squares.append(x * x)

Можно отбирать элементы условием в конце:
    [x for x in numbers if x > 0]

Условие внутри выражения выбирает одно из двух значений для КАЖДОГО
элемента (ничего не пропускает):
    ["+" if x > 0 else "-" for x in numbers]

Несколько for читаются слева направо, как вложенные циклы:
    [(x, y) for x in [1, 2] for y in [3, 4]]
    # [(1, 3), (1, 4), (2, 3), (2, 4)]

Распаковка кортежа позволяет сразу дать имена его элементам:
    index, word = (0, "кот")  # index == 0, word == "кот"

То же самое работает в цикле. enumerate(words) выдаёт пары
(индекс, элемент), а запись «for index, word» распаковывает каждую пару:
    words = ["кот", "пёс"]
    for index, word in enumerate(words):
        print(index, word)  # сначала 0 кот, затем 1 пёс

Во включении списка распаковка записывается точно так же:
    [word for index, word in enumerate(words) if index == 1]  # ["пёс"]

В задачах 1–10 надо использовать включение списка для построения результата и не менять входные списки.
В остальных задачах выбрать подходящий способ самостоятельно.

Запуск:
    python hw2.py                # все тесты; остановка на первой ошибке
    python hw2.py squares        # тесты одной функции
"""

import copy
import sys
from collections.abc import Callable, Sequence


# Часть 1. Включения списков: от простого к более сложному.

def squares(n: int) -> list[int]:
    """1. Квадраты чисел от 0 до n включительно. n >= 0.

    squares(3) -> [0, 1, 4, 9]
    """
    raise NotImplementedError


def even_numbers(numbers: list[int]) -> list[int]:
    """2. Оставить только чётные числа, сохранив порядок.

    even_numbers([3, 2, -4, 7]) -> [2, -4]
    """
    raise NotImplementedError


def signs(numbers: list[int]) -> list[str]:
    """3. Для каждого числа вернуть его знак или 0: '+', '-', '0'.

    signs([-2, 0, 5]) -> ['-', '0', '+']
    Подсказка: условное выражение можно вложить в другое.
    """
    raise NotImplementedError


def clean_words(words: list[str]) -> list[str]:
    """4. Убрать пробелы по краям слов и пропустить пустые результаты.

    clean_words(['  кот ', ' ', ' пёс']) -> ['кот', 'пёс']
    Не меняй исходный список.
    """
    raise NotImplementedError


def positions(items: list[str], target: str) -> list[int]:
    """5. Индексы всех вхождений target в items.

    positions(['а', 'б', 'а'], 'а') -> [0, 2]
    Подсказка: enumerate() даёт пару (индекс, элемент).
    """
    raise NotImplementedError


def flatten(rows: list[list[int]]) -> list[int]:
    """6. Собрать строки в один список, сохранив их порядок.

    flatten([[1, 2], [], [3]]) -> [1, 2, 3]
    """
    raise NotImplementedError


def pairs_with_even_sum(left: list[int], right: list[int]) -> list[tuple[int, int]]:
    """7. Пары (x, y), для которых x + y чётно.

    Сначала перебери все значения left, для каждого — все значения right.
    pairs_with_even_sum([1, 2], [3, 4]) -> [(1, 3), (2, 4)]
    """
    raise NotImplementedError


def multiplication_table(n: int) -> list[list[int]]:
    """8. Таблица умножения от 1 до n по строкам и столбцам. n >= 0.

    multiplication_table(3) -> [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    Для каждой строки построй отдельный список.
    """
    raise NotImplementedError


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """9. Поменять местами строки и столбцы прямоугольной матрицы.

    transpose([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
    Матрица непустая, каждая строка непустая и одинаковой длины.
    Не использовать zip() и не менять исходную матрицу.
    """
    raise NotImplementedError


def first_occurrences(items: list[str]) -> list[str]:
    """10. Убрать повторы, сохранив первое вхождение каждого значения.

    first_occurrences(['а', 'б', 'а', 'в', 'б']) -> ['а', 'б', 'в']
    Используй срез: проверь, встречалось ли значение до текущего индекса.
    Не меняй исходный список.
    """
    raise NotImplementedError


# Часть 2. Списки, ссылки и локальные имена.

def make_board() -> list[list[str]]:
    """11. Создать пустое поле 3 x 3 для крестиков-ноликов.

    Пустая клетка обозначается ''. После создания запись в одну клетку
    должна менять только эту клетку. Разные вызовы дают независимые поля.

    Подсказка: [0] * 3 == [0, 0, 0]
    """
    raise NotImplementedError


def append_in_place(values: list[int], value: int) -> None:
    """12. Добавить value в полученный список; ничего не возвращать."""
    raise NotImplementedError


def replaced_last(values: list[int], value: int) -> list[int]:
    """13. Вернуть НОВЫЙ список с заменённым последним элементом.

    values — непустой список. Исходный список должен остаться прежним. Используй срез.
    replaced_last([1, 2, 3], 9) -> [1, 2, 9]
    """
    raise NotImplementedError


def append_then_rebind(values: list[int], added: int, replacement: int) -> list[int]:
    """14. Сначала добавить added в переданный список на месте.

    Затем присвоить локальному имени values НОВЫЙ список [replacement]
    и вернуть его. После вызова у вызывающего кода должны быть два разных
    списка: его прежний список с added и возвращённый [replacement].
    """
    raise NotImplementedError


def remove_negatives_in_place(values: list[int]) -> None:
    """15. Удалить из переданного списка все отрицательные числа.

    Порядок оставшихся чисел сохранить, ничего не возвращать. Вызывающий
    код должен увидеть изменение в своём списке, в том числе через другое
    имя этого же списка.
    remove_negatives_in_place([3, -1, -2, 0]) меняет список на [3, 0].
    Подсказка: срезу values[:] можно присвоить новый набор элементов.
    """
    raise NotImplementedError


def marked_copy(
    board: list[list[str]], row: int, column: int, mark: str,
) -> list[list[str]]:
    """16. Вернуть копию поля, в которой в клетке (row, column) стоит mark.

    Поле — непустой прямоугольный список списков; индекс клетки допустим.
    Исходное поле не менять. После вызова изменение ЛЮБОЙ клетки копии не
    должно менять исходное поле, и наоборот. Продумай, достаточно ли
    скопировать только внешний список.
    
    Подсказка: можно использовать метод .copy() списка для создания копии.
    """
    raise NotImplementedError


### TESTS ###
# Публичные тесты

class PublicTests:
    """Кейсы (аргументы, ожидаемый результат)."""

    def __init__(self, cases: Sequence[tuple[tuple[object, ...], object]]) -> None:
        self.cases = cases

    def check(self, function: Callable[..., object]) -> int:
        for index, (arguments, expected) in enumerate(self.cases, start=1):
            original_arguments = copy.deepcopy(arguments)
            actual = function(*arguments)
            assert actual == expected, (
                f"кейс {index}: аргументы {arguments!r}; "
                f"ожидалось {expected!r}, получено {actual!r}"
            )
            assert arguments == original_arguments, (
                f"кейс {index}: входные данные изменились"
            )
        return len(self.cases)


def check_make_board(function: Callable[[], list[list[str]]]) -> int:
    board = function()
    assert board == [["", "", ""]
                     for _ in range(3)], "поле должно быть пустым 3 x 3"
    board[0][1] = "X"
    assert board == [["", "X", ""], ["", "", ""], ["", "", ""]], (
        "после изменения одной клетки остальные должны остаться пустыми"
    )
    second = function()
    assert second == [["", "", ""] for _ in range(3)], (
        "новый вызов должен создавать пустое поле"
    )
    second[2][2] = "O"
    assert board[2][2] == "", "поля из разных вызовов должны быть независимы"
    return 4


def check_append_in_place(function: Callable[[list[int], int], None]) -> int:
    for initial, value, expected in [([1, 2], 3, [1, 2, 3]), ([], -1, [-1])]:
        values = initial.copy()
        alias = values
        result = function(values, value)
        assert result is None, "функция должна возвращать None"
        assert values == expected and alias == expected, (
            f"переданный список должен стать {expected!r}"
        )
    return 2


def check_replaced_last(function: Callable[[list[int], int], list[int]]) -> int:
    for initial, value, expected in [([1, 2, 3], 9, [1, 2, 9]), ([7], 0, [0])]:
        values = initial.copy()
        result = function(values, value)
        assert result == expected, f"ожидалось {expected!r}, получено {result!r}"
        assert values == initial, "исходный список изменился"
        assert result is not values, "нужен новый список, даже для одного элемента"
    return 2


def check_append_then_rebind(
    function: Callable[[list[int], int, int], list[int]],
) -> int:
    for initial, added, replacement in [([1, 2], 3, 9), ([], 0, -1)]:
        values = initial.copy()
        alias = values
        result = function(values, added, replacement)
        assert values == initial + \
            [added], "изменение переданного списка не видно"
        assert alias == initial + \
            [added], "второе имя должно видеть изменение списка"
        assert result == [replacement], "вернулся неверный новый список"
        assert result is not values, "возвращённый список должен быть отдельным объектом"
    return 2


def check_remove_negatives_in_place(
    function: Callable[[list[int]], None],
) -> int:
    for initial, expected in [
        ([3, -1, -2, 0], [3, 0]),
        ([-3, -1], []),
        ([0, 2], [0, 2]),
        ([], []),
    ]:
        values = initial.copy()
        alias = values
        result = function(values)
        assert result is None, "функция должна возвращать None"
        assert values == expected, f"ожидался список {expected!r}, получено {values!r}"
        assert alias == expected, "изменение должно быть видно через другое имя"
    return 4


def check_marked_copy(
    function: Callable[[list[list[str]], int, int, str], list[list[str]]],
) -> int:
    for initial, row, column, mark in [
        ([["", ""], ["", ""]], 0, 1, "X"),
        ([["a", "b", "c"], ["d", "e", "f"]], 1, 2, "O"),
    ]:
        board = [line.copy() for line in initial]
        result = function(board, row, column, mark)
        expected = [line.copy() for line in initial]
        expected[row][column] = mark
        assert result == expected, f"ожидалось {expected!r}, получено {result!r}"
        assert board == initial, "исходное поле изменилось"
        assert result is not board, "нужен новый внешний список"
        for line_index in range(len(board)):
            assert result[line_index] is not board[line_index], (
                f"строка {line_index} осталась общей у двух полей"
            )
    return 2


PUBLIC_TESTS: dict[str, Callable[[], int]] = {
    "squares": lambda: PublicTests([
        ((0,), [0]), ((3,), [0, 1, 4, 9]), ((5,), [0, 1, 4, 9, 16, 25]),
    ]).check(squares),
    "even_numbers": lambda: PublicTests([
        (([3, 2, -4, 7, 0],), [2, -4, 0]), (([],), []), (([1, 3],), []),
    ]).check(even_numbers),
    "signs": lambda: PublicTests([
        (([-2, 0, 5],), ["-", "0", "+"]), (([],),
                                           []), (([0, -1, 1],), ["0", "-", "+"]),
    ]).check(signs),
    "clean_words": lambda: PublicTests([
        ((["  кот ", " ", " пёс"],), ["кот", "пёс"]),
        (([],), []), ((["", "  ", "  привет  "],), ["привет"]),
    ]).check(clean_words),
    "positions": lambda: PublicTests([
        ((["а", "б", "а"], "а"), [0, 2]),
        ((["а", "б"], "в"), []), (([], "а"), []),
    ]).check(positions),
    "flatten": lambda: PublicTests([
        (([[1, 2], [], [3]],), [1, 2, 3]),
        (([],), []), (([[], []],), []), (([[0], [-1, -2]],), [0, -1, -2]),
    ]).check(flatten),
    "pairs_with_even_sum": lambda: PublicTests([
        (([1, 2], [3, 4]), [(1, 3), (2, 4)]),
        (([2, 4], [6, 8]), [(2, 6), (2, 8), (4, 6), (4, 8)]),
        (([], [1]), []), (([1], []), []),
    ]).check(pairs_with_even_sum),
    "multiplication_table": lambda: PublicTests([
        ((0,), []), ((1,), [[1]]),
        ((3,), [[1, 2, 3], [2, 4, 6], [3, 6, 9]]),
    ]).check(multiplication_table),
    "transpose": lambda: PublicTests([
        (([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
        (([[7]],), [[7]]), (([[1], [2], [3]],), [[1, 2, 3]]),
    ]).check(transpose),
    "first_occurrences": lambda: PublicTests([
        ((["а", "б", "а", "в", "б"],), ["а", "б", "в"]),
        (([],), []), ((["x", "x", "x"],), ["x"]),
    ]).check(first_occurrences),
    "make_board": lambda: check_make_board(make_board),
    "append_in_place": lambda: check_append_in_place(append_in_place),
    "replaced_last": lambda: check_replaced_last(replaced_last),
    "append_then_rebind": lambda: check_append_then_rebind(append_then_rebind),
    "remove_negatives_in_place": lambda: check_remove_negatives_in_place(
        remove_negatives_in_place),
    "marked_copy": lambda: check_marked_copy(marked_copy),
}


def run_public_tests(function_name: str | None = None) -> None:
    if function_name is not None and function_name not in PUBLIC_TESTS:
        names = ", ".join(PUBLIC_TESTS)
        raise SystemExit(
            f"Неизвестная функция {function_name!r}. Доступны: {names}")

    names_to_run = [function_name] if function_name is not None else list(
        PUBLIC_TESTS)
    for name in names_to_run:
        try:
            passed = PUBLIC_TESTS[name]()
        except (AssertionError, NotImplementedError) as error:
            detail = str(error) or "функция пока не реализована"
            raise SystemExit(f"Тесты {name}: ОШИБКА — {detail}") from None
        print(f"{name}: пройдено проверок — {passed}")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise SystemExit("Использование: python hw2.py [имя_функции]")
    run_public_tests(sys.argv[1] if len(sys.argv) == 2 else None)
