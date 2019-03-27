import pygame
from pygame.locals import *
from EnumTypes.RunMode import RunMode
from FileHelper import FileHelper
from GameModels.GameState import GameState

class UserInput:

    def __init__(self):
        self.StartTicks = pygame.time.get_ticks()
        self.GameState = GameState()
        self._debounce = 0

    def HandleInput(self, events, board):
        if(self._debounce > 0):
            self._debounce -= self._debounce                

        for event in events:
            if event.type == pygame.QUIT:
                self.GameState.Done = True
            if event.type == pygame.MOUSEBUTTONUP:                 
                self.SelectBox(pygame.mouse.get_pos(), board)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if(self._debounce == 0):
                    self._debounce = 10
                    self.GameState.RunMode = RunMode.MANUAL
                    self.GameState.AllowNextStep = True
            if keys[pygame.K_r]:
                self.GameState.RunMode = RunMode.MANUAL
                self.GameState.AllowNextStep = False
                self.GameState.Reset = True
            if keys[pygame.K_a]:
                if   self.GameState.RunMode == RunMode.MANUAL:
                    self.GameState.RunMode = RunMode.AUTO
                else:
                    self.GameState.RunMode = RunMode.MANUAL  
            if keys[pygame.K_s]:
                board.SaveBoard()
            if keys[pygame.K_o]:
                path = FileHelper.OpenFile()
                board.LoadFigure(path)

        if self.GameState.RunMode == RunMode.AUTO:
            seconds=(pygame.time.get_ticks() - self.StartTicks)/1000
            if seconds >= board.Layout.AutoRunTime:   
                self.StartTicks = pygame.time.get_ticks()
                self.GameState.AllowNextStep = True
            else:
                self.GameState.AllowNextStep = False    
            

    def SelectBox(self, position, board):
        x = int(position[0]/board.Layout.BoxSize)
        y = int(position[1]/board.Layout.BoxSize)
        if board.Board[y][x] == 1:
            board.Board[y][x] = 0
        else:           
            board.Board[y][x] = 1