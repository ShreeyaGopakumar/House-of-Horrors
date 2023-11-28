from cmu_graphics import *

def features(app):
    app.visitedClues=[]
    app.showBox=True
    app.showPainting=False
def redrawAll(app):
    if app.showBox:
        drawImage(app.room3_frame1,0,0,width=app.width,height=app.height)
    else:
        if app.showPainting:
            drawImage(app.room3_frame3,0,0,width=app.width,height=app.height)
        else:
            drawImage(app.room3_frame2,0,0,width=app.width,height=app.height)
    drawLine(0,290,app.width,290, fill='pink')
    drawLine(0,320,app.width,320,fill='pink')
    drawLine(app.width-440,0,app.width-440,app.height,fill='pink')
    drawLine(app.width-490,0,app.width-490,app.height,fill='pink')
        
def onMousePress(app,mouseX,mouseY):
    if 620<=mouseY<=650 and app.width-70<=mouseX<=app.width-40 and app.showBox:
        app.showBox=False
    if not app.showBox and 530<=mouseY<=570 and app.width-270<=mouseX<=app.width-230:
        app.showPainting=True
    
    
    