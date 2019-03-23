import pygame
import math
import random

class INIT_GAME():
    DELAY_TIME = 60
    FPS = 60


    clock = pygame.time.Clock()
    def __init__(self) -> None:

        pygame.init()
        pygame.display.set_caption("Racing with me!")

        self.IC_CIRCLE = pygame.image.load("data/ic_circle.png")
        self.IC_CLOUD = pygame.image.load("data/ic_cloud.png")
        self.IC_RACETRACK = pygame.image.load("data/ic_racetrack.png")
        self.IC_GRASS = pygame.image.load("data/ic_grass.png")
        self.IC_RANK = pygame.image.load("data/ic_rank.png")

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


class Racer(pygame.sprite.Sprite):
    """ Doi tuong dua """
    def __init__(self, x, y, game, pack ="ic_snail", num="tron"):
        self.pack_sprite = pack
        self.num = num
        name = "data/"
        ic_name = name + pack + str(num) + ".png"
        self.img = pygame.image.load(ic_name)
        self.x = x
        self.y = y
        self.stun = 0
        self.time = 0
        self.speed = random.randrange(15, 30)/10
        self.rank = num + 1
        self.game = game
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.bk_nowDraw = self.lastDrawRect

    def update(self, *args):
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.x += self.speed
        if self.x > self.game.GAME_WIDTH:
            self.x = 0

    def draw(self):
        self.bk_nowDraw = self.backupRect(self.lastDrawRect)

        self.game.SCREEN.blit(self.img, (self.x, self.y))
        rect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.lastDrawRect = rect

        return rect
    def backupRect(self, rect):
        return

    def clear(self):
        return self.lastDrawRect

    def win(self):
        """" An mung """

    def lose(self):
        """ Buon """


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
        self.name = "NULL"
        self.password = "NULL"
        self.money = 0
        self.history = 0
        self.chose = 0
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


class Ranking():
    """ Bang xep hang"""
    def __init__(self, game, rs):
        self.game = game
        self.racers= rs
        self.img = self.game.IC_RANK
        self.size = self.img.get_rect().size
        self.img = pygame.transform.scale(self.img, (int(self.size[0]*(game.GAME_WIDTH/960)),
                                                     int(self.size[1]*(game.GAME_HEIGHT/540))))
        self.size = self.img.get_rect().size

        self.x = game.GAME_WIDTH - self.size[0]
        self.y = 0

    def draw(self):
        m = self.x + int(self.size[0] / 2.5)
        n = int(self.size[1] / 7.7)
        self.game.SCREEN.blit(self.img, (self.x, self.y))
        for i in range(0, 6):
            self.game.SCREEN.blit(self.racers[i].img, (m, n*(self.racers[i].rank+0.33)))
            print(self.racers[i].rank)

    def update(self, rs):
        self.racers = rs

        for i in range(0, 6):
            for j in range(0, 6):
                if rs[i].x > rs[j].x and rs[i].rank > rs[j].rank:
                    rs[i].rank, rs[j].rank = rs[j].rank, rs[i].rank
                """if int(rs[i].x) > int(rs[j].x):
                    self.racers[i].rank -= 1
                if rs[i].x == rs[j].x:
                    if rs[i].rank <= rs[j].rank:
                        if i!=j:
                            self.racers[i].rank -= 1
                            """

        self.draw()
        return self.racers

