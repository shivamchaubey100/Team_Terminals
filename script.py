import random
import math

name = "my.py"

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

def setIslandCoordinatesToTeamSignal(pirate):
    if (islandNameAndCoord(pirate)!=''):
        raw_string = pirate.getTeamSignal()
        island_number = int(islandNameAndCoord(pirate)[0]) 
        strinG = ''.join(islandNameAndCoord(pirate)[1])
        new_string = raw_string[:(island_number-1)*4] + strinG + raw_string[island_number*4:]
        pirate.setTeamSignal(new_string)

def select_movement(x0, y0, x1, y1, factor=0.1):
    # Calculate differences
    dx = x0 - x1
    dy = y0 - y1

    # Calculate probabilities based on exponential of differences
    prob_decrease_y = math.exp(0.1*dy)
    prob_increase_x = math.exp(0.1*dx)
    prob_increase_y = math.exp(-0.1*dy)
    prob_decrease_x = math.exp(-0.1*dx)

    # Normalize probabilities
    total_prob = prob_decrease_y + prob_increase_x + prob_increase_y + prob_decrease_x
    prob_decrease_y /= total_prob
    prob_increase_x /= total_prob
    prob_increase_y /= total_prob
    prob_decrease_x /= total_prob

    # Randomly select a movement based on probabilities
    rand = random.uniform(0, 1)
    if rand < prob_decrease_y:
        return 1
    elif rand < prob_decrease_y + prob_increase_x:
        return 2
    elif rand < prob_decrease_y + prob_increase_x + prob_increase_y:
        return 3
    else:
        return 4

#this function will make the pirate move around the given coordinates
def moveAround(pirate,x0, y0, factor=0.1) :
    (x1,y1) = pirate.getPosition()
    #issue resolved: if the pirate is at the centre then it will take the next step randomly
    return select_movement(x0,y0,x1,y1,factor)





#pre-conditions: the coordinates of the captured island are known
#this function will return an integer cooresopnding to movement if the pirate id belongs to a particular gropup of defenders and 
#that island has been captured

#to add, building walls 
#how will they respond to enemy
def DenfenceFunction(pirate):

    #to implement: prevent all the functions from returning move which takes them towars wall when they are adjacent to a wall
    if (pirate.getSignal()[4]=='d'):
        raw_string = pirate.getTeamSignal()
        
        if (raw_string[48]==1):
                #it is expected that the team signals are stored in such a way that the characters from index 12 to 47 belong to the ids of first 
            defender_ids = pirate.getTeamSignal()[12:24]
                #so defender_ids will be a string of length 12
                #extracting individual ids of each pirate
            for i in range(0,12,2):
                if (int(pirate.getID())==int(defender_ids[i:i+2])) :
                    island_coords = pirate.getTeamSignal()[0:4]
                    x0 = int(island_coords[0:2])
                    y0 = int(island_coords[2:4])
                    if (pirate.trackPlayers[0]!='myCaptured'):
                        return moveAround(pirate,x0,y0,10) #tell the pirates to converge around when their designated island is out of reach
                    else: 
                        return moveAround(pirate,x0,y0)
                    
        if (raw_string[49]==2):
            #it is expected that the team signals are stored in such a way that the characters from index 12 to 47 belong to the ids of first 
            defender_ids = pirate.getTeamSignal()[24:36]
            #so defender_ids will be a string of length 12
            #extracting individual ids of each pirate
            for i in range(0,12,2):
                if (int(pirate.getID())==int(defender_ids[i:i+2])) :
                    island_coords = pirate.getTeamSignal()[4:8]
                    x0 = int(island_coords[0:2])
                    y0 = int(island_coords[2:4])
                    if (pirate.trackPlayers[1]!='myCaptured'):
                        return moveAround(pirate,x0,y0,10)
                    else: 
                        return moveAround(pirate,x0,y0)                                  

        if (raw_string[50]==1):
                #it is expected that the team signals are stored in such a way that the characters from index 12 to 47 belong to the ids of first 
                defender_ids = pirate.getTeamSignal()[36:48]
                #so defender_ids will be a string of length 12
                #extracting individual ids of each pirate
                for i in range(0,12,2):
                    if (int(pirate.getID())==int(defender_ids[i:i+2])) :
                        island_coords = pirate.getTeamSignal()[8:12]
                        x0 = int(island_coords[0:2])
                        y0 = int(island_coords[2:4])
                        if (pirate.trackPlayers[2]!='myCaptured'):
                            return moveAround(pirate,x0,y0,10)
                        else: 
                            return moveAround(pirate,x0,y0)                         



