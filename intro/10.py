'''Given two strings, find the number of common characters between them.'''


def solution(str1: str, str2: str):
    dict_word = {}
    for s1 in str1:
        if (s1 in str2 and dict_word.get(s1) is None):
            dict_word[s1] = min([str1.count(s1), str2.count(s1)])
    acc = 0
    for i in dict_word:
        acc += dict_word[i]
    return acc


print(solution('aabcc', 'adcaa'))
