__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массива к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    sum_odd = 0
    sum_even = 0
    for i in arr:
        if (i % 2) == 0:
            sum_even += i
        else: sum_odd += i
    if sum_odd != 0:    
        return sum_even/sum_odd
    else: return 0