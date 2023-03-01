import sys
import math
import string

SEPARATOR = ":"

cases = int(sys.stdin.readline().rstrip())

country_list = []

for caseNum in range(cases):
    country_list.append(sys.stdin.readline().rstrip())

country_list.sort()
for country in country_list:
    print(country)
