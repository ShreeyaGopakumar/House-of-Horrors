from cmu_graphics import*
from PIL import Image
import os, pathlib
import image

def redrawAll(app):
    drawImage(app.floor2,0,0,width=app.width,height=app.height)
    if "room4" not in app.roomsVisited:
        drawImage(app.redArrow,app.width//2-60,app.height//2+250,width=40,height=40,align='center')
    

def onMousePress(app,mouseX,mouseY):
    if app.width//2-60-20<=mouseX<=app.width//2-60+20 and app.height//2+250-20<=mouseY<=app.height//2+250+20 and "room1" not in app.roomsVisited:
        return "room4"
    