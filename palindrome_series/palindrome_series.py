"""System Module"""
import sys

def check_for_pal(pal:str):
    if len(pal)%2 == 1:
        pal = pal[:(len(pal)//2)] + pal[(len(pal)//2)+1:]
    if pal == pal[::-1]:
        return True
    return False
    


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        cases2 = int(sys.stdin.readline().rstrip())
        not_pal:list[int] = []
        for i in range(cases2):
            line = sys.stdin.readline().rstrip().lower()
            check = check_for_pal(line)
            if not check:
                not_pal.append(i+1)
        if len(not_pal) == 0:
            print("True")
        else:
            print(f"False - ",end='')
            print(*not_pal,sep=", ")


main()