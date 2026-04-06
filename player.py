"""
This module defines the player, its sprites and its mechanics.

Since this is the first module I (Aseda) wrote, there will be alot of comments explaining some lines and the general idea of how it works
My understanding of pygame is that it uses surfaces to represent objects in a game, and those surfaces can be drawn to a screen

Now rectangles (pygame.rect) are especially useful for handling collisions, moving, activations etc. which makes them suitable for controlling
But when you play a game, you see the character, not the rectangle.
So how I have designed the player is that, you control a rectangle that you cannot see, but on top of the rectangle, you see the character images playing

"""
import pygame

class Player:
    ###self.STATES = {IDLE,MOVING,DEAD}
    ###self.x_pos, self.y_pos : int; The position of the player
    ###self.velocity : int; The speed of the player
    ###self.animation : dict(); The animations to be used by the player
    ###self.animation_frame : float; Stores the current frame in the animation
    ###self.direction : bool; Stores the direction the player is facing. False for right, True for left
    ###self.image : pygame.image; The current image/frame of the player
    ###self.rect : pygame.rect; A rectangle which is actually being controlled by the player
    
    def __init__(self,x_pos,y_pos,character=1):
        ##STATES{ - A shoddy representation of an enum used to represent the player state
        self.IDLE = 1
        self.MOVING = 2
        self.HURT = 3
        ##}
        
        self.velocity = 5
        self.state = self.IDLE
        if character == 1:
            self.animation = {
            "idle":[pygame.image.load("assets/player/fox/idle/fox-idle-1.png"),
                    pygame.image.load("assets/player/fox/idle/fox-idle-2.png"),
                    pygame.image.load("assets/player/fox/idle/fox-idle-3.png"),
                    pygame.image.load("assets/player/fox/idle/fox-idle-1.png"),
                    pygame.image.load("assets/player/fox/idle/fox-idle-2.png"),
                    pygame.image.load("assets/player/fox/idle/fox-idle-3.png")]
            
            ,"run":[pygame.image.load("assets/player/fox/run/fox-run-1.png"),
                   pygame.image.load("assets/player/fox/run/fox-run-2.png"),
                   pygame.image.load("assets/player/fox/run/fox-run-3.png"),
                   pygame.image.load("assets/player/fox/run/fox-run-4.png"),
                   pygame.image.load("assets/player/fox/run/fox-run-5.png"),
                   pygame.image.load("assets/player/fox/run/fox-run-6.png")]
            
            ,"hurt":[pygame.image.load("assets/player/fox/hurt/fox-hurt-1.png"),
                     pygame.image.load("assets/player/fox/hurt/fox-hurt-2.png"),
                     pygame.image.load("assets/player/fox/hurt/fox-hurt-1.png"),
                     pygame.image.load("assets/player/fox/hurt/fox-hurt-2.png"),
                     pygame.image.load("assets/player/fox/hurt/fox-hurt-1.png"),
                     pygame.image.load("assets/player/fox/hurt/fox-hurt-2.png")
                    ]                      
            }
        elif character == 2:
            self.animation = {
            "idle":[pygame.image.load("assets/player/knight/idle/knight-idle-1.png"),
                    pygame.image.load("assets/player/knight/idle/knight-idle-2.png"),
                    pygame.image.load("assets/player/knight/idle/knight-idle-3.png"),
                    pygame.image.load("assets/player/knight/idle/knight-idle-1.png"),
                    pygame.image.load("assets/player/knight/idle/knight-idle-2.png"),
                    pygame.image.load("assets/player/knight/idle/knight-idle-3.png")]
            
            ,"run":[pygame.image.load("assets/player/knight/run/knight-run-1.png"),
                   pygame.image.load("assets/player/knight/run/knight-run-2.png"),
                   pygame.image.load("assets/player/knight/run/knight-run-3.png"),
                   pygame.image.load("assets/player/knight/run/knight-run-4.png"),
                   pygame.image.load("assets/player/knight/run/knight-run-5.png"),
                   pygame.image.load("assets/player/knight/run/knight-run-6.png")]
            
            ,"hurt":[pygame.image.load("assets/player/knight/hurt/knight-hurt-1.png"),
                     pygame.image.load("assets/player/knight/hurt/knight-hurt-2.png"),
                     pygame.image.load("assets/player/knight/hurt/knight-hurt-1.png"),
                     pygame.image.load("assets/player/knight/hurt/knight-hurt-2.png"),
                     pygame.image.load("assets/player/knight/hurt/knight-hurt-1.png"),
                     pygame.image.load("assets/player/knight/hurt/knight-hurt-2.png")
                    ]                      
            }

            
        self.animation_frame = 0
        self.direction = False
        
        self.image = pygame.image.load("assets/player/fox/idle/fox-idle-1.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image,2)
        self.rect = self.image.get_rect(center=(x_pos,y_pos))
        #Coin collider is what the coin collides with before collecting it
        self.coin_collider = (self.rect.copy()).scale_by(0.95)
        #cactus_collider is what the cactus collides with before determining if the game is over.
        self.cactus_collider = (self.rect.copy()).scale_by(0.8)
        
        
    
    def move(self,boundry):
        if self.state != self.HURT: #The player can move if the state is not hurt
            key = pygame.key.get_pressed() #Get the state of all buttons to see if they are pressed or not
        
            #Change the state of the player if they are moving
            if key[pygame.K_LEFT] or key[pygame.K_RIGHT] or key[pygame.K_UP] or key[pygame.K_DOWN]:
                self.state = self.MOVING
            else:
                self.state = self.IDLE
            
            #Change the direction the player is facing
            if key[pygame.K_LEFT]:
                self.direction = True
            elif key[pygame.K_RIGHT]:
                self.direction = False
        
            if key[pygame.K_LEFT]: self.rect.x -= self.velocity #If the left arrow key is pressed, shift the x position by -velocity
            if key[pygame.K_RIGHT]: self.rect.x += self.velocity
            if key[pygame.K_UP]: self.rect.y -= self.velocity
            if key[pygame.K_DOWN]: self.rect.y += self.velocity
        
            #Keep the player within the boundry with clamping
            self.rect.clamp_ip(boundry.get_rect())
        
    def animate(self,animation,framerate):
        ##Animation number update
        self.animation_frame += 1*(10/framerate)
        if self.animation_frame>len(animation)-1:  self.animation_frame = 0
        
        ##Show the current frame
        self.image = animation[int(self.animation_frame)].convert_alpha()
        self.image = pygame.transform.scale_by(self.image,2)
        if self.direction: self.image = pygame.transform.flip(self.image,True, False) #If the player is facing left, reflect the image along the x-direction

        
    def update(self,screen,framerate):
        #Animations to play
        if self.state == self.IDLE:
             self.animate(self.animation["idle"],framerate)
        elif self.state == self.MOVING:
             self.animate(self.animation["run"],framerate)
        elif self.state == self.HURT:
            self.animate(self.animation["hurt"],framerate)
            
        #Adjust colliders
        self.cactus_collider.center = self.rect.center
        self.coin_collider.center = self.rect.center
        
        #Draw player
        screen.blit(self.image,self.rect)
        
        
            
    
###TESTING###
if __name__ == "__main__":#Used for testing this part only before adding it to the main program
    
    pygame.init() #Initialize pygame
    
    SCREEN = pygame.display.set_mode((500,500)) #Create a new 500 x 500 px screen (window)
    pygame.display.set_caption("Player module") #Set the name of the screen
    
    FRAMERATE = 60 #Game runs at 60 fps
    clock = pygame.time.Clock()
    
    player = Player(100,100,2) #Create a player object
    
    RUNNING = True 
    while RUNNING:
        #We use a loop because without it, the screen will show for about a millisecond and then close
        
        SCREEN.fill("#222222")#Continuoulsy fill the background with black        
        
        player.move(SCREEN) #Move the player within the boundry of the screen

        pygame.draw.rect(SCREEN,"#ffffff",player.rect)
        pygame.draw.rect(SCREEN,"#00bb00",player.coin_collider)
        pygame.draw.rect(SCREEN,"#bb0000",player.cactus_collider)

        
        player.update(SCREEN,FRAMERATE)
        pygame.display.update()#Update the screen (move to the next frame)
        
        clock.tick(FRAMERATE)
        
        for event in pygame.event.get(): #If the x button is pressed, close the game
            if event.type == pygame.QUIT:
                RUNNING = False
    pygame.quit()
    
    
    