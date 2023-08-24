import pygame
from Utilities.game import Game
from Utilities.tilemap import Tilemap
import random

class Game(Game):
    def __init__(self):
        super().__init__()
        self.grid = Tilemap(self.screen,32)
        self.grid.fill_screen()
        self.head_color = pygame.Color(0,200,0,255)
        self.body_color = pygame.Color(0,255,0,255)
        self.movement = "right"
        self.length_counter = 1
        self.snake = {
            "head": [random.randint(0,10),random.randint(0,10)],
        }
        self.snake[f"body{self.length_counter}"] = [self.snake["head"][0],self.snake["head"][1]-1]
        print(self.snake)
        
    def draw(self) -> None:
        """draws everything to the screen"""
        self.screen.fill((255,255,255))
        self.grid.draw(color=pygame.Color(0,0,0,255))
        self.grid.set_tile(self.snake["head"],self.head_color,32)
        
        for key, value in self.snake.items():
            if key is not "head":
                self.grid.set_tile(value,self.body_color,32)
            else:
                self.grid.set_tile(value,self.head_color,32)
        pygame.display.flip()
    
    def update_grid(self):
        temp = (self.snake["head"][0],self.snake["head"][1])
        if self.movement == "right":
            self.snake["head"][0] +=1
        elif self.movement == "left":
            self.snake["head"][0] -=1
        elif self.movement == "up":
            self.snake["head"][1] -= 1
        elif self.movement == "down":
            self.snake["head"][1] += 1
        self.grid.fill_screen()
        
        for key, value in self.snake.items():
            if key == "head":
                self.grid.set_tile((value[0],value[1]),self.head_color,32)
            if key == "body1":
                self.grid.set_tile((self.snake["head"][0],self.snake["head"][1]),self.body_color,32)
        
    
    def logic_checks(self) -> None:
        """runs all the game logic"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and not self.movement == "left":
                    self.movement = "right"
                if event.key == pygame.K_s and not self.movement == "up":
                    self.movement = "down"
                if event.key == pygame.K_a and not self.movement == "right":
                    self.movement = "left"
                if event.key == pygame.K_w and not self.movement == "down":
                    self.movement = "up"
        self.update_grid()
    
    def run(self) -> None:
        """initial call to get the game to run"""
        while self.running:
            self.logic_checks()
            self.draw()
            self.clock.tick(10)
      
Game().run()