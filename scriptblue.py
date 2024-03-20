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

def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()[1]
    # print(up)
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum
    
def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
   
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 , y == 0):
        return random.randint(1,4)
    
    if(sorted_dict[list(sorted_dict())[3]] == 0 ):
        return random.randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)

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
    if (islandNameAndCoord(pirate)!=None):
        raw_string = pirate.getTeamSignal()
        island_number = int(islandNameAndCoord(pirate)[0])
        strinG = ''.join(islandNameAndCoord(pirate)[1])
        new_string = raw_string[:(island_number-1)*4] + strinG + raw_string[island_number*4:]
        pirate.setTeamSignal(new_string)           

def is_between(value, var1, var2):
    lower_bound = min(var1, var2)
    upper_bound = max(var1, var2)
    return lower_bound <= value <= upper_bound

def attack1(pirate):
    xmid= pirate.getDimensionX()/2
    ymid= pirate.getDimensionY()/2

    xdep= pirate.getDeployPoint()[0]
    ydep= pirate.getDeployPoint()[1]
    if xdep==0:
        xopp= xdep+ 2*xmid
    else:
        xopp= 0
    
    if ydep== 0:
        yopp = ydep + 2*ymid
    else:
        yopp= 0
    xmopp= (xopp+xmid)/2
    ymopp= (yopp+ ymid)/2

    pos= pirate.getPosition()

    if is_between(pos[0], xmid, xopp) and is_between(pos[1], ymid, yopp):
        isnum= 0
        for i in range(1,4):
            if pirate.investigate_current()[0] == f'island{i}':
                isnum= i
        if isnum != 0: 
            raw_string = pirate.getTeamSignal()       
            if pirate.trackPlayers()[i-1] != 'myCaptured' and pirate.getTeamSignal()[57] != 'p':           
                new_string = raw_string[:57] + f'p{isnum}' + raw_string[59:]           
            else:
                new_string = raw_string[:57] + f'c{isnum}' + raw_string[59:]                
            pirate.setTeamSignal(new_string)
            
        
        if len(pirate.getTeamSignal())>57 and pirate.getTeamSignal()[57] == 'p':
            isnum= int(pirate.getTeamSignal()[58])
            xcord= int(pirate.getTeamSignal()[(isnum-1)*4:4*(isnum-1)+2])
            ycord= int(pirate.getTeamSignal()[4*(isnum-1)+2:4*(isnum-1)+4])        
            return moveTo(xcord, ycord, pirate)
    if is_between(pos[0], xmid, xopp) and is_between(pos[1], ymid, yopp):
        return spread(pirate)
    else:
        return moveTo(xmopp, ymopp, pirate)

def attack2(pirate):
    xmid= pirate.getDimensionX()/2
    ymid= pirate.getDimensionY()/2

    xdep= pirate.getDeployPoint()[0]
    ydep= pirate.getDeployPoint()[1]

    x= (xdep+xmid)/2

    if ydep==0:
        yopp= pirate.getDimensionY()       
    else:
        yopp=0
    y= (yopp+ymid)/2
    pos= pirate.getPosition()

    if is_between(pos[0], xmid, xdep) and is_between(pos[1], ymid, yopp):
        isnum= 0
        for i in range(1,4):
            if pirate.investigate_current()[0] == f'island{i}':
                isnum= i
        if isnum != 0: 
            raw_string = pirate.getTeamSignal()       
            if pirate.trackPlayers()[i-1] != 'myCaptured' and pirate.getTeamSignal()[59] != 'p':           
                new_string = raw_string[:59] + f'p{isnum}' + raw_string[61:]           
            else:
                new_string = raw_string[:59] + f'c{isnum}' + raw_string[61:]                
            pirate.setTeamSignal(new_string)
            
        
        if len(pirate.getTeamSignal())>59 and pirate.getTeamSignal()[59] == 'p':
            isnum= int(pirate.getTeamSignal()[60])
            xcord= int(pirate.getTeamSignal()[(isnum-1)*4:4*(isnum-1)+2])
            ycord= int(pirate.getTeamSignal()[4*(isnum-1)+2:4*(isnum-1)+4])        
            return moveTo(xcord, ycord, pirate)

    if is_between(pos[0], xmid, xdep) and is_between(pos[1], ymid,yopp):
        return spread(pirate)
    else:
        return moveTo(x, y, pirate)

def attack3(pirate):
    xmid= pirate.getDimensionX()/2
    ymid= pirate.getDimensionY()/2

    xdep= pirate.getDeployPoint()[0]
    ydep= pirate.getDeployPoint()[1]

    y= (ydep+ymid)/2

    if xdep==0:
        xopp= pirate.getDimensionX()       
    else:
        xopp=0
    x= (xopp+xmid)/2
    pos= pirate.getPosition()

    if is_between(pos[0], xmid, xopp) and is_between(pos[1], ymid, ydep):
        isnum= 0
        for i in range(1,4):
            if pirate.investigate_current()[0] == f'island{i}':
                isnum= i
        if isnum != 0: 
            raw_string = pirate.getTeamSignal()       
            if pirate.trackPlayers()[i-1] != 'myCaptured' and pirate.getTeamSignal()[61] != 'p':           
                new_string = raw_string[:61] + f'p{isnum}' + raw_string[63:]           
            else:
                new_string = raw_string[:61] + f'c{isnum}' + raw_string[63:]                
            pirate.setTeamSignal(new_string)
            
        
        if len(pirate.getTeamSignal())>61 and pirate.getTeamSignal()[61] == 'p':
            isnum= int(pirate.getTeamSignal()[62])
            xcord= int(pirate.getTeamSignal()[(isnum-1)*4:4*(isnum-1)+2])
            ycord= int(pirate.getTeamSignal()[4*(isnum-1)+2:4*(isnum-1)+4])        
            return moveTo(xcord, ycord, pirate)

    if is_between(pos[0], xmid, xopp) and is_between(pos[1], ymid,ydep):
        return spread(pirate)
    else:
        return moveTo(x, y, pirate)

