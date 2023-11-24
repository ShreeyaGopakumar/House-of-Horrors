from cmu_graphics import*

def features(app):
    app.height=750
    app.width=1300
    app.color='maroon'
    app.cx=200
    app.cy=300
    app.answer="clock"
    app.message=""
    app.currentLetter=app.answer[0]
    app.points=[(app.cx,app.cy)]
    app.guessedWrong=False
    app.gameOver=False
def redrawAll(app):
    
    if app.gameOver:
        drawLabel("GAME OVER",app.width//2,app.height//2)
    else:
        drawCircle(app.cx,app.cy,20,fill='black')
        for i in range(len(app.points)-1):
            (x,y)=app.points[i]
            (x2,y2)=app.points[i+1]
            drawLine(x,y,x2,y2,fill='black')
        drawLabel(f'{app.message}',app.width//2,350)
        if app.guessedWrong:
            drawLabel("WRONG!",app.width//2,10)
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
                        app.cx=150
                        app.cy=300
                    else:
                        app.cx=200
                        app.cy=300
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
        if app.cx<150:
            app.cx+=10
    if key=='right':
        if app.cy==200 or app.cy==300:
            app.cx+=10
            if app.cx>200:
                app.cx-=10
    if key=='up':
        if app.cx==150:
            app.cy-=10
            if app.cy<200:
                app.cy+=10
    if key=='down':
        if app.cx==150:
            app.cy+=10
            if app.cy>300:
                app.cy-=10
    app.points.append((app.cx,app.cy))

def L(app,key):
    if key=='left':
        if app.cy==300:
            app.cx-=10
            if app.cx<150:
                app.cx+=10
    if key=='right':
        if app.cy==300:
            app.cx+=10
            if app.cx>200:
                app.cx-=10
    if key=='up':
        if app.cx==150:
            app.cy-=10
            if app.cy<200:
                app.cy+=10
    if key=='down':
        if app.cx==150:
            app.cy+=10
            if app.cy>300:
                app.cy-=10
    app.points.append((app.cx,app.cy))

def O(app,key):
    if key=='left':
        if app.cy==300 or app.cy==200:
            app.cx-=10
            if app.cx<150:
                app.cx+=10
    if key=='right':
        if app.cy==300 or app.cy==200:
            app.cx+=10
            if app.cx>200:
                app.cx-=10
    if key=='up':
        if app.cx==150 or app.cx==200:
            app.cy-=10
            if app.cy<200:
                app.cy+=10
    if key=='down':
        if app.cx==150 or app.cx==200:
            app.cy+=10
            if app.cy>300:
                app.cy-=10
    app.points.append((app.cx,app.cy))

def K(app,key):
    if key=='left':
        if (app.cy==300 and app.cx==200) or (250<=app.cy<300 and 150<=app.cx<200):
                app.cx-=10
                app.cy-=10
                if(app.cx<150):
                    app.cx+=10
                    app.cy+=10
    if key=='right':
        if (app.cy>250 and app.cx!=150) or (app.cy==250 and app.cx==150):
            app.cx+=10
            app.cy+=10
            if app.cx>200:
                app.cx-=10
            if app.cy>300:
                app.cy-=10
    if key=='up':
        if app.cx==150:
            app.cy-=10
            if app.cy<200:
                app.cy+=10
    if key=='down':
        if app.cx==150:
            app.cy+=10
            if app.cy>300:
                app.cy-=10
    app.points.append((app.cx,app.cy))
