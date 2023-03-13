"""System Module"""
import sys

def check_alive(pos, grid):
    num_alive = 0
    check_poses = [(-1,-1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)] 
    for poses in check_poses:
        try:
            check = grid[pos[1]+poses[1]][pos[0]+poses[0]]
            if pos[1]+poses[1] >= 0 and pos[0]+poses[0] >= 0 and pos[1]+poses[1] < 10 and pos[0]+poses[0] < 10:
                if grid[pos[1]+poses[1]][pos[0]+poses[0]] == 1:
                    num_alive += 1
        except:
            pass
    return num_alive        

def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        run_time = int(sys.stdin.readline().rstrip())
        grid:list[list[int]] = []
        for j in range (10):
            line = sys.stdin.readline().rstrip()
            grid.append([])
            for char in line:
                grid[j].append(int(char))
        
        for _ in range(run_time):
            out_grid = grid.copy()
            for j in range(10):
                for i in range(10):
                    num_alive = check_alive((i,j), grid)  
                    if num_alive <= 1 and grid[j][i] == 1:
                        out_grid[j][i] = 0
                    elif num_alive <= 3 and grid[j][i] == 1:
                        pass    
                    elif num_alive == 3 and grid[j][i] == 0:
                        out_grid[j][i] = 1
                    elif num_alive >= 4 and grid[j][i] == 1:
                        out_grid[j][i] = 0
            grid = out_grid.copy()
        for val in grid:
            for char in val:
                print(char,end='')
            print()

                    



        
        

main()