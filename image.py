
from cmu_graphics import*
from PIL import Image
import os, pathlib
def loadImages(app):
    def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
    
    app.bg = openImage("images/bg.png")
    app.bgWidth,app.bgHeight = app.width,app.height
    app.bg = CMUImage(app.bg)

    app.intro = openImage("images/intro.png")
    app.introWidth,app.introHeight = app.width,app.height
    app.intro = CMUImage(app.intro)

    app.candles = openImage("images/candles.png")
    app.candles = CMUImage(app.candles)
    
    app.killerclown=openImage("images/killerclown.png")
    app.killerclown=CMUImage(app.killerclown)
    
    app.killerclown_2=openImage("images/killerclown_2.png")
    app.killerclown_2=CMUImage(app.killerclown_2)
    
    app.clown = openImage("images/clown.png")
    app.clown = CMUImage(app.clown)
    
    app.bg2=openImage("images/bg_2.png")
    app.bg2=CMUImage(app.bg2)
    
    app.scary = openImage("images/scary.png")
    app.scary = CMUImage(app.scary)
    
    app.nun = openImage("images/nun.png")
    app.nun = CMUImage(app.nun)
    
    app.room3_intro=openImage("images/room3_intro.png")
    app.room3_intro=CMUImage(app.room3_intro)
    
    app.skull=openImage("images/skull.png")
    app.skull=CMUImage(app.skull)
    
    app.door1 = openImage("images/door1.png")
    app.door1Width,app.door1Height = app.door1.width,app.door1.height
    app.door1 = CMUImage(app.door1)
    
    app.door2 = openImage("images/door2.png")
    app.door2Width,app.door2Height = app.door2.width,app.door2.height
    app.door2 = CMUImage(app.door2)
    
    app.room1_frame1=openImage("images/room1_frame1.png")
    app.room1_frame1=CMUImage(app.room1_frame1)
    
    app.room1_frame2=openImage("images/room1_frame2.png")
    app.room1_frame2=CMUImage(app.room1_frame2)
    
    app.control=openImage("images/Control and Instructions.png")
    app.control=CMUImage(app.control)
    
    app.room2_intro=openImage("images/room2_intro.png")
    app.room2_intro=CMUImage(app.room2_intro)
    
    app.room2=openImage("images/room2.png")
    app.room2=CMUImage(app.room2)

    app.arrow=openImage("images/arrow.png")
    app.arrowWidth,app.arrowHeight=app.arrow.width,app.arrow.height
    app.arrow=CMUImage(app.arrow)
    
    app.tick=openImage("images/tick.png")
    app.tick=CMUImage(app.tick)
    
    app.letter_puzzle=openImage("images/letter_puzzle.png")
    app.letter_puzzleWidth,app.letter_puzzleHeight=app.letter_puzzle.width,app.letter_puzzle.height
    app.letter_puzzle=CMUImage(app.letter_puzzle)

    app.chest=openImage("images/chest.png")
    app.chest=CMUImage(app.chest)

    app.over=openImage("images/over.png")
    app.over=CMUImage(app.over)

    app.player=openImage("images/player.png")
    app.player=CMUImage(app.player)
    
    app.key=openImage("images/key.png")
    app.key=CMUImage(app.key)
    
    app.door=openImage("images/door.png")
    app.door=CMUImage(app.door)
    
    app.bg3=openImage("images/bg3.jpg")
    app.bg3=CMUImage(app.bg3)

    app.gameOverImage=openImage("images/gameOver.png")
    app.gameOverImage=CMUImage(app.gameOver)

    app.timer=openImage("images/timer.png")
    app.timer=CMUImage(app.timer)
    
    app.jumpscare=openImage("images/jumpscare.gif")
    app.jumpscare=CMUImage(app.jumpscare)
    #___________________________________________________________________________
    '''Images used:
    Background_1: https://www.ngpf.org/blog/activities/escape-from-the-haunted-mansion-a-new-halloween-activity/
    Background_2: https://www.deviantart.com/kuzy62/art/Spooky-Graveyard-934651358
    Candles: https://gallery.yopriceville.com/Free-Clipart-Pictures/Halloween-PNG-Pictures/Lighted_Candles_Transparent_Image
    Clown mask: https://www.walmart.com/ip/Adult-Whacko-Clown-Full-Face-Mask/1402672413?wmlspartner=wlpa&selectedSellerId=737
    Doors: https://community.boschsecurity.com/t5/Security-Access-Control/How-to-set-up-interlock-APE/ta-p/12325
    Jumpscare: https://www.deviantart.com/zueiroooooooooooo/art/Nightmare-Freddy-Ucn-Jumpscare-FullBody-828859450
    Nun: https://www.newburyportnews.com/news/lifestyles/movie-review-in-the-nun-what-evil-lurks-beneath-a-habit/article_cfddb3f0-7974-5e1b-9e97-80bee389f993.html
    Map: https://brainchase.com/national-scavenger-hunt-day-coming/
    Room2 (corridor): <a href="https://www.freepik.com/free-photo/abandoned-alley-psychiatric-hospital_5600084.htm#query=creepy%20corridor&position=0&from_view=search&track=ais&uuid=b257c826-e514-4c68-be4b-33706549068d">Image by jcomp</a> on Freepik
    Room2 (mortuary): <a href="https://www.freepik.com/free-photo/abandoned-morgue-psychiatric-hospital_5600088.htm#query=creepy%20lab&position=0&from_view=search&track=ais&uuid=251a2fa0-7336-42d8-9fec-09b092841387">Image by jcomp</a> on Freepik
    Room3 (clown intro): https://www.amazon.com/Halloween-Decoration-Background-Photography-Backdrop/dp/B09C38SX8K?th=1
    killerclown (spirits): https://genius.com/Andrews-imagination-at-sablon-beach-lyrics
    
    Other screens and elements - made on Canva
    '''
    #___________________________________________________________________________
