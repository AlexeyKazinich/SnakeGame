import pygame
from Utilities.game import Game
from Utilities.tilemap import Tilemap
from Utilities.screens import SceneManager

class Game(Game):
    def __init__(self):
        super().__init__()
            
        self.scene_manager = SceneManager(self.screen)
        
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
      
Game().run()