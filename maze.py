from cmu_graphics import*
from PIL import Image
import os, pathlib
def features(app):
    app.width=1300
    app.height=750
    app.wall='w'
    app.cell='c'
    app.unvisited='u'
    app.mazeHeight=11
    app.mazeWidth=11
    app.maze=[]
    app.rooms=["a","b","d"]
    app.diaryX=0
    app.diaryY=0
    process(app)
    rooms(app)
    

def rooms(app):
    if app.rooms==[]:
         return 
    else:
        dx=int(random()*app.mazeWidth)
        dy=int(random()*app.mazeHeight)
        if app.maze[dx][dy]=='c' and dx!=app.starting_width and dy!=app.starting_height:
            app.maze[dx][dy]=app.rooms[0]
            app.rooms=app.rooms[1:]
            rooms(app)
        else:
            rooms(app)
    
def printMaze(app):
    for x in range(len(app.maze)):
        for y in range(len(app.maze[0])):
            character=app.maze[x][y]
            if x==app.playerX and y==app.playerY:
                drawImage(app.player,350+x*50,100+y*50,width=50,height=50)
            else:
                if character=='p':
                    if set(app.clues_tofind)==set(app.clues):
                        drawImage(app.key,350+x*50,100+y*50,width=50,height=50)
                    else:
                        drawImage(app.chucky,350+x*50,100+y*50,width=50,height=50)
                
                if character=='w':
                    drawRect(350+x*50,100+y*50,50,50,fill='black')
                if character=='a':
                    drawRect(350+x*50,100+y*50,50,50,fill='brown')
                if character=='b':
                    drawRect(350+x*50,100+y*50,50,50,fill='pink')
                if character=='d':
                    drawRect(350+x*50,100+y*50,50,50,fill='red')
                if character=='c':
                    drawRect(350+x*50,100+y*50,50,50,fill='white')

            

