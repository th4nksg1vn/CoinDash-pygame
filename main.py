# 
#   ____ ___ ___ _   _   ____    _    ____  _   _ _ 
#  / ___/ _ \_ _| \ | | |  _ \  / \  / ___|| | | | |
# | |  | | | | ||  \| | | | | |/ _ \ \___ \| |_| | |
# | |__| |_| | || |\  | | |_| / ___ \ ___) |  _  |_|
#  \____\___/___|_| \_| |____/_/   \_\____/|_| |_(_)
# 
# 
# This module serves as the main entry point of the game.
# The reason is that this file manages all menus, screens, and overall flow,
# which can involve handling multiple screens such as gameplay, customization,
# score display, and tutorials...
# 
# It is responsible for initializing the window, handling user input across
# different screens, and coordinating transitions between them.
# 
# It also manages score saving/loading, character and background selection.
# 

#Import game components
from game import play_game
from button import Button

#Import necessary modules
import pygame

pygame.init()

#GLOBALS
SCREEN = pygame.display.set_mode((480,720))
FRAMERATE = 60 #The game runs optimally at 60fps, any less will cause it to lag, any more would make it very fast.
BACKGROUND = pygame.image.load("assets/bg-grass.png")
CLOCK = pygame.time.Clock()
CHARACTER = 1
pygame.display.set_caption("Coin Dash!")

def save_score(new_score):
    """Read the scores from the file, add score, sort scores, store top 5 scores.
    If scores.txt is nonexistent, create a new one with template scores."""
    
    try:#Try to open the file if it exists
        scores_file = open("scores.txt","r")
        
    except FileNotFoundError: #If not create a new file from the template
        #Create new file, store template scores there
        scores_file = open("scores.txt","w")
        scores = [(555,'ASD'),(350,'TNA'),(225,'JSM'),(130,'MCL'),(50,'KVN')]
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
        


