#CPT: Insert Game Title Here
# Authors : Conner & Aniekan
# Course: ICS-3U
# Date: Jan 01 2016

#sudo apt-get install python-pygame
#sudo apt-get install idle

#Imports
import pygame
from math import *
from random import *

# -------- Colors Palet/Constants --------
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GREY = (100,100,100)
CYAN = (0,255,255)
PI = 3.14159265358979323
TAU = 2 * PI

#Not Python 2.x Compatable: Change chr to uni_char
ESC = chr(pygame.K_ESCAPE); U_ARROW = chr(pygame.K_UP); D_ARROW = chr(pygame.K_DOWN); R_ARROW = chr(pygame.K_RIGHT); L_ARROW = chr(pygame.K_LEFT); SPACE = chr(pygame.K_SPACE)
NUM0 = chr(pygame.K_KP0);NUM1 = chr(pygame.K_KP1);NUM2 = chr(pygame.K_KP2);NUM3 = chr(pygame.K_KP3);NUM4 = chr(pygame.K_KP4);NUM5 = chr(pygame.K_KP5);NUM6 = chr(pygame.K_KP6);NUM7 = chr(pygame.K_KP7);NUM8 = chr(pygame.K_KP8);NUM9 = chr(pygame.K_KP9);

# Teleportation Parameters [up,right,down,left]
portalParam = [(570,0,70,10,[580,30]),(1190,270,10,70,[1130,285]),(570,590,70,10,[580,530]),(0,270,10,70,[30,285])]
#portals = [[(570,610),0],[1200,(270,310)],[(570,610),50],[0,(270,310)]]

# ============ Classes and Function ==============

#Aniekan
# @param - sprite1, sprite2 (bullet,wall)
# Returns an angle (radians) which corresponds to the side you collided with
def detectSide(static, dynamic):
    collisions = []
    dataBase = {"RL":0.0*TAU,"TB":1.0/4.0*TAU,"LR":1.0/2.0*TAU,"BT":3.0/4.0*TAU}
    
    topBottom = (abs(static.rect.top - dynamic.rect.bottom),"TB")
    collisions.append(topBottom)
    bottomTop = (abs(static.rect.bottom - dynamic.rect.top),"BT")
    collisions.append(bottomTop)
    leftRight = (abs(static.rect.left - dynamic.rect.right),"LR")
    collisions.append(leftRight)
    rightLeft = (abs(static.rect.right - dynamic.rect.left),"RL")
    collisions.append(rightLeft)
    minimum = min(collisions)
    return dataBase[minimum[1]]
  
#https://pygame.org/wiki/RotateCenter?parent
# @Param - image: image to rotate
# @Param - angle: angle to rotate by
# @Return - rotated image
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

#Tenn
# @Param - deg:Degree
# @Return - Radian equivalent of Degree
def degToRad(deg):
  rad = deg / 360.0 * TAU
  return rad

#Tenn
# @Param - rad:Radian
# @Return - Degree equivalent of Radian
def radToDeg(rad):
  deg = rad / TAU * 360.0
  return deg

