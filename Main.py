from cmu_graphics import*
from PIL import Image
import os, pathlib
import doors
import Room1
import Room2
import floor1
import floor2
import image
import Room3
import maze
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
  

#def onAppStart(app):
#    image.loadImages(app)
#    app.clues_tofind=[app.candles,app.skull,app.chucky,app.clown]
#    app.sidePanel=False
#    app.width=1300
#    app.height=750
#    
#    app.clues=[]
    
def welcome_onAppStart(app):
    image.loadImages(app)
    app.clues_tofind=[app.candles,app.skull,app.chucky,app.clown]
    app.sidePanel=False
    app.width=1300
    app.height=750
    app.clues=[]
    app.roomsVisited=[]
    app.roomsLeft=["room1","room2"]
    app.playerX=0
    app.playerY=1
    app.maze=["XXXXXXXXX",
                "  X     X",
                "X XXXXX X",
                "X  C  X X",
                "X XXX X X",
                "X A  BX X",
                "X XXXXX X",
                "X XD    X",
                "XXXXXXXXX"]
    
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
#______________________________________________________

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
#________________________________________________
def instructions_redrawAll(app):
    drawImage(app.control,0,0,width=app.width,height=app.height)
    drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')

def instructions_onMousePress(app,mouseX,mouseY):
    if inArrow(app,mouseX,mouseY):
        setActiveScreen('maze')

#________________________________________________
'''def map_redrawAll(app):
    #drawRect(0,0,app.width,app.height,fill='black')
    #crossed_distance=50
    #for x in range(len(app.clues_tofind)):
    #    if app.clues_tofind[x] in app.clues:
    #        drawImage(app.clues[x],crossed_distance+20,app.height//2-140,width=100,height=140)
    #        drawImage(app.tick,crossed_distance+70,app.height//2+20,width=40,height=40,align='center')
    #        
    #    else:
    #        drawImage(app.clues_tofind[x],crossed_distance+20,app.height//2-140,width=100,height=140,opacity=50)
    #    crossed_distance+=250
    

        
    #drawLabel("PROGRESS",app.width//2,40,fill='white', size=80, font='monospace')
    #drawRect(app.width-65,app.height//2,app.arrowWidth//2,app.arrowHeight//2-10,fill='white',align='center')
    drawImage(app.map,app.width//2,app.height//2,width=app.width,height=app.height-10,align='center')
    drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')
        


def map_onMousePress(app,mouseX,mouseY):
    if inArrow(app,mouseX,mouseY):
        setActiveScreen(app.callingForMap)'''
#__________________________________________________
'''
def whereToGo_redrawAll(app):
    if "room1" not in app.roomsVisited or "room2" not in app.roomsVisited:
        floor1Color="white"
    else:
        floor1Color="grey"
    if app.clues_tofind == app.clues:
        atticColor="white"
    else:
        atticColor="grey"
    drawRect(0,0,app.width,app.height,fill='black')
    drawLabel("Where would you like to go?",app.width//2,150,fill='white')
    drawRect(app.width//2,250,200,100,fill=floor1Color,align='center',border='black')
    drawLabel("Floor 1",app.width//2,250,fill='black',font='monospace')
    drawRect(app.width//2,350,200,100,fill='white',align='center',border='black')
    drawLabel("Floor 2",app.width//2,350,fill='black',font='monospace')
    drawRect(app.width//2,450,200,100,fill=atticColor,align='center',border='black')
    drawLabel("Attic",app.width//2,450,fill='black',font='monospace')
    drawOptions(app)
    drawSidePanel(app)
    
    
def whereToGo_onMousePress(app,mouseX,mouseY):
    if app.width//2-100<=mouseX<=app.width//2+100 and 250-50<=mouseY<=250+50:
        if "room1" not in app.roomsVisited or "room2" not in app.roomsVisited or "room3" not in app.roomsVisited:
            setActiveScreen("floor1")
    if app.width//2-100<=mouseX<=app.width//2+100 and 350-50<=mouseY<=350+50:
        if "room4" not in app.roomsVisited:
            setActiveScreen("floor2")
    if app.width//2-100<=mouseX<=app.width//2+100 and 450-50<=mouseY<=450+50:
        if app.clues_tofind == app.clues:
            setActiveScreen("over")
    sidePanelClick(app,mouseX,mouseY)
    if distance(mouseX,mouseY,40,110)<=30:
        app.callingForMaze="whereToGo"
        setActiveScreen("map")'''
