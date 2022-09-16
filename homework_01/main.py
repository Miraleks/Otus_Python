"""
Домашнее задание №1
Функции и структуры данных
"""


def is_prime(n):
    if n > 1:
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n
    else:
        return False


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [x**2 for x in args]


# filter types
# таки да, я знаю, что присваивать константе лямбду нехорошо
ODD = lambda x: x if x % 2 != 0 else False
EVEN = lambda x: x if x % 2 == 0 else False
PRIME = is_prime


def filter_numbers(nums, func):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    return list(filter(func, nums))