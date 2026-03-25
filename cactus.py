"""
This module defines each cactus the game
"""
import pygame
class Cactus(pygame.sprite.Sprite):
    #cactus is a member of the pygame.sprite class because it will be needed to use the sprite.Group object
    
    def __init__(self, x_pos,y_pos):
        super().__init__() #Initilize the base class
        self.image = pygame.image.load("assets/cactus.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x_pos,y_pos))
        
        #collider is what the player collides with before determining if the game is over.
        #It is smaller than the image/rect to allow for leniency
        self.collider = (self.rect.copy()).scale_by(0.8) 
        
    def update(self,screen):
        #Draw cactus
        screen.blit(self.image,self.rect)
        
        
if __name__ == "__main__":
    import random
    pygame.init()
    
    SCREEN = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Cactus module")
    
    FRAMERATE = 60
    clock = pygame.time.Clock()
    
    #3 Cactii will be spawned on screen at random locations
    cactii = pygame.sprite.Group() #Create the sprite group
    for i in range(3):
        #If the cactus spawns at (500,500), it will not be visible, so we want it to spawn such that...
        #The maximum position is when the bottom right of the cactus is at the corner
        
        spawn_x = random.randint(0,452) #500-48, where 48 is the width of the image
        spawn_y = random.randint(0,439) #500-61, where 61 is the height of the image
        
        cactii.add(Cactus(spawn_x,spawn_y))
    
    RUNNING = True 
    while RUNNING:
        
        SCREEN.fill("#333333") 
        
        #Draw the boundry and collision boxes for each cactus
        for cact in cactii:
            pygame.draw.rect(SCREEN,"#ffffff",cact.rect)
            pygame.draw.rect(SCREEN,"#bb0000",cact.cactus_collider)
        
        cactii.draw(SCREEN)
        
        pygame.display.update()#Update the screen (move to the next frame)
        
        clock.tick(FRAMERATE)
        
        for event in pygame.event.get(): #If the x button is pressed, close the game
            if event.type == pygame.QUIT:
                RUNNING = False
    pygame.quit()
