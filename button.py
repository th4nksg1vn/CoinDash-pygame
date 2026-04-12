"""
    This module defines each button in the game.
"""

import pygame

class Button:
    ##self.image : pygame.image; The image of the button
    ##self.text : str; Text that should be shown atop the button
    ##self.font : int; Font size of the text
    ##self.original_width : int; The initial width of the self.image
    ##self.original_height : int; The initial height of the self.image
    ##self.new_width : int; The final width of the self.image
    ##self.new : int; The final height of the self.image
    ##self.rect : pygame.rect; A rect representing the button
    ##self.pressed : bool; check if button has been pressed or not
    
    def __init__(self, image_path, position, text=None, font_path=None, font_size=24, text_color="#ffffff",background_color=None, scale=1.0):

        #initialisation
        self.image = pygame.image.load(image_path).convert_alpha()
        if text is None:
            self.text = ""
        else: self.text = text
        
        if font_path is None: 
            self.font = pygame.font.Font(size=font_size)
        else:
            self.font = pygame.font.Font(font_path,font_size)
        
        #Get original dimensions of the image
        self.original_width = self.image.get_width()
        self.original_height = self.image.get_height()
        
        #Get new dimensions
        self.new_width = int(self.original_width * scale)
        self.new_height = int(self.original_height * scale)
        
        #Finalise button
        self.image = pygame.transform.smoothscale(self.image, (self.new_width, self.new_height))
        self.rendered_text = self.font.render(self.text,True,text_color,background_color)

        #Create a rect at the center of the button to draw the text on
        self.text_rect = self.rendered_text.get_rect(center=(int(self.new_width/2)+position[0],int(self.new_height/2)+position[1]))
        
        self.rect = self.image.get_rect(topleft = position)
        self.pressed = False

    def is_pressed(self):
        self.pressed = False #By default buttons are not considered pressed
        mouse_pos = pygame.mouse.get_pos() #Get mouse position

        if self.rect.collidepoint(mouse_pos): #If the mouse position is in the button area...
                self.pressed = True

        return self.pressed 

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.rendered_text, self.text_rect)

if __name__ == "__main__":
    #Test by Christina
    #Modified slightly so that Each button records a single press
    
    import pygame, sys

    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Button Module")

    background = pygame.image.load("assets/UI/background.jpeg").convert()

    start_button = Button("assets/UI/btn_blue.png", (300, 150), "Start", font_size=52, scale=0.65) #Create a blue button with the text "Start" on it
    exit_button = Button("assets/UI/btn_red.png", (300, 300), "Exit", font_size=52, scale=0.65)

    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: #Has the left mouse button been clicked?
                if start_button.is_pressed():
                    print("Start Button pressed")

                if exit_button.is_pressed():
                    pygame.quit()
                    sys.exit()

        window.fill("black")
        window.blit(background, (0, 0))
        start_button.draw(window)
        exit_button.draw(window)

        pygame.display.flip()
        clock.tick(60)



    