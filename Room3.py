from cmu_graphics import *

def features(app):
    app.visitedClues=[]
    app.showBox=True
    app.showPainting=False
    app.showMask=False
def redrawAll(app):
    if app.showBox:
        drawImage(app.room3_frame1,0,0,width=app.width,height=app.height)
    else:
        if app.showPainting:
            drawImage(app.room3_frame3,0,0,width=app.width,height=app.height)
            
        else:
            if not app.showMask:
                drawImage(app.room3_frame2,0,0,width=app.width,height=app.height)
            if app.showMask:
                drawImage(app.room3_frame4,0,0,width=app.width,height=app.height)
            
    
def onMousePress(app,mouseX,mouseY):
    if 620<=mouseY<=650 and app.width-70<=mouseX<=app.width-40 and app.showBox:
        app.showBox=False
    if not app.showBox and 530<=mouseY<=570 and app.width-270<=mouseX<=app.width-230:
        app.showPainting=True
    if not app.showPainting and 290<=mouseY<=320 and app.width-600<=mouseX<=app.width-550:
        app.showPainting=False
        app.showMask=True
        print("hello")
    
    