import sys
import math
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    num_of_sensors = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().rstrip()

    sensors_list = list(line.split(SEPARATOR))
    check_list = []

    sensors_list.sort()

    for i in range(num_of_sensors):
        check_list.append(i+1)
    
    for sensor in check_list:
        if str(sensor) not in sensors_list:
            print(sensor)