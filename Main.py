from cmu_graphics import*
from PIL import Image
import os, pathlib
import doors
import Room1
import Room2
import image
def drawSidePanel(app):
    if app.sidePanel:
        drawRect(0,0,150,app.height,fill='black',border="white")
        drawRect(150,app.height//2,25,100,align='center',fill='white')
        crossed_distance=0
        for x in range(len(app.clues)):
            drawImage(app.clues[x],150/2-20,crossed_distance+20,width=60,height=100)
            crossed_distance+=125
        crossed_distance=0
        for x in range(len(app.clues_tofind)):
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
    drawCircle(40,110,30,fill='black',border='white')
    drawLabel("*",40,110,fill='white',font='monospace',size=30)

def onAppStart(app):
    app.sidePanel=False
    app.width=1300
    app.height=750
    image.loadImages(app)
    app.clues=[]
    app.clues_tofind=[app.candles,app.skull,app.chucky,app.clown]

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
        app.callingForMap="door1"
        setActiveScreen('map')

#________________________________________________
def map_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill='black')
    #drawImage(app.map,app.width//2,app.height//2,width=1000,height=500,align='center')
    #drawImage(app.clown,app.width//2-270,app.height//2-100,width=75,height=100,align='center')
    #drawImage(app.candles,app.width//2-400,app.height//2-100,width=75,height=100,align='center')
    crossed_distance=50
    for x in range(len(app.clues)):
        drawImage(app.clues[x],crossed_distance+20,app.height//2-140,width=100,height=140)
        drawImage(app.tick,crossed_distance+70,app.height//2+20,width=40,height=40,align='center')
        crossed_distance+=250

        
    crossed_distance=50
    for x in range(len(app.clues_tofind)):
        drawImage(app.clues_tofind[x],crossed_distance+20,app.height//2-140,width=100,height=140,opacity=50)
        crossed_distance+=250
    
    drawLabel("PROGRESS",app.width//2,40,fill='white', size=80, font='monospace')
    drawRect(app.width-65,app.height//2,app.arrowWidth//2,app.arrowHeight//2-10,fill='white',align='center')
    drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')
    
        

def map_onMousePress(app,mouseX,mouseY):
    if inArrow(app,mouseX,mouseY):
        setActiveScreen(app.callingForMap)
#__________________________________________________

def door1_onAppStart(app):
    doors.features(app)
    
def door1_redrawAll(app):
    doors.redrawAll(app)
    drawOptions(app)
    drawSidePanel(app)
    
def door1_onMousePress(app,mouseX,mouseY):
    doors.click(mouseX,mouseY)
    sidePanelClick(app,mouseX,mouseY)
    if distance(mouseX,mouseY,40,110)<=30:
        app.callingForMap="door1"
        setActiveScreen("map")
    if app.flag==3:
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
    if distance(mouseX,mouseY,40,110)<=30:
        app.callingForMap="room1"
        setActiveScreen("map")
    if app.candles in app.clues:
        if inArrow(app,mouseX,mouseY):
            setActiveScreen("room2_intro")
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
    if distance(mouseX,mouseY,40,110)<=30:
        app.callingForMap="room2_intro"
        setActiveScreen("map")
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
    if distance(mouseX,mouseY,40,110)<=30:
        app.callingForMap="room2"
        setActiveScreen("map")
    if app.skull in app.clues:
        if inArrow(app,mouseX,mouseY):
            setActiveScreen("over")


def room2_onKeyPress(app,key):
    Room2.onKeyPress(app,key)
#_______________________________________________
def over_redrawAll(app):
    #drawRect(0,0,app.width,app.height,fill='black')
    #drawRect(app.width//2-100,app.height//2+100,200,50,fill='black',border='white')
    #drawLabel("YOU WON!",app.width//2,app.height//2+125,fill="white",font="monospace",size=25)
    drawImage(app.over,0,0,width=app.width,height=app.height)

def main():
    runAppWithScreens(initialScreen='welcome')

if __name__ == '__main__':
    main()

