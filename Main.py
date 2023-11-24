from cmu_graphics import *
from PIL import Image
import os, pathlib
import doors
import Room1
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
    drawCircle(40,40,30,fill='black')
    drawLabel("CLUES",40,40,fill='white',font='monospace')
    drawCircle(40,110,30,fill='black')
    drawLabel("MAP",40,110,fill='white',font='monospace')
    
def onAppStart(app):
    app.sidePanel=False
    app.width=1300
    app.height=750
    def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
    app.bg = openImage("images/bg.jpg")
    app.bgWidth,app.bgHeight = app.width,app.height
    app.bg = CMUImage(app.bg)

    app.intro = openImage("images/intro.jpg")
    app.introWidth,app.introHeight = app.width,app.height
    app.intro = CMUImage(app.intro)

    app.candles = openImage("images/candles.png")
    app.candles = CMUImage(app.candles)
    
    app.clown = openImage("images/clown.png")
    app.clown = CMUImage(app.clown)
    app.scary = openImage("images/scary.png")
    app.scary = CMUImage(app.scary)
    app.nun = openImage("images/nun.png")
    app.nun = CMUImage(app.nun)
    app.map = openImage("images/map.jpg")
    app.map = CMUImage(app.map)
    
    app.clues=[]
    app.clues_tofind=[app.candles,app.clown]
    
    app.door1 = openImage("images/door1.png")
    app.door1Width,app.door1Height = app.door1.width,app.door1.height
    app.door1 = CMUImage(app.door1)
    
    app.door2 = openImage("images/door2.png")
    app.door2Width,app.door2Height = app.door2.width,app.door2.height
    app.door2 = CMUImage(app.door2)
    
    app.draw1=openImage("images/draw1.png")
    app.draw1 = CMUImage(app.draw1)
    app.draw2=openImage("images/draw2.png")
    app.draw2 = CMUImage(app.draw2)
    

def welcome_redrawAll(app):
    drawImage(app.bg,0,0,width=app.bgWidth,height=app.bgHeight)
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
    drawRect(0,0,app.width,app.height,fill='black')  
    drawImage(app.intro,0,0,width=app.introWidth,height=app.introHeight)
    nextArrow = chr(0x21e8)
    drawLabel(nextArrow, app.width-65, app.height//2, size=200, font='symbols')

def inArrow(app,mouseX,mouseY):
    if app.width-115<=mouseX<=app.width-15 and app.height//2-60<=mouseY<=app.height//2+60:
        return True
    return False
def introScreen_onMousePress(app,mouseX,mouseY):
    if inArrow(app,mouseX,mouseY):
        app.callingForMap="door1"
        setActiveScreen('map')
#________________________________________________
def map_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill='black')
    drawImage(app.map,app.width//2,app.height//2,width=1000,height=500,align='center')
    drawImage(app.clown,app.width//2-270,app.height//2-100,width=75,height=100,align='center')
    drawImage(app.candles,app.width//2-400,app.height//2-100,width=75,height=100,align='center')
    drawCircle(app.width-50,50,30,fill='white')
    drawLabel(">",app.width-50,50,fill='black',bold=True,size=60)

def map_onMousePress(app,mouseX,mouseY):
    if distance(mouseX,mouseY,app.width-50,50)<=30:
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
def room1_redrawAll(app):
    Room1.redrawAll(app)
    drawRect(0,0,app.width,app.height,fill="grey")
    drawOptions(app)
    drawSidePanel(app)

def room1_onMousePress(app,mouseX,mouseY):
    if inBegin(app,mouseX,mouseY):
        setActiveScreen('over')
    sidePanelClick(app,mouseX,mouseY)
    if distance(mouseX,mouseY,40,110)<=30:
        app.callingForMap="room1"
        setActiveScreen("map")
#_______________________________________________
def over_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill='black')
    drawRect(app.width//2-100,app.height//2+100,200,50,fill='black',border='white')
    drawLabel("YOU WON!",app.width//2,app.height//2+125,fill="white",font="monospace",size=25)


def main():
    runAppWithScreens(initialScreen='welcome')

if __name__ == '__main__':
    main()

