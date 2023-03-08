"""System Module"""
import sys

vowels = ["a","e","i","o","u"]

def main():

    cases = int(sys.stdin.readline().rstrip())
    check = False
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        for i, char in enumerate(line):
            if char in (vowels) and not check:
                print(line[i+1],end="")
                check = True
            else:
                check = False
        print()


main()