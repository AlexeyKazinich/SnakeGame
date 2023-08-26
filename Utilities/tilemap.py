import pygame
from Utilities.objects import Rectangle
from random import randint

NEIGHBOR_OFFSETS = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (0,0), (-1,1),(0,1),(1,1)]

class Tile:
    def __init__(self,screen: pygame.display, pos: tuple,tile_size: int = 16,fill_type: str = "outline",color: pygame.Color = pygame.Color(255,255,255,255)):
        self.tile_size = tile_size
        self.pos = pos
        self.screen = screen
        self.fill_type = fill_type
        self.color = color
        
    
    def draw(self,offset:tuple = (0,0),color: pygame.Color = pygame.Color(0,0,0,255)) -> None:
        if self.fill_type == "fill":
            self.rect = Rectangle((int(self.pos[0]) + int(offset[0]))*self.tile_size,(int(self.pos[1])+int(offset[1]))*self.tile_size,self.tile_size,self.tile_size,self.screen,self.color)
            self.rect.draw()
        elif self.fill_type == "outline":
            self.rect = Rectangle((int(self.pos[0]) + int(offset[0]))*self.tile_size,(self.pos[1]+offset[1])*self.tile_size,self.tile_size,self.tile_size,self.screen,color)
            self.rect.draw_box()
        
        
class Tilemap:
    def __init__(self,screen: pygame.display, tile_size: int = 16):
        self.head_color = pygame.Color(0,200,0,255)
        self.body_color = pygame.Color(0,255,0,255)
        
        self.tile_size = tile_size
        self.tilemap ={}
        self.offgrid_tiles = {}
        self.snake = {"head": Tile(screen, (randint(0,10),randint(0,10)),tile_size,"fill",self.head_color)}
        self.snake_length = 1
        self.screen = screen
    
    def draw_grid(self,size:tuple) -> None:
        """call this to draw a grid"""
        for i in range(size[0]):
            for j in range(size[0]):
                get_loc = (i,j)
                self.tilemap[f"{get_loc[0]},{get_loc[1]}"] = Tile(self.screen,get_loc,self.tile_size)
    
    def fill_screen(self) -> None:
        size = [self.screen.get_width(),self.screen.get_height()]
        for i in range(int(size[0] / self.tile_size)+1):
            for j in range(int(size[1] / self.tile_size)+1):
                get_loc = (i,j)
                self.tilemap[f"{get_loc[0]},{get_loc[1]}"] = Tile(self.screen,get_loc,self.tile_size)
    
    
    def draw(self,offset:tuple = (0,0),color: pygame.Color = pygame.Color(255,255,255,255)):
        self.fill_screen()
        for key, value in self.tilemap.items():
            value.draw("fill")
        for key, value in self.snake.items():
            value.draw()
            
    
    
    def logic(self,move:str) -> None:
        """"""
        pass
    