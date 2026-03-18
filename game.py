"""
This module handles the playing of the game.
The reason is that this code is planned to be especially long...
so the main game would probably be stored in a file called "main" or something like that

I plan to set up the screen, frame rate, and caption in the main file
"""
from player import Player

score, time, level = 0
player = None

def initialize(screen):
    global score,time,level,player
    
    screen_size=(screen.get_rect().right,screen.get_rect().bottom) #Get the size of the screen
    score = 0 #Set score
    time = 10 #Set time to 10s
    level = 1 #Set level to 1
    player = Player(int(screen_size[0]/2),int(screen_size[1]/2)) #Spawn the player at the center of the screen
    
    start_sound = pygame.mixer.Sound("assets/audio/Level.wav") #Play the sound to start the game
    start_sound.play()
    


if __name__ == "__main__":
    import pygame
    
    pygame.init()
    
    SCREEN = pygame.display.set_mode((480,720))
    pygame.display.set_caption("Game module")
    
    FRAMERATE = 60
    clock = pygame.time.Clock()
    
    initialize(SCREEN)
    background = pygame.image.load("assets/bg-grass.png")
    
    RUNNING = True 
    while RUNNING:
        
        SCREEN.blit(background,(0,0))  #Draw the grass background image onto the screen     
        
        player.move(SCREEN)
        
        player.update(SCREEN)
        pygame.display.update()#Update the screen (move to the next frame)
        
        clock.tick(FRAMERATE)
        
        for event in pygame.event.get(): #If the x button is pressed, close the game
            if event.type == pygame.QUIT:
                RUNNING = False
    pygame.quit()
