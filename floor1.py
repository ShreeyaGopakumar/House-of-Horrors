##plan: get a corridor with 4 doors and one main door 
#do something like google maps that lets the user go deeper into the corridor - perspective. 
#They can try to choose the main door but it should not work
#bcos we said we wanted the lab to be in the basement, have something that lets you go down 
#maybe have a main corridor at first where they can choose to go up or down
#if they go down, they have to find the skull
#if they go up, they go to a corridor where they choose between his study or his storage room. 
#further up the stairs is the corridor with 4 rooms and a main - 3 are restricted as they hold released spirits or something. another is the doll museum where the person can find the chucky
#The chucky has the key to the 'ritual room' where you find an altar with the professor's diary. 
#Perform the ritual that saves mankind!

from cmu_graphics import*
from PIL import Image
import os, pathlib
import image

def redrawAll(app):
    drawImage(app.floor1,0,0,width=app.width,height=app.height)
    if "room1" not in app.roomsVisited or "room3" not in app.roomsVisited:
        drawImage(app.redArrow,app.width//2-40,app.height//2+250,width=40,height=40,align='center')
    if "room2" not in app.roomsVisited:
        drawImage(app.redArrow,app.width//2+120,app.height//2+250,width=40,height=40,rotateAngle=180,align='center')

def onMousePress(app,mouseX,mouseY):
    if app.width//2-40-20<=mouseX<=app.width//2-40+20 and app.height//2+250-20<=mouseY<=app.height//2+250+20 and "room1" not in app.roomsVisited:
        return "corridor1"
    if app.width//2+120-20<=mouseX<=app.width//2+120+20 and app.height//2+250-20<=mouseY<=app.height//2+250+20 and "room2" not in app.roomsVisited:
        return "room2_intro"