"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        word, index = line.split(" ")
        index = int(index)
        for i, char in enumerate(word):
            if i != index:
                print(char,end='')
        print()


main()