import sys

SEPARATOR1 = " "
SEPARATOR2 = "-"

cases = int(sys.stdin.readline().rstrip())
key = sys.stdin.readline().rstrip()

for caseNum in range(cases-1):
    line = sys.stdin.readline().rstrip()

    words = line.split(SEPARATOR1)
    for i, word in enumerate(words):
        words[i] = word.split(SEPARATOR2) # type: ignore   

    for i, word in enumerate(words):
        for letter in word:
            letter = int(letter)
            print(key[letter-1],end="")
        if i < len(words)-1:
            print(" ",end="")
    print()
             
