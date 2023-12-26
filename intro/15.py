"""Add Border Given a rectangular matrix of characters, add a border of asterisks(*) to it."""


def solution(picture: list[str]) -> list[str]:
    picture.insert(0, '*'*(len(picture[0])))
    picture.append('*'*(len(picture[0])))
    return ['*'+x+'*' for x in picture]


solution(["abc",
          "ded"])