def ActPirate(pirate):

    if pirate.getTeamSignal() == '':
        string= ''.zfill(100)
        pirate.setTeamSignal(string)

    print(pirate.getTeamSignal())
    setIslandCoordinatesToTeamSignal(pirate)

    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    
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
    
    for i in range(3):
        if s[i] == "myCaptured":
            signalTeam = pirate.getTeamSignal()[12+12*i:12+12*(i+1)]
            for j in range(6):
                if ids == int(signalTeam[j*2:j*2+2]):
                    signal = sid + "d" 
                    pirate.setSignal(signal)
    
    if pirate.getID() == '1':
        return moveTo(20,20,pirate)

    # if (
    #     (up == "island1" and s[0] != "myCaptured")
    #     or (up == "island2" and s[1] != "myCaptured")
    #     or (up == "island3" and s[2] != "myCaptured")
    # ):  
    #     if(up == "island1"):
    #         island_coord1 = [x,y-1]
    #     elif(up == "island2"):
    #         island_coord2 = [x,y-1]
    #     elif(up == "island3"):
    #         island_coord3 = [x,y-1]
    #     s = up[-1] + str(x) + "," + str(y - 1)
    #     pirate.setTeamSignal(s)

    # if (
    #     (down == "island1" and s[0] != "myCaptured")
    #     or (down == "island2" and s[1] != "myCaptured")
    #     or (down == "island3" and s[2] != "myCaptured")
    # ):
    #     if(down == "island1"):
    #         island_coord1 = [x,y-1]
    #     elif(down == "island2"):
    #         island_coord2 = [x,y-1]
    #     elif(down == "island3"):
    #         island_coord3 = [x,y-1]
    #     s = down[-1] + str(x) + "," + str(y + 1)
    #     pirate.setTeamSignal(s)

    # if (
    #     (left == "island1" and s[0] != "myCaptured")
    #     or (left == "island2" and s[1] != "myCaptured")
    #     or (left == "island3" and s[2] != "myCaptured")
    # ):
    #     if(left == "island1"):
    #         island_coord1 = [x,y-1]
    #     elif(left == "island2"):
    #         island_coord2 = [x,y-1]
    #     elif(left == "island3"):
    #         island_coord3 = [x,y-1]
    #     s = left[-1] + str(x - 1) + "," + str(y)
    #     pirate.setTeamSignal(s)

    # if (
    #     (right == "island1" and s[0] != "myCaptured")
    #     or (right == "island2" and s[1] != "myCaptured")
    #     or (right == "island3" and s[2] != "myCaptured")
    # ):
    #     if(right == "island1"):
    #         island_coord1 = [x,y-1]
    #     elif(right == "island2"):
    #         island_coord2 = [x,y-1]
    #     elif(right == "island3"):
    #         island_coord3 = [x,y-1]
    #     s = right[-1] + str(x + 1) + "," + str(y)
    #     pirate.setTeamSignal(s)

    # print(island_coord1)
    # print(island_coord2)
    # print(island_coord3)
    # print(islandNameAndCoord(pirate))

    return attack2(pirate)

    for i in range(1,4):
        if pirate.investigate_current()[0] == f"island{i}":
            if pirate.trackPlayers()[i-1] != "myCaptured":
                return 0
    if "myCaptured" not in pirate.trackPlayers():
        return spread(pirate)
    else:
        if(pirate.getSignal()[3] == 'a'):
            signal = pirate.getSignal()
            if(len(signal)== 4):
                signal = signal[:4] + f'{random.randint(0,1)}'
                pirate.setSignal(signal)

    
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        # x = int(l[0][1:])
        # y = int(l[1])
    
    #     return moveTo(x, y, pirate)

    # else:
    return random.randint(1, 4)


def ActTeam(team):
    if team.getTeamSignal() == '':
        string= ''.zfill(100)
        team.setTeamSignal(string)
    xdim = team.getDimensionX()
    ydim = team.getDimensionY()
    Mdim = (xdim, ydim)
    l = team.trackPlayers()
    s = team.getTeamSignal()
    
    alive_players=[]
    # print(team.getListOfSignals())
    # if team.getListOfSignals() !=['', '', '', '', '', '', '', '']:
    for string in team.getListOfSignals():
        lists = string.split()
        if lists != []:
            strl= lists[0]
            alive_players.append(strl[1:3])
            # print(lists[0])
    
    def_alive= alive_players[:18]
    sig_alive = ''.join(def_alive)
    # print(sig_alive)
    raw_string = team.getTeamSignal()
    new_string = raw_string[:12] + sig_alive + raw_string[48:]
    team.setTeamSignal(new_string)

    #Only for testing
    raw_string = team.getTeamSignal()
    new_string = raw_string[:48] + 'charaterss' + raw_string[57:]
    team.setTeamSignal(new_string)


    # print(team.getListOfSignals())
    # print(alive_players)    
    # print(team.getListOfSignals())
    # print(team.getDimensionX())
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    # if s:
    #     island_no = int(s[0])
    #     signal = l[island_no - 1]
    #     if signal == "myCaptured":
    #         team.setTeamSignal("")
