"""
This module handles the playing of the game.
The reason is that this code is planned to be especially long...
so the main game would probably be stored in a file called "main" or something like that

I plan to set up the screen, frame rate, and caption in the main file
"""
#Import all game components
from player import Player
from cactus import Cactus

#Import necessary modules
from pygame import sprite
import random

#GLOBALS
playing = True #If the player is still playing/game has not ended. This is NOT the same as RUNNING's function
time_of_death = 0

score, time, level = 0,0,0
player = None #Will be set in initialize

coins = ...
cactii = sprite.Group() #All coins to be collected will be stored in this group instead of an list

def spawn_coin():
    #Spawn coins in the game
    pass


def spawn_cactus(level,screen):
    """First cactus spawns at level 5.
    n//5 cactii spawn every n levels
    (so level 10 will spawn 2 cactii, level 15 will spawn 3...)

    """
    global cactii,player
    
    screen_size= (screen.get_rect().right,screen.get_rect().bottom) #Get the size of the screen
    spawn_no = level//5 #Number of cactii to spawn
    
    #The logic behind this loop is in the cactus module. I might have to change the values later to variables
    for i in range(spawn_no):
        spawn_x = random.randint(0,452)
        spawn_y = random.randint(0,439)
        
        #Spawn the cactus somewhere else in the event it spawns on top of the player
        while (spawn_x in range(player.rect.left,player.rect.right)) or (spawn_y in range(player.rect.top,player.rect.bottom)):
            print("On Player!")
            spawn_x = random.randint(0,452)
            spawn_y = random.randint(0,439)

        print("Not on Player anymore!")
        cactii.add(Cactus(spawn_x,spawn_y))

def new_level(screen):
    global level
    
    level+=1
    #spawn_coin(level,screen)
    spawn_cactus(level,screen)

def check_collided():
    global cactii, player, playing
    for this_cactus in cactii.sprites(): #For each cactus in the sprite.Group
        if player.cactus_collider.colliderect(this_cactus.collider): #If the player has collided with the cactus
            playing = False
            game_over() #End the game
            return True
    return False

def game_over():
    global player

    end_sound = pygame.mixer.Sound("assets/audio/EndSound.wav")
    end_sound.play()
    
    player.state = player.HURT #Set player state to hurt

    #Delete the player
    

def initialize(screen):
    global score,time,level,player
    
    screen_size=(screen.get_rect().right,screen.get_rect().bottom) #Get the size of the screen
    score = 0 #Set score
    time = 10 #Set time to 10s
    level = 0 #Set level to 0
    player = Player(int(screen_size[0]/2),int(screen_size[1]/2)) #Spawn the player at the center of the screen
    new_level(screen) #Call new_level to spawn the appropriate number of cactii and coins
    
    
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

    #For testing - set level to n and spawn n//5 cactii
    level = 14
    new_level(SCREEN)
    #----------------------
    
    background = pygame.image.load("assets/bg-grass.png")
    
    RUNNING = True 
    while RUNNING:
        
        SCREEN.blit(background,(0,0))  #Draw the grass background image onto the screen     
        cactii.draw(SCREEN) #Draw all cactii on the screen
        
        player.move(SCREEN)
        
        if playing: #If the game is still playing
            if check_collided(): #If the player has hit a cactus...
                time_of_death = pygame.time.get_ticks() #Get the exact time the player died
                    
        else:#The game has ended
            if pygame.time.get_ticks()- time_of_death >= 3000: #If 3s have elapsed since time of death
                RUNNING = False #Since this is done in the game.py module, we will just close the game. In the main file, we will need to switch screens and save scores
            
        
        player.update(SCREEN)
        pygame.display.update()#Update the screen (move to the next frame)
        
        clock.tick(FRAMERATE)
        
        for event in pygame.event.get(): #If the x button is pressed, close the game
            if event.type == pygame.QUIT:
                RUNNING = False
    pygame.quit()
