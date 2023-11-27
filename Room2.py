from cmu_graphics import *
def clues(app):
    app.drawerOpen=False
    app.blockPuzzle=False
    app.skullAppear=False
    app.puzzle=False
    app.password=False
    app.input=""
    app.showHint=False
def redrawAll(app):
    drawImage(app.room2,0,0,width=app.width,height=app.height)
    
    if not app.skullAppear:
        drawImage(app.chest,app.width//2+40,app.height//2+30,width=100,height=50,align='center')
        if not app.puzzle:
            drawRect(200,app.height//2+100,50,30,fill='white',rotateAngle=-8)
            drawLabel("X",225,app.height//2+115,fill='black',rotateAngle=-8,font='monospace' )
        if app.puzzle:
            drawLabel("X",app.width//2+65,app.height//2+15,fill='maroon',bold=True,font='monospace')
            drawImage(app.letter_puzzle,app.width-310,0,width=300,height=200)
        
        if app.password:
            drawRect(app.width//2+40,app.height//2+280,400,200,fill='black',align='center')
            drawLabel("Enter the 4-letter password",app.width//2+40,app.height//2+200,fill='white',font='monospace')
            if app.showHint:
                drawLabel("The blood and the grid reveals something horrifying",app.width//2+40,app.height//2+240,font='monospace',fill="white")
            drawLabel(app.input,app.width//2+40,app.height//2+270,fill='white',font='monospace',size=40)
            if not app.showHint:
                drawRect(app.width//2-160,app.height-50,70,50,fill='white')
                drawLabel("Hint",app.width//2-130, app.height-50+20,fill='black')
    if app.skullAppear and app.skull not in app.clues:
        drawImage(app.skull,app.width//2+40,app.height//2+20,width=40,height=60,align='center')
    

def click(mouseX,mouseY):
    if app.width//2+40-50<=mouseX<=app.width//2+40+50 and app.height//2+30-25<=mouseY<=app.height//2+30+25 and app.puzzle:
        if app.skullAppear and app.width//2+20<=mouseX<=app.width//2+60 and app.height//2+20-30<=mouseY<=app.height//2+20+30:
            app.clues.append(app.skull)
        app.password=True
    if app.password and app.width//2-160<=mouseX<=app.width//2-160+70 and app.height-50<=mouseY<=app.height:
        app.showHint=True
    if 200<=mouseX<=200+50 and app.height//2+100<=mouseY<=app.height//2+100+30:
        app.puzzle=True

def onKeyPress(app,key):
    if len(key)==1 and 'a'<=key<='z' and len(app.input)<4 and app.password:
        app.input+=key
    if key=='enter' and app.password:
        if app.input=='pain':
            app.skullAppear=True
            app.password=False
        else:
            app.input=""    
    if key=='backspace':
        app.input=app.input[:-1]
    
 
