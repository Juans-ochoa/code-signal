'''Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not'''


def solution(n):
    tikes = tuple(str(n))
    sum1, sum2 = 0, 0
    for i, value in enumerate(tikes):
        if (i <= len(tikes)/2 - 1):
            sum1 += int(value)
        else:
            sum2 += int(value)

    return sum1 == sum2


solution(1230)
