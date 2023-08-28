import pygame

class Rectangle:
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 window, 
                 color: pygame.Color = pygame.Color(255,255,255))-> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.__rect = pygame.Rect(x,y,width,height)
        self.window = window

    def set_color(self,color:pygame.Color) -> None:
        """sets the color of the Rectangle"""
        self.color = color
    
    def draw(self)-> None:
        """draws a filled rectangle"""
        pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height))
    
    def draw_box(self)-> None:
        """draws an outline of a rectangle"""
        pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height),1)

    def collidepoint(self,locations: tuple) -> bool:
        """checks if the coords passed are colliding with this box"""
        self.__rect = pygame.Rect(self.x,self.y,self.width,self.height)
        if(self.__rect.collidepoint(locations)):
            return True
        else:
            return False

class Button:
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 text,
                 window,
                 color: pygame.Color = pygame.Color('lightskyblue3'),
                 text_color: pygame.Color = pygame.Color('lightskyblue3'),
                 hover_color: pygame.Color = pygame.Color('deepskyblue1'), 
                 active_color: pygame.Color = pygame.Color('dodgerblue2')) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
            
        self.text = text
        self.color = color
        self.text_color = text_color
        self.hover_color = hover_color
        self.active_color = active_color
        self.deactive_color = self.color
        self.font = pygame.font.Font(None,32)
        self.__rectangle = Rectangle(self.x,self.y,self.width,self.height,self.window)
        self.__rectangle.set_color(self.color)
        

        #mouse events
        self.pressed = False
        self.confirmed = False
        self.hover = False
        
        
    def get_pressed(self) -> None:
        """checks if the button was pressed, sets the value to false to prevent the button from staying pressed"""
        temp = self.pressed
        self.pressed = False
        return temp
    
    def center_of_screen_x(self) -> None:
        """center the button on the x axis"""
        self.x = (self.window.get_width() / 2) - (self.width / 2)
        self.__rectangle.x = self.x
    
    def align_on_y_axis(self, position: int = 1, amount: int = 1) -> None:
        """this will spread the buttons out evenly vertically"""
        self.y = (self.window.get_height()*position / (amount +1)) - (self.height / 2)
        self.__rectangle.y = self.y
        
    def set_active(self)-> None:
        """makes the button active"""
        self.color = self.active_color
        self.text_color = self.active_color
        self.__rectangle.set_color(self.active_color)

    def set_deactive(self)-> None:
        """makes the button inactive"""
        self.color = self.deactive_color
        self.text_color = self.deactive_color
        self.__rectangle.set_color(self.deactive_color)
    
    def set_hover(self)-> None:
        """sets the button to hover"""
        self.color = self.hover_color
        self.text_color = self.hover_color
        self.__rectangle.set_color(self.hover_color)

    def set_color(self,color)-> None:
        """sets the color of the button"""
        self.color = pygame.Color(color)
        self.textColor = pygame.Color(color)


    def collidepoint(self,locations) -> bool:
        """checks if the coords passed are colliding with the button"""
        if(self.__rectangle.collidepoint(locations)):
            return True
        else:
            return False

    def draw(self)-> None:
        """draw the button"""
        #render the current font
        self.textRender = self.font.render(self.text,True,self.text_color)

        #draw the outline
        self.__rectangle.draw_box()

        #draw the text
        self.window.blit(self.textRender,(self.x+5,self.y+5))
    
    def update(self) -> None:
        """run this to draw the button as well as check for collisions"""
        self.draw()
        self.check_click()
    
    def check_click(self)-> None:
        """checks if the button was clicked"""
        mouse_pos = pygame.mouse.get_pos() #mouse pos
        #if hovering
        if self.__rectangle.collidepoint(mouse_pos):
            self.hover = True
            self.set_hover()
        else: 
            self.hover = False
            self.set_deactive()
            
        #if clicking while hovering
        if(self.hover):
            if(pygame.mouse.get_pressed()[0]):
                self.set_active()
                self.pressed = True
            else: self.pressed = False