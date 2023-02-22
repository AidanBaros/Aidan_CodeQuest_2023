import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    speed, is_birthday = line.split(SEPARATOR)
    bday_mod = 0
    if is_birthday == "true":
        bday_mod = 5

    if int(speed) <= 60 + bday_mod:
        print("no ticket")
    elif int(speed) <= 80 + bday_mod:
        print("small ticket")
    elif int(speed) > 80 + bday_mod:
        print("big ticket")