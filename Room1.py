from cmu_graphics import *
import block_puzzle
def clues(app):
    app.room1clues_tofind=["clock","key"]
    app.room1clues_found=[]
    app.drawerOpen=False
    app.key=False
    app.blockPuzzle=False
    app.clock=False
    block_puzzle.features(app)
def redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="maroon")
    if app.drawerOpen:
        drawImage(app.room1_frame2,0,0,width=app.width,height=app.height)
    else:
        drawImage(app.room1_frame1,0,0,width=app.width,height=app.height)
    drawRect(200,app.height//2+100,50,30,fill='black',rotateAngle=-8)
    if app.blockPuzzle:
        block_puzzle.redrawAll(app)
    

def click(mouseX,mouseY):
    if 200<=mouseX<=200+50 and app.height//2+100<=mouseY<=app.height//2+100+30:
        app.blockPuzzle=True
    if app.clock:
        app.clues_found.append("clock")
    #if "key" in app.room1clues_found:
    #    app.drawerOpen=True
    #if "clock" in app.room1clues_found:
    #    app.key=True

def onKeyPress(app,key):
    block_puzzle.click(app,key)
