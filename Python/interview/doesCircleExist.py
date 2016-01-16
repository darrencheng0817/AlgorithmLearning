'''
Created on 2016年1月15日

@author: Darren
'''
def  doesCircleExist( commands):
    if not commands or len(commands)==0:
        return "YES"
    direction=0
    x,y=0,0
    for command in commands:
        if command=="G":
            if direction==0:
                x+=1
            if direction==1:
                y+=1
            if direction==2:
                x-=1
            if direction==3:
                y-=1
        if command=="L":
            direction-=1
            if direction<0:
                direction+=4
        if command=="R":
            direction+=1
            if direction>3:
                direction-=4
    return "YES" if x==0 and y==0 else "NO"
# commands="GLGLGLGL"
# print(doesCircleExist(commands))