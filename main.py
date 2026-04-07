"""
This is the file to be opened if you want to play the game.
All the screens, score handling and others will be handled here.
"""
#Import game components
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
CHARACTER = 1
pygame.display.set_caption("Coin Dash!")

def save_score(new_score):
    """Read the scores from the file, add score, sort scores, store top 5 scores.
    If scores.txt is nonexistent, create a new one with template scores."""
    
    try:
        scores_file = open("scores.txt","r")
        
    except FileNotFoundError:
        #Create new file, store template scores there
        scores_file = open("scores.txt","w")
        scores = [(171,'ASD'),(152,'TNA'),(116,'JSM'),(58,'MCL'),(43,'KVN')]
        written_line = ""
        for this_score in scores:
            written_line += f"{this_score[0]},{this_score[1]}|"
            
        written_line = written_line[:-1]
        scores_file.write(written_line)
        scores_file = open("scores.txt","r")
    finally:
        scores = []
        read_line = scores_file.read().split('|')
        for this_group in read_line:
            group_info = this_group.split(',')
            scores.append(tuple([int(group_info[0]),group_info[1]]))
        scores.append((new_score,'YOU'))
        
        #Sort scores in descending order, then remove the lowest score
        scores.sort()
        scores = scores[::-1]
        scores = scores[:-1]
        
        #Write new scores to the file
        scores_file = open("scores.txt","w")
        written_line = ""
        for this_score in scores:
            written_line += f"{this_score[0]},{this_score[1]}|"
            
        written_line = written_line[:-1]
        scores_file.write(written_line)
        scores_file.close()
        


def settings():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK,CHARACTER
    title = pygame.font.Font("assets/Kenney Bold.ttf",42).render("Settings",True,"#ffffff")
    background_label = pygame.font.Font("assets/Kenney Bold.ttf",12).render("background",True,"#ffffff")
    character_label = pygame.font.Font("assets/Kenney Bold.ttf",12).render("character",True,"#ffffff")
    
    plains_btn = Button("assets/btn_background.png",(60,225),"plains","assets/Kenney Bold.ttf",font_size=15,scale=0.45)
    dungeon_btn = Button("assets/btn_background.png",(250,225),"dungeon","assets/Kenney Bold.ttf",font_size=15,scale=0.45)

    fox_btn = Button("assets/player/fox/idle/fox-idle-1.png",(60,360),scale=4)
    knight_btn = Button("assets/player/knight/idle/knight-idle-1.png",(250,360),scale=4.2)

    back_btn = Button("assets/btn_background.png",(155,570),"back","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    
    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(title,(90,100))
        SCREEN.blit(background_label,(185,200))
        SCREEN.blit(character_label,(185,350))
        
        
        #Draw buttons on the screen
        plains_btn.draw(SCREEN)
        dungeon_btn.draw(SCREEN)
        fox_btn.draw(SCREEN)
        knight_btn.draw(SCREEN)
        back_btn.draw(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if plains_btn.is_pressed(): BACKGROUND = pygame.image.load("assets/bg-grass.png") #Change the background to grass
                elif dungeon_btn.is_pressed(): BACKGROUND = pygame.image.load("assets/bg-dungeon.png") #Change the background to stone
                
                #Beacause there is no indicator to see if a new character has been selected, when choosing a new character, go back to the previous screen immediately
                elif fox_btn.is_pressed():
                    CHARACTER = 1 #Select the fox
                    return
                elif knight_btn.is_pressed():
                    CHARACTER = 2 #Select the knight
                    return
                
                elif back_btn.is_pressed():return #Go back to the previous screen
                
        CLOCK.tick(FRAMERATE)
        pygame.display.update()
    
    
def scores():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK
    
    save_score(0) #Create the new file if the file is non-existent. This is a cheap way of achieving that... I'm tired.
    
    title = pygame.font.Font("assets/Kenney Bold.ttf",34).render("High Scores",True,"#ffffff")

    def get_scores():
        scores_file = open("scores.txt","r")
        result = []
        read_line = scores_file.read().split('|')
        for this_group in read_line:
            group_info = this_group.split(',')
            result.append(tuple([int(group_info[0]),group_info[1]]))
        scores_file.close()
        return result
        
    read_scores = get_scores()
    name_labels =  []# A list of Font.renders which stores all the names
    score_labels = []# A list of Font.renders which stores all corresponding scores
    
    for this_score in read_scores:
        name_labels.append(pygame.font.Font("assets/Kenney Bold.ttf",34).render(f"{this_score[1]}",True,"#ffffff"))
        score_labels.append(pygame.font.Font("assets/Kenney Bold.ttf",34).render(f"{this_score[0]}",True,"#ffffff"))        
        
    
    back_btn = Button("assets/btn_background.png",(155,570),"back","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    
    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(title,(60,100))
        
        for i in range(len(score_labels)):
            SCREEN.blit(name_labels[i],(100,200+(60*i)))
            SCREEN.blit(score_labels[i],(250,200+(60*i)))
        
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
                    final_result = play_game(SCREEN,FRAMERATE,CLOCK,CHARACTER,BACKGROUND)
                    save_score(final_result)
                    scores()
                elif scores_btn.is_pressed(): scores()
                elif settings_btn.is_pressed():settings()
                elif exit_btn.is_pressed():
                    RUNNING=False
                    pygame.quit()
                    exit()
        
        CLOCK.tick(FRAMERATE)        
        pygame.display.update()



main_menu()
