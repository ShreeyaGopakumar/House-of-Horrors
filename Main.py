from cmu_graphics import*
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
    drawLabel("*",40,110,fill='white',font='monospace',size=30)
#_______________________________________________________________
'''Images used:
Background: https://www.ngpf.org/blog/activities/escape-from-the-haunted-mansion-a-new-halloween-activity/
Candles: https://gallery.yopriceville.com/Free-Clipart-Pictures/Halloween-PNG-Pictures/Lighted_Candles_Transparent_Image
Clown mask: https://www.walmart.com/ip/Adult-Whacko-Clown-Full-Face-Mask/1402672413?wmlspartner=wlpa&selectedSellerId=737
Doors: https://community.boschsecurity.com/t5/Security-Access-Control/How-to-set-up-interlock-APE/ta-p/12325
Jumpscare: https://www.deviantart.com/zueiroooooooooooo/art/Nightmare-Freddy-Ucn-Jumpscare-FullBody-828859450
Nun: https://www.newburyportnews.com/news/lifestyles/movie-review-in-the-nun-what-evil-lurks-beneath-a-habit/article_cfddb3f0-7974-5e1b-9e97-80bee389f993.html
Map: https://brainchase.com/national-scavenger-hunt-day-coming/
Room2 (corridor): <a href="https://www.freepik.com/free-photo/abandoned-alley-psychiatric-hospital_5600084.htm#query=creepy%20corridor&position=0&from_view=search&track=ais&uuid=b257c826-e514-4c68-be4b-33706549068d">Image by jcomp</a> on Freepik
Room2 (mortuary): <a href="https://www.freepik.com/free-photo/abandoned-morgue-psychiatric-hospital_5600088.htm#query=creepy%20lab&position=0&from_view=search&track=ais&uuid=251a2fa0-7336-42d8-9fec-09b092841387">Image by jcomp</a> on Freepik

Other screens - made on Canva
'''
#_______________________________________________________________
def onAppStart(app):
    app.sidePanel=False
    app.width=1300
    app.height=750
    def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
    #________________________________
    app.bg = openImage("images/bg.png")
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
    
    app.door1 = openImage("images/door1.png")
    app.door1Width,app.door1Height = app.door1.width,app.door1.height
    app.door1 = CMUImage(app.door1)
    
    app.door2 = openImage("images/door2.png")
    app.door2Width,app.door2Height = app.door2.width,app.door2.height
    app.door2 = CMUImage(app.door2)
    
    
    app.room1_frame1=openImage("images/room1_frame1.png")
    app.room1_frame1=CMUImage(app.room1_frame1)
    app.room1_frame2=openImage("images/room1_frame2.png")
    app.room1_frame2=CMUImage(app.room1_frame2)
    app.control=openImage("images/Control and Instructions.png")
    app.control=CMUImage(app.control)
    
    app.room2_intro=openImage("images/room2_intro.jpg")
    app.room2_intro=CMUImage(app.room2_intro)
    app.room2=openImage("images/room2.jpg")
    app.room2=CMUImage(app.room2)

    app.skull=openImage("images/skull.png")
    app.skull=CMUImage(app.skull)
    app.chucky=openImage("images/chucky.png")
    app.chucky=CMUImage(app.chucky)
    app.arrow=openImage("images/arrow.png")
    app.arrowWidth,app.arrowHeight=app.arrow.width,app.arrow.height
    app.arrow=CMUImage(app.arrow)
    app.tick=openImage("images/tick.png")
    app.tick=CMUImage(app.tick)
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

def room2_redrawAll(app):
    drawImage(app.room2,0,0,width=app.width,height=app.height)
    drawRect(app.width-65,app.height//2,app.arrowWidth//2,app.arrowHeight//2-10,fill='white',align='center')
    drawImage(app.arrow, app.width-65, app.height//2, width=app.arrowWidth//2,height=app.arrowHeight//2,align='center')
    

    drawOptions(app)
    drawSidePanel(app)
    

def room2_onMousePress(app,mouseX,mouseY):
    sidePanelClick(app,mouseX,mouseY)
    if distance(mouseX,mouseY,40,110)<=30:
        app.callingForMap="room2"
        setActiveScreen("map")
    if inArrow(app,mouseX,mouseY):
            setActiveScreen("over")
#_______________________________________________
def over_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill='black')
    drawRect(app.width//2-100,app.height//2+100,200,50,fill='black',border='white')
    drawLabel("YOU WON!",app.width//2,app.height//2+125,fill="white",font="monospace",size=25)


def main():
    runAppWithScreens(initialScreen='welcome')

if __name__ == '__main__':
    main()

