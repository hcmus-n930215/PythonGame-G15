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

        self.IC_CIRCLE = pygame.image.load("img/ic_circle.png")
        self.IC_CLOUD = pygame.image.load("img/ic_cloud.png")
        self.IC_RACETRACK = pygame.transform.scale(pygame.image.load("img/ic_way.png"), (200,150))
        self.IC_GRASS = pygame.image.load("img/ic_grass.png")
        self.IC_GRASS = pygame.transform.scale(self.IC_GRASS, (80, 80))
        self.IC_RANK = pygame.image.load("img/ic_rank.png")
        self.IC_STONE = pygame.transform.scale(pygame.image.load("img/ic_stone.png"),(100,100))
        self.IC_FINISH_FLAG = pygame.transform.scale(pygame.image.load("img/ic_fisish_line.png"), (200, 200))
        self.INFOR_DISPLAY = pygame.display.Info()
        self.SCREEN_SIZE = (self.INFOR_DISPLAY.current_w, self.INFOR_DISPLAY.current_h)
        self.GAME_WIDTH = int(self.SCREEN_SIZE[1] )
        self.GAME_HEIGHT = int(self.GAME_WIDTH / 3 * 2)
        self.ROLLBACK_STEP = 3
        self.SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))

        super().__init__()

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
        self.img = pygame.image.load(ic_name)
        self.x = x
        self.y = y
        self.stun = 0
        self.time = 0
        self.speed = random.randrange(18, 25)/10
        self.rank = num + 1
        self.game = game
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.bk_nowDraw = self.lastDrawRect
        self.test_amulet = 0 #Kiểm tra xem racers có đang dính bùa nào không

    def update(self, *args):
        self.lastDrawRect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.x += self.speed
        self.speed = random.randrange(15, 40)/10
        if self.x > self.game.GAME_WIDTH:
            self.x = 0
        """if self.test_amulet != 0:
            lenght = self.x
            if (self.test_amulet == 3):
                self.speed += 50
            while (self.x - lenght < 100):
                self.x += self.speed
            self.test_amulet = 0"""

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
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind

    def stop_amulet(self):
        """Bua dung"""
        self.speed = 0
        self.x += self.speed

    def slow_amulet(self):
        """Bua giam toc"""
        self.speed = 1
        self.x += self.speed

    def fast_amulet(self):
        """Bua tang toc"""
        self.speed = 4
        self.x += self.speed

    def turnback_amulet(self):
        """Bua quay dau"""
        self.speed = -1.5
        self.x += self.speed

    def attack_amulet(self):
        """Bua lam ngung chuyen dong cua doi phuong"""
        i=0
        while (i<5):
            self.x += random.randrange(15, 40)/10
            i += 1

    def active(self):
        #Thuc hien chuc nang cua bua
        #vòng lặp sau 1 khoảng thời gian sẽ xuất hiện 1 bùa khác
        if(self.kind ==  1):
            self.stop_amulet()
        elif(self.kind ==  2):
            self.slow_amulet()
        elif (self.kind == 3):
            self.fast_amulet()
        elif (self.kind == 4):
            self.turnback_amulet()
        elif (self.kind == 5):
            self.attack_amulet()


"""def Vebua_Xoabua(rs, l_amulet):
    #Tạo bùa, xóa bùa dựa vào trạng thái racers
    icon = pygame.display.set_mode()
    IC_FAST = pygame.image.load("img/ic_fast.png")
    for i in range(0, 6):
        if l_amulet.kind == 3:
            #xoa bua hoặc là vẽ 1 bùa mới khi không có racers nào dính bùa
            if (rs[i].x >= l_amulet.x - 50 and rs[i].y == l_amulet.y):
                rs[i].test_amulet = 0
                l_amulet.kind = 0

                lenght = rs[i].x
                rs[i].speed_now = rs[i].speed
                rs[i].speed += 0.05
                while (rs[i].x - lenght < 50):
                    rs[i].x += rs[i].speed
                rs[i].speed = rs[i].speed_now
            else:
                if(l_amulet.kind == 3):
                    icon.blit(IC_FAST, (l_amulet.x, l_amulet.y))


    
    
    """


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
        #return self.racers
class User():
    def __init__(self):
        self.name = "NULL"
        self.password = "NULL"
        self.winrate = 0
        self.playtime = 0
        self.coins = 0
    pass