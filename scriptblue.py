import random
import math

name = "scriptblue"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

Mdim= [40,40]
# island_coord1 = [0,0]
# island_coord2 = [0,0]
# island_coord3 = [0,0]


def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    global island_coord1, island_coord2,   island_coord3
    island_coord1 = [0,0]
    island_coord2 = [0,0]
    island_coord3 = [0,0]
    # if pirate.getID() == 1 and pirate.getCurrentFrame()==100:
    #     return 0

    # stop one of the pirates from moving if island is captured
    # print(pirate.getID())
    # if pirate.getID() == 1 and s[0] == "myCaptured":
    #     print("pirate1 stopped")
    #     return 0
    # if pirate.getID() == 2 and s[1] == "myCaptured":
    #     print("pirate2 stopped")
    #     return 0
    # if pirate.getID() == 3 and s[2] == "myCaptured":
    #     print("pirate3 stopped")
    #     return 0
    if pirate.getID() == '1':
        # print(pirate.getPosition())
        return moveTo(20,20,pirate)
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):  
        if(up == "island1"):
            island_coord1 = [x,y-1]
        elif(up == "island2"):
            island_coord2 = [x,y-1]
        elif(up == "island3"):
            island_coord3 = [x,y-1]
        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        if(down == "island1"):
            island_coord1 = [x,y-1]
        elif(down == "island2"):
            island_coord2 = [x,y-1]
        elif(down == "island3"):
            island_coord3 = [x,y-1]
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        if(left == "island1"):
            island_coord1 = [x,y-1]
        elif(left == "island2"):
            island_coord2 = [x,y-1]
        elif(left == "island3"):
            island_coord3 = [x,y-1]
        s = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        if(right == "island1"):
            island_coord1 = [x,y-1]
        elif(right == "island2"):
            island_coord2 = [x,y-1]
        elif(right == "island3"):
            island_coord3 = [x,y-1]
        s = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(s)

    print(island_coord1)
    print(island_coord2)
    print(island_coord3)
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
    
        return moveTo(x, y, pirate)

    else:
        return random.randint(1, 4)


def ActTeam(team):
    xdim = team.getDimensionX()
    ydim = team.getDimensionY()
    Mdim = (xdim, ydim)
    l = team.trackPlayers()
    s = team.getTeamSignal()

    print(team.getDimensionX())
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
