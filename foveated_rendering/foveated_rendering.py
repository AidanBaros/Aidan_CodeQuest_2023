import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    y, x = (int(val) for val in line.split(SEPARATOR))

    fifties = [
        (x-1,y-1),
        (x,y-1),
        (x+1,y-1),
        (x-1,y),
        (x+1,y),
        (x-1,y+1),
        (x,y+1),
        (x+1,y+1),
        ]

    twentyfives = [
        (x-2,y-2),
        (x-1,y-2),
        (x,y-2),
        (x+1,y-2),
        (x+2,y-2),
        (x-2,y-1),
        (x+2,y-1),
        (x-2,y),
        (x+2,y),
        (x-2,y+1),
        (x+2,y+1),
        (x-2,y+2),
        (x-1,y+2),
        (x,y+2),
        (x+1,y+2),
        (x+2,y+2),
        ]

    map = [[ "10" for _ in range(0,20)] for _ in range(0,20)]

    map[y][x] = "100"
    for cord in fifties:
        if (cord[1] >= 0 and cord[1] <= 19) and (cord[0] >= 0 and cord[0] <= 19):
            map[cord[1]][cord[0]] = "50"
    for cord in twentyfives:
        if (cord[1] >= 0 and cord[1] <= 19) and (cord[0] >= 0 and cord[0] <= 19):
            map[cord[1]][cord[0]] = "25"

    for j in range(20):
        for i in range(20):
            if i == 19:
                print(map[j][i],end="")
            else:
                print(map[j][i],end=" ")
        print("")

    

    