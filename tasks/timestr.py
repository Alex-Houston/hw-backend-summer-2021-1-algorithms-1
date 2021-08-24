__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    """
    if seconds >= 86400:
        return f"{seconds // 86400}d{seconds // 3600 % 24}h{seconds // 60 % 60}m{seconds % 60}s"
    elif seconds >= 3600:
        return f"{seconds // 3600 % 24}h{seconds // 60 % 60}m{seconds % 60}s"
    elif seconds >= 60:
        return f"{seconds // 60 % 60}m{seconds % 60}s"
    else: 
        return f"{seconds % 60}s"
    """
    if seconds >= 86400:
        return "{0:0>2}d{1:0>2}h{2:0>2}m{3:0>2}s".format(seconds // 86400, seconds // 3600 % 24, seconds // 60 % 60, seconds % 60)
    if seconds >= 3600:
        return "{0:0>2}h{1:0>2}m{2:0>2}s".format(seconds // 3600 % 24, seconds // 60 % 60, seconds % 60)
    if seconds >= 60:
        return "{0:0>2}m{1:0>2}s".format(seconds // 60 % 60, seconds % 60)
    else:
        return "{0:0>2}s".format(seconds % 60)


