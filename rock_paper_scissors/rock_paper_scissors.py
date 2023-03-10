"""System Module"""
import sys


def main():
    check_list = ["P", "R", "S"]
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        hands = line.split(" ")
        r_num = 0
        p_num = 0
        s_num = 0
        R_wins = 0
        P_wins = 0
        S_wins = 0
        for hand in hands:
            if hand == "R":
                r_num += 1
            elif hand == "P":
                p_num += 1
            elif hand == "S":
                s_num += 1
        for hand in hands:
            for fingers in hands:
                if hand == "R":
                    if fingers == "S":
                        R_wins += 1
                elif hand == "P":
                    if fingers == "R":
                        P_wins += 1
                elif hand == "S":
                    if fingers == "P":
                        S_wins += 1
        if max(R_wins, P_wins, S_wins) == 0 or min(R_wins, P_wins, S_wins) > 0:
            print("NO WINNER")
        elif R_wins >= 1 and max(P_wins, S_wins) == 0 and r_num == 1:
            print("ROCK")
        elif P_wins >= 1 and max(R_wins, S_wins) == 0 and p_num == 1:
            print("PAPER")
        elif S_wins >= 1 and max(P_wins, R_wins) == 0 and s_num == 1:
            print("SCISSORS")
        else:
            print("NO WINNER")



main()