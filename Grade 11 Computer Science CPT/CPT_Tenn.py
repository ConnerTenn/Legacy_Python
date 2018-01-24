# CPT: Insert Game Title Here
# Authors : Conner & Aniekan
# Course: ICS-3U
# Date: 2016-06-01

import pygame
from math import *

# -------- Colors Palet/Constants --------
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GREY = (100,100,100)
PI = 3.14159265358979323
TAU = 2*PI
#Not Python 2.x Compatable: Change chr to uni_char
ESC=chr(pygame.K_ESCAPE); U_ARROW = chr(pygame.K_UP); D_ARROW = chr(pygame.K_DOWN); R_ARROW = chr(pygame.K_RIGHT); L_ARROW = chr(pygame.K_LEFT); SPACE = chr(pygame.K_SPACE)

# ============ Classes and Function ==============

def degToRad(deg):
  rad = deg / 360.0 * TAU
  return rad

def radTodeg(rad):
  deg = rad / TAU * 360.0
  return deg

class Player(pygame.sprite.Sprite):
    def __init__(self):
        #Python 2.x
        #super.(Player,self)__init__()
        #Python 3.x
        super().__init__()
        self.rotation = 0.0
        self.speed = 0.0
        self.pos = [0,0]
        self.weapon = "default"
        self.ammo = 0 
        self.maxAmmo = 0
        # Number of frames between each shot
        self.fireTimeout = 10
        
        self.image = pygame.Surface([10,10])
        self.image.blit(pygame.image.load("bullet.png").convert(), [0, 0])
        self.displayedImage = self.image # the image that is actually put on the screen
        self.rect = self.image.get_rect()

    #Tenn
    def move(self, rotation):
        self.pos[0]+=cos(rotation)*self.speed
        self.pos[1]+=sin(rotation)*self.speed
        
    # Aniekan 
    # @param: angle of rotation (radians)
    def rotate(self, rotation):
        self.rotation += rotation
        deg = radToDeg(rotation)
        self.displayImage = pygame.transform.rotate(self.image, self.rotation)
        
    #Tenn
    def shoot(self):
        newBullet = Bullet(self.pos[0], self.pos[1], self.rotation)
        return newBullet
      
      

class Drops:
    #Tenn
    def __init__(self):
        #Python 2.x
        #super.(Player,self)__init__()
        #Python 3.x
        super().__init__()
        
        self.image = pygame.Surface([10,10])
        self.image.blit(pygame.image.load("bullet.png").convert(), [0, 0])
        self.rect = self.image.get_rect()
        
      
# Aniekan     
class Bullet(pygame.sprite.Sprite):
    # @param: x, y (integers) position of the bullet
    # @param: width, height (integers) dimensions of the bullet
    
    # Aniekan
    def __init__(self,x,y,rotation):
        #Python 2.x
        #super.(Player,self)__init__()
        #Python 3.x
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # Drawing the visible image of the circle
        pygame.draw.ellipse(self.image, BLACK, [0,0,10,10])
        # Set top-left corner of bullet to passed in location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    
    
    
# Aniekan
class Walls(pygame.sprite.Sprite):
    # @param: x, y (integers) position of wall on the screen
    # @param: width, hieght (integers) dimensions of the wall
    # Aniekan
    def __init__(self, x, y, width, height):
        #Initializing the parent class
        #Python 2.x
        #super.(Player,self)__init__()
        #Python 3.x
        super().__init__()
        # 
        self.image = pygame.Surface(width,height) # Setting the size of the wall
        self.rect = self.image.get_rect()
        self.image.fill(GREY)
        # Make the top left corner the passed in location
        self.rect.x = x
        self.rect.y = y


# --------------- Main Class --------------

class Main:
    #Tenn
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1200, 600])
        pygame.display.set_caption("Game")
        pygame.mouse.set_visible(True)
        self.clock = pygame.time.Clock()

        #Fix is needed for python 2.x
        #Player1 w,s,a,d, t,y,SPACE
        #Player2 U,D,L,R, 5,6,0
        self.pressed = {"q":False, ESC:False, \
            "w":False, "s":False, "a":False, "d":False, "t":False, "y":False, SPACE:False, \
            U_ARROW:False, D_ARROW:False, L_ARROW:False, R_ARROW:False, "5":False, "6":False, "0":False}
        #self.pressed2 = []
        
        self.allSprites = pygame.sprite.Group()
        self.bulletSprites = pygame.sprite.Group()
        self.wallSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        
        self.player1 = Player()
        self.allSprites.add(self.player1)
        self.playerSprites.add(self.player1)
        self.player2 = Player()
        self.allSprites.add(self.player2)
        self.playerSprites.add(self.player2)
        
        self.play = True
    
    # Aniekan    
    def initLevel(self):
      newWall = Wall(0,0,10,)
      self.allSprites.add(newWall)
      self.wallSprites.add(newWall)
  
    #Tenn
    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            #Not Python 2.x Compatable: Change chr to uni_char
            if event.type == pygame.KEYDOWN:
                #self.pressed2.append(chr(event.key))
                self.pressed[chr(event.key)] = True
            if event.type == pygame.KEYUP:
                self.pressed[chr(event.key)] = False
                #self.pressed2.remove(chr(event.key))

    #Tenn
    def loop(self):
        while self.play:
            self.eventHandler()
            self.update()
            self.render()
            self.clock.tick(60)

    #Tenn
    def update(self):
        #if "q" in self.pressed2 or ESC in self.pressed2:
        if self.pressed["q"] or self.pressed[ESC]:
            self.play = False
        
        
        

    #Tenn & Aniekan
    def render(self):
        self.screen.fill([255,255,255])
        # == Draw Code ==
        self.wallSprites.draw()
        self.playerSprites.draw() #Unfin
        
        # == End Draw Code ==
        pygame.display.flip()

#Tenn
if __name__ == "__main__":
    main = Main()
    main.loop()
    pygame.quit()
    

