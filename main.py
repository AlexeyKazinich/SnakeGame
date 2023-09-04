import pygame
from Utilities.game import Game
from Utilities.screens import GameStateManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 608
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = True
        self.clock = pygame.time.Clock()    
            
        self.scene_manager = GameStateManager(self.screen)
        
    def draw(self) -> None:
        self.scene_manager.draw()
    
    def logic_checks(self) -> None:
        self.scene_manager.logic_checks()
    
    def run(self) -> None:
        """initial call to get the game to run"""
        while self.running:
            self.logic_checks()
            self.draw()
            self.clock.tick(10)
      

if __name__ == "__main__":
    Game().run()