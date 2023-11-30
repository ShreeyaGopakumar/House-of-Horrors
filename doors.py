from cmu_graphics import *

def features(app):
    app.sidePanel=False
    app.foundCandle=False
    app.MdoorOpen=False
    app.LdoorOpen=False
    app.RdoorOpen=False
    app.flag=1
    app.flag2=1
def redrawAll(app):
    drawRect(0,0,app.width,app.height,fill='grey')
    drawRect(0,0,app.width,100,fill='white')
    drawLabel("ONE DOOR LEADS TO A STUDY, TWO DOORS LEAD TO A SCARE",app.width//2,20,font="monospace",size=20,fill='maroon')
    drawLabel("CHOOSE THE RIGHT DOOR IF YOU DARE!",app.width//2,60,font="monospace",size=20,fill='maroon')
    if not app.MdoorOpen:
        drawImage(app.door1,app.width//2,app.height//2,width=app.door1Width,height=app.door1Height,align='center')
    
    else:
        drawRect(app.width//2,app.height//2,app.door2Width,app.door2Height-70,align='center')   
        drawImage(app.door2,app.width//2,app.height//2+15,width=app.door2Width,height=app.door2Height,align='center')
        drawImage(app.scary,app.width//2,app.height//2,width=app.door2Width+40,height=app.door2Height-50,align='center')
        
    
    if not app.LdoorOpen:
        drawImage(app.door1,app.width//2-app.door1Width-60,app.height//2,width=app.door1Width,height=app.door1Height,align='center')
    else:
        drawRect(app.width//2-app.door1Width-60,app.height//2+15,app.door2Width,app.door2Height-70,align='center')   
        drawImage(app.door2,app.width//2-app.door1Width-60,app.height//2+15,width=app.door2Width,height=app.door2Height,align='center')
        drawImage(app.nun,app.width//2-app.door1Width-60,app.height//2+15,width=app.door2Width+40,height=app.door2Height-50,align='center')
        
    if not app.RdoorOpen:
        drawImage(app.door1,app.width//2+app.door1Width+60,app.height//2,width=app.door1Width,height=app.door1Height,align='center')
    else:
        drawRect(app.width//2+app.door1Width+60,app.height//2+15,app.door2Width,app.door2Height-70,align='center')   
        drawImage(app.door2,app.width//2+app.door1Width+60,app.height//2+15,width=app.door2Width,height=app.door2Height,align='center')
    drawRect(0,app.height//2+app.door1Height//2-10,app.width,app.height-app.height//2-app.door1Height//2,fill='black')

    
def click(mouseX,mouseY):
    if app.width//2-app.door1Width//2<=mouseX<=app.width//2+app.door1Width//2 and app.height//2-app.door1Height//2<=mouseY<=app.height//2+app.door2Height:
        app.MdoorOpen=not app.MdoorOpen
    if app.width//2-app.door1Width-45-app.door1Width//2<=mouseX<=app.width//2-app.door1Width-60+app.door1Width//2 and app.height//2-app.door1Height//2<=mouseY<=app.height//2+app.door1Height//2:
        app.LdoorOpen=not app.LdoorOpen 
    
    if app.width//2+app.door1Width+60-app.door1Width//2<=mouseX<=app.width//2+app.door1Width+60+app.door1Width//2 and app.height//2-app.door1Height//2<=mouseY<=app.height//2+app.door1Height//2:
        if app.RdoorOpen:
            app.flag+=1
        else:
            app.RdoorOpen=True
    


