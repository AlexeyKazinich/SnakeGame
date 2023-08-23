import pygame
import time
import math


class FpsCounter:
    """This class is designed only to show the current FPS, it does not allow to limit the framerate of the game"""
    def __init__(self,window: pygame.display,font_size: int = 12,background_color: tuple = (0,0,0,0))-> None:
        pygame.font.init()
        
        self.cSec = 0
        self.cFrame = 0
        self.FPS= 0
        self.deltatime = 0
        self.font_fps = pygame.font.Font(None,font_size)
        self.color_fps = pygame.Color(0,255,0)
        self.area = window.get_rect()
        self.window = window
        self.tickrate = 100
    
    def count_fps(self)-> None:
        """run this inside the game loop"""
        if self.cSec == time.strftime("%S"):
            self.cFrame +=1
        else:
            self.FPS = self.cFrame
            self.cFrame = 0
            self.cSec = time.strftime("%S")
            if self.FPS > 0:
                self.deltatime = 1 / self.FPS
                
                
    def draw(self)-> None:
        """call this to draw the frame counter"""
        #background rectangle
        
        
        #text
        self.FPS_counter_surface = self.font_fps.render(str(math.floor(self.FPS))+"FPS",True,self.color_fps)
        self.window.blit(self.FPS_counter_surface,(self.area.width-self.FPS_counter_surface.get_width(),0))