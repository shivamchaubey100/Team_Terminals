import random
import math

name = "scriptblue"


def checkIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]
    if up[:-1] == 'island':
        return [True, 1, up[-1]]
    elif down[:-1] == 'island':
        return [True, 2, down[-1]]
    elif left[:-1] == 'island':
        return [True, 3, left[-1]]
    elif right[:-1] == 'island':
        return [True, 4, right[-1]]
    elif ne[:-1] == 'island':
        return [True, 1, ne[-1]]
    elif nw[:-1] == 'island':
        return [True, 1, nw[-1]]
    elif se[:-1] == 'island':
        return [True, 2, se[-1]]
    elif sw[:-1] == 'island':
        return [True, 2, sw[-1]] 
    else:
        return [False]

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


def attack1(pirate,i):
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
    print(i)
    if( i == 1):
        xmopp= (xopp+3*xmid)/4
        ymopp= (3 * yopp+ ymid)/4
    elif( i == 2):
        xmopp= (3*xopp+xmid)/4
        ymopp= (3*yopp+ymid)/4
    elif(i==3):
        xmopp= (xopp+3*xmid)/4
        ymopp= (yopp+3*ymid)/4
    elif(i==4):
        xmopp= (3*xopp+xmid)/4
        ymopp= (yopp+3*ymid)/4         

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
            # return moveTo(xcord, ycord, pirate)
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

    # if is_between(pos[0], xmid, xdep) and is_between(pos[1], ymid, yopp):
    #     isnum= 0
    #     for i in range(1,4):
    #         if pirate.investigate_current()[0] == f'island{i}':
    #             isnum= i
    #     if isnum != 0: 
    #         raw_string = pirate.getTeamSignal()       
    #         if pirate.trackPlayers()[i-1] != 'myCaptured' and pirate.getTeamSignal()[59] != 'p':           
    #             new_string = raw_string[:59] + f'p{isnum}' + raw_string[61:]           
    #         else:
    #             new_string = raw_string[:59] + f'c{isnum}' + raw_string[61:]                
    #         pirate.setTeamSignal(new_string)
            
        
    #     if len(pirate.getTeamSignal())>59 and pirate.getTeamSignal()[59] == 'p':
    #         isnum= int(pirate.getTeamSignal()[60])
    #         xcord= int(pirate.getTeamSignal()[(isnum-1)*4:4*(isnum-1)+2])
    #         ycord= int(pirate.getTeamSignal()[4*(isnum-1)+2:4*(isnum-1)+4])        
    #         # return moveTo(xcord, ycord, pirate)

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
            # return moveTo(xcord, ycord, pirate)

    if is_between(pos[0], xmid, xopp) and is_between(pos[1], ymid,ydep):
        return spread(pirate)
    else:
        return moveTo(x, y, pirate)

def attack0(pirate):
    xmid= pirate.getDimensionX()/2
    ymid= pirate.getDimensionY()/2

    xdep= pirate.getDeployPoint()[0]
    ydep= pirate.getDeployPoint()[1]

    y= (ydep+ymid)/2
    x= (xdep+xmid)/2

    pos= pirate.getPosition()

    if is_between(pos[0], xmid, xdep) and is_between(pos[1], ymid, ydep):
        isnum= 0
        for i in range(1,4):
            if pirate.investigate_current()[0] == f'island{i}':
                isnum= i
        if isnum != 0: 
            raw_string = pirate.getTeamSignal()       
            if pirate.trackPlayers()[i-1] != 'myCaptured' and pirate.getTeamSignal()[63] != 'p':           
                new_string = raw_string[:63] + f'p{isnum}' + raw_string[65:]           
            else:
                new_string = raw_string[:63] + f'c{isnum}' + raw_string[65:]                
            pirate.setTeamSignal(new_string)
            
        
        if len(pirate.getTeamSignal())>63 and pirate.getTeamSignal()[63] == 'p':
            isnum= int(pirate.getTeamSignal()[64])
            xcord= int(pirate.getTeamSignal()[(isnum-1)*4:4*(isnum-1)+2])
            ycord= int(pirate.getTeamSignal()[4*(isnum-1)+2:4*(isnum-1)+4])        
            # return moveTo(xcord, ycord, pirate)

    if is_between(pos[0], xmid, xdep) and is_between(pos[1], ymid, ydep):
        return moveAround(pirate, x, y)
    else:
        return moveTo(x ,y, pirate)


