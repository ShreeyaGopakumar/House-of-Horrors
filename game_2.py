from cmu_graphics import*
def features(app):
    app.gameOver4=False
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
    if not app.gameOver4:
        app.playerY3+=app.playerdy
        if app.playerIsJumping:
            app.playerIsFalling=True
            app.playerdy+=0.5
        
        if app.playerY3+30>=750-30:
            features(app)
        i=0
        for (x,y) in app.platforms:
            if distance(x,y,app.playerX3,app.playerY3)<=(20) and x-25<=app.playerX3<=x+25:
                if (x,y)==(app.width//2+60-130,50):
                    app.gameOver4=True
                if not app.gameOver4:
                    app.playerIsJumping=False
                    app.playerdy=0
                    app.playerIsFalling=False
        
def check(app):
    for (x,y) in app.platforms:
        if x-25<=app.playerX3<=x+25:
            return False
    return True
            
def onKeyHold(app,keys):
    if not app.gameOver4:
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
    if not app.gameOver4:
        if key=='space' and not app.playerIsFalling:
            for (x,y) in app.platforms:
                if app.playerY3-30==y and x-25<=app.playerX3<=x+25:
                    app.playerIsFalling=True
            app.jump.play(restart=True)
            app.playerIsJumping=True
            app.playerdy=-10

def redrawAll(app):
    drawRect(0,0,app.width,app.height,fill='black')
    for (x,y) in app.platforms:
        if (x,y)==(app.width//2+60-130,50) and not app.gameOver4:
            drawImage(app.knife,x,y,width=30,height=40,align='center')
        else:
            drawRect(x,y,40,30,fill='white',align='center')
    drawImage(app.player,app.playerX3,app.playerY3,width=50,height=50,align='center')
        