class Player(pygame.sprite.Sprite):
    #Tenn
    # @Param - pos: initial position
    # @Param - rotation: initial facing direction
    # @Param - color: colour of player
    def __init__(self, pos, rotation, color):
        #Python 2.x
        super(Player, self).__init__()
        #Python 3.x
        #super().__init__()
        
        #Init movement data
        self.rotation = rotation #initially facing right
        self.speed = 0.0
        self.pos = [pos[0], pos[1]]
        
        #sinit weapon data
        self.ammo = 0 
        #self.maxAmmo = 0
        # Number of frames between each shot
        self.fireTimeout = 0
        self.maxFireTimeout = 20
        self.bulletSize = 10
        self.ricochet = 0
        self.dieCollideBullet = True
        self.dieCollideWall = True
        
        #init image data
        self.image = pygame.Surface([30,30])
        self.originalImage = pygame.Surface([30,30])
        self.originalImage.fill(WHITE)
        self.originalImage.set_colorkey(WHITE)
        pygame.draw.ellipse(self.originalImage,color,[0,0,30,30])
        pygame.draw.line(self.originalImage, GREEN, [15, 15], [30, 15], 3)
        self.image = self.originalImage.copy()
        
        #init rect data
        self.rect = self.originalImage.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    #Tenn & Aniekan
    # @Param - vect: vector direction to move
    # @Param - sprites: sprites to collide with
    def move(self, vect, sprites):#, portals):#rotation):
        #self.rect.x+=cos(rotation)*self.speed
        #self.rect.y+=sin(rotation)*self.speed
        self.pos[0]+=vect[0] * 2.0
        self.rect.x = self.pos[0]
        collisionList = pygame.sprite.spritecollide(self, sprites, False)
        for sprite in collisionList:
            if sprite is self or type(sprite) is Bullet: continue
            elif vect[0] > 0:
                self.rect.right = sprite.rect.left
            else:
                self.rect.left = sprite.rect.right
                
        self.pos[1]+=vect[1] * 2.0
        self.rect.y = self.pos[1]
        collisionList = pygame.sprite.spritecollide(self, sprites, False)
        for sprite in collisionList:
            if sprite is self or type(sprite) is Bullet : continue
            elif vect[1] > 0:
                self.rect.bottom = sprite.rect.top
            else:
                self.rect.top = sprite.rect.bottom
        '''
        # Teleportation Feature
        collisionList = pygame.sprite.spritecollide(self,portals,False)
        tempPortalList = portals.sprites()
        if len(collisionList) > 0:
            for sprite in collisionList:
                newPos = sprite.teleport(tempPortalList)
                self.rect.x = newPos[0]
                self.rect.y = newPos[1]
                
                # Top Portal
                if vect[1] < 0:
                    tempPortalList.remove(sprite)
                    index = randrange(0,3)
                    self.rect.x = tempPortalList[index].dest[0]
                    self.rect.y = tempPortalList[index].dest[1]
                # Right Portal
                elif vect[0] > 0:
                    tempPortalList.remove(sprite)
                    index = randrange(0,3)
                    self.rect.x = tempPortalList[index].dest[0]
                    self.rect.y = tempPortalList[index].dest[1]
                # Down Portal
                elif vect[1] > 0:
                    tempPortalList.remove(sprite)
                    index = randrange(0,3)
                    self.rect.x = tempPortalList[index].dest[0]
                    self.rect.y = tempPortalList[index].dest[1]
                # Right Portal
                elif vect[0] < 0:
                    tempPortalList.remove(sprite)
                    index = randrange(0,3)
                    self.rect.x = tempPortalList[index].dest[0]
                    self.rect.y = tempPortalList[index].dest[1]'''
                   
        self.pos[0] = self.rect.x
        self.pos[1] = self.rect.y      
        
    # Tenn 
    # @param: angle of rotation (radians)
    def rotate(self, rotation):
        #set the new rotation and rotate the sprite
        self.rotation += rotation
        deg = radToDeg(self.rotation)
        self.image = rot_center(self.originalImage, deg)
        #self.image = pygame.transform.rotate(self.image, deg)
        
    #Tenn
    def shoot(self):
        #test if shoot delay has elapsed
        if self.fireTimeout == 0:
            #create new bullet
            newBullet = Bullet([self.pos[0] + self.rect.width/2.0 - self.bulletSize/2, self.pos[1] + self.rect.height/2.0 - self.bulletSize/2], self.bulletSize,self.rotation, self.ricochet, self.dieCollideBullet, self.dieCollideWall, self)
            #reset shoot timmer
            self.fireTimeout = self.maxFireTimeout
            self.ammo -= 1
            return newBullet
        #no bullet
        return None
    
    #Tenn
    def update(self):
        #update the rect off of pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        
        #step the shoot timmer
        if self.fireTimeout > 0:
            self.fireTimeout -= 1
        
        #test if player runs out of ammo
        if self.ammo == 0:
            #reset default weapon params
            self.ammo = -1
            self.maxFireTimeout = 20
            self.fireTimeout = 0
            self.bulletSize = 10
            self.ricochet = 0
            self.dieCollideBullet = True
            self.dieCollideWall = True
        
        if self.ammo < -1:
            self.ammo = -1