# Find number of surrounding cells
def surroundingCells(app,rand_wall):
	s_cells = 0
	if (app.maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (app.maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (app.maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (app.maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1

	return s_cells


def process(app):
    app.maze=[['u']*(app.mazeWidth) for x in range(app.mazeHeight)]
    

    # Randomize starting point and set it a cell
    app.starting_height = int(random()*app.mazeHeight)
    app.starting_width = int(random()*app.mazeWidth)
    if (app.starting_height == 0):
        app.starting_height += 1
    if (app.starting_height == app.mazeHeight-1):
        app.starting_height -= 1
    if (app.starting_width == 0):
        app.starting_width += 1
    if (app.starting_width == app.mazeWidth-1):
        app.starting_width -= 1

    # Mark it as cell and add surrounding walls to the list
    app.maze[app.starting_height][app.starting_width] = 'c'
    walls = []
    walls.append([app.starting_height - 1, app.starting_width])
    walls.append([app.starting_height, app.starting_width - 1])
    walls.append([app.starting_height, app.starting_width + 1])
    walls.append([app.starting_height + 1, app.starting_width])

    # Denote walls in maze
    app.maze[app.starting_height-1][app.starting_width] = 'w'
    app.maze[app.starting_height][app.starting_width - 1] = 'w'
    app.maze[app.starting_height][app.starting_width + 1] = 'w'
    app.maze[app.starting_height + 1][app.starting_width] = 'w'

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random()*len(walls))-1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (app.maze[rand_wall[0]][rand_wall[1]-1] == 'u' and app.maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                # Find the number of surrounding cells
                s_cells = surroundingCells(app,rand_wall)

                if (s_cells < 2):
                    # Denote the new path
                    app.maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (app.maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            app.maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])


                    # Bottom cell
                    if (rand_wall[0] != app.mazeHeight-1):
                        if (app.maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                            app.maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):	
                        if (app.maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                            app.maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (app.maze[rand_wall[0]-1][rand_wall[1]] == 'u' and app.maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

                s_cells = surroundingCells(app,rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    app.maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (app.maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            app.maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (app.maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                            app.maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    # Rightmost cell
                    if (rand_wall[1] != app.mazeWidth-1):
                        if (app.maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            app.maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if (rand_wall[0] != app.mazeHeight-1):
            if (app.maze[rand_wall[0]+1][rand_wall[1]] == 'u' and app.maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

                s_cells = surroundingCells(app,rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    app.maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Mark the new walls
                    if (rand_wall[0] != app.mazeHeight-1):
                        if (app.maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                            app.maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (app.maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                            app.maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    if (rand_wall[1] != app.mazeWidth-1):
                        if (app.maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            app.maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)


                continue

        # Check the right wall
        if (rand_wall[1] != app.mazeWidth-1):
            if (app.maze[rand_wall[0]][rand_wall[1]+1] == 'u' and app.maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

                s_cells = surroundingCells(app,rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    app.maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Mark the new walls
                    if (rand_wall[1] != app.mazeWidth-1):
                        if (app.maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            app.maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    if (rand_wall[0] != app.mazeHeight-1):
                        if (app.maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                            app.maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[0] != 0):	
                        if (app.maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            app.maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)
        


    # Mark the remaining unvisited cells as walls
    for i in range(0, app.mazeHeight):
        for j in range(0, app.mazeWidth):
            if (app.maze[i][j] == 'u'):
                app.maze[i][j] = 'w'

    # Set entrance and exit
    for i in range(0, app.mazeWidth):
        if (app.maze[1][i] == 'c'):
            app.maze[0][i] = 'c'
            app.playerX=0
            app.playerY=i
            break

    for i in range(app.mazeWidth-1, 0, -1):
        if (app.maze[app.mazeHeight-2][i] == 'c'):
            app.maze[app.mazeHeight-1][i] = 'p'
            
            break


def redrawAll(app):
    printMaze(app)    

def onKeyPress(app,key):
    if key=="up":
        
        if app.maze[app.playerX][app.playerY-1]=="c":
            app.playerY-=1
        elif app.maze[app.playerX][app.playerY-1]=="a":
            app.playerY-=1
            return "corridor1"
        elif app.maze[app.playerX][app.playerY-1]=="b":
            app.playerY-=1
            return "room2_intro"
        elif app.maze[app.playerX][app.playerY-1]=="d":
            app.playerY-=1
            return "room3"
        elif app.maze[app.playerX][app.playerY-1]=="p"and set(app.clues_tofind)==set(app.clues):
            app.playerY-=1
            return "over"
        
        
    if key=="down":
        if app.maze[app.playerX][app.playerY+1]=="c":
            app.playerY+=1
        elif app.maze[app.playerX][app.playerY+1]=="a":
            app.playerY+=1
            return "corridor1"
        elif app.maze[app.playerX][app.playerY+1]=="b":
            app.playerY+=1
            return "room2_intro"
        elif app.maze[app.playerX][app.playerY+1]=="d":
            app.playerY+=1
            return "room3"
        elif app.maze[app.playerX][app.playerY+1]=="p" and set(app.clues_tofind)==set(app.clues):
            print(app.clues)
            app.playerY+=1
            return "over"
    if key=="left":
        if app.maze[app.playerX-1][app.playerY]=="c":
            app.playerX-=1
        elif app.maze[app.playerX-1][app.playerY]=="a":
            app.playerX-=1
            return "corridor1"
        elif app.maze[app.playerX-1][app.playerY]=="b":
            app.playerX-=1
            return "room2_intro"
        elif app.maze[app.playerX-1][app.playerY]=="d":
            app.playerX-=1
            return "room3"
        elif app.maze[app.playerX-1][app.playerY]=="p"and set(app.clues_tofind)==set(app.clues):
            app.playerX-=1
            return "over"
        
    if key=="right":
        if app.maze[app.playerX+1][app.playerY]=="c":
            app.playerX+=1
        elif app.maze[app.playerX+1][app.playerY]=="a":
            app.playerX+=1
            return "corridor1"
        elif app.maze[app.playerX+1][app.playerY]=="b":
            app.playerX+=1
            return "room2_intro"
        elif app.maze[app.playerX+1][app.playerY]=="d":
            app.playerX+=1
            return "room3"
        elif app.maze[app.playerX+1][app.playerY]=="p"and set(app.clues_tofind)==set(app.clues):
            app.playerX+=1
            return "over"
        

     