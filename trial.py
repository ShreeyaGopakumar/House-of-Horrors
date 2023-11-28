from cmu_graphics import*
import random
def onAppStart(app):
    app.height=750
    app.width=1300
    app.cols=10
    app.rows=15
    app.board = [[False,True,True,True,True,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [True, True, True, True, False, False, False, False, False, False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False, False, False, False, True, True, True, True, True],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 [False, False,False,False,False,False,False,False,False,False],
                 ]
    app.boardLeft = 95
    app.boardTop = 50
    app.boardWidth = 210
    app.boardHeight = 280
    app.cellBorderWidth = 2
    app.cellWidth= app.boardWidth//app.cols
    app.cellHeight=app.boardHeight//app.rows
    app.pieceColor='white'
    


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

def main():
    runApp()

main()