class Drops(pygame.sprite.Sprite):
    #Tenn
    # @Param - pos: position of the drop
    # @Param - maxFireTimeout: shoot delay; fire rate
    # @Param - ammo: the ammo that the drop holds
    # @Param - bulletSize
    # @Param - 
    def __init__(self, pos, maxFireTimeout, ammo, bulletSize, ricochet, dieCollideBullet, dieCollideWall):
        #Python 2.x
        super(Drops,self).__init__()
        #Python 3.x
        #super().__init__()
        
        self.pos = [pos[0], pos[1]]
        self.maxFireTimeout = maxFireTimeout
        self.ammo = ammo
        self.bulletSize = bulletSize
        self.ricochet = ricochet
        self.dieCollideBullet = dieCollideBullet
        self.dieCollideWall = dieCollideWall
        
        self.image = pygame.Surface([20,20])
        #self.image.blit(pygame.image.load("bullet.png").convert(), [0, 0])
        pygame.draw.rect(self.image, BLACK, [0, 0, 20, 20])
        for i in range(4, 20, 8):
          pygame.draw.rect(self.image, GREY, [i, 4, 4, 16])
        self.rect = self.image.get_rect()
        
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        
    def checkCol(self,sprites):
        collisionList = pygame.sprite.spritecollide(self,sprites,False)
        if len(collisionList) == 0:
            return False
        else:
            return True
    
class Bullet(pygame.sprite.Sprite):
    # @param: x, y (integers) position of the bullet
    # @param: width, height (integers) dimensions of the bullet
    
    # Aniekan
    def __init__(self, pos, size, rotation, ricochet, dieCollideBullet, dieCollideWall, creator):
        #Python 2.x
        super(Bullet,self).__init__()
        #Python 3.x
        #super().__init__()
        
        self.creator = creator
        self.pos = [pos[0], pos[1]]
        self.rotation = rotation
        self.ricochet = ricochet
        self.dieCollideBullet = dieCollideBullet
        self.dieCollideWall = dieCollideWall
        
        self.image = pygame.Surface([size, size])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # Drawing the visible image of the circle
        pygame.draw.ellipse(self.image, BLACK, [0,0,size,size])
        # Set top-left corner of bullet to passed in location
        
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
    
    #Tenn
    def update(self):
        #print(" Rot" + str(self.rotation))
        self.pos[0] += cos(self.rotation) * 6.0
        self.pos[1] -= sin(self.rotation) * 6.0
        
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        
    # Tenn & Aniekan
    def ricochetBullet(self, wallSprites):
        # If the number of ricochets a bullet has is not zero and it collides with a wall then don't destroy it
        collisionList = pygame.sprite.spritecollide(self, wallSprites, False)
        if self.ricochet > 0 and len(collisionList) > 0:
            for wall in collisionList:
                self.rotation = TAU/2.0 + 2.0 * detectSide(wall, self) - self.rotation
                self.ricochet -= 1
            return True
        # If the number of ricochets is 0 and it collided with a wall then destroy the bullet
        elif len(collisionList) > 0 and self.dieCollideWall:
            return False
    
# Aniekan
class Walls(pygame.sprite.Sprite):
    # @param: x, y (integers) position of wall on the screen
    # @param: width, height (integers) dimensions of the wall
    # Aniekan
    def __init__(self, x, y, width, height):
        #Initializing the parent class
        #Python 2.x
        super(Walls,self).__init__()
        #Python 3.x
        #super().__init__()
        # 
        self.image = pygame.Surface((width,height)) # Setting the size of the wall
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        # Make the top left corner the passed in location
        self.rect.x = x
        self.rect.y = y
        
# Aniekan       
class Portal(pygame.sprite.Sprite):
    # @param: x, y (integers) position of wall on the screen
    # @param: width, height (integers) dimensions of the wall
    def __init__(self, x, y, width, height, dest):
        #Initializing the parent class
        #Python 2.x
        super(Portal,self).__init__()
        #Python 3.x  
        #super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dest = dest
    # @param: group of portals (sprite objects) which contain possible teleportation destinations
    # @param: group of non-portal sprites
    def teleport(self, portals, sprites):
        collisionList = pygame.sprite.spritecollide(self,sprites,False)
        tempPortalList = portals.sprites()
        tempPortalList.remove(self)
        for sprite in collisionList:
            index = randrange(0,3)
            newPos = [tempPortalList[index].dest[0],tempPortalList[index].dest[1]]
            sprite.pos[0] = newPos[0]
            sprite.pos[1] = newPos[1]
            sprite.rect.x = sprite.pos[0]
            sprite.rect.y = sprite.pos[1]
            
