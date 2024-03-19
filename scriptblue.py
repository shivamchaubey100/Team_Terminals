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

#will return the island number and the centre coordinates of the island
def format_number(num):
    if num < 10:
        return f"0{num}"
    else:
        return str(num)
def islandNameAndCoord(pirate):
    (x,y) = pirate.getPosition() 
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]

    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (se=='wall' or se=='blank') and (right=='wall' or right=='blank') and (ne=='island1' or ne=='island2' or ne=='island3')):
        return [ne[-1],[format_number(x+2),format_number(y-2)]]    
    
    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (se=='wall' or se=='blank') and (right=='island1' or right=='island2' or right=='island3') and (ne=='island1' or ne=='island2' or ne=='island3')):
        return [ne[-1],[format_number(x+2),format_number(y-1)]]
    
    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (se=='island1' or se=='island2' or se=='island3' ) and (right=='island1'  or right=='island2' or right=='island3') and (ne=='island1' or ne=='island2' or ne=='island3')):
        return [ne[-1],[format_number(x+2),format_number(y)]]

    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (ne=='wall' or ne=='blank') and (right=='island1') and (se=='island1')):
        return [1, [format_number(x+2), format_number(y+1)]]
    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (ne=='wall' or ne=='blank') and (right=='island2') and (se=='island2')):
        return [2, [format_number(x+2), format_number(y+1)]]
    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (ne=='wall' or ne=='blank') and (right=='island3') and (se=='island3')):
        return [3, [format_number(x+2), format_number(y+1)]]

    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='island1')):
        return [1, [format_number(x+2), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='island2')):
        return [2, [format_number(x+2), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='island3')):
        return [3, [format_number(x+2), format_number(y+2)]]
    #left side ka

    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='wall' or sw=='blank') and (left=='wall' or left=='blank') and (nw=='island1')):
        return [1, [format_number(x-2), format_number(y-2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='wall' or sw=='blank') and (left=='wall' or left=='blank') and (nw=='island2')):
        return [2, [format_number(x-2), format_number(y-2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='wall' or sw=='blank') and (left=='wall' or left=='blank') and (nw=='island3')):
        return [3, [format_number(x-2), format_number(y-2)]]
    
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='wall' or sw=='blank') and (left=='island1') and (nw=='island1')):
        return [1, [format_number(x-2), format_number(y-1)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='wall' or sw=='blank') and (left=='island2') and (nw=='island2')):
        return [2, [format_number(x-2), format_number(y-1)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='wall' or sw=='blank') and (left=='island3') and (nw=='island3')):
        return [3, [format_number(x-2), format_number(y-1)]]
    
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='island1') and (left=='island1') and (nw=='island1')):
        return [1, [format_number(x-2), format_number(y)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='island2') and (left=='island2') and (nw=='island2')):
        return [2, [format_number(x-2), format_number(y)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (sw=='island3') and (left=='island3') and (nw=='island3')):
        return [3, [format_number(x-2), format_number(y)]]

    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (nw=='wall' or nw=='blank') and (left=='island1') and (sw=='island1')):
        return [1, [format_number(x-2), format_number(y+1)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (nw=='wall' or nw=='blank') and (left=='island2') and (sw=='island2')):
        return [2, [format_number(x-2), format_number(y+1)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (nw=='wall' or nw=='blank') and (left=='island3') and (sw=='island3')):
        return [3, [format_number(x-2), format_number(y+1)]]

    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island1')):
        return [1, [format_number(x-2), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island2')):
        return [2, [format_number(x-2), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='wall' or down=='blank') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island3')):
        return [3, [format_number(x-2), format_number(y+2)]]

    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='island1') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island1')):
        return [1, [format_number(x-1), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='island2') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island2')):
        return [2, [format_number(x-1), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='wall' or sw=='blank') and (down=='island3') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island3')):
        return [3, [format_number(x-1), format_number(y+2)]]

    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='island1') and (down=='island1') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island1')):
        return [1, [format_number(x), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='island2') and (down=='island2') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island2')):
        return [2, [format_number(x), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (se=='island3') and (down=='island3') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (sw=='island3')):
        return [3, [format_number(x), format_number(y+2)]]

    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (sw=='wall' or sw=='blank') and (down=='island1') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (se=='island1')):
        return [1, [format_number(x+1), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (sw=='wall' or sw=='blank') and (down=='island2') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (se=='island2')):
        return [2, [format_number(x+1), format_number(y+2)]]
    if ((up=='wall' or up=='blank') and (ne=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (sw=='wall' or sw=='blank') and (down=='island3') and (nw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (se=='island3')):
        return [3, [format_number(x+1), format_number(y+2)]]

    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (ne=='wall' or nw=='blank') and (up=='island1') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (ne=='island1')):
        return [1, [format_number(x-1), format_number(y-2)]]
    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (ne=='wall' or nw=='blank') and (up=='island2') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (ne=='island2')):
        return [2, [format_number(x-1), format_number(y-2)]]
    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (ne=='wall' or nw=='blank') and (up=='island3') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (ne=='island3')):
        return [3, [format_number(x-1), format_number(y-2)]]

    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (ne=='wall' or nw=='blank') and (up=='island1') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (nw=='island1')):
        return [1, [format_number(x), format_number(y-2)]]
    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (ne=='wall' or nw=='blank') and (up=='island2') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (nw=='island2')):
        return [2, [format_number(x), format_number(y-2)]]
    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (ne=='wall' or nw=='blank') and (up=='island3') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (nw=='island3')):
        return [3, [format_number(x), format_number(y-2)]]

    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (nw=='wall' or nw=='blank') and (up=='island1') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (ne=='island1')):
        return [1, [format_number(x+1), format_number(y-2)]]
    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (nw=='wall' or nw=='blank') and (up=='island2') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (ne=='island2')):
        return [2, [format_number(x+1), format_number(y-2)]]
    if ((down=='wall' or down=='blank') and (se=='wall' or ne=='blank') and (right=='wall' or right=='blank') and (nw=='wall' or nw=='blank') and (up=='island3') and (sw=='wall' or nw=='blank') and (left=='wall' or left=='blank') and (ne=='island3')):
        return [3, [format_number(x+1), format_number(y-2)]]

           

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
    # global island_coord1, island_coord2,   island_coord3
    # island_coord1 = [0,0]
    # island_coord2 = [0,0]
    # island_coord3 = [0,0]
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
    ids= int(pirate.getID())
    #set the first string of the signal to be the pirate id, this will be used in team signals
    if 10<=ids<100:
        sid="0"+ str(ids)
    elif ids<10:
        sid="00"+ str(ids)
    else:
        sid=str(ids)
    sig= sid+ "a"
    pirate.setSignal(sig)
    ids= int(ids) 
    if s[0] == "myCaptured" and s[1] == "myCaptured" :
        if ids<=12:
            signal= sid + "d" 
            pirate.setSignal(signal)
        
    elif s[0]=="myCaptured" and s[2]=="myCaptured":
            if ids<=6 or 18>=ids>12:
                signal= sid + "d" 
                pirate.setSignal(signal)

    elif s[1]=="myCaptured" and s[2]=="myCaptured":
            if 18>=ids>6:
                signal= sid + "d" 
                pirate.setSignal(signal)    

    elif s[0]=="myCaptured":
            if ids<=6 :
                signal= sid + "d" 
                pirate.setSignal(sig)

    elif s[1]=="myCaptured":
            if 12>=ids>6:
                signal= sid + "d" 
                pirate.setSignal(signal)
    elif s[2]=="myCaptured":
            if 18>=ids>12:
                signal= sid + "d"
                pirate.setSignal(signal)

    if pirate.getID() == '1':
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

    # print(island_coord1)
    # print(island_coord2)
    # print(island_coord3)
    # print(islandNameAndCoord(pirate))

    
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

    alive_players=[]
    print(team.getListOfSignals())
    # if team.getListOfSignals() !=['', '', '', '', '', '', '', '']:
    for string in team.getListOfSignals():
        lists = string.split()
        # print(lists)
        if lists != []:
            alive_players.append(lists[0])
            # print(lists[0])
    
    # print(team.getListOfSignals())
    # print(alive_players)    
    # print(team.getListOfSignals())
    # print(team.getDimensionX())
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
