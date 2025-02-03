
def robot_movement(command):
    x=0 
    y=0

    for c in command:
        if c=='D':
            y-=1
        if c=='U':
            y+=1
        if c=='R':
            x+=1
        if c=='L':
            x-=1


    return(x,y)

command="UD"
print(robot_movement(command))