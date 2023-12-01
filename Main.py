from cmu_graphics import*
from PIL import Image
import os, pathlib
import doors
import Room1
import Room2
import image
import game_3
import maze

#common functions_______________________________________________________________

def drawSidePanel(app):
    if app.sidePanel:
        drawRect(0,0,150,app.height,fill='black',border="white")
        drawRect(150,app.height//2,25,100,align='center',fill='white')
        crossed_distance=0
        for x in range(len(app.clues_tofind)):
            if app.clues_tofind[x] in app.clues:
                drawImage(app.clues_tofind[x],150/2-20,crossed_distance+20,width=60,height=100)
                drawImage(app.tick,150/2-20,crossed_distance+40,width=20,height=20,align='center')
            else:    
                drawImage(app.clues_tofind[x],150/2-20,crossed_distance+20,width=60,height=100,opacity=50)
            crossed_distance+=125

def sidePanelClick(app,mouseX,mouseY):
    if  distance(mouseX,mouseY,50,40)<=30 and app.sidePanel==False:
        app.sidePanel=True
    if app.sidePanel:
        if 150-25/2<=mouseX<=150+25/2 and app.height//2-50<=mouseY<=app.height//2+50:
            app.sidePanel=False
def drawOptions(app):
    drawCircle(40,40,30,fill='black',border='white')
    drawLabel("CLUES",40,40,fill='white',font='monospace')
  
#_______________________________________________________________________________  

def welcome_onAppStart(app):
    image.loadImages(app)
    app.clues_tofind=[app.candles,app.skull,app.clown]
    app.sidePanel=False
    app.width=1300
    app.height=750
    app.clues=[]
    app.roomsVisited=[]
    app.gameOver2=False
        
def welcome_redrawAll(app):
    drawImage(app.bg,0,0,width=app.bgWidth,height=app.bgHeight)
    drawRect(app.width//2,app.height//2-100,app.width,100,fill='black', align='center')
    drawLabel("HOUSE OF HORRORS",app.width//2,app.height//2-100,fill='white',font="monospace",size=100,bold=True)
    drawLabel("Face your biggest fears!",app.width//2,app.height//2,fill="white",font="monospace",size=45)
    drawRect(app.width//2-100,app.height//2+100,200,50,fill='black',border='white')
    drawLabel("Begin",app.width//2,app.height//2+125,fill="white",font="monospace",size=25)

def inBegin(app,mouseX,mouseY):
    if app.width//2-100<=mouseX<=app.width//2-100+200 and app.height//2+100<=mouseY<=app.height//2+100+50:
        return True
    return False  
  
def welcome_onMousePress(app,mouseX,mouseY):
    if inBegin(app,mouseX,mouseY):
        setActiveScreen('introScreen')
def welcome_onKeyPress(app,key):
    if key=='enter':
        setActiveScreen('introScreen')
#_______________________________________________________________________________

def introScreen_redrawAll(app):
    drawImage(app.intro,0,0,width=app.introWidth,height=app.introHeight)
    drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')

def inArrow(app,mouseX,mouseY):
    if app.width-115<=mouseX<=app.width-15 and app.height//2-60<=mouseY<=app.height//2+60:
        return True
    return False
def introScreen_onMousePress(app,mouseX,mouseY):
    if inArrow(app,mouseX,mouseY):
        setActiveScreen('instructions')
#_______________________________________________________________________________

def instructions_redrawAll(app):
    drawImage(app.control,0,0,width=app.width,height=app.height)
    drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')

def instructions_onMousePress(app,mouseX,mouseY):
    if inArrow(app,mouseX,mouseY):
        setActiveScreen('maze')

#_______________________________________________________________________________

def corridor1_onAppStart(app):
    doors.features(app)
    
def corridor1_redrawAll(app):
    doors.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
    
def corridor1_onMousePress(app,mouseX,mouseY):
    doors.click(mouseX,mouseY)
    sidePanelClick(app,mouseX,mouseY)
    if app.flag==2:
        setActiveScreen("room1")    
#_______________________________________________
def room1_onAppStart(app):
    Room1.clues(app)

def room1_redrawAll(app):
    Room1.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
    if app.candles in app.clues:
        drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')

def room1_onMousePress(app,mouseX,mouseY):
    Room1.click(mouseX,mouseY)
    sidePanelClick(app,mouseX,mouseY)
    
    if app.candles in app.clues:
        app.roomsVisited.append("room1")
        if inArrow(app,mouseX,mouseY):
            app.maze[app.playerX][app.playerY]='c'
            setActiveScreen("maze")

def room1_onKeyPress(app,key):
    Room1.onKeyPress(app,key)
#_______________________________________________________________________________

def room2_intro_redrawAll(app):
    drawImage(app.room2_intro,0,0,width=app.width,height=app.height)
    drawRect(app.width-65,app.height//2,app.arrowWidth//2,app.arrowHeight//2-10,fill='white',align='center')
    drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')
    drawOptions(app)
    drawSidePanel(app)
    

def room2_intro_onMousePress(app,mouseX,mouseY):
    sidePanelClick(app,mouseX,mouseY)
    
    if inArrow(app,mouseX,mouseY):
            setActiveScreen("room2")

#_______________________________________________________________________________

def room2_onAppStart(app):
    Room2.clues(app)

def room2_redrawAll(app):
    Room2.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
    if app.skull in app.clues:
        drawRect(app.width-65,app.height//2,app.arrowWidth//2,app.arrowHeight//2-10,fill='white',align='center')
        drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')
        
def room2_onMousePress(app,mouseX,mouseY):
    sidePanelClick(app,mouseX,mouseY)
    Room2.click(mouseX,mouseY)
    if app.skull in app.clues:
        app.roomsVisited.append("room2")
        if inArrow(app,mouseX,mouseY):
            app.maze[app.playerX][app.playerY]='c'
            setActiveScreen("maze")

def room2_onKeyPress(app,key):
    Room2.onKeyPress(app,key)

#_______________________________________________________________________________

def room3_intro_redrawAll(app):
    drawImage(app.room3_intro,0,0,width=app.width,height=app.height)
    drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')
    drawOptions(app)
    drawSidePanel(app)
    

def room3_intro_onMousePress(app,mouseX,mouseY):
    sidePanelClick(app,mouseX,mouseY)
    if inArrow(app,mouseX,mouseY):
            setActiveScreen("room3")
#_______________________________________________________________________________

def room3_onAppStart(app):
    game_3.Points.features(app)

def room3_redrawAll(app):
    game_3.Points.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
    if app.gameOver2:
        app.clues.append(app.clown)
    if app.clown in app.clues:
        drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')
    
def room3_onMousePress(app,mouseX,mouseY):
    sidePanelClick(app,mouseX,mouseY)
    if app.clown in app.clues:
        app.roomsVisited.append("room3")
        if inArrow(app,mouseX,mouseY):
            app.maze[app.playerX][app.playerY]='c'
            setActiveScreen("maze")

def room3_onKeyPress(app,key):
    if not app.gameOver2:
        game_3.Points.onKeyPress(app,key)
    
def room3_onStep(app):
    if not app.gameOver2:
        game_3.Points.onStep(app)
#_______________________________________________________________________________

def maze_onAppStart(app):
    maze.features(app)

def maze_redrawAll(app):
    drawImage(app.bg3,0,0,width=app.width,height=app.height)
    maze.printMaze(app)
    drawOptions(app)
    drawSidePanel(app)

def maze_onMousePress(app,mouseX,mouseY):
    sidePanelClick(app,mouseX,mouseY)
def maze_onKeyPress(app,key):
    room=maze.onKeyPress(app,key)
    if room!=None:
        setActiveScreen(room)  
#_______________________________________________

def over_redrawAll(app):
    drawImage(app.over,0,0,width=app.width,height=app.height)
    
#________________________________________________
def main():
    runAppWithScreens(initialScreen='welcome')

if __name__ == '__main__':
    main()

