"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        check_list = ["11th", "12th", "13th"]
        if line[-3] == "1" and line[-4:] not in check_list:
            line = line.rstrip("th")
            line += "st"
        elif line[-3] == "2" and line[-4:] not in check_list:
            line = line.rstrip("th")
            line += "nd"
        elif line[-3] == "3" and line[-4:] not in check_list:
            line = line.rstrip("th")
            line += "rd"
        print(line)



main()