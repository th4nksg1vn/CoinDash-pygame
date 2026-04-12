"""
This module handles the core gameplay loop and logic.
The reason is that this file contains most of the mechanics such as spawning,
collision detection, scoring, and level progression, which can become quite long...

The main file is expected to handle setup tasks like initializing the screen,
frame rate, and window caption, while this module focuses purely on the game part.

It also manages global game state such as the player, score, timer,
and active sprites (coins and cactii), as well as transitions between levels
and the game over state.
"""
#Import all game components
from player import Player
from cactus import Cactus
from coin import Coin

#Import necessary modules
import pygame
import random

#GLOBALS
playing = True #If the player is still playing/game has not ended. This is NOT the same as RUNNING's function
time_of_death = 0

score, time, level = 0,0,0

#player has been made global for character selection purposes
player = None #Spawn the player at the center of the screen

cactii = pygame.sprite.Group() #All cactii will be stored in this group instead of an list
coins = pygame.sprite.Group() #All coins to be collected will be stored in this group instead of an list

def increase_score():
    global score
    score+=1

def set_time(framerate):
    global time
    time=time-(1/framerate)

def spawn_coin(screen):
    """First 3 coins spawn at level 1
    3+n//3 coins spawn every n levels
    (so level 1 will spawn 3 coins, level 3 will spawn 4, level 6 will sapwn 5...)

    """
    global coins,level,player
    
    screen_size = (screen.get_rect().right,screen.get_rect().bottom) #Get the size of the screen
    spawn_no = 3 + level//3 #Number of coins to spawn
    
    #The logic behind this loop is in the coin module.
    for i in range(spawn_no):
        spawn_x = random.randint(0,screen.get_width() - Coin(0,0).rect.right)
        spawn_y = random.randint(0,screen.get_height() - Coin(0,0).rect.bottom)
        
        #Spawn the coin somewhere else in the event it spawns on top of the player
        while (spawn_x in range(player.rect.left,player.rect.right)) or (spawn_y in range(player.rect.top,player.rect.bottom)):
            spawn_x = random.randint(0,screen.get_width() - Coin(0,0).rect.right)
            spawn_y = random.randint(0,screen.get_height() - Coin(0,0).rect.bottom)

        coins.add(Coin(spawn_x,spawn_y))

def spawn_cactus(screen):
    """First cactus spawns at level 5.
    n//5 cactii spawn every n levels
    (so level 10 will spawn 2 cactii, level 15 will spawn 3...)

    """
    global cactii,level,player
    
    screen_size = (screen.get_rect().right,screen.get_rect().bottom) #Get the size of the screen
    spawn_no = level//5 #Number of cactii to spawn
    
    
    #The logic behind this loop is in the cactus module.
    for i in range(spawn_no):
        spawn_x = random.randint(0,screen.get_width() - Cactus(0,0).rect.right)
        spawn_y = random.randint(0,screen.get_height() - Cactus(0,0).rect.bottom)
        
        #Spawn the cactus somewhere else in the event it spawns on top of the player or on top of a coin
        while ((spawn_x in range(player.rect.left,player.rect.right)) or (spawn_y in range(player.rect.top,player.rect.bottom))) or len(pygame.sprite.spritecollide(Cactus(spawn_x,spawn_y),coins,False))!=0:
            spawn_x = random.randint(0,screen.get_width() - Cactus(0,0).rect.right)
            spawn_y = random.randint(0,screen.get_height() - Cactus(0,0).rect.bottom)

        cactii.add(Cactus(spawn_x,spawn_y))

def new_level(screen):
    global level,time
    
    level_sound = pygame.mixer.Sound("assets/audio/Level.wav") #The sound to start the level
    level_sound.play() #Play the sound
    
    level+=1
    time+=5
    spawn_coin(screen)
    spawn_cactus(screen)
    
def check_collected():
    global coins, player
    
    pickup_sound = pygame.mixer.Sound("assets/audio/Coin.wav") #Sound to play when picking up a coin
    
    for this_coin in coins.sprites(): #For each coin in the sprite.Group
        if player.coin_collider.colliderect(this_coin.collider): #If the player.rect has collided with the coin.rect
            pickup_sound.play() #Play the coin pickup_sound
            increase_score() #Update the score
            this_coin.kill() #Remove this coin

