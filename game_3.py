from cmu_graphics import*
class Points:
    def __init__(self,points):
        self.points=points
    def draw(self,app,d):
        for (x,y) in self.points:
            if d==-1:
                drawImage(app.killerclown,x,y,width=60,height=60,align='center')
            else:
                drawImage(app.killerclown_2,x,y,width=60,height=60,align='center')

    def col(self,app):
        for (x,y) in self.points:
            if distance(x,y,app.player2X,app.player2Y)<=40:
                return True
        return False
    def change(self,d):
        for i in range(len(self.points)):
            (x,y)=self.points[i]
            self.points[i]=(x+(d*10),y)
        (x,y)=self.points[len(self.points)-1]
        self.points.append((x-(d*200),y))
        

def features(app):
    restart(app)
    
def restart(app):

    app.height=750
    app.width=1300
    app.player2X=60
    app.player2Y=60
    app.points_1=Points([(app.width-500,500),(app.width-700,500),(app.width-900,500)])
    app.points_2=Points([(100,300),(300,300),(500,300)])
    app.points_3=Points([(app.width-500,100),(app.width-700,100),(app.width-900,100)])
    app.gameOver=False
    
    

def redrawAll(app):
    if not app.gameOver:
        drawRect(0,0,app.width,app.height,fill='black')
        drawImage(app.bg2,0,0,width=app.width,height=app.height)
        drawRect(0,app.height-100,app.width,app.height,fill='maroon')
        app.points_1.draw(app,-1)
        app.points_2.draw(app,1)
        app.points_3.draw(app,-1)
        drawImage(app.player,app.player2X,app.player2Y,width=60,height=60,align='center')
        drawImage(app.clown,app.width-35,app.height-45,width=70,height=90,align='center')
        
        
def collision(app):
    return app.points_1.col(app) or app.points_2.col(app) or app.points_3.col(app)

def onKeyPress(app,key):
    print("hello")
    if collision(app):
        restart(app)
    if not app.gameOver:
        if key=="left":
            
            if not app.gameOver:
                app.player2X-=10
                
            
        if key=='right':
            
            if not app.gameOver:
                app.player2X+=10
            
        if key=="up":
            
            if not app.gameOver:
                app.player2Y-=10
            
        if key=="down":
            if not app.gameOver:
                app.player2Y+=10
                if distance(app.player2X,app.player2Y,app.width-35,app.height-45)<=(35+30):
                    app.gameOver=True


def onStep(app):
    if not app.gameOver:
        if collision(app):
            restart(app)
        if not app.gameOver:
            app.points_1.change(-1)
            app.points_2.change(1)
            app.points_3.change(-1)
        
