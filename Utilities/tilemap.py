import pygame
from Utilities.objects import Rectangle
from random import randint

NEIGHBOR_OFFSETS = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (0,0), (-1,1),(0,1),(1,1)]

class Tile:
    def __init__(self,screen: pygame.display, pos: tuple,tile_size: int = 16,fill_type: str = "outline",color: pygame.Color = pygame.Color(255,255,255,255)):
        self.tile_size = tile_size
        self.pos = pos
        self.previous_pos = (0,0)
        self.screen = screen
        self.fill_type = fill_type
        self.color = color
        self.rect = Rectangle(0,0,0,0,self.screen,(255,255,255))
        
    
    def draw(self,offset:tuple = (0,0),color: pygame.Color = pygame.Color(0,0,0,255)) -> None:
        """draws the rectangle"""
        if self.fill_type == "fill":
            self.rect = Rectangle((int(self.pos[0]) + int(offset[0]))*self.tile_size,(int(self.pos[1])+int(offset[1]))*self.tile_size,self.tile_size,self.tile_size,self.screen,self.color)
            self.rect.draw()
        elif self.fill_type == "outline":
            self.rect = Rectangle((self.pos[0] + int(offset[0])) *self.tile_size,(self.pos[1]+offset[1])*self.tile_size,self.tile_size,self.tile_size,self.screen,color)
            self.rect.draw_box()
            
    def collide(self,rect: Rectangle) -> bool:
        """checks if the rectangle is colliding with a different rectangle"""
        return self.rect.collidepoint((rect.x,rect.y))
        
        
class Tilemap:
    def __init__(self,screen: pygame.display, tile_size: int = 16):
        self.head_color = pygame.Color(0,200,0,255)
        self.body_color = pygame.Color(0,255,0,255)
        self.apple_color = pygame.Color(255,0,0,255)
        
        self.tile_size = tile_size
        self.tilemap ={}
        self.offgrid_tiles = {}
        self.snake = {"head": Tile(screen, (randint(0,10),randint(0,10)),tile_size,"fill",self.head_color)}
        self.snake_length = 1
        self.screen = screen
        
        self.apple = Tile(self.screen,(randint(0,10),randint(0,10)),32,"fill",self.apple_color)
    
    def draw_grid(self,size:tuple) -> None:
        """call this to draw a grid"""
        for i in range(size[0]):
            for j in range(size[0]):
                get_loc = (i,j)
                self.tilemap[f"{get_loc[0]},{get_loc[1]}"] = Tile(self.screen,get_loc,self.tile_size)
    
    def get_loc_part(self,name: str) -> tuple:
        """gets the location from the dictionary for a given snake part"""
        location = (self.snake[name].pos[0],self.snake[name].pos[1] + 1)
        return location
    
    def extend_snake(self) -> None:
        """extends the snake by 1"""
        if self.snake_length == 1:
            self.snake[f"body{self.snake_length}"] =Tile(self.screen,self.get_loc_part("head"),fill_type="fill",color=self.body_color,tile_size=self.tile_size)
            self.snake_length += 1
        else:
            self.snake[f"body{self.snake_length}"] = Tile(self.screen,self.get_loc_part(f"body{self.snake_length-1}"),fill_type="fill",color=self.body_color,tile_size=self.tile_size)
            self.snake_length += 1
    
    def fill_screen(self) -> None:
        """fills the screen with a grid"""
        size = [self.screen.get_width(),self.screen.get_height()]
        for i in range(int(size[0] / self.tile_size)+1):
            for j in range(int(size[1] / self.tile_size)+1):
                get_loc = (i,j)
                self.tilemap[f"{get_loc[0]},{get_loc[1]}"] = Tile(self.screen,get_loc,self.tile_size)
    
    def get_tiles_around(self) -> None:
        """gets the tiles around the head to check for collisions"""
        loc = self.snake["head"].pos
    
    def draw(self,offset:tuple = (0,0),color: pygame.Color = pygame.Color(255,255,255,255)):
        self.fill_screen()
        for _, value in self.tilemap.items():
            value.draw()
        for _, value in self.snake.items():
            value.draw()
        self.apple.draw()
            
    def update_apple(self) -> None:
        """relocates the apple to a new location"""
        self.apple = Tile(self.screen,(randint(0,24),randint(0,19)),self.tile_size,"fill",self.apple_color)
    
    
    def logic(self,move:str) -> None:
        """runs the logic for the tilemap"""
        if self.snake["head"].collide(self.apple.rect):
            self.extend_snake()
            self.update_apple()
            
        
        count = 1
        for key, value in self.snake.items():
            if key == "head" and move == "right":
                value.previous_pos = value.pos
                value.pos = (value.pos[0] + 1,value.pos[1])
            elif key == "head" and move == "left":
                value.previous_pos = value.pos
                value.pos = (value.pos[0] - 1,value.pos[1])
            elif key == "head" and move == "up":
                value.previous_pos = value.pos
                value.pos = (value.pos[0],value.pos[1]-1)
            elif key == "head" and move == "down":
                value.previous_pos = value.pos
                value.pos = (value.pos[0],value.pos[1]+1)
                
            elif key == "body1":
                value.previous_pos = value.pos
                value.pos = self.snake["head"].previous_pos
            else:
                value.previous_pos = value.pos
                value.pos = self.snake[f"body{count}"].previous_pos
                count += 1
        
        