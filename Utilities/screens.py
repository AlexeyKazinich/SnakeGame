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
        self.screen.fill((0,100,255))
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

class GameScreen:
    def __init__(self,screen, sceneManager):
        self.screen = screen
        self.grid = Tilemap(self.screen,32)
        self.grid.fill_screen()
        self.movement = "right"
        self.sceneManager = sceneManager
        self.paused = False
        self.pause_menu_button = {
            "resume":       Button(self.screen.get_width()//2 - 50, 0, 100,25,"resume",
                                   self.screen,color=(0,0,122,255),show_background=False, on_click_func=self.resume_button_onclick),
            
            "main_menu" :   Button(self.screen.get_width()//2 - 60, 0, 120,25,"main menu",
                                   self.screen,color=(0,0,122,255),show_background=False, on_click_func=self.main_menu_button_onclick),
            
            "quit":         Button(self.screen.get_width()//2 - 12, 0, 50,25,"quit",
                                   self.screen,color=(0,0,122,255),show_background=False, on_click_func=self.quit_button_onclick),
        }
        
        count = 1
        for _, button in self.pause_menu_button.items():
            button.align_on_y_axis(count,4)
            count += 1
    
    def resume_button_onclick(self) -> None:
        self.paused = False
    
    def main_menu_button_onclick(self) -> None:
        self.sceneManager.change_scene("main_menu")
    
    def quit_button_onclick(self) -> None:
        self.quit()
    
    def update_grid(self) -> None:
        """updates the grid"""
        self.grid.logic(self.movement)
        self.grid.fill_screen()
    
    
    def draw(self):
        """draws everything to the screen"""
        self.screen.fill((255,255,255))
        self.grid.draw(offset=(0,0),color=pygame.Color(0,0,0,255))
        
        if self.paused:
            pause_color = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
            pause_color.fill((255,255,255,150))
            self.screen.blit(pause_color,(0,0))
            
            for _, button in self.pause_menu_button.items():
                button.draw()
        
        pygame.display.flip()
    
    def quit(self) -> None:
        self.running = False
        pygame.quit()
        sys.exit()
    
    def logic_checks(self):
        """runs all the game logic"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and not self.paused:
                if event.key == pygame.K_d and not self.movement == "left":
                    self.movement = "right"
                if event.key == pygame.K_s and not self.movement == "up":
                    self.movement = "down"
                if event.key == pygame.K_a and not self.movement == "right":
                    self.movement = "left"
                if event.key == pygame.K_w and not self.movement == "down":
                    self.movement = "up"
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                    print(self.paused)
                    
            elif event.type == pygame.KEYDOWN and self.paused:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                    print(self.paused)
        
        if not self.paused:          
            self.update_grid()
            
        elif self.paused:
            for _, button in self.pause_menu_button.items():
                button.update()  
    
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