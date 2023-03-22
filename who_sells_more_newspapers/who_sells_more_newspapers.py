"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        times, harold = (int(val) for val in line.split(" "))
        if times > harold:
            print(f"Times has {times-harold} more subscribers")
        elif times < harold:
            print(f"Herald has {harold-times} more subscribers")
        else:
            print("Times and Herald have the same number of subscribers")


main()