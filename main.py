"""
This is the file to be opened if you want to play the game.
All the screens, score handling and others will be handled here.
"""
#Import all game components
from game import play_game
from button import Button

#Import necessary modules
import pygame

pygame.init()

#GLOBALS
SCREEN = pygame.display.set_mode((480,720))
FRAMERATE = 60
BACKGROUND = pygame.image.load("assets/bg-grass.png")
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Coin Dash!")


def settings():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK
    title = pygame.font.Font("assets/Kenney Bold.ttf",42).render("Settings",True,"#ffffff")
    back_btn = Button("assets/btn_background.png",(155,570),"back","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    
    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(title,(90,100))
        
        
        #Draw buttons on the screen
        back_btn.draw(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.is_pressed():return #Go back to the previous screen
        CLOCK.tick(FRAMERATE)
        pygame.display.update()
    
    
def scores():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK
    back_btn = Button("assets/btn_background.png",(155,570),"back","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    
    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(BACKGROUND,(0,0))
        
        #Draw buttons on the screen
        back_btn.draw(SCREEN)
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.is_pressed():return #Go back to the previous screen
        CLOCK.tick(FRAMERATE)
        pygame.display.update()    
        
def main_menu():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK
    title = pygame.font.Font("assets/Kenney Bold.ttf",42).render("COIN DASH!",True,"#ffffff")
    
    start_btn = Button("assets/btn_background.png",(130,250),"Start","assets/Kenney Bold.ttf",font_size=28,scale=0.65)
    scores_btn = Button("assets/btn_background.png",(155,370),"Scores","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    settings_btn = Button("assets/btn_background.png",(155,470),"settings","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    exit_btn = Button("assets/btn_background.png",(155,570),"exit","assets/Kenney Bold.ttf",font_size=20,scale=0.50)

    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(title,(70,125))
        
        #Draw buttons on the screen
        start_btn.draw(SCREEN)
        scores_btn.draw(SCREEN)
        settings_btn.draw(SCREEN)
        exit_btn.draw(SCREEN)
        
   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.is_pressed():
                    results = play_game(SCREEN,FRAMERATE,CLOCK,bg=BACKGROUND)
                    
                elif scores_btn.is_pressed(): scores()
                elif settings_btn.is_pressed():settings()
                elif exit_btn.is_pressed():
                    RUNNING=False
                    pygame.quit()
                    exit()
        
        CLOCK.tick(FRAMERATE)        
        pygame.display.update()

    
main_menu()
    