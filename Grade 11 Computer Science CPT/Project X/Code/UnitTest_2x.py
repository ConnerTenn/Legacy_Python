#CPT: Insert Game Title Here
# Authors : Conner & Aniekan
# Course: ICS-3U
# Date: Jan 01 2016

# Imports
import unittest
import pygame
import Shoot_Em_2x

# Constants
PI = 3.14159265358979323
TAU = 2 * PI

#class which tests all functions in the program
class MyFileTest(unittest.TestCase):

    #Funtions beginning with "test_" will be tested
    def test_degToRad(self):
        self.assertEqual(Shoot_Em_2x.degToRad(360), TAU)
        self.assertEqual(Shoot_Em_2x.degToRad(90), 1.0/4.0*TAU)
        self.assertEqual(Shoot_Em_2x.degToRad(45), 1.0/8.0*TAU)
    
    def test_radToDeg(self):
        self.assertEqual(Shoot_Em_2x.radToDeg(2.0/5.0*TAU), 144)
        self.assertEqual(Shoot_Em_2x.radToDeg(3.0/4.0*TAU), 270)
        self.assertEqual(Shoot_Em_2x.radToDeg(1.0/9.0*TAU), 40)
        
    def test_shoot(self):
        player = Shoot_Em_2x.Player([2,2], 0, [255, 255, 255])
        player.fireTimeout = 10
        self.assertEqual(player.shoot(), None)
        player.fireTimeout = -10
        self.assertIsNotNone(player.shoot())
        
    def test_checkCol(self):
        sprites = pygame.sprite.Group()
        player = Shoot_Em_2x.Player([0,0], 0, [255, 255, 255])
        sprites.add(player)
        player = Shoot_Em_2x.Player([40,40], 0, [255, 255, 255])
        sprites.add(player)
        player = Shoot_Em_2x.Player([80,80], 0, [255, 255, 255])
        sprites.add(player)
        
        drop = Shoot_Em_2x.Drops([100, 100], 60, 60, 10, 0, True, True)
        self.assertEqual(drop.checkCol(sprites), True)
        drop = Shoot_Em_2x.Drops([110, 11], 60, 60, 10, 0, True, True)
        self.assertEqual(drop.checkCol(sprites), False)
        drop = Shoot_Em_2x.Drops([0, 0], 60, 60, 10, 0, True, True)
        self.assertEqual(drop.checkCol(sprites), True)
        
    def test_ricochetBullet(self):
        sprites = pygame.sprite.Group()
        wall = Shoot_Em_2x.Walls(0, 0, 100, 10)
        sprites.add(wall)
        
        bullet = Shoot_Em_2x.Bullet([0,0],10,0,0,True,True,None)
        self.assertEqual(bullet.ricochetBullet(sprites),False)
        bullet = Shoot_Em_2x.Bullet([0,0],10,0,10,True,True,None)
        self.assertEqual(bullet.ricochetBullet(sprites),True)
        bullet = Shoot_Em_2x.Bullet([0,1000],10,0,10,True,True,None)
        self.assertEqual(bullet.ricochetBullet(sprites),False)
        bullet = Shoot_Em_2x.Bullet([0,0],10,0,10,True,True,None)
        self.assertEqual(bullet.ricochetBullet([]),False)
    
#Main
if __name__ == "__main__":
    unittest.main()
