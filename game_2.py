from cmu_graphics import*
def onAppStart(app):
    app.height=750
    app.width=400
    app.gameOver=False
    app.playerX3=app.width//2
    app.playerY3=630
    app.control=app.playerY3
    app.playerdy=0
    app.playerdx=0
    app.radius=30
    app.playerIsJumping=False
    app.platforms=[(app.width//2,650),(app.width//2+80-130,550),(app.width//2+40-130,450),(app.width//2-130,350),(app.width//2+60-130,250),(app.width//2+110-130,150),(app.width//2+60-130,50)]
    app.flag=0
    app.playerIsFalling=False

def onStep(app):
    app.playerY3+=app.playerdy
    if app.playerIsJumping:
        app.playerIsFalling=True
        app.playerdy+=0.5
    
    if app.playerY3+30>=750-30:
        app.playerdy=0
        app.playerIsJumping=False
        app.playerIsFalling=False
    i=0
    for (x,y) in app.platforms:
        if distance(x,y,app.playerX3,app.playerY3)<=(20) and x-25<=app.playerX3<=x+25:
            app.playerIsJumping=False
            app.playerdy=0
            app.playerIsFalling=False
        
def check(app):
    for (x,y) in app.platforms:
        if x-25<=app.playerX3<=x+25:
            return False
    return True
            
def onKeyHold(app,keys):
    if not app.gameOver:
        if 'right' in keys:
            if not app.playerIsJumping:
                if not check(app):
                    app.playerIsJumping=True
            app.playerX3+=5
            
        elif 'left' in keys :
            if not app.playerIsJumping:
                if not check(app):
                    app.playerIsJumping=True
            app.playerX3-=5
    
def onKeyPress(app,key):
    if not app.gameOver:
        if key=='space' and not app.playerIsFalling:
            for (x,y) in app.platforms:
                if app.playerY3-30==y and x-25<=app.playerX3<=x+25:
                    app.playerIsFalling=True
            app.playerIsJumping=True
            app.playerdy=-10

def redrawAll(app):
    if not app.gameOver:
        for (x,y) in app.platforms:
            drawRect(x,y,40,30,fill='black',align='center')
        drawCircle(app.playerX3,app.playerY3,20,fill='blue')
        

def main():
    runApp()

main()
