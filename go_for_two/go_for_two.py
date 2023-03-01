import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

points_check = {
    -15:"2",
    -14:"1",
    -13:"2",
    -12:"1",
    -11:"2",
    -10:"2",
    -9:"1",
    -8:"2",
    -7:"1",
    -6:"1",
    -5:"2",
    -4:"2",
    -3:"1",
    -2:"2",
    -1:"1",
    0:"1",
    1:"2",
    2:"1",
    3:"1",
    4:"1",
    5:"2",
    6:"1",
    7:"1",
    8:"1",
    9:"1",
    10:"1",
    11:"1",
    12:"2",
}

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    team1, team2 = line.split(SEPARATOR)
    team1, team2 = int(team1), int(team2)

    dif = team1-team2
    if dif < -15 or dif > 12:
        print("1")
    else:
        print(points_check[team1-team2])