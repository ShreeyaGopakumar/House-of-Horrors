from cmu_graphics import*

def features(app):
    app.height=750
    app.width=1300
    app.color='maroon'
    app.answer="clock"
    app.message=""
    app.currentLetter=app.answer[0]
    app.guessedWrong=False
    app.gameOver=False
    app.canvasLeft=app.width//2-175
    app.canvasTop=app.height//2-250
    app.cx=app.canvasLeft+200
    app.cy=app.canvasTop+300
    app.points=[(app.cx,app.cy)]
    app.showHints=False
    
def redrawAll(app):
    
        
    if not app.gameOver:
        drawRect(app.width//2,app.height//2,400,400,fill='black',align='center')
        if app.showHints:
            for i in range(len(app.points)-1):
                (x,y)=app.points[i]
                (x2,y2)=app.points[i+1]
                drawLine(x,y,x2,y2,fill='white')

        drawCircle(app.cx,app.cy,20,fill='white')
        drawCircle(app.cx,app.cy,10,fill='black')
        
        drawLabel(f'{app.message}',app.width//2,app.canvasTop+100,fill='white',size=40,font='monospace')
        drawLabel("<>",app.width//2,app.canvasTop+150,fill='white',size=20,font='monospace')
        drawLabel("Guess what the eyeball is writing!",app.width//2,app.canvasTop+130,fill='white',font='monospace')
        if app.guessedWrong:
            drawLabel("WRONG!",app.width//2,app.height//2+100,fill='white')
        
        if not app.showHints:
            drawRect(app.width//2-180,app.height//2+180,40,20,fill='white',align='center')
            drawLabel("Hints",app.width//2-180,app.height//2+180,fill='black')
            
    if app.gameOver and not app.clock:
        drawRect(app.width//2,app.height//2,400,400,fill='black',align='center')
        drawLabel("You crossed the first puzzle!",app.width//2,app.height//2-100,fill='white',font='monospace',size=23)
        drawLabel("Use the word you found to guess the next location",app.width//2,app.height//2-50,fill='white',font='monospace')
        drawRect(app.width//2,app.height//2+150,70,50,border='white',align='center')
        drawLabel("Proceed",app.width//2,app.height//2+150,fill='white',font='monospace')
        
def click(app,key):
    if not app.gameOver:
        if len(key)==1 and 'a'<=key<='z':
            app.message+=key
            if key!=app.currentLetter:
                app.guessedWrong=True
                app.message=app.message[:-1]
            else:
                if app.message=='clock':
                    app.gameOver=True
                    
                else:
                    if app.message=="cloc":
                        app.cx=app.canvasLeft+150
                        app.cy=app.canvasTop+300
                    else:
                        app.cx=app.canvasLeft+200
                        app.cy=app.canvasTop+300
                    app.points=[(app.cx,app.cy)]
                    app.guessedWrong=False
                    app.answer=app.answer[1:]
                    app.currentLetter=app.answer[0]  
            
        if app.message=="" or app.message=="clo":
            C(app,key)
        if app.message=='c':
            L(app,key)
        if app.message=='cl':
            O(app,key)
        if app.message=='clo':
            C(app,key)
        if app.message=='cloc':
            K(app,key)
        

def C(app,key):
    if key=='left':
        app.cx-=10
        if app.cx<app.canvasLeft+150:
            app.cx+=10
    if key=='right':
        if app.cy==app.canvasTop+200 or app.cy==app.canvasTop+300:
            app.cx+=10
            if app.cx>app.canvasLeft+200:
                app.cx-=10
    if key=='up':
        if app.cx==150+app.canvasLeft:
            app.cy-=10
            if app.cy<200+app.canvasTop:
                app.cy+=10
    if key=='down':
        if app.cx==150+app.canvasLeft:
            app.cy+=10
            if app.cy>300+app.canvasTop:
                app.cy-=10
    app.points.append((app.cx,app.cy))

def L(app,key):
    if key=='left':
        if app.cy==app.canvasTop+300:
            app.cx-=10
            if app.cx<app.canvasLeft+150:
                app.cx+=10
    if key=='right':
        if app.cy==app.canvasTop+300:
            app.cx+=10
            if app.cx>app.canvasLeft+200:
                app.cx-=10
    if key=='up':
        if app.cx==app.canvasLeft+150:
            app.cy-=10
            if app.cy<app.canvasTop+200:
                app.cy+=10
    if key=='down':
        if app.cx==app.canvasLeft+150:
            app.cy+=10
            if app.cy>app.canvasTop+300:
                app.cy-=10
    app.points.append((app.cx,app.cy))

def O(app,key):
    if key=='left':
        if app.cy==app.canvasTop+300 or app.cy==app.canvasTop+200:
            app.cx-=10
            if app.cx<app.canvasLeft+150:
                app.cx+=10
    if key=='right':
        if app.cy==app.canvasTop+300 or app.cy==app.canvasTop+200:
            app.cx+=10
            if app.cx>app.canvasLeft+200:
                app.cx-=10
    if key=='up':
        if app.cx==app.canvasLeft+150 or app.cx==app.canvasLeft+200:
            app.cy-=10
            if app.cy<app.canvasTop+200:
                app.cy+=10
    if key=='down':
        if app.cx==app.canvasLeft+150 or app.cx==app.canvasLeft+200:
            app.cy+=10
            if app.cy>app.canvasTop+300:
                app.cy-=10
    app.points.append((app.cx,app.cy))

def K(app,key):
    if key=='left':
        if (app.cy==app.canvasTop+300 and app.cx==app.canvasLeft+200) or (250+app.canvasTop<=app.cy<300+app.canvasTop and 150+app.canvasLeft<=app.cx<200+app.canvasLeft):
                app.cx-=10
                app.cy-=10
                if(app.cx<150+app.canvasLeft):
                    app.cx+=10
                    app.cy+=10
    if key=='right':
        if (app.cy>250+app.canvasTop and app.cx!=150+app.canvasLeft) or (app.cy==250+app.canvasTop and app.cx==150+app.canvasLeft):
            app.cx+=10
            app.cy+=10
            if app.cx>200+app.canvasLeft:
                app.cx-=10
            if app.cy>300+app.canvasTop:
                app.cy-=10
    if key=='up':
        if app.cx==150+app.canvasLeft:
            app.cy-=10
            if app.cy<200+app.canvasTop:
                app.cy+=10
    if key=='down':
        if app.cx==150+app.canvasLeft:
            app.cy+=10
            if app.cy>300+app.canvasTop:
                app.cy-=10
    app.points.append((app.cx,app.cy))

def onMousePress(mouseX,mouseY):
    if not app.gameOver and app.width//2-180-20<=mouseX<=app.width//2-180+20 and app.height//2+180-10<=mouseY<=app.height//2+180+10:
        app.showHints=True
    if app.gameOver and app.width//2-35<=mouseX<=app.width//2+35 and app.height//2+150-25<=mouseY<=app.height//2+150+25:
        app.clock=True
