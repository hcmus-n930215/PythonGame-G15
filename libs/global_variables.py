import pygame
import math
import time
import random
from libs.Widgets import *

class INIT_GAME():
    DELAY_TIME = 60
    FPS = 60


    clock = pygame.time.Clock()
    def __init__(self) -> None:

        pygame.init()
        pygame.display.set_caption("Racing with me!")
        self.VERSION_INFO = "2.0"
        self.INFOR_DISPLAY = pygame.display.Info()
        self.SCREEN_SIZE = (self.INFOR_DISPLAY.current_w, self.INFOR_DISPLAY.current_h)

        self.GAME_WIDTH = int(self.SCREEN_SIZE[1])
        self.GAME_HEIGHT = int(self.GAME_WIDTH / 3 * 2)
        self.SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.GAME_WIDTH_DEFAULT = 1080
        self.GAME_HEIGHT_DEFAULT = 720

        self.btn_play_again = Button(self.GAME_WIDTH/3 - self.GAME_WIDTH / 20,
                                     self.GAME_HEIGHT/4*3 + self.GAME_HEIGHT / 20,
                                     self.GAME_WIDTH / 10, self.GAME_HEIGHT / 10,
                                     "PLAY AGAIN")

        self.btn_end = Button(self.GAME_WIDTH / 3 * 2 - self.GAME_WIDTH / 20,
                              self.GAME_HEIGHT / 4*3 + self.GAME_HEIGHT / 20,
                              self.GAME_WIDTH / 10, self.GAME_HEIGHT / 10,
                              "QUIT")

        self.IC_RACETRACK = self.load_img("img/ic_way.png", 200, 150)
        self.IC_GRASS = self.load_img("img/ic_grass.png", 80, 80)
        self.IC_RANK = self.load_img("img/ic_rank.png", 0.8, 0.8)
        self.IC_STONE = self.load_img("img/ic_stone.png", 100, 100)
        self.IC_CAMERA = (self.load_img("img/camera0.png", 0.8, 0.8),
                          self.load_img("img/camera1.png", 0.8, 0.8),
                          self.load_img("img/camera2.png", 0.8, 0.8))
        self.IC_FINISH_FLAG = self.load_img("img/line.png", 20, 355)
        self.BG_0 = self.load_img("img/Background0.png", self.GAME_WIDTH, self.GAME_HEIGHT)  # Nhập số để thay đổi

        self.IC_RESULT_BOARD = self.load_img("img/ic_result_board.png", 800, 600)
        self.IC_WIN = self.load_img("img/ic_win.png", 300, 300)
        self.IC_LOSE = self.load_img("img/ic_lose.png", 300, 300)
        self.IC_TOP1 = self.load_img("img./ic_top1.png", 0.8,0.8)

        self.ROLLBACK_STEP = 0
        self.BTN_VERSION = Button(10, 5, 100, 100, "Versions: " + self.VERSION_INFO)
        self.TIME_INTERVAL = 1000 / self.FPS
        # some boolean
        self.IS_SIGNED_IN = True
        self.IS_GAME_PLAYING = False
        self.IS_GAME_ENDED = False
        self.RESTART = False

        # Dieu chinh quang duong dua
        # Length of road
        self.START_POS = 300
        self.DISTANCE = 1000

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
        # self.SCREEN.fill(180)
        self.START_POS = 300 + rollback
        # 6 - draw the screen elements

        """for x in range(0, 100):
                    for y in range(-1, 2):
                        self.SCREEN.blit(self.IC_GRASS, (x * 40 + rollback, y * 40))
                for x in range(0, 16):
                    for y in range(0, 1):
                        self.SCREEN.blit(self.IC_CLOUD, (x * 90, y * 90))
                for i in range(0, 50):
                    for j in range(0, 7):
                        self.SCREEN.blit(self.IC_RACETRACK, (i * 60 + rollback, j * 50 + 100))
                for i in range(0, 100):
                    self.SCREEN.blit(self.IC_STONE, (i * 100 + rollback, 450))
                for x in range(0, 33):
                    for y in range(0, 5):
                        self.SCREEN.blit(self.IC_GRASS, (x * 40, y * 40 + 500))
                for i in range(0, 9):
                    self.SCREEN.blit(self.IC_FINISH_FLAG, (300 + rollback, i * 40 + 100))
                    self.SCREEN.blit(self.IC_FINISH_FLAG, (self.DISTANCE - 50, i * 40 + 100))"""
        # for i in range (0,6):
        for i in range(-1, 6):
            self.SCREEN.blit(self.BG_0, (self.GAME_WIDTH * i + rollback, 0))
        self.SCREEN.blit(self.IC_FINISH_FLAG, (290 + rollback, 255))
        self.SCREEN.blit(self.IC_FINISH_FLAG, (self.DISTANCE - 20, 255))
        self.BTN_VERSION.show()

    pass



