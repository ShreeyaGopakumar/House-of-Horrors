from cmu_graphics import*
import random
def onAppStart(app):
    app.height=750
    app.width=1300
    app.cols=40
    app.rows=20
    app.board=[([False]*app.cols)for row in range(app.rows)]
    app.cy=app.rows-(app.rows-1)%4
    print(app.cy)
    app.cx=0
    for x in range(1,app.rows,4):
        newRow=[]
        ran=random.randint(0,app.cols//2)
        ran2=random.randint(app.cols//2,app.cols-3)
        ran=random.randint(min(ran,ran2),max(ran,ran2))
        for col in range(app.cols):
            if col==ran or col==ran+1 or col==ran+2:
                app.cx=ran+1
                newRow.append(True)
            else:
                newRow.append(False)
        app.board[x]=newRow
    app.boardLeft = 0
    app.boardTop = 0
    app.boardWidth = app.width
    app.boardHeight = app.height
    app.cellBorderWidth = 2
    app.cellWidth= app.boardWidth//app.cols
    app.cellHeight=app.boardHeight//app.rows
    app.pieceColor='white'
    app.dx=0
    app.dy=0
    
def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            if app.board[row][col]:
                color='white'
            else:
                color='black'
            drawCell(app, row, col, color)

def drawBoardBorder(app):
  # draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill="black", border='black',
           borderWidth=2*app.cellBorderWidth)


def getCellLeftTop(app, row, col,color):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col,color)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)


def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

def redrawAll(app):
    drawBoardBorder(app)
    drawBoard(app)
    drawCircle((app.cx+1)*app.cellWidth,(app.cy)*app.cellHeight,10,fill='red')

#def onKeyPress(app,key):
    


def main():
    runApp()

main()