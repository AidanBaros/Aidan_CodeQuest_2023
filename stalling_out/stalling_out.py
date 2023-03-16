"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        attack, sensor1, sensor2 = (float(val) for val in line.split(" "))

        if sensor1 - sensor2 > 5 or sensor1 - sensor2 < -5:
            print("WARNING")
        elif (sensor1 + sensor2)/2 > attack + 2:
            print("ALARM")
        else:
            print("OK")


main()