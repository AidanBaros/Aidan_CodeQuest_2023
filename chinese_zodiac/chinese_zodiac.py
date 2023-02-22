import sys
import math
import string

SEPARATOR = ":"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    year = int(sys.stdin.readline().rstrip())
    yin_or_yang = ""
    element = ""
    element_list = ["Wood", "Fire", "Earth", "Metal", "Water"]
    animal = ""
    animal_list = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

    if year % 2 == 0:
        yin_or_yang = "Yang"
    else:
        yin_or_yang = "Yin"

    element = element_list[((year - 4) % 10)//2]

    animal = animal_list[(year - 4) % 12]

    message = f"{year} {yin_or_yang} {element} {animal}"

    print(message)