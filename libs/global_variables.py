import pygame
import math
import time
import random

class INIT_GAME():
    DELAY_TIME = 60
    FPS = 60


    clock = pygame.time.Clock()
    def __init__(self) -> None:

        pygame.init()
        pygame.display.set_caption("Racing with me!")

        self.INFOR_DISPLAY = pygame.display.Info()
        self.SCREEN_SIZE = (self.INFOR_DISPLAY.current_w, self.INFOR_DISPLAY.current_h)
        self.GAME_WIDTH = int(self.SCREEN_SIZE[1])
        self.GAME_HEIGHT = int(self.GAME_WIDTH / 3 * 2)
        self.GAME_WIDTH_DEFAULT = 1080
        self.GAME_HEIGHT_DEFAULT = 720

        self.IC_CIRCLE = self.load_img("img/ic_circle.png", 1, 1)
        #self.IC_CLOUD = pygame.image.load("img/ic_cloud.png")
        self.IC_RACETRACK = self.load_img("img/ic_way.png", 200, 150)
        self.IC_GRASS = self.load_img("img/ic_grass.png", 80, 80)
        self.IC_RANK = self.load_img("img/ic_rank.png", 1, 1)
        self.IC_STONE = self.load_img("img/ic_stone.png", 100, 100)
        self.IC_FINISH_FLAG = self.load_img("img/ic_fisish_line.png", 200, 200)


        self.ROLLBACK_STEP = 3
        self.SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))

        super().__init__()

    def load_img(self, link, scale_x, scale_y):
        img = pygame.image.load(link)
        if scale_x <= 1 and scale_y <= 1:
            size = img.get_rect().size
            scale_x = size[0]*scale_x
            scale_y = size[1]*scale_y
        img = pygame.transform.scale(img, (int(scale_x * (self.GAME_WIDTH / self.GAME_WIDTH_DEFAULT)),
                                           int(scale_y * (self.GAME_HEIGHT / self.GAME_HEIGHT_DEFAULT))))
        return img

    def draw_map(self, rollback):
        self.SCREEN.fill(180)
        # 6 - draw the screen elements
        for x in range(0, 100):
            for y in range(-1, 2):
                self.SCREEN.blit(self.IC_GRASS, (x * 40+rollback, y * 40))
        """for x in range(0, 16):
            for y in range(0, 1):
                self.SCREEN.blit(self.IC_CLOUD, (x * 90, y * 90))
                """
        for i in range(0, 50):
            for j in range(0, 7):
                self.SCREEN.blit(self.IC_RACETRACK , (i * 60+rollback, j * 50 + 100))
        for i in range(0, 100):
            self.SCREEN.blit(self.IC_STONE, (i * 100 + rollback, 450))
        """for x in range(0, 33):
            for y in range(0, 5):
                self.SCREEN.blit(self.IC_GRASS, (x * 40, y * 40 + 500))
        """
        for i in range(0, 9):
            self.SCREEN.blit(self.IC_FINISH_FLAG, (50 + rollback, i * 40 + 100))
            self.SCREEN.blit(self.IC_FINISH_FLAG, (2000 + rollback, i * 40 + 100))
    pass


class Racer(pygame.sprite.Sprite):
    """ Doi tuong dua """
    def __init__(self, x, y, game, pack ="ic_snail", num="tron"):
        self.pack_sprite = pack
        self.num = num
        name = "img/"
        ic_name = name + pack + str(num) + ".png"
        self.img = game.load_img(ic_name, 0.8, 0.8)
        self.x = x
        self.y = y
        self.stun = 0
        self.time = 0
        self.speed = random.randrange(18, 25)/10
        self.rank = num + 1
        self.game = game
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.bk_nowDraw = self.lastDrawRect

    def update(self, *args):
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.x += self.speed
        self.speed = random.randrange(15, 40)/10
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
        self.IC_FAST = pygame.image.load("img/ic_coin.png")
        self.speed = "NULL"
        self.speed_now = self.speed

    def stop_amulet(self):
        """Bua dung"""
        if (self.x >= self.appear_Amulet):
            self.speed = 0
        t =time.clock()
        while (time.clock() - t >= 5 ):
            self.speed += self.speed

    def slow_amulet(self):
        """Bua giam toc"""
        lenght = self.x
        if (self.x >= self.appear_Amulet):
            self.speed -= 0.5
        while (self.x - lenght < 15):
            self.speed += self.speed
        self.speed = self.speed_now

    def fast_amulet(self):
        """Bua tang toc"""
        lenght = self.x
        if (self.x >= self.appear_Amulet):
            self.speed += 0.5
        while (self.x - lenght < 20):
            self.speed += self.speed
        self.speed = self.speed_now

    def draw_amulet(self):
        ride = [170, 220, 270, 320, 370, 420]
        x = random.randrange(100,1000,50)
        y = random.choice(ride)
        self.game.SCREEN.blit(self.IC_FAST, (x, y))

    def active(self):
        """ Thuc hien chuc nang cua bua"""
        #vòng lặp sau 1 khoảng thời gian sẽ xuất hiện 1 bùa khác
        temp = False
        while not temp:
            self.appear_Amulet = random.randrange(self.x, self.x +250, 100)
            if(self.kind ==  1):
                Amulet.stop_amulet(self)
                temp = True
            elif(self.kind ==  2):
                Amulet.slow_amulet(self)
                temp = True
            elif (self.kind == 3):
                Amulet.draw_amulet(self)
                Amulet.fast_amulet(self)
                temp = True



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
        self.img = self.game.IC_RANK

        self.size = self.img.get_rect().size

        self.x = game.GAME_WIDTH - self.size[0]
        self.y = 0

    def draw(self, rs):
        m = self.x + int(self.size[0] / 2.5)
        n = int(self.size[1] / 7.7)
        self.game.SCREEN.blit(self.img, (self.x, self.y))
        for i in range(0, 6):
            self.game.SCREEN.blit(rs[i].img, (m, n*(rs[i].rank+0.33)))
            #print(self.racers[i].rank)

    def update(self, rs):

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

        self.draw(rs)
        #return self.racers
class User():
    def __init__(self):
        self.name = "NULL"
        self.password = "NULL"
        self.winrate = 0
        self.playtime = 0
        self.coins = 0
    pass