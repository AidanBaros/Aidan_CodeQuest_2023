
import sys
import math
import string

SEPARATOR = ":"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    VowelList = ["a","e","i","o","u"]
    NumVowels = 0
    for char in line:
        if char in VowelList:
            NumVowels += 1
    print(NumVowels)