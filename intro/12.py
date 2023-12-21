'''Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!'''


def solution(a: list[int]):
    heights = [i for i in a if i != -1]
    trees_index = [i for i, value in enumerate(a) if value == -1]
    heights.sort()

    for tree in trees_index:
        heights.insert(tree, -1)

    return heights


solution([-1, 150, 190, 170, -1, -1, 160, 180])
