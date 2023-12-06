from cmu_graphics import *
import block_puzzle
#room to find candle
def clues(app):
    app.drawerOpen=False
    app.keyFound=False
    app.blockPuzzle=False
    app.clock=False
    block_puzzle.features(app)

def redrawAll(app):
    if app.drawerOpen:
        drawImage(app.room1_frame2,0,0,width=app.width,height=app.height)
        if app.candles not in app.clues:
            drawImage(app.candles,250,600,width=30,height=50,align='center')
    else:
        drawImage(app.room1_frame1,0,0,width=app.width,height=app.height)
    if not app.clock:
        drawRect(200,app.height//2+100,50,30,fill='black',rotateAngle=-8)
        drawLabel("X",225,app.height//2+100+15,fill='white',rotateAngle=-8,font='monospace' )
    if app.blockPuzzle:
        block_puzzle.redrawAll(app)
    
def click(mouseX,mouseY):
    block_puzzle.onMousePress(mouseX,mouseY)
    if 200<=mouseX<=200+50 and app.height//2+100<=mouseY<=app.height//2+100+30:
        app.blockPuzzle=True
    if app.clock:
        if 1090<=mouseX<=1275 and 110<=mouseY<=app.height//2+10:
            app.drawerOpen=True
            
    if 250-15<=mouseX<=250+15 and 600-25<=mouseY<=600+25 and app.candles not in app.clues and app.clock:
        app.clues.append(app.candles)
    
def onKeyPress(app,key):
    if app.blockPuzzle:
        block_puzzle.click(app,key)
