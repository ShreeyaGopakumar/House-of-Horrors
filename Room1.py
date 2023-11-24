from cmu_graphics import *
import block_puzzle
def clues(app):
    app.room1clues_tofind=["morse code","key"]
    app.room1clues_found=[]
    app.drawerOpen=False
    app.key=False

def redrawAll(app):

    drawRect(0,0,app.width,app.height,fill="maroon")
    if app.drawerOpen:
        drawImage(app.room1_frame2,0,50,width=app.width,height=app.height-100)
    else:
        drawImage(app.room1_frame1,0,50,width=app.width,height=app.height-100)
    

def click(mouseX,mouseY):
    if "key" in app.room1clues_found:
        app.drawerOpen=True
    if "morse code" in app.room1clues_found:
        app.key=True


