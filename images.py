import Room
from cmu_graphics import *
from PIL import Image
import os, pathlib

#See: https://pillow.readthedocs.io/en/stable/reference/Image.html 

def onAppStart(app):
    app.margin = 5

    # Open image from local directory
    app.image = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/clock.png"))
    
    # Note that you need to "import os, pathlib" for this to work!
    # If this is the solution that works on your operating system,
    # I recommend defining a custom function to open images as such:
    
    def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
    
    app.image = openImage("images/clock.png")
    
    
    # Moving on...
    # Access attributes like width and height
    app.imageWidth,app.imageHeight = app.image.width,app.image.height

    
    # Cast image type to CMUImage to allow for faster drawing
    app.image = CMUImage(app.image)
    
def redrawAll(app):
    newWidth, newHeight = (app.imageWidth//2,app.imageHeight//2)
    drawImage(app.image,200,200,width=newWidth,height=newHeight)

    
def main():
    runApp(width=800,height=800)

if __name__ == '__main__':
    main()

