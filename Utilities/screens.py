import sys
import pygame
from Utilities.tilemap import Tilemap
from Utilities.objects import Button
    
class MainMenu:
    def __init__(self,screen,sceneManager):
        self.screen = screen
        self.sceneManager = sceneManager
        self.buttons = {
            "start_game": Button(self.screen.get_width() //2 - 35,0,75,25,"start",self.screen,on_click_func=self.start_onclick)
        }
        
    def draw(self):
        """draws everything to the screen"""
        self.screen.fill((0,255,0))
        for _, button in self.buttons.items():
            button.draw()
        pygame.display.flip()
    
    def start_onclick(self):
        self.sceneManager.change_scene("game")
    
    def logic_checks(self):
        """runs all the game logic"""
        for _, button in self.buttons.items():
            button.update()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.sceneManager.change_scene("game")

class GameScreen:
    def __init__(self,screen, sceneManager):
        self.screen = screen
        self.grid = Tilemap(self.screen,32)
        self.grid.fill_screen()
        self.movement = "right"
        self.sceneManager = sceneManager
    
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
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and not self.movement == "left":
                    self.movement = "right"
                if event.key == pygame.K_s and not self.movement == "up":
                    self.movement = "down"
                if event.key == pygame.K_a and not self.movement == "right":
                    self.movement = "left"
                if event.key == pygame.K_w and not self.movement == "down":
                    self.movement = "up"
                if event.key == pygame.K_ESCAPE:
                    self.sceneManager.change_scene("main_menu")
        self.update_grid()
    
class GameStateManager:
    def __init__(self,screen):
        self.screen = screen
        self.current_scene = "main_menu"
        self.scene = {
            "game" : GameScreen(self.screen,self),
            "main_menu": MainMenu(self.screen,self),
        }
        
    def reset_scenes(self):
        self.scene["game"] = GameScreen(self.screen, self)
        self.scene["main_menu"] = MainMenu(self.screen, self)
        
    def change_scene(self,new_scene: str = "main_menu"):
        
        if new_scene in self.scene.keys(): 
            self.current_scene = new_scene
            self.reset_scenes()
        else:
            raise Exception("Scene passed does not exist")
    
    def draw(self):
        self.scene[self.current_scene].draw()
    
    
    def logic_checks(self):
        self.scene[self.current_scene].logic_checks()