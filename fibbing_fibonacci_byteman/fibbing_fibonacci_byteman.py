import sys
import math
import string


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    num = int(sys.stdin.readline().rstrip())

    fib_list = []
    check_num = 1
    check_last_num = 0
    check_new_num = 0

    while True:
        if num == 0:
            print("TRUE")
            break
        check_new_num = check_num + check_last_num
        check_num, check_last_num = check_new_num, check_num
        fib_list.append(check_new_num)
        if fib_list[-1] == num:
            print("TRUE")
            break
        elif fib_list[-1] > num:
            print("FALSE")
            break
