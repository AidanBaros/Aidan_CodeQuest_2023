import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    isbn = sys.stdin.readline().rstrip()

    total = 0
    for i, digit in enumerate(isbn[0:9]):
        digit = 10 if digit == "X" else int(digit)
        total += digit*(10-i)

    total += (10 if isbn[9] == "X" else int(isbn[9]))
    print("VALID" if total % 11 == 0 else "INVALID")