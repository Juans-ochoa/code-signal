'''Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.'''


def solution(a, b):
    equal_list = sorted(a) == sorted(b)
    differences = [i for i in range(len(a)) if a[i] != b[i]]

    return len(differences) <= 2 and equal_list


solution([1, 1, 4], [1, 2, 3])
