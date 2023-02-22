import sys
import math
import string


cases = int(sys.stdin.readline().rstrip())

alphabet = {
    "a":"Alpha","b":"Bravo",
    "c":"Charlie","d":"Delta",
    "e":"Echo","f":"Foxtrot",
    "g":"Golf","h":"Hotel",
    "i":"India","j":"Juliet",
    "k":"Kilo","l":"Lima",
    "m":"Mike","n":"November",
    "o":"Oscar","p":"Papa",
    "q":"Quebec","r":"Romeo",
    "s":"Sierra","t":"Tango",
    "u":"Uniform","v":"Victor",
    "w":"Whiskey","x":"Xray",
    "y":"Yankee","z":"Zulu",
}

for caseNum in range(cases):
    cases2 = int(sys.stdin.readline().rstrip())
    for caseNumNum in range(cases2):
        line = sys.stdin.readline().rstrip().lower()
        message = ""

        for i, char in enumerate(line):
            if char == ' ':
                message += " "
            else:
                if line[i-1] != " " and char != " " and i != 0:
                    message += "-"
                message += alphabet[char]
                
        print(message)