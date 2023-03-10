"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        misspell, correct = line.split(" ")
        not_legable = False
        for char in misspell:
            if char not in correct:
                not_legable = True

        if not not_legable and misspell[0] == correct[0] and misspell[-1] == correct[-1]:
            print(correct)
        else:
            print(misspell)


main()