from GameModels.GameState import GameState
import json
from JsonParser import JsonParser
from FileHelper import FileHelper

class Board:

    def __init__ (self, layout):
        self.Layout = layout
        self.Board = []
        self.InitiateBoard()

    def CreateBoard(self, board):
        for i in range(self.Layout.VerticalLength):
            board.append([])
            for j in range(self.Layout.HorizontalLength):
                board[i].append(0)

    def InitiateBoard(self):
        self.Board = []
        for i in range(self.Layout.VerticalLength):
            self.Board.append([])
            for j in range(self.Layout.HorizontalLength):
                 self.Board[i].append(0)

    def NextStep(self, gameState):
        if(gameState.AllowNextStep and not gameState.Reset):
            self.NextGeneration(gameState)
        elif(gameState.Reset):
            self.Reset(gameState)

    def NextGeneration(self, gameState):
        tempList = []
        self.CreateBoard(tempList)
        for i in range(self.Layout.VerticalLength):
            for j in range(self.Layout.HorizontalLength):
                amount = self.AmountOfNeighbours(i,j)
                if self.Board[i][j] == 1:
                    if amount >= 4:
                        tempList[i][j] = 0
                    elif amount < 2:
                        tempList[i][j] = 0
                    else:
                        tempList[i][j] = 1
                elif self.Board[i][j] == 0:
                    if amount == 3:
                        tempList[i][j] = 1                       
        self.Board = tempList.copy()
        gameState.StepNumber += 1
        gameState.AllowNextStep = False

    def Reset(self, gameState):
        self.Board = []
        self.InitiateBoard()
        gameState.Reset = False

    def AmountOfNeighbours(self, i, j):
        count = 0              
        if j < self.Layout.HorizontalLength-1:
            if self.Board[i][j+1] == 1:
                count = count + 1
            if i < self.Layout.VerticalLength-1:
                if self.Board[i+1][j+1] == 1:
                    count = count + 1
            if i >= 1:
                if self.Board[i-1][j+1] == 1:
                    count = count + 1

        if j >= 1:       
            if self.Board[i][j-1] == 1:
                count = count + 1
            if i < self.Layout.VerticalLength-1:
                if self.Board[i+1][j-1] == 1:
                    count = count + 1
            if i >= 1:
                if self.Board[i-1][j-1] == 1:
                    count = count + 1

        if i < self.Layout.VerticalLength-1:
                if self.Board[i+1][j] == 1:
                    count = count + 1

        if i >= 1:
                if self.Board[i-1][j] == 1:
                    count = count + 1
        return count

    def SaveBoard(self):
        cellActiveList = []
        minSizeX = 0
        minSizeY = 0
        for i in range(self.Layout.VerticalLength):
                for j in range(self.Layout.HorizontalLength):
                    if(self.Board[i][j] == 1):
                        cellActiveList.append((j,i))
                        if(minSizeX == 0 or minSizeX < j):
                            minSizeX = j
                        if(minSizeY == 0 or minSizeY < i):
                            minSizeY = i
        path = FileHelper.SaveFile({"minSizeX": minSizeX, "minSizeY": minSizeY, "Active": cellActiveList})

    def LoadFigure(self, path):
        figure = JsonParser.CreateFigure(path)
        if(figure.MinSizeX+1 >= self.Layout.HorizontalLength):
            self.Layout.HorizontalLength = figure.MinSizeX+1
            self.InitiateBoard()

        if(figure.MinSizeY+1 >= self.Layout.VerticalLength):
            self.Layout.VerticalLength = figure.MinSizeY+1
            self.InitiateBoard()

        for temp in figure.ActiveCells:
            self.Board[temp[1]][temp[0]] = 1
