"""
This module defines each coin in the game
"""
import pygame

class Coin(pygame.sprite.Sprite):
    # Coin is a sprite so it can be used in sprite groups and collisions
    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.image = pygame.image.load("assets/coin/coin-frame-1.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image,0.4)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

        # Smaller collider for fair collision
        self.collider = (self.rect.copy()).scale_by(0.8)
        
        
        self.animation = [pygame.image.load("assets/coin/coin-frame-1.png"),
                          pygame.image.load("assets/coin/coin-frame-2.png"),
                          pygame.image.load("assets/coin/coin-frame-3.png"),
                          pygame.image.load("assets/coin/coin-frame-4.png"),
                          pygame.image.load("assets/coin/coin-frame-5.png"),
                          pygame.image.load("assets/coin/coin-frame-6.png"),
                          pygame.image.load("assets/coin/coin-frame-7.png"),
                          pygame.image.load("assets/coin/coin-frame-8.png"),
                          pygame.image.load("assets/coin/coin-frame-9.png"),
                          pygame.image.load("assets/coin/coin-frame-10.png"),
                          pygame.image.load("assets/coin/coin-frame-11.png"),]
                           
        self.animation_frame = 0
        
    def animate(self, framerate):
        #Animation number update
        self.animation_frame += 1*(10/framerate)
        if self.animation_frame > len(self.animation)-1:
            self.animation_frame = 0
            
        #Show the current frame
        self.image = self.animation[int(self.animation_frame)].convert_alpha()
        self.image = pygame.transform.scale_by(self.image,0.4)
        

    def update(self):
        # Keep collider aligned with rect
        self.animate(60)
        self.collider.center = self.rect.center
        
    
if __name__ == "__main__":
    import random
    pygame.init()
    
    SCREEN = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Cactus module")
    
    FRAMERATE = 60
    clock = pygame.time.Clock()
    
    #3 Cactii will be spawned on screen at random locations
    coins = pygame.sprite.Group() #Create the sprite group
    for i in range(3):
        #If the coin spawns at (500,500), it will not be visible, so we want it to spawn such that...
        #The maximum position is when the bottom right of the coin is at the corner
        
        spawn_x = random.randint(0,452) #500-48, where 48 is the width of the image
        spawn_y = random.randint(0,439) #500-61, where 61 is the height of the image
        
        coins.add(Coin(spawn_x,spawn_y))
    
    RUNNING = True 
    while RUNNING:
        
        SCREEN.fill("#333333") 
        
        #Draw the boundry and collision boxes for each cactus
        for coin in coins:
            pygame.draw.rect(SCREEN,"#ffffff",coin.rect)
            pygame.draw.rect(SCREEN,"#bb0000",coin.collider)
            coin.update()
        
        coins.draw(SCREEN)
        
        pygame.display.update()#Update the screen (move to the next frame)
        
        clock.tick(FRAMERATE)
        
        for event in pygame.event.get(): #If the x button is pressed, close the game
            if event.type == pygame.QUIT:
                RUNNING = False
    pygame.quit()

