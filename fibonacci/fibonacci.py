import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    num = int(sys.stdin.readline().rstrip())

    check_num = 1
    check_last_num = 0
    check_new_num = 0

    for i in range(num-1):
        check_new_num = check_num + check_last_num
        check_num, check_last_num = check_new_num, check_num
        
    print(f"{num} = {check_last_num}")