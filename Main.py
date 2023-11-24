from cmu_graphics import *
from PIL import Image
import os, pathlib
import door1
def drawSidePanel(app):
    if app.sidePanel:
        drawRect(0,0,150,app.height,fill='black',border="white")
        drawRect(150,app.height//2,25,100,align='center',fill='white')
        for x in range(len(app.clues)):
            drawImage(app.clues[x],150//2,20,width=50,height=80)
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
        setActiveScreen('map')
#________________________________________________
def map_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill='black')
    drawImage(app.map,app.width//2,app.height//2,width=1000,height=500,align='center')
    drawRect(app.width//2,app.height//2+300,200,50,fill='black',border='white',align='center')
    drawImage(app.clown,app.width//2-270,app.height//2-100,width=75,height=100,align='center')
    drawImage(app.candles,app.width//2-400,app.height//2-100,width=75,height=100,align='center')
    if app.clues==[]:
        drawLabel("I'm READY!",app.width//2,app.height//2+300,fill="white",font="monospace",size=25)

def map_onMousePress(app,mouseX,mouseY):
    if app.width//2-100<=mouseX<=app.width//2+100 and app.height//2+150<=mouseY<=app.height//2+450:
        setActiveScreen('door1')
#__________________________________________________

def door1_onAppStart(app):
    door1.features(app)
    
def door1_redrawAll(app):
    door1.redrawAll(app)
    drawCircle(40,40,30,fill='black')
    drawLabel("CLUES",40,40,30,fill='white',font='monospace')
    drawSidePanel(app)
    if app.foundCandle:
        nextArrow = chr(0x21e8)
        drawLabel(nextArrow, app.width-65, app.height//2, size=200, font='symbols')

def door1_onMousePress(app,mouseX,mouseY):
    door1.click(mouseX,mouseY)
    sidePanelClick(app,mouseX,mouseY)
    if app.flag==3:
        setActiveScreen("room1_intro")
#_______________________________________________
def room1_intro_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="grey")
    drawLabel("INTRO TO MINI-GAME 1",app.width//2,app.height//2,font='monospace',size=60)
    drawLabel("START!",app.width//2,app.height//2+125,fill="white",font="monospace",size=25)
    drawCircle(40,40,30,fill='black')
    drawSidePanel(app)

def room1_intro_onMousePress(app,mouseX,mouseY):
    if inBegin(app,mouseX,mouseY):
        setActiveScreen('over')
    sidePanelClick(app,mouseX,mouseY)
#_______________________________________________
def over_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill='black')
    drawRect(app.width//2-100,app.height//2+100,200,50,fill='black',border='white')
    drawLabel("YOU WON!",app.width//2,app.height//2+125,fill="white",font="monospace",size=25)


def main():
    runAppWithScreens(initialScreen='welcome')

if __name__ == '__main__':
    main()