def check_collided():
    global cactii, player, playing
    
    hit_sound = pygame.mixer.Sound("assets/audio/Hit.wav") #Sound to play when a cactus is touched
    
    for this_cactus in cactii.sprites(): #For each cactus in the sprite.Group
        if player.cactus_collider.colliderect(this_cactus.collider): #If the player has collided with the cactus
            hit_sound.play() #Play the hit sound.
            return True
    return False

def game_over():
    global player

    end_sound = pygame.mixer.Sound("assets/audio/EndSound.wav") #Sound to play when the game has ended
    end_sound.play() #Play the sound
    
    player.state = player.HURT #Set player state to hurt
    

def initialize(screen,character=1):
    global score,time,level,player, cactii, coins, playing
    
    #These globals must be reset in order to start the game again from main
    playing = True
    cactii.empty()
    coins.empty()

    screen_size=(screen.get_rect().right,screen.get_rect().bottom) #Get the size of the screen
    score = 0 #Set score
    time = 5 #Set time to 10s, new level adds 5s
    level = 0 #Set level to 0
    player=Player(int(screen_size[0]/2),int(screen_size[1]/2),character)
    new_level(screen) #Call new_level to spawn the appropriate number of cactii and coins
    

def play_game(screen,framerate,clock,character=1,bg=None):
    global playing, time_of_death, score, time, level, player, cactii, coins
    
    initialize(screen,character)
    
    if bg is None:
        background = pygame.image.load("assets/bg-grass.png")
    else:
        background = bg
    
    ui_font = pygame.font.Font('assets/Kenney Bold.ttf',24) #Font for all UI elements
    
    RUNNING = True 
    while RUNNING:

        screen.blit(background,(0,0))  #Draw the grass background image onto the screen     

        
        coins.draw(screen)
        cactii.draw(screen) #Draw all cactii on the screen

        player.move(screen)
        
        if playing: #If the game is still playing
            check_collected()
            
            set_time(framerate) #decrease the time
            
            if len(coins.sprites()) == 0: #If all the coins have been collected
                cactii.empty() #Remove all the cactii in this level (new ones will be drawn in the next level)
                new_level(screen) #Go to the next level
            
            if check_collided() or time<0: #If the player has hit a cactus or time has run out...
                playing = False
                game_over() #End the game
                time_of_death = pygame.time.get_ticks() #Get the exact time the player died
                    
        else:#The game has ended
            if pygame.time.get_ticks()- time_of_death >= 3000: #If 3s have elapsed since time of death
                RUNNING = False #Since this is done in the game.py module, we will just close the game. In the main file, we will need to switch screens and save scores
            
        
        player.update(screen,framerate)        
        coins.update()
        
        if time<=0: #Show "Time up!" when the timer has ended
            time_text = ui_font.render(f'Time Up!',True,"#e3242b")
        elif time<1:#make the timer red and decimal when less than 1 second is remaining
            time_text = ui_font.render(f'{round(time,1)}s',True,"#e3242b")
        else:#Else keep it white
            time_text = ui_font.render(f'{ int(time)}s',True,"#ffffff")
            
        score_text = ui_font.render(f'{score}pts',True,"#ffffff")
        
        screen.blit(time_text,(10,10))  #Display the time on the screen
        screen.blit(score_text,(10,50))  #Display the score on the screen

        pygame.display.update()#Update the screen (move to the next frame)

        clock.tick(framerate)
        
        for event in pygame.event.get(): #If the x button is pressed, close the game
            if event.type == pygame.QUIT:
                RUNNING = False
    return score


if __name__ == "__main__":
    import pygame
    
    pygame.init()
    
    SCREEN = pygame.display.set_mode((480,720))
    pygame.display.set_caption("Game module")
    
    FRAMERATE = 60
    CLOCK = pygame.time.Clock()
    
    final_result = play_game(SCREEN,FRAMERATE,CLOCK,1)
    print(f"Game Over!\nFinal Level: {level}\nFinal Score: {final_result}pts")
    pygame.quit()
