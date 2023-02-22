import sys
import math
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    temp, water, magnetic_field, eccentricity = line.split(SEPARATOR)
    temp = float(temp)
    eccentricity = float(eccentricity)

    if temp > 100:
        print("The planet is too hot.")
    elif temp < 0:
        print("The planet is too cold.")
    elif water == "false":
        print("The planet has no water.")
    elif magnetic_field == "false":
        print("The planet has no magnetic field.")
    elif eccentricity > 0.6:
        print("The planet's orbit is not ideal.")
    else:
        print("The planet is habitable.")