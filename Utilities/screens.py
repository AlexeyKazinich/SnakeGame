import pygame
from Utilities.tilemap import Tilemap

class Screen:
    def __init__(self):
        pass
    
    def draw(self):
        pass
    
    def update(self):
        pass
    


class GameScreen:
    def __init__(self,screen):
        self.screen = screen
        self.grid = Tilemap(self.screen,32)
        self.grid.fill_screen()
        self.movement = "right"
    
    def update_grid(self) -> None:
        """updates the grid"""
        self.grid.logic(self.movement)
        self.grid.fill_screen()
    
    def draw(self):
        """draws everything to the screen"""
        self.screen.fill((255,255,255))
        self.grid.draw(offset=(0,0),color=pygame.Color(0,0,0,255))
        pygame.display.flip()
    
    def logic_checks(self):
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
    
class SceneManager:
    def __init__(self,screen):
        self.screen = screen
        self.current_scene = "game"
        self.scene = {
            "game" : GameScreen(self.screen),
            "main_menu": Screen(),
        }
        
    def change_scene(self,new_scene: str = "main_menu"):
        
        if new_scene in self.scene.keys(): 
            self.current_scene = new_scene
        else:
            raise Exception("Scene passed does not exist")
    
    def draw(self):
        self.scene[self.current_scene].draw()
    
    
    def logic_checks(self):
        self.scene[self.current_scene].logic_checks()