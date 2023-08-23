import pygame
from Utilities.game import Game
from Utilities.tilemap import Tilemap

class Game(Game):
    def __init__(self):
        super().__init__()
        self.grid = Tilemap(self.screen,32)
        self.grid.fill_screen()
        
        
    def draw(self) -> None:
        """draws everything to the screen"""
        self.screen.fill((255,255,255))
        self.grid.draw(color=pygame.Color(0,0,0,255))
        pygame.display.flip()
    
    def logic_checks(self) -> None:
        """runs all the game logic"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            
      
Game().run()