#__________________________________________________
def floor1_redrawAll(app):
    floor1.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
def floor1_onMousePress(app,mouseX,mouseY):
    room=floor1.onMousePress(app,mouseX,mouseY)
    if room!=None:
        setActiveScreen(room)
    sidePanelClick(app,mouseX,mouseY)
    #if distance(mouseX,mouseY,40,110)<=30:
    #    app.callingForMaze="floor1"
    #    setActiveScreen("maze")
#__________________________________________________
def corridor1_onAppStart(app):
    doors.features(app)
    
def corridor1_redrawAll(app):
    doors.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
    
def corridor1_onMousePress(app,mouseX,mouseY):
    doors.click(mouseX,mouseY)
    sidePanelClick(app,mouseX,mouseY)
    #if distance(mouseX,mouseY,40,110)<=30:
    #    app.callingForMaze="corridor1"
    #    setActiveScreen("maze")
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
            app.maze[app.playerY]=app.maze[app.playerY][0:app.playerX]+" "+app.maze[app.playerY][app.playerX+1:]
            setActiveScreen("maze")

def room1_onKeyPress(app,key):
    Room1.onKeyPress(app,key)
#_______________________________________________

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

#_______________________________________________
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
            newRow=[]
            for y in range(len(app.maze)):
                if y==app.playerX:
                    i=app.maze[y].index("B")
                    newRow=[app.maze[y][0:i]+" "+app.maze[y][i+1:]]
            app.maze=app.maze[0:app.playerY]+newRow+app.maze[app.playerY+1:]
            setActiveScreen("maze")


def room2_onKeyPress(app,key):
    Room2.onKeyPress(app,key)
#_______________________________________________
'''def floor2_redrawAll(app):
    floor2.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
def floor2_onMousePress(app,mouseX,mouseY):
    room=floor2.onMousePress(app,mouseX,mouseY)
    if room!=None:
        setActiveScreen("over")
    sidePanelClick(app,mouseX,mouseY)
    if distance(mouseX,mouseY,40,110)<=30:
        app.callingForMap="floor2"
        setActiveScreen("map")'''
#_______________________________________________
def room3_onAppStart(app):
    Room3.features(app)
def room3_redrawAll(app):
    Room3.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
    if app.clown in app.clues:
        drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')
    
def room3_onMousePress(app,mouseX,mouseY):
    sidePanelClick(app,mouseX,mouseY)
    Room3.onMousePress(app,mouseX,mouseY)
    if app.clown in app.clues:
        app.roomsVisited.append("room3")
        if inArrow(app,mouseX,mouseY):
            app.maze[app.playerY]=app.maze[app.playerY][0:app.playerX]+" "+app.maze[app.playerY][app.playerX+1:]
            setActiveScreen("maze")

    

#_______________________________________________


def maze_redrawAll(app):
    maze.redrawAll(app)

def maze_onKeyPress(app,key):
    r=maze.onKeyPress(app,key)
    if r!=None:
        setActiveScreen(r)

#_______________________________________________
def over_redrawAll(app):
    #drawRect(0,0,app.width,app.height,fill='black')
    #drawRect(app.width//2-100,app.height//2+100,200,50,fill='black',border='white')
    #drawLabel("YOU WON!",app.width//2,app.height//2+125,fill="white",font="monospace",size=25)
    drawImage(app.over,0,0,width=app.width,height=app.height)
#________________________________________________
def main():
    runAppWithScreens(initialScreen='welcome')

if __name__ == '__main__':
    main()

