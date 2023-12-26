def solution(a):
    team_one = a[::2]
    team_tow = a[1::2]
    return [sum(team_one), sum(team_tow)]


res = solution([50, 60, 60, 45, 70])
print(res)
