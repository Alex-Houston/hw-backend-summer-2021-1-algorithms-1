from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    minlen = 999
    maxlen = 0
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    while text.find('  ') != -1:
        text = text.replace('  ', ' ')

    for i in text.split(" "):
        if text.isspace() or len(text)<1:
            return None, None
        if len(i) > maxlen:
            maxlen = len(i)
            maxi = i
        if len(i) < minlen:
            minlen = len(i)
            mini = i
    return mini, maxi

