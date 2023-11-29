from cmu_graphics import*



def redrawAll(app):
    drawMaze(app)    
def drawMaze(app):
    for y in range (len(app.maze)):
        for x in range(len(app.maze[0])):
            character=app.maze[y][x]
            if character=="X":
                drawRect(300+x*75,y*75,75,75,fill='black')
            if character=="A" or character=="B" or character=="C" or character=="D":
                drawRect(300+x*75,y*75,75,75,fill='brown')
            if y==app.playerY and x==app.playerX:
                drawRect(300+x*75,y*75,75,75,fill='blue')
def onKeyPress(app,key):
    if key=="up":
        if app.maze[app.playerY-1][app.playerX]==" ":
            app.playerY-=1
        elif app.maze[app.playerY-1][app.playerX]=="A":
            app.playerY-=1
            return "corridor1"
        elif app.maze[app.playerY-1][app.playerX]=="B":
            app.playerY-=1
            return "room2_intro"
        elif app.maze[app.playerY-1][app.playerX]=="C":
            app.playerY-=1
            return "room3"
        
    if key=="down":
        if app.maze[app.playerY+1][app.playerX]==" ":
            app.playerY+=1
        elif app.maze[app.playerY+1][app.playerX]=="A":
            app.playerY+=1
            return "corridor1"
        elif app.maze[app.playerY+1][app.playerX]=="B":
            app.playerY+=1
            return "room2_intro"
        elif app.maze[app.playerY+1][app.playerX]=="C":
            app.playerY+=1
            return "room3"
    if key=="left":
        if app.maze[app.playerY][app.playerX-1]==" ":
            app.playerX-=1
        elif app.maze[app.playerY][app.playerX-1]=="A":
            app.playerX-=1
            return "corridor1"
        elif app.maze[app.playerY][app.playerX-1]=="B":
            app.playerX-=1
            return "room2_intro"
        elif app.maze[app.playerY][app.playerX-1]=="C":
            app.playerX-=1
            return "room3"
        
    if key=="right":
        if app.maze[app.playerY][app.playerX+1]==" ":
            app.playerX+=1
        elif app.maze[app.playerY][app.playerX+1]=="A":
            app.playerX+=1
            return "corridor1"
        elif app.maze[app.playerY][app.playerX+1]=="B":
            app.playerX+=1
            return "room2_intro"
        elif app.maze[app.playerY][app.playerX+1]=="C":
            app.playerX+=1
            return "room3"
        

     