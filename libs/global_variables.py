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
        self.SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        #self.IC_CIRCLE = pygame.image.load("img/ic_circle.png")
        #self.IC_CLOUD = pygame.image.load("img/ic_cloud.png")
        self.IC_RACETRACK = self.load_img("img/ic_way.png", 200, 150)
        self.IC_GRASS = self.load_img("img/ic_grass.png", 80, 80)
        self.IC_RANK = self.load_img("img/ic_rank.png", 0.8, 0.8)
        self.IC_STONE = self.load_img("img/ic_stone.png",100,100)
        self.IC_CAMERA = (self.load_img("img/camera0.png", 0.8, 0.8),
                          self.load_img("img/camera1.png", 0.8, 0.8),
                          self.load_img("img/camera2.png", 0.8, 0.8))
        self.IC_FINISH_FLAG = self.load_img("img/ic_fisish_line.png", 200, 200)

        self.ROLLBACK_STEP = 0

        self.TIME_INTERVAL = 1000/self.FPS
        # some boolean
        self.IS_SIGNED_IN = False
        self.IS_GAME_PLAYING = False

        # Dieu chinh quang duong dua
        # Length of road
        self.DISTANCE = 2000

        super().__init__()

    def load_img(self, link, scale_x, scale_y):
        img = pygame.image.load(link).convert_alpha()
        if scale_x <= 1 and scale_y <= 1:
            size = img.get_rect().size
            scale_x = size[0] * scale_x
            scale_y = size[1] * scale_y
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
            self.SCREEN.blit(self.IC_FINISH_FLAG, (300 + rollback, i * 40 + 100))
            self.SCREEN.blit(self.IC_FINISH_FLAG, (self.DISTANCE-50, i * 40 + 100))
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
        self.speed = random.randrange(15, 30) / 10
        self.rank = num + 1
        self.game = game
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.bk_nowDraw = self.lastDrawRect
        #self.distance = 0

    def update(self, camera):
        # if self.distance > self.game.DISTANCE:
        #    return False
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())

        # if self.x > self.game.GAME_WIDTH // 2:

        if self.x + self.speed + camera.delta > self.game.DISTANCE:
            self.x = self.game.DISTANCE
            self.speed = 0
            return False
        else:
            # self.x += self.speed - rollback
            self.x += self.speed + camera.delta
        # self.distance += self.speed + camera.delta
        # print(self.distance, end=" ")
        # else:
        #    self.x += self.speed
        # if self.x > self.game.GAME_WIDTH:
        #   self.x = 0
        return True

    def updatespeed(self):
        self.speed = random.randrange(15, 30) / 10

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
        self.img = pygame.transform.scale(self.img, (int(self.size[0]*(game.GAME_WIDTH/1280)),
                                                     int(self.size[1]*(game.GAME_HEIGHT/720))))
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


class User():
    def __init__(self):
        self.name = "NULL"
        self.password = "NULL"
        self.winrate = 0
        self.playtime = 0
        self.coins = 0
    pass


class Camera():
    def __init__(self, game):
        self.game = game
        self.follow = 3
        self.x = game.GAME_WIDTH/3
        self.delta = 0
        self.anim = 0
        self.time = 0

    def update(self, rs):
        delta = self.x - rs.x
        if int(self.time % 10) == 0:
            self.time = 0
            self.anim = (self.anim + 1) % 3
        self.time += 1
        self.game.SCREEN.blit(self.game.IC_CAMERA[self.anim], (rs.x, rs.y-20))

        if abs(delta) < rs.speed:
            self.delta = rs.x - self.x
        else:
            if delta == 0:
                self.delta = 0
            else:
                self.delta = rs.speed*(delta/abs(delta))
        if abs(delta) > 80:
            self.delta = max(delta/4, 15)*(delta/abs(delta))

        # change following
        if pygame.key.get_pressed()[pygame.K_1]:
            self.follow = 0
            return
        if pygame.key.get_pressed()[pygame.K_2]:
            self.follow = 1
            return
        if pygame.key.get_pressed()[pygame.K_3]:
            self.follow = 2
            return
        if pygame.key.get_pressed()[pygame.K_4]:
            self.follow = 3
            return
        if pygame.key.get_pressed()[pygame.K_5]:
            self.follow = 4
            return
        if pygame.key.get_pressed()[pygame.K_6]:
            self.follow = 5
            return

    pass