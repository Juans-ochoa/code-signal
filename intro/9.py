'''Given an array of strings, return another array containing all of its longest strings.'''


def solution(array: list[str]) -> list[str]:
    max_string_length = max([len(x) for x in array])
    return [word for word in array if len(word) == max_string_length]


print(solution(["aba", "aa", "ad", "vcd", "aba"]))
