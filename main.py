import pygame
from GameModels.GameLayout import GameLayout
from DrawHelper import DrawHelper
from GameModels.Board import Board
from UserInput import UserInput
from JsonParser import JsonParser
from EnumTypes.RunMode import RunMode
from GameModels.GameState import GameState
import time


 
if __name__ == "__main__" :
    pygame.init()
    pygame.display.set_caption("Game of Life By Neggie")
    BLACK = (0,0,0)
    done = False
    
    layout = JsonParser.CreateLayout("config/layout.config")
    screen = pygame.display.set_mode(layout.GetWindowDimensions())
    board = Board(layout)
    userInput = UserInput()

    while not done:
        userInput.HandleInput(pygame.event.get(), board)
        done = userInput.GameState.Done
        board.NextStep(userInput.GameState)

        if(layout.DimensionsChanged == True):
             screen = pygame.display.set_mode(layout.GetWindowDimensions())

        DrawHelper.DrawBoard(screen, board) 
        DrawHelper.DrawRaster(screen, board)  
        
        pygame.display.flip()
        screen.fill(BLACK)  
