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
    
def redrawAll(app):
    
    if app.gameOver:
        drawLabel("GAME OVER",app.width//2,app.height//2)
    else:
        drawRect(app.width//2,app.height//2,400,400,fill='black',align='center')
        drawCircle(app.cx,app.cy,20,fill='white')
        for i in range(len(app.points)-1):
            (x,y)=app.points[i]
            (x2,y2)=app.points[i+1]
            drawLine(x,y,x2,y2,fill='white')
        drawLabel(f'{app.message}',app.width//2,app.height//2+300,fill='white')
        if app.guessedWrong:
            drawLabel("WRONG!",app.width//2,app.height//2+100,fill='white')
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
