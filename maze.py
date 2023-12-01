from cmu_graphics import*
from PIL import Image
import os, pathlib
import random
def features(app):
    app.width=1300
    app.height=750
    app.wall='w'
    app.cell='c'
    app.unvisited='u'
    app.mazeHeight=11
    app.mazeWidth=11
    app.maze=[]
    app.rooms=["1","2","3"]
    app.names={"1":"corridor1","2":"room2_intro","3":"room3_intro"}
    
    process(app)
    '''
    maze generation that uses the iterative randomized Prim's algorithm 
    references: https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
                https://en.wikipedia.org/wiki/Maze_generation_algorithm'''

    solveMaze(app) #solving the maze using backtracking
    rooms(app) #placing the rooms randomly in the maze
    

def rooms(app):
    if app.rooms==[]:
         return 
    else:
        dx=random.randint(0,app.mazeWidth-1)
        dy=random.randint(0,app.mazeHeight-1)
        
        if app.maze[dx][dy]=='v' and dx!=app.playerX and dy!=app.playerY:
            app.maze[dx][dy]=app.rooms[0]
            app.rooms=app.rooms[1:]
            rooms(app)
        else:
            rooms(app)
    
def printMaze(app):
    for x in range(len(app.maze)):
        for y in range(len(app.maze[0])):
            Left=((app.width-(50*app.mazeWidth))//2)+x*50
            Top=((app.height-(50*app.mazeHeight))//2)+y*50
            
            character=app.maze[x][y]
            if x==app.playerX and y==app.playerY:
                drawImage(app.player,Left,Top,width=50,height=50)
            else:
                if character=='p':
                    drawImage(app.key,Left,Top,width=50,height=50)
                if character in "123":
                    drawImage(app.door,Left,Top,width=50,height=50)
                if character=='w':
                    drawRect(Left,Top,50,50,fill='red',border='maroon')


#helper functions for maze generation                
def countSurroundings(app,randomWall):
    c=0
    for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
        if app.maze[randomWall[0]+dx][randomWall[1]+dy]=='c':
            c+=1
    return c

def upperCell(randomWall,app):
    if (randomWall[0] != 0):
        if (app.maze[randomWall[0]-1][randomWall[1]] != 'c'):
            app.maze[randomWall[0]-1][randomWall[1]] = 'w'
        if ([randomWall[0]-1, randomWall[1]] not in app.walls):
            app.walls.append([randomWall[0]-1, randomWall[1]])

def bottomCell(randomWall,app):
    if (randomWall[0] != app.mazeHeight-1):
        if (app.maze[randomWall[0]+1][randomWall[1]] != 'c'):
            app.maze[randomWall[0]+1][randomWall[1]] = 'w'
        if ([randomWall[0]+1, randomWall[1]] not in app.walls):
            app.walls.append([randomWall[0]+1, randomWall[1]])

def leftCell(randomWall,app):
    if (randomWall[1] != 0):
        if (app.maze[randomWall[0]][randomWall[1]-1] != 'c'):
            app.maze[randomWall[0]][randomWall[1]-1] = 'w'
        if ([randomWall[0], randomWall[1]-1] not in app.walls):
            app.walls.append([randomWall[0], randomWall[1]-1])
def rightCell(randomWall,app):
    if (randomWall[1] != app.mazeWidth-1):
        if (app.maze[randomWall[0]][randomWall[1]+1] != 'c'):
            app.maze[randomWall[0]][randomWall[1]+1] = 'w'
        if ([randomWall[0], randomWall[1]+1] not in app.walls):
            app.walls.append([randomWall[0], randomWall[1]+1])

def deleteWall(randomWall,app):
    for wall in app.walls:
        if (wall[0] == randomWall[0] and wall[1] == randomWall[1]):
            app.walls.remove(wall)

#_______________________________________________________________________________

def process(app):
    app.maze=[['u']*(app.mazeWidth) for x in range(app.mazeHeight)]
    #random starting point
    app.startHeight = random.randint(0,app.mazeHeight-1)
    app.startWidth = random.randint(0,app.mazeWidth-1)
    
    #make sure the starting is not an edge
    dx=0
    dy=0
    if (app.startWidth == 0):
        dx=1
    if (app.startWidth == app.mazeWidth-1):
        dx=-1
    if (app.startHeight == app.mazeHeight-1):
        dy=-1
    if (app.startHeight == 0):
        dy=1
    app.startWidth+=dx
    app.startHeight+=dy

    # Set the starting point to be a cell
    app.maze[app.startHeight][app.startWidth] = 'c'

    # make app.walls around the cell and add it to the maze
    app.walls = []
    for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
        app.walls.append([app.startHeight+dy,app.startWidth+dx])
        app.maze[app.startHeight+dy][app.startWidth+dx]='w'
    

    while (app.walls):
        # Choose a random wall
        randomWall = app.walls[random.randint(0,len(app.walls)-1)]

        # checks left wall
        if (randomWall[1] != 0):#makes sure it is not the bordering wall
            if (app.maze[randomWall[0]][randomWall[1]-1] == 'u' and app.maze[randomWall[0]][randomWall[1]+1] == 'c'):
                # find the number of surrounding cells
                cells = countSurroundings(app,randomWall)
                
                if (cells < 2):#only one of the cells the wall divides is visited
                    #adds unvisited cell to the maze
                    app.maze[randomWall[0]][randomWall[1]] = 'c'
                    #creates passage and adds neighbouring walls to app.walls
                    upperCell(randomWall,app)
                    bottomCell(randomWall,app)
                    leftCell(randomWall,app)
                
                #removes wall from the list
                deleteWall(randomWall,app)
                
                continue

        # checks upper wall
        if (randomWall[0] != 0):#makes sure it is not the bordering wall
            if (app.maze[randomWall[0]-1][randomWall[1]] == 'u' and app.maze[randomWall[0]+1][randomWall[1]] == 'c'):
                # find the number of surrounding cells
                cells = countSurroundings(app,randomWall)
                
                if (cells < 2):#only one of the cells the wall divides is visited
                    #adds unvisited cell to the maze
                    app.maze[randomWall[0]][randomWall[1]] = 'c'
                    #creates passage and adds neighbouring walls to app.walls
                    upperCell(randomWall,app)
                    leftCell(randomWall,app)
                    rightCell(randomWall,app)

                #deletes wall from list
                deleteWall(randomWall,app)
                continue

        # checks bottom wall
        if (randomWall[0] != app.mazeHeight-1):#makes sure it is not the bordering wall
            if (app.maze[randomWall[0]+1][randomWall[1]] == 'u' and app.maze[randomWall[0]-1][randomWall[1]] == 'c'):

                cells = countSurroundings(app,randomWall)
                if (cells < 2):#only one of the cells the wall divides is visited
                    #adds unvisited cell to the maze
                    app.maze[randomWall[0]][randomWall[1]] = 'c'
                    #creates passage and adds neighbouring walls to app.walls
                    bottomCell(randomWall,app)
                    leftCell(randomWall,app)
                    upperCell(randomWall,app)
                #deletes wall from list
                deleteWall(randomWall,app)
                continue

        # Check the right wall
        if (randomWall[1] != app.mazeWidth-1):#makes sure it is not the bordering wall
            if (app.maze[randomWall[0]][randomWall[1]+1] == 'u' and app.maze[randomWall[0]][randomWall[1]-1] == 'c'):

                cells = countSurroundings(app,randomWall)
                if (cells < 2):#only one of the cells the wall divides is visited
                    #adds unvisited cell to the maze
                    app.maze[randomWall[0]][randomWall[1]] = 'c'
                    #creates passage and adds neighbouring walls to app.walls
                    rightCell(randomWall,app)
                    bottomCell(randomWall,app)
                    upperCell(randomWall,app)

                #deletes wall from list
                deleteWall(randomWall,app)
                continue

        #even if none of the conditions are satisfied, we delete the wall from the list
        deleteWall(randomWall,app)
        


    # remaining univisited cells become walls
    for x in range(0, app.mazeHeight):
        for y in range(0, app.mazeWidth):
            if (app.maze[x][y] == 'u'):
                app.maze[x][y] = 'w'

    # Start and finish
    for x in range(0, app.mazeWidth):
        if (app.maze[1][x] == 'c'):
            app.maze[0][x] = 'c'
            app.playerX=0
            app.playerY=x
            break

    for x in range(app.mazeWidth-1, 0, -1):
        if (app.maze[app.mazeHeight-2][x] == 'c'):
            app.maze[app.mazeHeight-1][x] = 'p'
            break

def solveMaze(app):
    maze=solve(app.playerX,app.playerY,app.maze,app.mazeHeight)
    app.maze=maze
    
    
def isValid(row, col, n, maze):
    return 0 <= row < n and 0 <= col < n and maze[row][col] != 'w'# not a wall

def solve(row, col, maze, n):

    if not isValid(row, col, n, maze):
        return None 

    if maze[row][col] == 'p':
        return maze  

    if maze[row][col] == 'v':#visited cell
        return None  

    maze[row][col] = 'v'  

    for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        solution = solve(row + dx, col + dy, maze, n)#recursive call
        if solution!=None:
            return solution

    maze[row][col] = 'c'#backtracking  

    return None
    
def redrawAll(app):
    printMaze(app)    

def change(app,dx,dy):
    if app.maze[app.playerX+dx][app.playerY+dy]=='c' or app.maze[app.playerX+dx][app.playerY+dy]=='v':
        app.playerY+=dy
        app.playerX+=dx
    elif app.maze[app.playerX+dx][app.playerY+dy] in "123":
        character=app.maze[app.playerX+dx][app.playerY+dy]
        app.playerY+=dy
        app.playerX+=dx
        return app.names[character]
    elif app.maze[app.playerX+dx][app.playerY+dy]=='p' and set(app.clues_tofind)==set(app.clues):
        app.playerY+=dy
        app.playerX+=dx
        return "over"
            
def onKeyPress(app,key):
    if key=="up":
        return change(app,0,-1)
              
    if key=="down":
        return change(app,0,1)
        
    if key=="left":
        return change(app,-1,0)
                
    if key=="right":
        return change(app,1,0)

     