import pygame
import math
import random

normal_speed = 10

class Racer(pygame.sprite.Sprite):
    """ Doi tuong dua """
    def __init__(self, x, y, icon_game):
        #self.racer_type = "ball" #add before init raecers
        #self.num = 0    #add before init raecers

        #init image for racer
        #direct = "image/racers/"
        #ic_name = direct + str(self.racer_type) + "/ic_" + str(self.racer_type) + str(self.num) + ".png"
        #self.img = pygame.image.load(ic_name)
        self.img = icon_game

        self.x = x
        self.y = y
        self.time = 0       #time of amulet effect
        self.speed = normal_speed
        self.rank = 0
        #self.game = game

    def update(self, *args):
        self.x += self.speed
        if self.x > self.game.GAME_WIDTH:
            self.x = 0

    def draw(self):
        self.game.SCREEN.blit(self.img, (self.x, self.y))


    def win(self):
        """" An mung """

    def lose(self):
        """ Buon """

class User():
    def __init__(self):
        self.name = "NULL"
        self.password = "NULL"
        self.winrate = 0
        self.playtime = 0
        self.coins = 0
    pass