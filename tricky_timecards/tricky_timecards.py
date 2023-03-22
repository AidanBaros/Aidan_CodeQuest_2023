"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        data = line.split(",")
        times = data[1:]
        hours = 0
        minutes = 0
        for time in times:
            h, m = time.split(":")
            hours += int(h)
            minutes += int(m)
        hours += minutes//60
        minutes = minutes%60
        if hours == 0:
            print(f"{data[0]}=1 minute" if minutes == 1 else f"{data[0]}={minutes} minutes")
        elif hours == 1 and minutes != 0:
            print(f"{data[0]}=1 hour 1 minute" if minutes == 1 else f"{data[0]}=1 hour {minutes} minutes")
        elif minutes == 0:
            print(f"{data[0]}=1 hour" if hours == 1 else f"{data[0]}={hours} hours")
        else:
            print(f"{data[0]}={hours} hours 1 minute" if minutes == 1 else f"{data[0]}={hours} hours {minutes} minutes")

main()