# --------------- Main Class --------------

class Main:
    #Tenn
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1200, 700])
        pygame.display.set_caption("Game")
        pygame.mouse.set_visible(True)
        self.clock = pygame.time.Clock()

        #Fix is needed for python 2.x
        #Player1 w,s,a,d, t,y,SPACE
        #Player2 U,D,L,R, 5,6,0
        self.pressed = {"q":False, ESC:False, \
            "w":False, "s":False, "a":False, "d":False, "t":False, "y":False, SPACE:False, \
            U_ARROW:False, D_ARROW:False, L_ARROW:False, R_ARROW:False, NUM5:False, NUM6:False, NUM0:False}
        #self.pressed2 = []
        
        pygame.mixer.init()
        pygame.mixer.music.load("Arcade_Bandit.mp3")
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        self.score = [0, 0]
        
        self.play = True
    
    # Aniekan    
    def initLevel(self):
        pygame.mixer.music.play()
        self.allSprites = pygame.sprite.Group()
        self.rigidBodySprites = pygame.sprite.Group()
        
        self.bulletSprites = pygame.sprite.Group()
        self.wallSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.dropSprites = pygame.sprite.Group()
        self.portalSprites = pygame.sprite.Group()
        
        self.player1 = Player([100.0-15.0, 300.0-15.0], 0.0, RED)#, p1_idle, p1_move, p1_shoot)
        self.allSprites.add(self.player1)
        self.playerSprites.add(self.player1)
        self.rigidBodySprites.add(self.player1)
        self.player2 = Player([1100.0-15.0, 300.0-15.0], TAU/2.0, BLUE)#, p2_idle, p2_move, p2_shoot)
        self.allSprites.add(self.player2)
        self.playerSprites.add(self.player2)
        self.rigidBodySprites.add(self.player2)
        
        # Creating Portal Objects
        for param in portalParam:
            newPortal = Portal(param[0],param[1],param[2],param[3],param[4])
            self.portalSprites.add(newPortal)
            self.allSprites.add(newPortal)
        Rooms = []
        # Storing parmaetrs for the creating of walls (initialising level)
        walls1 = [[0,0,10,260],[0,340,10,260],[10,0,550,10],[10,590,550,10],
                    [650,0,550,10],[1190,10,10,250],[1190,350,10,250],[650,590,540,10],
                    [0,260,100,10],[0,340,100,10],[90,90,10,100],[90,410,10,100],
                    [90,90,400,10],[90,500,400,10],[560,0,10,100],[640,0,10,100],
                    [560,500,10,100],[640,500,10,100],[1100,260,100,10],[1100,340,100,10],
                    [1100,90,10,100],[710,90,390,10],[1100,410,10,100],[710,500,390,10],
                    [490,210,220,10],[490,220,10,50],[700,220,10,50],[490,380,220,10],
                    [490,330,10,50],[700,330,10,50],[390,170,10,250],[800,170,10,250]]
        Rooms.append(walls1)
        for wall in walls1:
            newWall = Walls(wall[0],wall[1],wall[2],wall[3])
            self.allSprites.add(newWall)
            self.rigidBodySprites.add(newWall)
            self.wallSprites.add(newWall)
        
        #pos, maxFireTimeout, ammo, bulletSize, ricochet: lives, dieCollideBullet, dieCollideWall
        #Rapid
        #Hulk
        #Bounce
        bulletTypes =                                                                                                                                                                       \
                [                                                                                                                                                                           \
                    [[], sample(range(4,  10), 1)[0], sample(range(10, 30), 1)[0], sample(range( 5, 10), 1)[0], 0, True, sample([True, True, True, False], 1)[0]],                          \
                    [[], sample(range(120, 240), 1)[0], sample(range( 5, 12), 1)[0], sample(range(20, 40), 1)[0], 0, False, False],                                                           \
                    [[], sample(range(20, 30), 1)[0], sample(range(10, 20), 1)[0], sample(range(15, 20), 1)[0], sample(range(5, 25), 1)[0], sample([True, True, True, False], 1)[0], True]  \
                ]
        # There is a one in three chance of spawning a drops
        for i in range(3):
            param = bulletTypes[randrange(0,3)]
            newX = randrange(0,1200)
            newY = randrange(0,600)
            param[0] = (newX,newY)
            newDrop = Drops(param[0],param[1],param[2],param[3],param[4],param[5],param[6])
            while newDrop.checkCol(self.allSprites) == True:
                newX = randrange(0,1200)
                newY = randrange(0,600)
                param[0] = (newX,newY)
                newDrop = Drops(param[0],param[1],param[2],param[3],param[4],param[5],param[6])
            self.allSprites.add(newDrop)
            self.dropSprites.add(newDrop)
        '''    
        newDrop = Drops([210, 410], 20, 20, 20, 10, True, False)
        self.allSprites.add(newDrop)
        self.dropSprites.add(newDrop)
        
        newDrop = Drops([710, 410], 50, 10, 30, 0, False, False)
        self.allSprites.add(newDrop)
        self.dropSprites.add(newDrop)
        
        newDrop = Drops([110, 210], 20, 10, 10, 10, True, True)
        #newDrop = Drops([110, 210], 4, 100, 10, 40, True, True)
        self.allSprites.add(newDrop)
        self.dropSprites.add(newDrop)'''
  
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
            if event.type == pygame.constants.USEREVENT:
                #self.music = pygame.mixer.music.load("Arcade_Bandit.wav")
                # This event is triggered when the music stops playing
                pygame.mixer.music.play()

    #Tenn
    def loop(self):
        self.initLevel()
        while self.play:
            self.eventHandler()
            self.update()
            self.render()
            self.clock.tick(60)

    #Tenn
    def update(self):
        #if "q" in self.pressed2 or ESC in self.pressed2:
        #end the game if player pressed ESC
        if self.pressed[ESC]:
            self.play = False
        
        #Player1 Movements
        vect = [0,0]
        if self.pressed["w"]:
            vect[1] -= 1
        if self.pressed["s"]:
            vect[1] += 1
        if self.pressed["a"]:
            vect[0] -= 1
        if self.pressed["d"]:
            vect[0] += 1
        #move the player by vector and pass objects to collide with
        self.player1.move(vect, self.rigidBodySprites)#, self.portalSprites)
        
        rotation = 0.0
        if self.pressed["t"]:
            rotation += 1.0/100.0 * TAU
        if self.pressed["y"]:
            rotation -= 1.0/100.0 * TAU
        self.player1.rotate(rotation)
        
        #Player2 Movements
        vect = [0,0]
        if self.pressed[U_ARROW]:
            vect[1] -= 1
        if self.pressed[D_ARROW]:
            vect[1] += 1
        if self.pressed[L_ARROW]:
            vect[0] -= 1
        if self.pressed[R_ARROW]:
            vect[0] += 1
        self.player2.move(vect, self.rigidBodySprites)#, self.portalSprites)
        
        rotation = 0.0
        if self.pressed[NUM5]:
            rotation += 1.0/100.0 * TAU
        if self.pressed[NUM6]:
            rotation -= 1.0/100.0 * TAU
        self.player2.rotate(rotation)
        
        # ---------------- Bullet Handling ----------------
        if self.pressed[SPACE]:
            newBullet = self.player1.shoot()
            if newBullet != None:
                self.allSprites.add(newBullet)
                self.bulletSprites.add(newBullet)
                self.rigidBodySprites.add(newBullet)
        if self.pressed[NUM0]:
            newBullet = self.player2.shoot()
            if newBullet != None:
                self.allSprites.add(newBullet)
                self.bulletSprites.add(newBullet)
                self.rigidBodySprites.add(newBullet)
           
        for bullet in self.bulletSprites:
            bullet.update() # applies changes to the bullet
        '''
            # Destroys the bullet if it goes off screen
            if bullet.rect.x < -60 or bullet.rect.x > 1200 or bullet.rect.y < -60 or bullet.rect.y > 600:
                self.bulletSprites.remove(bullet)
                self.allSprites.remove(bullet)
                self.rigidBodySprites.remove(bullet)
                #print(len(self.bulletSprites)'''
        
        # Ensures that when bullets collide (with the exception of the HULK), they annihilate eachother    
        for bullet in self.bulletSprites:
            collisionList = pygame.sprite.spritecollide(bullet, self.bulletSprites, False)
            for collisionObject in collisionList:
                # The HULK's dieCollideBullet attributs is false and thus cannot be destroyed by bullets
                if collisionObject.dieCollideBullet and len(collisionList) - 1 > 0:
                    self.bulletSprites.remove(collisionObject)
                    self.allSprites.remove(collisionObject)
                    self.rigidBodySprites.remove(collisionObject)      
            if bullet.ricochetBullet(self.wallSprites) == False:
                self.bulletSprites.remove(bullet)
                self.allSprites.remove(bullet)
                self.rigidBodySprites.remove(bullet)
            '''   
            # If the number of ricochets a bullet has is not zero and it collides with a wall then don't destroy it
            collisionList = pygame.sprite.spritecollide(bullet, self.wallSprites, False)
            if bullet.ricochet > 0 and len(collisionList) > 0:
                for wall in collisionList:
                    bullet.rotation = TAU/2.0 + 2.0 * detectSide(wall, bullet) - bullet.rotation
                    bullet.ricochet -= 1
            # If the number of ricochets is 0 and it collided with a wall then destroy the bullet
            elif: len(collisionList) > 0 and bullet.dieCollideWall:
                    self.bulletSprites.remove(bullet)
                    self.allSprites.remove(bullet)
                    self.rigidBodySprites.remove(bullet)'''
            
            collisionList = pygame.sprite.spritecollide(bullet, self.playerSprites, False)
            if bullet.creator in collisionList:
                collisionList.remove(bullet.creator)
                #collisionObject = None
            else:
                bullet.creator = None
               
            for collisionObject in collisionList:
                # Executes if player 2 is killed
                if collisionObject == self.player2:
                    # Increase the score of player 1 
                    self.score[0] += 1
                    # Revert it back to its original position
                    self.player1.pos = [100.0-15.0, 300.0-15.0]
                    self.player1.rotation = 0.0
                    self.player2.pos = [1100.0-15.0, 300.0-15.0]
                    self.player2.rotation = TAU/2.0
                    self.player1.fireTimeout = 0
                    
                    self.rigidBodySprites.remove(self.bulletSprites)
                    self.allSprites.remove(self.bulletSprites)
                    self.bulletSprites = pygame.sprite.Group()
                    
                # Executes if player 1 is killed   
                elif collisionObject == self.player1:
                    # Increase the score for player 2
                    self.score[1] += 1
                    # Revert it back to it's start position and rotation
                    self.player1.pos = [100.0-15.0, 300.0-15.0]
                    self.player1.rotation = 0.0
                    self.player2.pos = [1100.0-15.0, 300.0-15.0]
                    self.player2.rotation = TAU/2.0
                    self.player2.fireTimeout = 0
                    
                    self.rigidBodySprites.remove(self.bulletSprites)
                    self.allSprites.remove(self.bulletSprites)
                    self.bulletSprites = pygame.sprite.Group()
                    
            # If none of the above conditions were satisfid but the bullet collided with something, then destroy it       
            if len(collisionList) > 0:
                self.bulletSprites.remove(bullet)
                self.allSprites.remove(bullet)
                self.rigidBodySprites.remove(bullet)
        
        # Apply changes to the players
        for player in self.playerSprites:
            player.update()
            
            collisionList = pygame.sprite.spritecollide(player, self.dropSprites, False)
            for collisionObject in collisionList:
                self.dropSprites.remove(collisionObject)
                self.allSprites.remove(collisionObject)
                player.maxFireTimeout = collisionObject.maxFireTimeout
                player.fireTimeout = 0
                player.ammo = collisionObject.ammo
                player.bulletSize = collisionObject.bulletSize
                player.ricochet = collisionObject.ricochet
                player.dieCollideBullet = collisionObject.dieCollideBullet
                player.dieCollideWall = collisionObject.dieCollideWall
            
        
        #pos, maxFireTimeout, ammo, bulletSize, ricochet: lives, dieCollideBullet, dieCollideWall
        #Rapid
        #Hulk
        #Bounce
        bulletTypes =                                                                                                                                                                       \
                [                                                                                                                                                                           \
                    [[], sample(range(4,  10), 1)[0], sample(range(10, 30), 1)[0], sample(range( 5, 10), 1)[0], 0, True, sample([True, True, True, False], 1)[0]],                          \
                    [[], sample(range(120, 240), 1)[0], sample(range( 5, 12), 1)[0], sample(range(20, 40), 1)[0], 0, False, False],                                                           \
                    [[], sample(range(20, 30), 1)[0], sample(range(10, 20), 1)[0], sample(range(15, 20), 1)[0], sample(range(5, 25), 1)[0], sample([True, True, True, False], 1)[0], True]  \
                ]
    
        # Drops only spwan if there are less than 3 already present
        if len(self.dropSprites) < 3:
            # There is a one in 1000 chance of spawning a drop
            if randrange(0,1000) == 0:
                param = bulletTypes[randrange(0,3)]
                newX = randrange(10,1200-1)
                newY = randrange(10,600-10)
                param[0] = [newX,newY]
                newDrop = Drops(param[0],param[1],param[2],param[3],param[4],param[5],param[6])
                while newDrop.checkCol(self.allSprites) == True:
                    newX = randrange(0,1200)
                    newY = randrange(0,600)
                    param[0] = (newX,newY)
                    newDrop = Drops(param[0],param[1],param[2],param[3],param[4],param[5],param[6])
                self.allSprites.add(newDrop)
                self.dropSprites.add(newDrop)
        #block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        
        # Teleportation Feature
        for portal in self.portalSprites:
           portal.teleport(self.portalSprites, self.playerSprites)
           portal.teleport(self.portalSprites, self.bulletSprites)
           
    #Tenn & Aniekan
    def render(self):
        self.screen.fill([255,255,255])
        # == Draw Code ==
        #Order is important
        self.portalSprites.draw(self.screen)
        self.wallSprites.draw(self.screen)
        self.dropSprites.draw(self.screen)
        self.playerSprites.draw(self.screen)
        self.bulletSprites.draw(self.screen)
        
        pygame.draw.rect(self.screen, [255, 255, 255], [0, 600, 1200, 100])
        font = pygame.font.SysFont('Consolas', 25, True, False)
        fontLarge = pygame.font.SysFont('Consolas', 35, True, False)
        
        # Player 1
        text = fontLarge.render("Score: " + str(self.score[0]),True,RED)
        self.screen.blit(text, [11, 610])
        ammo = str(self.player1.ammo)
        if ammo == "-1":
            ammo = ""
        text = font.render("Ammo: " + ammo,True,RED)
        self.screen.blit(text, [11, 650])
        pygame.draw.rect(self.screen, GREEN, [10,680, 100, 10], 1)
        pygame.draw.rect(self.screen, GREEN, [10,680, 100 - self.player1.fireTimeout/self.player1.maxFireTimeout * 100, 10])
        
        # Player 2
        offset = len(str(self.score[1])) * 20
        text = fontLarge.render("Score: " + str(self.score[1]),True,RED)
        self.screen.blit(text, [1200-145-offset, 610])
        ammo = str(self.player2.ammo)
        if ammo == "-1":
            ammo = ""
        offset = len(ammo) * 10
        text = font.render("Ammo: " + ammo,True,RED)
        self.screen.blit(text, [1200-100-offset, 650])
        pygame.draw.rect(self.screen, GREEN, [1090,680, 100, 10], 1)
        pygame.draw.rect(self.screen, GREEN, [1090,680, 100 - self.player2.fireTimeout/self.player2.maxFireTimeout * 100, 10])
        
        #mousePos = pygame.mouse.get_pos()
        #print(mousePos[0],mousePos[1])
        # == End Draw Code ==
        pygame.display.flip()

#Tenn
if __name__ == "__main__":
    main = Main()
    main.loop()
    pygame.quit()
    