def select_movement(x0, y0, x1, y1, factor=0.1):
    # Calculate differences
    dx = -( x0 - x1)
    dy = -(y0 - y1)

    # Calculate probabilities based on exponential of differences
    prob_decrease_y = math.exp(factor*dy)
    prob_increase_x = math.exp(factor*dx)
    prob_increase_y = math.exp(-factor*dy)
    prob_decrease_x = math.exp(-factor*dx)

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
        return 4
    elif rand < prob_decrease_y + prob_increase_x + prob_increase_y:
        return 3
    else:
        return 2

#this function will make the pirate move around the given coordinates
def moveAround(pirate,x0, y0, factor=0.1) :
    (x1,y1) = pirate.getPosition()
    #issue resolved: if the pirate is at the centre then it will take the next step randomly
    return select_movement(x0,y0,x1,y1,factor)

def DenfenceFunction(pirate):

    #to implement: prevent all the functions from returning move which takes them towars wall when they are adjacent to a wall
    if (pirate.getSignal()[3]=='d'):
        raw_string = pirate.getTeamSignal()
        
        if (raw_string[48]=='1'):
                #it is expected that the team signals are stored in such a way that the characters from index 12 to 47 belong to the ids of first 
            defender_ids = pirate.getTeamSignal()[12:24]
                #so defender_ids will be a string of length 12
                #extracting individual ids of each pirate
            for i in range(0,12,2):
                if (int(pirate.getID())==int(defender_ids[i:i+2])) :
                    island_coords = pirate.getTeamSignal()[0:4]
                    x0 = int(island_coords[0:2])
                    y0 = int(island_coords[2:4])
                    if (pirate.trackPlayers()[0]!='myCaptured'):
                        return moveAround(pirate,x0,y0,10) #tell the pirates to converge around when their designated island is out of reach
                    else: 
                        return moveAround(pirate,x0,y0)
                    
        if (raw_string[49]== '2'):
            #it is expected that the team signals are stored in such a way that the characters from index 12 to 47 belong to the ids of first 
            defender_ids = pirate.getTeamSignal()[24:36]
            #so defender_ids will be a string of length 12
            #extracting individual ids of each pirate
            for i in range(0,12,2):
                if (int(pirate.getID())==int(defender_ids[i:i+2])) :
                    island_coords = pirate.getTeamSignal()[4:8]
                    x0 = int(island_coords[0:2])
                    y0 = int(island_coords[2:4])
                    if (pirate.trackPlayers()[1]!='myCaptured'):
                        return moveAround(pirate,x0,y0,10)
                    else: 
                        return moveAround(pirate,x0,y0)                                  

        if (raw_string[50]== '3'):
                #it is expected that the team signals are stored in such a way that the characters from index 12 to 47 belong to the ids of first 
                defender_ids = pirate.getTeamSignal()[36:48]
                #so defender_ids will be a string of length 12
                #extracting individual ids of each pirate
                for i in range(0,12,2):
                    if (int(pirate.getID())==int(defender_ids[i:i+2])) :
                        island_coords = pirate.getTeamSignal()[8:12]
                        x0 = int(island_coords[0:2])
                        y0 = int(island_coords[2:4])
                        if (pirate.trackPlayers()[2]!='myCaptured'):
                            return moveAround(pirate,x0,y0,10)
                        else: 
                            return moveAround(pirate,x0,y0)                         


