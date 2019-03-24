import pygame
import math
import random

#normal_speed = 10 for racer

class INIT_GAME():
    DELAY_TIME = 60
    FPS = 60


    clock = pygame.time.Clock()
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Racing with me!")
        #color_code = ['red', 'green']
        self.IC_CIRCLE = pygame.image.load("image/racers/ball/ic_ball0.png")
        self.IC_CLOUD = pygame.image.load("image/map/ic_cloud.png")
        self.IC_RACETRACK = pygame.image.load("image/map/ic_racetrack.png")
        self.IC_GRASS = pygame.image.load("image/map/ic_grass.png")

        self.INFOR_DISPLAY = pygame.display.Info()
        self.SCREEN_SIZE = (self.INFOR_DISPLAY.current_w, self.INFOR_DISPLAY.current_h)
        self.GAME_WIDTH = int(self.SCREEN_SIZE[0] / 2)
        self.GAME_HEIGHT = int(self.SCREEN_SIZE[1] / 2)

        self.SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))

        super().__init__()

    def draw_map(self):
        self.SCREEN.fill(0)
        # 6 - draw the screen elements
        for x in range(0, 16):
            for y in range(0, 1):
                self.SCREEN.blit(self.IC_CLOUD, (x * 90, y * 90))
        for x in range(0, 25):
            for y in range(0, 7):
                self.SCREEN.blit(self.IC_RACETRACK , (x * 50, y * 50 + 130))
        for x in range(0, 33):
            for y in range(0, 1):
                self.SCREEN.blit(self.IC_GRASS, (x * 40, y * 40 + 90))
        for x in range(0, 33):
            for y in range(0, 5):
                self.SCREEN.blit(self.IC_GRASS, (x * 40, y * 40 + 500))

    pass


class Amulet(pygame.sprite.Sprite):
    """ Bua """
    def __init__(self, x, y, kind, game):
        self.x = x
        self.y = y
        self.kind = kind
        self.game = game
        self.img = game.IC_CIRCLE

    def active(self):
        """ Thuc hien chuc nang cua bua """



class GameController():
    """ Dieu khien UI, noi dung """
    def __init__(self):
        """ Khoi tao """

    def start(self):
        """ Dang nhap, chon racer, chon tien, bat dau dua"""

    def update(self):
        """ """

    def finsh(self):
        """ Hien bang xep hang, hien thang thua"""



class Player():
    """ Nguoi choi """
    def __init__(self):
        #self.name = "NULL"
        #self.password = "NULL"

        self.money = 0
        self.history = 0
        self.racer_chosen = 0
        self.pay = 0

    def sign_in(self, name, password):
        """ Dang nhap """

    def addmoney(self, money):
        """ Nap them tien """

    def choose(self, racer_num):
        """ Chon racer thang """

    def win(self):
        """ Thang """

    def lose(self):
        """ Thua """







