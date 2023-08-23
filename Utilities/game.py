import pygame

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = True
        self.clock = pygame.time.Clock()
     
    def run(self) -> None:
        """initial call to get the game to run"""
        while self.running:
            self.logic_checks()
            self.draw()
            self.clock.tick(60)
    
    def draw(self) -> None:
        """draws everything to the screen"""
        self.screen.fill((255,255,255))
        pygame.display.flip()
    
    def logic_checks(self) -> None:
        """runs all the game logic"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()