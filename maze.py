from cmu_graphics import*

def onAppStart(app):
    app.width=1300
    app.height=750
    app.playerX=0
    app.playerY=1
    app.maze=["XXXXXXXXX",
                "  X     X",
                "X X XXX X",
                "X  C  X X",
                "X XXX X X",
                "X A  BX X",
                "X XXXXX X",
                "X XD    X",
                "XXXXXXX  "]

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
    if key=="down":
        if app.maze[app.playerY+1][app.playerX]==" ":
            app.playerY+=1
    if key=="left":
        if app.maze[app.playerY][app.playerX-1]==" ":
            app.playerX-=1
    if key=="right":
        if app.maze[app.playerY][app.playerX+1]==" ":
            app.playerX+=1
    



def main():
    runApp()

main()
                