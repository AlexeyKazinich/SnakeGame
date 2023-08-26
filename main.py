import pygame
from Utilities.game import Game
from Utilities.tilemap import Tilemap
import random

class Game(Game):
    def __init__(self):
        super().__init__()
        self.grid = Tilemap(self.screen,32)
        self.grid.fill_screen()
        
        self.movement = "right"
        
    def draw(self) -> None:
        """draws everything to the screen"""
        self.screen.fill((255,255,255))
        self.grid.draw(color=pygame.Color(0,0,0,255))
        pygame.display.flip()
    
    def update_grid(self):
        if self.movement == "right":
            self.grid.logic("right")
        elif self.movement == "left":
            self.grid.logic("left")
        elif self.movement == "up":
            self.grid.logic("up")
        elif self.movement == "down":
            self.grid.logic("down")
        self.grid.fill_screen()
    
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