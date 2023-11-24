from cmu_graphics import *

def redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="maroon")
    drawImage(app.drawer1,0,app.height//2-150,width=app.drawer1Width,height=app.drawer1Height)
    