def customize():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK,CHARACTER
    title = pygame.font.Font("assets/Kenney Bold.ttf",42).render("Customize",True,"#ffffff")
    background_label = pygame.font.Font("assets/Kenney Bold.ttf",12).render("background",True,"#ffffff")
    character_label = pygame.font.Font("assets/Kenney Bold.ttf",12).render("character",True,"#ffffff")
    
    plains_btn = Button("assets/UI/btn_blue.png",(60,225),"plains","assets/Kenney Bold.ttf",font_size=15,scale=0.45)
    dungeon_btn = Button("assets/UI/btn_blue.png",(250,225),"dungeon","assets/Kenney Bold.ttf",font_size=15,scale=0.45)

    fox_btn = Button("assets/UI/fox_select.png",(60,360))
    knight_btn = Button("assets/UI/knight_select.png",(250,360))

    highlight = pygame.font.Font("assets/Kenney Bold.ttf",12).render("selected",True,"#ffffff")
    
    back_btn = Button("assets/UI/btn_red.png",(155,570),"back","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    
    
    
    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(title,(70,100))
        SCREEN.blit(background_label,(185,200))
        SCREEN.blit(character_label,(185,345))
        if CHARACTER==1:
            SCREEN.blit(highlight,(75,500))
        elif CHARACTER==2:
            SCREEN.blit(highlight,(270,500))
        
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
                return
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if plains_btn.is_pressed(): BACKGROUND = pygame.image.load("assets/bg-grass.png") #Change the background to grass
                elif dungeon_btn.is_pressed(): BACKGROUND = pygame.image.load("assets/bg-dungeon.png") #Change the background to stone

                elif fox_btn.is_pressed():
                    CHARACTER = 1 #Select the fox
                elif knight_btn.is_pressed():
                    CHARACTER = 2 #Select the knight
                
                elif back_btn.is_pressed():return #Go back to the previous screen
                
        CLOCK.tick(FRAMERATE)
        pygame.display.update()
    
    
def scores():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK
    
    save_score(0) #Create the new file if the 'scores' file is non-existent. This is a cheap way of achieving that...
    
    title = pygame.font.Font("assets/Kenney Bold.ttf",34).render("High Scores",True,"#ffffff")

    def get_scores():
        """Get the scores from scores.txt"""
        
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
        if this_score[1] == "YOU": #Make the name and score blue if it's the player's score
            name_labels.append(pygame.font.Font("assets/Kenney Bold.ttf",34).render(f"{this_score[1]}",True,"#89CFF0"))
            score_labels.append(pygame.font.Font("assets/Kenney Bold.ttf",34).render(f"{this_score[0]}",True,"#89CFF0"))
        else:
            name_labels.append(pygame.font.Font("assets/Kenney Bold.ttf",34).render(f"{this_score[1]}",True,"#ffffff"))
            score_labels.append(pygame.font.Font("assets/Kenney Bold.ttf",34).render(f"{this_score[0]}",True,"#ffffff"))        
        
    
    back_btn = Button("assets/UI/btn_red.png",(155,570),"back","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    
    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(title,(70,100))
        
        for i in range(len(score_labels)):
            SCREEN.blit(name_labels[i],(110,200+(60*i)))
            SCREEN.blit(score_labels[i],(260,200+(60*i)))
        
        #Draw buttons on the screen
        back_btn.draw(SCREEN)
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                return
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.is_pressed():return #Go back to the previous screen
                
        CLOCK.tick(FRAMERATE)
        pygame.display.update()
        
def how_to_play():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK
    
    back_btn = Button("assets/UI/btn_red.png",(155,575),"back","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    
    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(pygame.image.load("assets/UI/tutorial.png"),(0,0))
        
        #Draw buttons on the screen
        back_btn.draw(SCREEN)
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                return
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.is_pressed():return #Go back to the previous screen
                
        CLOCK.tick(FRAMERATE)
        pygame.display.update()
        
def main_menu():
    global SCREEN,FRAMERATE,BACKGROUND,CLOCK
    title = pygame.font.Font("assets/Kenney Bold.ttf",42).render("COIN DASH!",True,"#ffffff")
    
    start_btn = Button("assets/UI/btn_green.png",(130,250),"Play","assets/Kenney Bold.ttf",font_size=28,scale=0.65)
    scores_btn = Button("assets/UI/btn_red.png",(155,370),"Scores","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    customize_btn = Button("assets/UI/btn_red.png",(155,470),"customize","assets/Kenney Bold.ttf",font_size=16,scale=0.50)
    exit_btn = Button("assets/UI/btn_red.png",(155,570),"exit","assets/Kenney Bold.ttf",font_size=20,scale=0.50)
    how_to_play_btn = Button("assets/UI/btn_blue.png",(370,670),"How to play","assets/Kenney Bold.ttf",font_size=8,scale=0.3)

    RUNNING = True
    while RUNNING:
        #Draw backgrounds and text
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(title,(70,125))
        
        #Draw buttons on the screen
        start_btn.draw(SCREEN)
        scores_btn.draw(SCREEN)
        customize_btn.draw(SCREEN)
        exit_btn.draw(SCREEN)
        how_to_play_btn.draw(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
                return
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if start_btn.is_pressed(): #If play button is pressed...
                    final_result = play_game(SCREEN,FRAMERATE,CLOCK,CHARACTER,BACKGROUND) #Play the game and get the score
                    save_score(final_result) #Save it to the file
                    scores() #Go to the scores screen
                    
                elif scores_btn.is_pressed(): scores() #Go to the scores screen
                elif customize_btn.is_pressed():customize() #Go to the customize screen
                elif how_to_play_btn.is_pressed():how_to_play() #Go to the scores screen
                elif exit_btn.is_pressed():
                    RUNNING=False
                    pygame.quit()
                    return
        
        CLOCK.tick(FRAMERATE)        
        pygame.display.update()



main_menu() #Start from the main menu, if exit is pressed, it would end the function call by returning nothing
exit() #Close the program