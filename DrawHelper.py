import pygame
from pygame.locals import *

class DrawHelper:

    @staticmethod
    def DrawRaster(screen, board):
        for i in range(board.Layout.HorizontalLength):
            pygame.draw.line(screen, board.Layout.LineColor, (board.Layout.BoxSize*i, 0), (board.Layout.BoxSize*i, board.Layout.VerticalLength*board.Layout.BoxSize))

        for j in range(board.Layout.VerticalLength):
            pygame.draw.line(screen, board.Layout.LineColor, (0, board.Layout.BoxSize*j), (board.Layout.HorizontalLength*board.Layout.BoxSize, j*board.Layout.BoxSize))

    @staticmethod
    def DrawBoard(screen, board):
        for i in range(board.Layout.HorizontalLength):
            for j in range(board.Layout.VerticalLength):
                if board.Board[j][i] == 1:
                    pygame.draw.rect(screen,board.Layout.BoxColor, (i*board.Layout.BoxSize,j*board.Layout.BoxSize,board.Layout.BoxSize,board.Layout.BoxSize))

        
            