def ActPirate(pirate):
    xDim=pirate.getDimensionX()
    yDim=pirate.getDimensionY()
    id=pirate.getID()
    #set the first string of the signal to be the pirate id, this will be used in team signals
    sig = id
    #next lines of code should come here
    setIslandCoordinatesToTeamSignal(pirate)        
    #this should be the last line
    pirate.setSignal(sig)

    

def ActTeam(team):
    

    #this should be at the top
    if (team.getTeamSignal == ''):
        string = ''.zfill(100)
        team.setTeamSignal(string)
    
    #below block of code (3 if statements) will set the team signal index 48,49 and 50 to the islands which we have captured or are attempting to capture    
    if(team.getTeamSignal()[48]==0) :
        if (team.trackPlayers()[0]=='myCaptured' or team.trackPlayers()[0]=='myCapturing'):
            string = team.getTeamSignal()
            sig = string[0:48] + '1' + string[49:100] 
            team.setTeamSignal(sig)

    if(team.getTeamSignal()[49]==0) :
        if (team.trackPlayers()[1]=='myCaptured' or team.trackPlayers()[1]=='myCapturing'):
            string = team.getTeamSignal()
            sig = string[0:49] + '2' + string[50:100] 
            team.setTeamSignal(sig)    

    if(team.getTeamSignal()[50]==0) :
        if (team.trackPlayers()[2]=='myCaptured' or team.trackPlayers()[2]=='myCapturing'):
            string = team.getTeamSignal()
            sig = string[0:50] + '3' + string[51:100] 
            team.setTeamSignal(sig)        

    get_my_status = team.getTeamSignal()
    status = team.trackPlayers()
    if (status[0]=='' and status[3]==''):
        r1 = '5'
    elif (status[0]=='myCaptured' and status[3]=='oppCapturing'):
        r1 = '1'
    elif (status[0]=='myCapturing'):
        r1 = '2'
    elif (status[0]=='myCaptured' and status[3]==''):
        r1 = '4'
    else: 
        r1 = '0'

    if (status[1]=='' and status[4]==''):
        r2 = '5'
    elif (status[1]=='myCaptured' and status[4]=='oppCapturing'):
        r2 = '1'
    elif (status[1]=='myCapturing'):
        r2 = '2'
    elif (status[1]=='myCaptured' and status[4]==''):
        r2 = '4'
    else :
        r2 = '0'

    if (status[2]=='' and status[4]==''):
        r3 = '5'
    elif (status[2]=='myCaptured' and status[5]=='oppCapturing'):
        r3 = '1'
    elif (status[2]=='myCapturing'):
        r3 = '2'
    elif (status[2]=='myCaptured' and status[5]==''):
        r3 = '4'
    else :
        r3 = '0'
    
    #now build wall under certain conditions
    if (r1==1 or (get_my_status[51]=='1' and r1=='4' ) or (get_my_status[51]=='5' and r1=='4')  ):
        team.buildWalls(1)
    if (r2==1 or (get_my_status[52]=='1' and r2=='4' ) or (get_my_status[52]=='5' and r2=='4')  ):
        team.buildWalls(2)
    if (r3==1 or (get_my_status[53]=='1' and r2=='4' ) or (get_my_status[53]=='5' and r3=='4')  ):
        team.buildWalls(3)
        

    
    alive_players=[]
    for string in team.getListOfSignals():
        raw = string.split()
        alive_players.append(raw[0])
    print(alive_players)

    
    #THIS CODE SHOULD COME AT THE END OF THE LOOP
    #storing the island status in team signal
    sigma = team.getTeamSignal() 
    #will be used to make walls
    status = team.trackPlayers()
    
    if (status[0]=='' and status[3]==''):
        r1 = '5'
    elif (status[0]=='myCaptured' and status[3]=='oppCapturing'):
        r1 = '1'
    elif (status[0]=='myCapturing'):
        r1 = '2'
    elif (status[3]=='myCaptured'):
        r1 = '4'
    else: 
        r1 = '0'

    if (status[1]=='' and status[4]==''):
        r2 = '5'
    elif (status[1]=='myCaptured' and status[4]=='oppCapturing'):
        r2 = '1'
    elif (status[1]=='myCapturing'):
        r2 = '2'
    elif (status[4]=='myCaptured'):
        r2 = '4'
    else :
        r2 = '0'

    if (status[2]=='' and status[4]==''):
        r3 = '5'
    elif (status[2]=='myCaptured' and status[5]=='oppCapturing'):
        r3 = '1'
    elif (status[2]=='myCapturing'):
        r3 = '2'
    elif (status[4]=='myCaptured'):
        r3 = '4'
    else :
        r3 = '0'
    

    final_sig = sigma[:51] + r1 + r2 + r3 +   sigma[54:]
    
        


    

