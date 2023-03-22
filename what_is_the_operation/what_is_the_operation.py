"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        equation = line.split(" ")

        if int(equation[0]) + int(equation[1]) == int(equation[2]):
            print("Addition")
        elif int(equation[0]) - int(equation[1]) == int(equation[2]):
            print("Subtraction")
        elif int(equation[0]) * int(equation[1]) == int(equation[2]):
            print("Multiplication")
        elif int(equation[0]) // int(equation[1]) == int(equation[2]):
            print("Division")
        elif int(equation[0]) % int(equation[1]) == int(equation[2]):
            print("Modulo")



main()