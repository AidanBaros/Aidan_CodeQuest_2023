"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        aluminum_can, plastic_bottle, glass_bottle  = (int(val) for val in line.split(" "))
        total = 0
        total += (aluminum_can*31)*0.05
        total += (plastic_bottle*15)*0.10
        total += (glass_bottle/2)*0.20
        print(f"${total:.2f}")


main()