class Amulet(pygame.sprite.Sprite):
    """ Bua """
    def __init__(self,game, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.game = game
        self.exist_ambulet = False






    def stop_amulet(self):
        """Bua dung"""
        self.speed = 0
        #self.x += self.speed
        self.time-=20



    def slow_amulet(self):
        """Bua giam toc"""
        self.speed=0.5
        #self.x+=self.speed
        self.time-=1

    def fast_amulet(self):
        """Bua tang toc"""
        self.speed = 3.5
        #self.x += self.speed
        self.time-=2


    def turnback_amulet(self):
        """Bua quay dau"""
        #self.speed = -100
        #self.x += self.speed
        self.x = self.game.START_POS
        self.time=0



    def teleport_amulet(self):
        """Bua lam ngung chuyen dong cua doi phuong"""
        i = 0
        while (i<25):
            self.x += random.randrange(3, 6)
            i += 1
        self.time = 0


    def active(self):
        if(self.kind ==  1):
            self.stop_amulet()
        elif(self.kind ==  2):
            self.slow_amulet()
        elif (self.kind == 3):
            self.fast_amulet()
        elif (self.kind == 4):
            self.turnback_amulet()
        elif (self.kind == 5):
            self.teleport_amulet()
        self.exist_ambulet = False

    def Amulet_appear(self):
        if(self.x<1000):
            self.amulet_x = random.randrange(450, 1000)
        elif(self.x<2000):
            self.amulet_x = random.randrange(1200, 1800)
        elif(self.x<3000):
            self.amulet_x = random.randrange(2200, 2800)
        self.kind = random.randrange(1,6)
        self.time = 50
        self.exist_ambulet = True

    def draw_amulet(self,rollback):
        if self.exist_ambulet:

            if (self.kind == 1):
                self.game.SCREEN.blit(self.IC_STOP, (self.amulet_x+rollback, self.y))
            elif (self.kind == 2):
                self.game.SCREEN.blit(self.IC_SLOW, (self.amulet_x+rollback, self.y))
            elif (self.kind == 3):
                self.game.SCREEN.blit(self.IC_FAST, (self.amulet_x+rollback, self.y))
            elif (self.kind == 4):
                self.game.SCREEN.blit(self.IC_TURNBACK, (self.amulet_x+rollback, self.y))
            elif (self.kind == 5):
                self.game.SCREEN.blit(self.IC_TELEPORT, (self.amulet_x+rollback, self.y))
            self.amulet_x += +rollback
            #self.game.SCREEN.blit(img_amulet, (self.amulet_x, self.y))
class Racer(Amulet):
    """ Doi tuong dua """
    def __init__(self, x, y, game, pack ="ic_snail", num=0):
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
        #self.speed = 2
        self.rank = num + 1
        self.game = game
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.bk_nowDraw = self.lastDrawRect
        self.distance = 0
        self.amulet_x = 0
        self.IC_STOP = pygame.image.load("img/ic_amulet" + "1" + ".png")
        self.IC_SLOW = pygame.image.load("img/ic_amulet" + "2" + ".png")
        self.IC_FAST = pygame.image.load("img/ic_amulet" + "3" + ".png")
        self.IC_TURNBACK = pygame.image.load("img/ic_amulet" + "4" + ".png")
        self.IC_TELEPORT = pygame.image.load("img/ic_amulet" + "5" + ".png")

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
            #s elf.x += self.speed - rollback
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
        #self.speed = 2
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

        self.show_top1 = False;

        self.x = game.GAME_WIDTH - self.size[0]
        self.y = 0

    def draw(self, rs):
        m = self.x + int(self.size[0] / 2.5)
        n = int(self.size[1] / 7.7)
        self.game.SCREEN.blit(self.img, (self.x, self.y))
        for i in range(0, 6):
            self.game.SCREEN.blit(rs[i].img, (m, self.y + n*(rs[i].rank+0.33)))

        if self.show_top1:
            self.game.SCREEN.blit(self.game.IC_TOP1, (m, self.y + n ))
            # print(self.racers[i].rank)

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
            self.anim = (self.anim + 1) % 3
            self.time =0
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
            self.delta = max(delta/3, 10)*(delta/abs(delta))

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