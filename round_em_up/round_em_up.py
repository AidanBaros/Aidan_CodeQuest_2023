"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        numbers = [int(val) for val in line.split(" ")]
        for i in range(len(numbers)):
            if numbers[i]%2 == 0:
               numbers[i] += 2
            else:
                numbers[i] += 1
        print(*numbers)


main()