def ActPirate(pirate):

    if (pirate.getSignal( )== ''):
        string = ''.zfill(100)
        pirate.setSignal(string)

    # print(pirate.getTeamSignal())
    setIslandCoordinatesToTeamSignal(pirate)

    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    
    s = pirate.trackPlayers()
    
    ids= int(pirate.getID())
    #set the first string of the signal to be the pirate id, this will be used in team signals
    
    raw_string = pirate.getSignal()
    
    
    if 10<=ids<100:
        sid="0"+ str(ids)
    elif ids<10:
        sid="00"+ str(ids)
    else:
        sid=str(ids)
    sig= sid+ "a" 
    new_string = sig + raw_string[4:]
    pirate.setSignal(new_string)

    teamSig= pirate.getTeamSignal()
    for i in range(3):
        if teamSig[i+48] == f'{i+1}':
            signalTeam = pirate.getTeamSignal()[12+12*i:12+12*(i+1)]
            for j in range(6):
                if sid[1:] == signalTeam[j*2:j*2+2]:
                    signal = sid + "d"
                    new_string = signal + raw_string[4:] 
                    pirate.setSignal(new_string)



    # if int(pirate.getID()) < 7:
    #     signal= sid+ "d"
    #     pirate.setSignal(signal)
    # print(pirate.getSignal())
    # if(pirate.getSignal()[3]=='d'):
    #     print(pirate.getSignal())


    if (pirate.getSignal()[3]=='d'):
        # print(DenfenceFunction(pirate))
        return DenfenceFunction(pirate)

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

    # return attack2(pirate)
    # print(pirate.getSignal())
    # for i in range(1,4):
    #     if pirate.investigate_current()[0] == f"island{i}":
    #         if pirate.trackPlayers()[i-1] != "myCaptured":
    #             return 0
    
    if teamSig[48] == '0' and teamSig[49] == '0' and teamSig[50] == '0':
        return attack0(pirate)
    # if "myCaptured" not in pirate.trackPlayers():
    #     return attack0(pirate)
    else:
        if(pirate.getSignal()[3] == 'a'):
            signal = pirate.getSignal()
            if(pirate.getSignal()[4]== '0'):
                signal = signal[:4] + f'{random.randint(1,2)}'
                # signal = signal + f'{random.randint(0,1) if signal[4] == '1' else ''} '
                if signal[4] == '1':
                    signal = signal + f'{random.randint(1,2)}'
                if signal[4] == '2':
                    signal = signal + f'{random.randint(1,4)}'
                pirate.setSignal(signal)
                # print(pirate.getSignal())
            else:
                if signal[4] == '2':
                    return attack1(pirate,int(signal[5]))
                elif signal[4] == '1':
                    if signal[5] == '1':
                        return attack2(pirate)
                    elif signal[5] == '2':
                        return attack3(pirate)

    
    # if pirate.getTeamSignal() != "":
    #     s = pirate.getTeamSignal()
    #     l = s.split(",")
        # x = int(l[0][1:])
        # y = int(l[1])
    
    #     return moveTo(x, y, pirate)

    # else:
    # return random.randint(1, 4)


def ActTeam(team):
    if (team.getTeamSignal( )== ''):
        string = ''.zfill(100)
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

    if len(sig_alive) < 36:
        sig_alive = sig_alive.ljust(36, ' ')  # Pad with spaces if shorter
    elif len(sig_alive) > 36:
        sig_alive = sig_alive[:36]  # Truncate if longer

    # print(sig_alive)
    raw_string = team.getTeamSignal()
    new_string = raw_string[:12] + sig_alive + raw_string[48:]
    team.setTeamSignal(new_string)
    # print(new_string)
    # print(team.getTeamSignal())
    
    #below block of code (3 if statements) will set the team signal index 48,49 and 50 to the islands which we have captured or are attempting to capture    
    if(team.getTeamSignal()[48]=='0') :
        if (team.getTeamSignal()[0:4]!='0000'):
            string = team.getTeamSignal()
            sig = string[0:48] + '1' + string[49:100] 
            team.setTeamSignal(sig)

    if(team.getTeamSignal()[49]=='0') :
        if (team.getTeamSignal()[4:8]!='0000'):
            string = team.getTeamSignal()
            sig = string[0:49] + '2' + string[50:100] 
            team.setTeamSignal(sig)    

    if(team.getTeamSignal()[50]=='0') :
        if (team.getTeamSignal()[8:12]!='0000'):
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
    
    if team.getTotalGunpowder() < 500:
        if (r1=='2' or (get_my_status[51]=='1' and r1=='4' ) or (get_my_status[51]=='5' and r1=='4') ):
            team.buildWalls(1)
        if (r2=='2' or (get_my_status[52]=='1' and r2=='4' ) or (get_my_status[52]=='5' and r2=='4')  ):
            team.buildWalls(2)
        if (r3=='2' or (get_my_status[53]=='1' and r2=='4' ) or (get_my_status[53]=='5' and r3=='4')  ):
            team.buildWalls(3)
        

    
    # alive_players=[]
    # for string in team.getListOfSignals():
    #     raw = string.split()
    #     alive_players.append(raw[0])
    # print(alive_players)

    
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
    team.setTeamSignal(final_sig)
    #Only for testing
    # raw_string = team.getTeamSignal()
    # new_string = raw_string[:48] + 'charaterss' + raw_string[57:]
    # team.setTeamSignal(new_string)


    # print(team.getListOfSignals())
    # print(alive_players)    
    # print(team.getListOfSignals())
    # print(team.getDimensionX())
    # team.buildWalls(1)
    # team.buildWalls(2)
    # team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    # if s:
    #     island_no = int(s[0])
    #     signal = l[island_no - 1]
    #     if signal == "myCaptured":
    #         team.setTeamSignal("")
