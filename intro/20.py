'''Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.'''


def solution(array):
    return max(abs(array[i-1] - array[i]) for i in range(1, len(array)))


solution([2, 4, 1, 0])
