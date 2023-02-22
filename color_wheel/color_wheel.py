import sys

cases = int(sys.stdin.readline().rstrip())

color_wheel = {
    "red":"No colors need to be mixed to make red.",
    "red-violet":"In order to make red-violet, blue and red must be mixed.",
    "violet":"In order to make violet, blue and red must be mixed.",
    "blue-violet":"In order to make blue-violet, blue and red must be mixed.",
    "blue":"No colors need to be mixed to make blue.",
    "blue-green":"In order to make blue-green, blue and yellow must be mixed.",
    "green":"In order to make green, blue and yellow must be mixed.",
    "yellow-green":"In order to make yellow-green, blue and yellow must be mixed.",
    "yellow":"No colors need to be mixed to make yellow.",
    "yellow-orange":"In order to make yellow-orange, red and yellow must be mixed.",
    "orange":"In order to make orange, red and yellow must be mixed.",
    "red-orange":"In order to make red-orange, red and yellow must be mixed.",
}

for caseNum in range(cases):
    color = sys.stdin.readline().rstrip()

    print(color_wheel[color])
    