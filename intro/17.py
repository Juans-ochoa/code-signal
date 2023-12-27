'''You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.'''


def solution(array):
    count = 0

    for i in range(len(array) - 1):
        if array[i] >= array[i+1]:
            operation = abs(array[i] - array[i+1]) + 1
            count += operation
            array[i+1] += operation

    return count


# solution([1, 1, 1])
# solution([2, 1, 10, 1])
solution([-1000, 0, -2, 0])
