"""System Module"""
import sys

class Ship():
    def __init__(self, ship_name, ship_class, xpos, ypos):
        self.ship_name = ship_name
        self.ship_class = ship_class
        self.xpos = xpos
        self.ypos = ypos

def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        list_of_ships:list[Ship] = []
        cases2 = int(sys.stdin.readline().rstrip())
        for _ in range(cases2):
            line = sys.stdin.readline().rstrip()
            ship, pos = line.split(":")
            ship_name, ship_class = ship.split("_")
            xpos, ypos = pos.split(",")
            list_of_ships.append(Ship(ship_name, ship_class, int(xpos), int(ypos)))

        for ship in list_of_ships:
            ships = list_of_ships.copy()
            ships.sort(key=lambda x: x.xpos)
            check_xpos = ships[0].xpos
            check_xpos_list:list[Ship] = []
            for j in ships:
                if j.xpos == check_xpos:
                    check_xpos_list.append(j)
            check_xpos_list.sort(key=lambda x: x.ypos,reverse=True)
            print(f"Destroyed Ship: {check_xpos_list[0].ship_name} xLoc: {check_xpos_list[0].xpos}")
            ships.pop(0)
            for s in ships:
                if s.ship_class == "A":
                    s.xpos -= 10
                elif s.ship_class == "B":
                    s.xpos -= 20
                elif s.ship_class == "C":
                    s.xpos -= 30
main()