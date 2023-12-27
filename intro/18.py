'''Given a string, find out if its characters can be rearranged to form a palindrome.'''


def solution(string):
    print([string.count(i) % 2 for i in set(string)])
    return sum([string.count(i) % 2 for i in set(string)]) <= 1


solution('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc')
solution('zyyzzzzz')
