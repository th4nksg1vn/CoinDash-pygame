"""
This module handles the playing of the game.
The reason is that this code is planned to be especially long...
so the main game would probably be stored in a file called "main" or something like that

I plan to set up the screen, frame rate, and caption in the main file
"""
#Import all game components
from player import Player
from cactus import Cactus
from coin import Coin

#Import necessary modules
from pygame import sprite
import random

#GLOBALS
playing = True #If the player is still playing/game has not ended. This is NOT the same as RUNNING's function
time_of_death = 0

score, time, level = 0,0,0
player = None #Will be set in initialize

cactii = sprite.Group() #All cactii will be stored in this group instead of an list
coins = sprite.Group() #All coins to be collected will be stored in this group instead of an list

def spawn_coin(screen):
    """First 2 coins spawn at level 1
    n+1 coins spawn every n levels
    (so level 2 will spawn 3 coins, level 3 will spawn 4...)

    """
    global coins,level,player
    
    screen_size = (screen.get_rect().right,screen.get_rect().bottom) #Get the size of the screen
    spawn_no = 1+level #Number of coins to spawn
    
    #The logic behind this loop is in the coin module. We might have to change the values later to variables
    for i in range(spawn_no):
        spawn_x = random.randint(0,452)
        spawn_y = random.randint(0,439)
        
        #Spawn the coin somewhere else in the event it spawns on top of the player
        while (spawn_x in range(player.rect.left,player.rect.right)) or (spawn_y in range(player.rect.top,player.rect.bottom)):
            print("Coin on player!")
            spawn_x = random.randint(0,452)
            spawn_y = random.randint(0,439)

        coins.add(Coin(spawn_x,spawn_y))

def spawn_cactus(screen):
    """First cactus spawns at level 5.
    n//5 cactii spawn every n levels
    (so level 10 will spawn 2 cactii, level 15 will spawn 3...)

    """
    global cactii,level,player
    
    screen_size = (screen.get_rect().right,screen.get_rect().bottom) #Get the size of the screen
    spawn_no = level//5 #Number of cactii to spawn
    
    #The logic behind this loop is in the cactus module. I might have to change the values later to variables
    for i in range(spawn_no):
        spawn_x = random.randint(0,452)
        spawn_y = random.randint(0,439)
        
        #Spawn the cactus somewhere else in the event it spawns on top of the player (TODO: DO NOT SPAWN ON COIN)
        while (spawn_x in range(player.rect.left,player.rect.right)) or (spawn_y in range(player.rect.top,player.rect.bottom)):
            print("On Player!")
            spawn_x = random.randint(0,452)
            spawn_y = random.randint(0,439)

        print("Not on Player anymore!")
        cactii.add(Cactus(spawn_x,spawn_y))

def new_level(screen):
    global level
    
    level_sound = pygame.mixer.Sound("assets/audio/Level.wav") #Play the sound to start the game
    level_sound.play()
    
    level+=1
    spawn_coin(screen)
    spawn_cactus(screen)

def check_collected():
    global coins, player
    
    pickup_sound = pygame.mixer.Sound("assets/audio/Coin.wav") #Sound to play when picking up a coin
    
    for this_coin in coins.sprites(): #For each coin in the sprite.Group
        if player.rect.colliderect(this_coin.collider): #If the player.rect has collided with the coin.rect
            pickup_sound.play() #Play the coin_pickup sound
            #increase_score() #Update the score
            this_coin.kill() #Remove this coin

def check_collided():
    global cactii, player, playing
    
    hit_sound = pygame.mixer.Sound("assets/audio/EndSound.wav") #Sound to play when a cactus is touched
    
    for this_cactus in cactii.sprites(): #For each cactus in the sprite.Group
        if player.cactus_collider.colliderect(this_cactus.collider): #If the player has collided with the cactus
            hit_sound.play()
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
    
    

if __name__ == "__main__":
    import pygame
    
    pygame.init()
    
    SCREEN = pygame.display.set_mode((480,720))
    pygame.display.set_caption("Game module")
    
    FRAMERATE = 60
    clock = pygame.time.Clock()
    
    initialize(SCREEN)

    #For testing - set level to n and spawn n//5 cactii
    #level = 2
    #new_level(SCREEN)
    #----------------------
    
    background = pygame.image.load("assets/bg-grass.png")
    
    RUNNING = True 
    while RUNNING:
        
        SCREEN.blit(background,(0,0))  #Draw the grass background image onto the screen     


        coins.draw(SCREEN)
        cactii.draw(SCREEN) #Draw all cactii on the screen

        player.move(SCREEN)
        
        if playing: #If the game is still playing
            check_collected()
            if len(coins.sprites()) == 0: #If all the coins have been collected
                cactii.empty() #Remove all the cactii in this level (new ones will be drawn in the next level)
                new_level(SCREEN) #Go to the next level
            
            if check_collided(): #If the player has hit a cactus...
                time_of_death = pygame.time.get_ticks() #Get the exact time the player died
                    
        else:#The game has ended
            if pygame.time.get_ticks()- time_of_death >= 3000: #If 3s have elapsed since time of death
                RUNNING = False #Since this is done in the game.py module, we will just close the game. In the main file, we will need to switch screens and save scores
            
        
        player.update(SCREEN)        
        coins.update()
        pygame.display.update()#Update the screen (move to the next frame)
        
        clock.tick(FRAMERATE)
        
        for event in pygame.event.get(): #If the x button is pressed, close the game
            if event.type == pygame.QUIT:
                RUNNING = False
    pygame.quit()
