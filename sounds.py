import os,pathlib
from cmu_graphics import*

#adapted from Sound Demo
def loadSound(relativePath):
    absolutePath = os.path.abspath(relativePath)
    url = pathlib.Path(absolutePath).as_uri()
    return Sound(url)

def allSounds(app):
    app.music = loadSound("horrormusic.mp3")
    app.scream=loadSound("scream.mp3")
    app.doorSound=loadSound("doorSound.mp3")
    app.jump=loadSound("jump.mp3")
    app.music.play(restart = True)
    
''''
jump sound: https://youtu.be/ZrP-30MmpvM?feature=shared
background music: https://youtu.be/FnS4OJWeuD4?feature=shared
scream: https://youtu.be/4JvJd6BkBJ4?feature=shared
door creaking: https://youtu.be/hvVSCwxCVDE?feature=shared
'''


