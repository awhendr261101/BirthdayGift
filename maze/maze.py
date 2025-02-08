
import random
import robot


def get_obstacles():
    global list_obstacles
    list_obstacles = []
    return list_obstacles

def create_random_obstacles():

    '''This is the function where the maze is drawn.'''
    global list_obstacles
    list_obstacles = get_obstacles()
   
    horizontal_wall(-500,500,300) 
    #This is an "H"
    horizontal_wall(-100,-68, 172)
    vertical_wall(148, 200, -100)
    vertical_wall(148, 200, -68)

    # This is an "A"
    vertical_wall(148, 180, -44)
    vertical_wall(148, 180, -12)
    acute_angle_wall(-44, -24, 180)
    obtuse_angle_wall(-28, -8,196)

    # this is a P 
    vertical_wall(148, 200, 12)
    horizontal_wall(12, 32, 196)
    horizontal_wall(12, 32, 172)
    acute_angle_wall(32, 40, 176)
    obtuse_angle_wall(32, 40, 192)
    list_obstacles.append((36, 184))

    # This is P2
    vertical_wall(148, 200, 60)
    horizontal_wall(60, 80, 196)
    horizontal_wall(60, 80, 172)
    acute_angle_wall(80, 88, 176)
    obtuse_angle_wall(80,88, 192)
    list_obstacles.append((84, 184))

    # This is the Y 
    xy1 = 120
    for obstacle in range(172, 196, 4):
        y = obstacle
        list_obstacles.append((xy1, y))
        xy1 -= 4
    
    acute_angle_wall(124,144,176)
    vertical_wall(148, 172, 120)


    # Next Line Max Y = 124
    # gaps betwwen words 24 
    maxy = 124

    # This is the B
    vertical_wall(maxy - 52, maxy, -176)  
    horizontal_wall(-176, -156, 124)
    horizontal_wall(-176, -156, 96)
    acute_angle_wall(-156, -148, 100)
    obtuse_angle_wall(-156, -148, 120)
    obtuse_angle_wall(-156, -148, 92)
    acute_angle_wall(-156, -148, 72)
    vertical_wall(80, 88, -152)  
    vertical_wall(108, 116, -152)  
    horizontal_wall(-176, -156, maxy - 56)

    # This is the I
    horizontal_wall(-132, -96, maxy)
    vertical_wall(maxy - 56, maxy, -116)  
    horizontal_wall(-132, -96, maxy - 56)

    # This is the R
    vertical_wall(maxy - 56, maxy + 4, -76)  
    horizontal_wall(-76, -56, maxy)
    obtuse_angle_wall(-60, -48, maxy)
    list_obstacles.append((-28 -24, maxy - 12))
    acute_angle_wall(-60, -48, maxy - 24)
    horizontal_wall(-76, -56, maxy - 24)
    obtuse_angle_wall(-76, -40, maxy - 24)
    list_obstacles.append((-44 -24, maxy - 28))
    list_obstacles.append((-48 -24, maxy - 32))

    # This is the T
    horizontal_wall(-28, 8, maxy)
    vertical_wall(maxy - 56, maxy, -12)  

    # This is H
    vertical_wall(maxy - 56, maxy + 4, 24)  
    horizontal_wall(28, 56, maxy - 28)
    vertical_wall(maxy - 56, maxy + 4, 56)  

    # This is D
    vertical_wall(maxy - 56, maxy + 4, 84)  
    horizontal_wall(84, 104, maxy)
    horizontal_wall(84, 104, maxy - 56)
    obtuse_angle_wall(104, 120, maxy)
    acute_angle_wall(104, 120, maxy - 56)
    vertical_wall(maxy - 44, maxy - 8, 116)  

    # This is A
    vertical_wall(maxy - 56, maxy - 16, 140)  
    acute_angle_wall(140, 160, maxy - 16)
    obtuse_angle_wall(156, 176, maxy)
    vertical_wall(maxy - 56, maxy - 16, 172)  

    # This is Y
    obtuse_angle_wall(184, 208, maxy)
    acute_angle_wall(208, 228, maxy - 16)
    vertical_wall(maxy - 56, maxy - 16, 204)


    # 3rd line 
    maxy = 36

    # This is C 
    vertical_wall(maxy -48, maxy-8, -248)
    acute_angle_wall(-248, -232, maxy-8)
    obtuse_angle_wall(-248, -232, maxy -48)
    horizontal_wall(-232, -216, maxy+4)
    horizontal_wall(-232, -216, maxy-60)

    # This is H 
    vertical_wall(maxy -60, maxy + 8,  -192)
    horizontal_wall(-192, -156, maxy - 28)
    vertical_wall(maxy -60, maxy + 8,  -156)

    # This is E 
    vertical_wall(maxy -60, maxy + 8,  -132)
    horizontal_wall(-132, -104, maxy - 28)
    horizontal_wall(-132, -96, maxy +4)
    horizontal_wall(-132, -96, maxy -60)

    # This is L 
    vertical_wall(maxy -60, maxy + 8, -72)
    horizontal_wall(-72, -36, maxy -60)

    # Another L
    vertical_wall(maxy -60, maxy + 8, -12)
    horizontal_wall(-12, 24, maxy -60)

    # This is A 
    vertical_wall(maxy -60, maxy - 16, 48)
    acute_angle_wall(48, 72, maxy - 16)
    obtuse_angle_wall(72, 92, maxy)
    vertical_wall(maxy -60, maxy - 16, 88)

    # This is p 
    vertical_wall(maxy -60, maxy +8, 116)
    horizontal_wall(116, 140, maxy +4)
    obtuse_angle_wall(140, 152, maxy +4)
    horizontal_wall(116, 140, maxy - 28)
    acute_angle_wall(140, 152,maxy - 28)
    vertical_wall(maxy -20, maxy, 148)

    # This is O 
    vertical_wall(maxy -48, maxy-8, 172)
    acute_angle_wall(172, 188, maxy-8)
    obtuse_angle_wall(172, 188, maxy -48)
    obtuse_angle_wall(204, 216, maxy)
    acute_angle_wall(204, 216, maxy-56)
    horizontal_wall(188, 204, maxy+4)
    horizontal_wall(188, 204, maxy-60)
    vertical_wall(maxy -48, maxy-8, 212)

    # The last letter 
    vertical_wall(maxy -60, maxy +8, 240)
    horizontal_wall(240, 264, maxy +4)
    obtuse_angle_wall(264, 276, maxy +4)
    horizontal_wall(240, 264, maxy - 28)
    acute_angle_wall(264, 276,maxy - 28)
    vertical_wall(maxy -20, maxy, 272)

    # The cherry on top 
    obtuse_angle_wall(-60, 4, maxy -176)
    acute_angle_wall( 4, 72, maxy -240)
    acute_angle_wall(-60, -44,maxy -136)
    obtuse_angle_wall(56,72, maxy -124)
    horizontal_wall(-44, -12, maxy -120)
    horizontal_wall(24, 56, maxy -120)
    acute_angle_wall(8, 24,maxy -136)
    obtuse_angle_wall(-12, 8, maxy -124)
    vertical_wall(maxy -176, maxy -136,  -60)
    vertical_wall(maxy -176, maxy -136,   68)
   
    return list_obstacles
    

def horizontal_wall(a,b,c):
    for obstacle in range(a, b, 4):
        x = obstacle
        y = c
        list_obstacles.append((x, y))

def vertical_wall(a,b,c):
    for obstacle in range(a, b, 4):
        y1 = obstacle
        x = c
        list_obstacles.append((x, y1))

def obtuse_angle_wall(a,b,c):
    y1b = c
    for obstacle in range(a, b, 4):
        x = obstacle
        list_obstacles.append((x, y1b))
        y1b -= 4

def acute_angle_wall(a,b,c):
    y1b = c
    for obstacle in range(a, b, 4):
        x = obstacle
        list_obstacles.append((x, y1b))
        y1b += 4
