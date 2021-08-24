__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number in [0,1]:
        return False
    elif number == 2:
        return True
    for i in [2, number-1]:
        if number%i == 0:
            return False
        else:
            return True 
