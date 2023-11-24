from cmu_graphics import *

def redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="maroon")
    if app.drawerOpen:
        drawImage(app.drawer2,50,0,width=app.drawer2Width,height=app.drawer2Height)

    else:
        drawImage(app.drawer1,50,0,width=app.drawer1Width,height=app.drawer1Height)

def click(mouseX,mouseY):
    app.drawerOpen=not app.drawerOpen

