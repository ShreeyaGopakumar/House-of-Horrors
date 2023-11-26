from cmu_graphics import *
def clues(app):
    app.drawerOpen=False
    app.blockPuzzle=False
    app.skull=False
    app.puzzle=False
def redrawAll(app):
    drawImage(app.room2,0,0,width=app.width,height=app.height)
    
    if not app.skull:
        drawRect(200,app.height//2+100,50,30,fill='white',rotateAngle=-8)
        drawLabel("X",225,app.height//2+100+15,fill='black',rotateAngle=-8,font='monospace' )
    #if app.puzzle:
        
    
    
    
def click(mouseX,mouseY):
    if 200<=mouseX<=200+50 and app.height//2+100<=mouseY<=app.height//2+100+30:
        app.puzzle=True
    
 
