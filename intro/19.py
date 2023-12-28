'''Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.'''


def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    yourStrong = max([yourLeft, yourRight])
    friendStrong = max([friendsLeft, friendsRight])

    if yourStrong != friendStrong:
        return False

    return sum([yourLeft, yourRight]) == sum([friendsLeft, friendsRight])


solution(10, 15, 5, 20)
