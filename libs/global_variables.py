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
        self.VERSION_INFO = "3.0 Release"
        self.INFOR_DISPLAY = pygame.display.Info()
        self.SCREEN_SIZE = (self.INFOR_DISPLAY.current_w, self.INFOR_DISPLAY.current_h)
        self.GAME_WIDTH = int(self.SCREEN_SIZE[1]//10*9)
        self.GAME_HEIGHT = int(self.GAME_WIDTH/3*2)
        #self.GAME_WIDTH = 1080
        #self.GAME_HEIGHT = 720
        self.SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.GAME_WIDTH_DEFAULT = 1080
        self.GAME_HEIGHT_DEFAULT = 720
        self.SCALE_X = self.GAME_WIDTH/self.GAME_WIDTH_DEFAULT
        self.SCALE_Y = self.GAME_HEIGHT/self.GAME_HEIGHT_DEFAULT
        self.IC_LOGOTEAM = self.load_img("img/ic_logoTeam.png", 70, -1)
        pygame.display.set_icon(self.IC_LOGOTEAM)
        self.BG_MAP = None
        self.btn_play_again = View(self.GAME_WIDTH/3 - self.GAME_WIDTH/20,
                                     self.GAME_HEIGHT/4*3 + self.GAME_HEIGHT/20, "PLAY AGAIN", color="#eafd00")
        self.btn_end = View(self.GAME_WIDTH/3*2 - self.GAME_WIDTH/20,
                              self.GAME_HEIGHT/4*3 + self.GAME_HEIGHT/20, "QUIT", color="#eafd00")
        self.list_tv = (View(self.GAME_WIDTH/4 - self.GAME_WIDTH/20, self.GAME_HEIGHT/2 + self.GAME_HEIGHT/20*1, color="#65d06f", gravity="center_horizontal"),
                   View(self.GAME_WIDTH/4 - self.GAME_WIDTH/20, self.GAME_HEIGHT/2 + self.GAME_HEIGHT/20*2, color="#65d06f", gravity="center_horizontal"),
                   View(self.GAME_WIDTH/4 - self.GAME_WIDTH/20, self.GAME_HEIGHT/2 + self.GAME_HEIGHT/20*3, color="#65d06f", gravity="center_horizontal"))
        self.IC_RESULT_BOARD = self.load_img("img/ic_result_board.png", 800, 600)
        self.IC_WIN = self.load_img("img/ic_win.png", 300, 300)
        self.IC_LOSE = self.load_img("img/ic_lose.png", 300, 300)
        self.IC_TOP1 = self.load_img("img./ic_top1.png", 0.8, 0.8)
        self.IC_APP_NAME = self.load_img("img/ic_app_name.png", self.GAME_WIDTH//2, -1)
        self.IC_RANK = self.load_img("img/ic_rank.png",0.8,0.8)
        self.IC_MINIMAP = self.load_img("img/minimap.png", 300, 50)
        self.IC_POINT_B = self.load_img("img/point_blue.png", 11, 11)
        self.IC_POINT_R = self.load_img("img/point_red.png", 11, 11)
        self.IC_MINIMAP_CAMERA = self.load_img("img/minimap_camera.png", 38, 21)

        self.IC_STAR = ImageView(self, self.GAME_WIDTH -  self.GAME_WIDTH//4 + 100, self.GAME_HEIGHT -120, 80, 80, "img/ic_star.png")
        self.IC_SHIELD = ImageView(self, self.GAME_WIDTH -  self.GAME_WIDTH//4 , self.GAME_HEIGHT -120, 80, 80, "img/ic_shield.png")
        self.IC_ARROW = self.load_img("img/arrow.png", 50, -1)
        self.IC_TICK = self.load_img("img/ic_tick.png", 50, -1)
        self.IC_PROFILE = self.load_img("img/ic_profile1.png", 50, -1)
        self.IC_SHIELD_MINI = self.load_img("img/ic_shield.png", 35, -1)
        self.IC_WINRATE = self.load_img("img/ic_win_rate.png", 45, -1)
        self.IC_PLAYED_TIME = self.load_img("img/ic_playedTime.png", 45, -1)

        self.IC_COIN = self.load_img("img/ic_coin.png", 50, -1)
        self.IC_CAMERA = (self.load_img("img/camera0.png", 0.8, 0.8),
                          self.load_img("img/camera1.png", 0.8, 0.8),
                          self.load_img("img/camera2.png", 0.8, 0.8))
        self.IC_FINISH_FLAG = self.load_img("img/line.png", 20, 355)

        self.SETTING_PREF = "data/setting_preferences"
        self.ROLLBACK_STEP = 0
        self.BTN_VERSION = View(self.GAME_WIDTH - 10, self.GAME_HEIGHT - 10, "Versions: "+self.VERSION_INFO,color="#000000", gravity="bottom_right")
        self.TIME_INTERVAL = 1000/self.FPS
        # some boolean
        self.IS_SIGNED_IN = False
        self.IS_GAME_PLAYING = False
        self.IS_GAME_ENDED = False
        self.IS_START_OPTIONS = False
        self.IS_IN_HISTORY = False
        self.IS_IN_SETTINGS = False
        self.IS_IN_SHOP = False
        # Dieu chinh quang duong dua
        self.RESTART = False
        self.START_POS = self.GAME_WIDTH/3
        self.DISTANCE_DEFAULT = 3000
        self.DISTANCE = self.DISTANCE_DEFAULT
        # setting file
        self.DEFAULT_MAP_CODE = 1
        self.DEFAULT_RACERS_CODE = 1
        self.DEFAULT_ACCOUNT_POS = 100000
        # List of sound: backgr, playing, result: 0 is off, 1 is on
        self.DEFAULT_SOUND_CODE = (1, 1, 1)
        self.load_setting_pref()
        super().__init__()

    def load_img(self, link, scale_x, scale_y):
        img = pygame.image.load(link).convert_alpha()
        size = img.get_rect().size
        if scale_x == -1:
            scale_x = size[0]*scale_y/size[1]
        if scale_y == -1:
            scale_y = size[1]*scale_x/size[0]
        if scale_x <= 3 and scale_y <= 3:
            scale_x = size[0]*scale_x
            scale_y = size[1]*scale_y
        img = pygame.transform.scale(img, (int(scale_x*self.SCALE_X), int(scale_y*self.SCALE_Y)))
        return img

    def draw_map(self, rollback):
        self.START_POS = self.GAME_WIDTH/3 + rollback
        for i in range(0, 2):
            self.SCREEN.blit(self.BG_MAP, (self.GAME_WIDTH*((-rollback//self.GAME_WIDTH)+i) + rollback, 0))
        self.SCREEN.blit(self.IC_FINISH_FLAG, (self.START_POS, 255*self.SCALE_Y))
        self.SCREEN.blit(self.IC_FINISH_FLAG, (self.DISTANCE-50*self.SCALE_X, 255*self.SCALE_Y))
        self.BTN_VERSION.isTransparent=False
        self.BTN_VERSION.show()
        self.SCREEN.blit(self.IC_LOGOTEAM, (self.GAME_WIDTH - 100*self.SCALE_X, self.GAME_HEIGHT - 100*self.SCALE_Y))

    def load_setting_pref(self):
        try:
            f = open(self.SETTING_PREF, "rt")
        except FileNotFoundError:
            # reset the default pref setting file
            fx = open(self.SETTING_PREF, "w")
            fx.write(
                "# The map are 0 and 1\ndefault_map=0\n\n# The racers are: rc_lead, rc_catus, rc_turtle, rc_snail\ndefault_racer=rc_snail\ncount_account=100023\ndefault_sound=7")
            fx.close()
            self.DEFAULT_MAP_CODE = 0
            self.DEFAULT_RACERS_CODE = "rc_snail"
            self.DEFAULT_ACCOUNT_POS = 100000
            self.DEFAULT_SOUND_CODE = (1, 1, 1)
            return -1

        data = f.readlines()
        for pref in data:
            pos = 0
            try:
                if pref[0]=='#': # skip line
                    continue
                pos = pref.index('=')
                if pref[:pos]=="default_map":
                    if len(pref[pos+1:]) > 0:
                        self.DEFAULT_MAP_CODE = str(int(pref[pos+1:]))
                        self.assign_map()
                if pref[:pos]=="default_racer":
                    if len(pref[pos+1:]) > 0:
                        buff = pref[pos+1:]
                        while buff[len(buff)-1]=='\n':
                            buff = buff[:len(buff)-1]
                        self.DEFAULT_RACERS_CODE = buff
                if pref[:pos]=="count_account":
                    if len(pref[pos+1:]) > 0:
                        buff = pref[pos+1:]
                        while buff[len(buff)-1]=='\n':
                            buff = buff[:len(buff)-1]
                        self.DEFAULT_ACCOUNT_POS = buff
                if pref[:pos]=="default_sound":
                    if len(pref[pos+1:]) > 0:
                        buff = pref[pos+1:]
                        while buff[len(buff)-1]=='\n':
                            buff = buff[:len(buff)-1]
                        num = int(buff)
                        list = [4, 2, 1]
                        list2 = []
                        for i in range(0,3):
                            if num//list[i]>=1:
                                list2.append(1)
                                num = num%list[i]
                            else:
                                list2.append(0)
                        self.DEFAULT_SOUND_CODE = (list2[0], list2[1], list2[2])
            except ValueError as e:
                print("Error in file %s" % __file__)
                print("Message: %s" % e)
        f.close()
    def update_setting_pref(self):
        try:
            f = open(self.SETTING_PREF, "rt")
        except FileNotFoundError:
            # reset the default pref setting file
            fx = open(self.SETTING_PREF, "w")
            fx.write("# The map are 0 and 1\ndefault_map="+str(int(self.DEFAULT_MAP_CODE))
                     +"\n\n# The racers are: rc_lead, rc_catus, rc_turtle, rc_snail\ndefault_racer="
                     + str(self.DEFAULT_RACERS_CODE) +"\n"+"count_account="+str(self.DEFAULT_ACCOUNT_POS)+"default_sound=7\n")
            fx.close()
            return -1
        data = f.readlines()
        buffer = ""
        for pref in data:
            try:
                if (pref[0]=='#') or (pref[0]=='\n'): # skip line
                    buffer+=pref
                    continue
                pos = pref.index('=')
                if pref[:pos]=="default_map":
                    buffer+="default_map="+str(int(self.DEFAULT_MAP_CODE))+"\n"
                    continue
                if pref[:pos]=="default_racer":
                    buffer += "default_racer=" + str(self.DEFAULT_RACERS_CODE)+"\n"
                    continue
                if pref[:pos]=="count_account":
                    buffer += "count_account=" + str(self.DEFAULT_ACCOUNT_POS)+"\n"
                    continue
                if pref[:pos]=="default_sound":
                    num = 0
                    list = [4, 2, 1]
                    for i in range(0,3):
                        num += self.DEFAULT_SOUND_CODE[i]*list[i]
                    buffer += "default_sound=" + str(num)+"\n"
                    continue


            except ValueError as e:
                print("Error in file %s" % __file__)
                print("Message: %s" % e)
        f.close()
        f = open(self.SETTING_PREF, "w")
        f.write(buffer)
        f.close()

    def assign_map(self):
        self.BG_MAP = self.load_img("img/Background"+ str(int(self.DEFAULT_MAP_CODE))+ ".png", self.GAME_WIDTH_DEFAULT, self.GAME_HEIGHT_DEFAULT)
    def assign_racers(self):
        space = int(60*self.GAME_HEIGHT/self.GAME_HEIGHT_DEFAULT)
        start_space = int(self.GAME_HEIGHT*260/self.GAME_HEIGHT_DEFAULT)
        racers = []
        for i in range(0,6):
            racers.append(Racer(self.START_POS, start_space + i*space, self, str(self.DEFAULT_RACERS_CODE), i))
        return racers
    pass

class Amulet(pygame.sprite.Sprite):
    def __init__(self,game, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.GAME = game

    def stop_amulet(self):                      # bau dung
        self.speed = 0

    def slow_amulet(self):                      # bua giam toc
        self.speed=0.75

    def fast_amulet(self):                      # bua tang toc
        if self.speed + 2 <= 5:
            self.speed += 2
        self.time -= 2

    def return_start_amulet(self):              # Bua quay ve vi tri xuat phat
        self.x = self.GAME.START_POS
        self.time = 0

    def teleport_amulet(self):                  # Bua toc bien
        self.x += 200
        self.time = 0

    def win_amulet(self):                       # Bua bay thang den dich
        self.x = self.GAME.DISTANCE
        self.time = 0

    def turnback_amulet(self):                  # Bua quay dau
        self.speed = -abs(self.speed)
        self.time -= 2
        self.exist_turn = True

    def active(self):
        if(self.kind ==  1):
            if(self.exist_shield_amulet != True):
                self.stop_amulet()
            else:
                self.kind = 0
                self.exist_shield_amulet = False
        elif(self.kind ==  2):
            if (self.exist_shield_amulet != True):
                self.slow_amulet()
            else:
                self.kind=0
                self.exist_shield_amulet = False
        elif self.kind == 3:
            if self.exist_shield_amulet != True:
                self.fast_amulet()
            else:
                self.kind = 0
                self.exist_shield_amulet = False
        elif self.kind == 4:
            if self.exist_shield_amulet != True:
                self.return_start_amulet()
            else:
                self.kind = 0
                self.exist_shield_amulet = False
        elif self.kind == 5:
            if (self.exist_shield_amulet != True):
                self.teleport_amulet()
            else:
                self.kind = 0
                self.exist_shield_amulet = False
        elif (self.kind == 6):
            if (self.exist_shield_amulet != True):
                self.win_amulet()
            else:
                self.kind = 0
                self.exist_shield_amulet = False
        elif (self.kind == 7):
            if (self.exist_shield_amulet != True):
                self.turnback_amulet()
            else:
                self.kind = 0
                self.exist_shield_amulet = False
        self.exist_amulet = False

    def Amulet_appear(self):
        object=[True, True, True, False, False]
        list_amulet=[1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,5,5,5,7,7,7,6]
        self.exist_amulet=random.choice(object)
        self.amulet_x = self.x + random.randrange(300, 700)
        if self.amulet_x > self.GAME.DISTANCE-500:
            self.exist_amulet = False
        if  self.exist_amulet == True:
            self.kind = random.choice(list_amulet)
            self.time=100
        else:
            self.kind=0

    def draw_amulet(self, rollback):
        if self.exist_amulet:
            if (self.kind == 1):
                self.GAME.SCREEN.blit(self.IC_STOP, (self.amulet_x + rollback, self.y))
            elif (self.kind == 2):
                self.GAME.SCREEN.blit(self.IC_SLOW, (self.amulet_x + rollback, self.y))
            elif (self.kind == 3):
                self.GAME.SCREEN.blit(self.IC_FAST, (self.amulet_x + rollback, self.y))
            elif (self.kind == 4):
                self.GAME.SCREEN.blit(self.IC_RETURN_START, (self.amulet_x + rollback, self.y))
            elif (self.kind == 5):
                self.GAME.SCREEN.blit(self.IC_TELEPORT, (self.amulet_x + rollback, self.y))
            elif (self.kind == 6):
                self.GAME.SCREEN.blit(self.IC_WIN, (self.amulet_x + rollback, self.y))
            elif (self.kind == 7):
                self.GAME.SCREEN.blit(self.IC_TURNBACK, (self.amulet_x + rollback, self.y))
            self.amulet_x += +rollback

class Racer(Amulet): # Doi tuong dua
    def __init__(self, x, y, game, pack="rc_snail", num="0"):
        self.pack_sprite = pack
        self.num = num
        name = "img/"
        self.ic_name = name + pack + str(num) + ".png"
        self.img = game.load_img(self.ic_name, -1, 48)
        self.imgbig = game.load_img(self.ic_name, -1, 48*2)
        ic_name_turn = name + pack + str(num) + str(num) + ".png"
        self.img_turn = game.load_img(ic_name_turn, -1, 48)
        self.x = x
        self.y = y
        self.y_def = y
        self.t_jump = 0
        self.stun = 0
        self.time = 0
        self.speed = random.randrange(15, 30)/10
        self.rank = num + 1
        self.GAME = game
        self.distance = 0
        self.amulet_x = 0
        self.IC_STOP = game.load_img("img/ic_amulet" + "1" + ".png", 55, 57)
        self.IC_SLOW = game.load_img("img/ic_amulet" + "2" + ".png", 55, 57)
        self.IC_FAST = game.load_img("img/ic_amulet" + "3" + ".png", 55, 57)
        self.IC_RETURN_START = game.load_img("img/ic_amulet" + "4" + ".png", 55, 57)
        self.IC_TELEPORT = game.load_img("img/ic_amulet" + "5" + ".png", 55, 57)
        self.IC_WIN = game.load_img("img/ic_amulet" + "6" + ".png", 55, 57)
        self.IC_TURNBACK = game.load_img("img/ic_amulet" + "7" + ".png", 55, 57)
        self.IC_SHIELD = game.load_img("img/ic_shield.png", 60, 60)
        self.img_protect= game.load_img("img/ic_protect.png", 100, 100)
        self.IC_STAR = game.load_img("img/ic_star.png", 80, 80)
        self.item_star_amulet = 1
        self.item_shield_amulet = 1
        self.kind=0
        self.exist_shield_amulet = False
        self.exist_star_amulet = False
        self.exist_amulet = False
        self.exist_turn = False
        self.button_shield_amulet = True
        self.pos_rank = self.rank

    def update(self,camera):
        if self.exist_turn==True :
            self.GAME.SCREEN.blit(self.img_turn, (self.x, self.y))
        elif(self.exist_shield_amulet):
            self.GAME.SCREEN.blit(self.img, (self.x, self.y))
            self.GAME.SCREEN.blit(self.img_protect, (self.x - 23*self.GAME.SCALE_X, self.y - 22*self.GAME.SCALE_Y))
        else:
            self.GAME.SCREEN.blit(self.img, (self.x, self.y))
        if self.pos_rank < self.rank:
            self.pos_rank += 0.25
        if self.pos_rank > self.rank:
            self.pos_rank -= 0.25
        if self.x +self.speed + camera.delta >= self.GAME.DISTANCE:
            self.x = self.GAME.DISTANCE
            self.speed = 0
            if self.rank == 1:
                if self.y <= self.y_def:
                    self.y = self.y_def - self.t_jump*self.GAME.GAME_HEIGHT/20 + 9.8*self.t_jump*self.t_jump/2
                    self.t_jump += 0.25
                else:
                    self.t_jump = 0
                    self.y = self.y_def
            return False
        else:
            if self.x + self.speed*self.GAME.SCALE_X + camera.delta <= self.GAME.DISTANCE:
                self.x += self.speed*self.GAME.SCALE_X + camera.delta
            else:
                self.x = self.GAME.DISTANCE
        return True
    def updatespeed(self):
        self.speed = random.randrange(15, 30)/10

class History():
    def __init__(self):
        self.racerType = ""
        self.racerNum = "0"
        self.coinResult = ""
    pass


class Ranking(): #Bang xep hang
    def __init__(self, game, rs):
        self.GAME = game
        self.show_top1 = False
        self.img = self.GAME.IC_RANK
        self.size = self.img.get_rect().size
        self.img = pygame.transform.scale(self.img, (int(self.size[0]*(game.GAME_WIDTH/1280)), int(self.size[1]*(game.GAME_HEIGHT/720))))
        self.size = self.img.get_rect().size
        self.x = game.GAME_WIDTH - self.size[0]
        self.y = 0

    def draw(self, rs):
        m = self.x + int(self.size[0]/2.5)
        n = int(self.size[1]/7.7)
        self.GAME.SCREEN.blit(self.img, (self.x, self.y))
        for i in range(0, 6):
            self.GAME.SCREEN.blit(rs[i].img, (m,self.y + n*(rs[i].pos_rank+0.33)))
        if self.show_top1:
            self.GAME.SCREEN.blit(self.GAME.IC_TOP1, (m, self.y + n))

    def update(self, rs):
        for i in range(0, 6):
            for j in range(0, 6):
                if rs[i].x > rs[j].x and rs[i].rank > rs[j].rank:
                    rs[i].rank, rs[j].rank = rs[j].rank, rs[i].rank
        self.draw(rs)


class User():
    def __init__(self, coin = "100000"):
        self.ID = 0
        self.name = "NULL"
        self.password = "NULL"
        self.winrate = "0"
        self.playTime = "0"
        self.coins = coin
        self.item_shield = 0
        self.use_star=False
    def cloneTo(self,temp_user):
        temp_user.ID = self.ID
        temp_user.name = self.name
        temp_user.password = self.password
        temp_user.winrate = self.winrate
        temp_user.playTime = self.playTime
        temp_user.coins = self.coins
        temp_user.item_shield = self.item_shield
    pass

class Camera():
    def __init__(self, game):
        self.GAME = game
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
        self.GAME.SCREEN.blit(self.GAME.IC_CAMERA[self.anim], (rs.x, rs.y-20))
        if abs(delta) < 2*abs(rs.speed*self.GAME.SCALE_X):
            self.delta = rs.x - self.x
        else:
            if delta == 0:
                self.delta = 0
            else:
                self.delta = rs.speed*(delta/abs(delta))*self.GAME.SCALE_X
        if abs(delta) > 80:
            self.delta = max(abs(delta)/3, 25)*(delta/abs(delta))

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

class Minimap():
    def __init__(self, game):
        self.GAME = game
        self.img_minimap = game.IC_MINIMAP
        self.size = self.img_minimap.get_rect().size
        self.img_b_point = game.IC_POINT_B
        self.size_p = self.img_b_point.get_rect().size
        self.img_r_point = game.IC_POINT_R
        self.img_camera = game.IC_MINIMAP_CAMERA
        self.size_c = self.img_camera.get_rect().size
        self.x = game.GAME_WIDTH/2 - self.size[0]/2
        self.y = game.GAME_HEIGHT/10*9

    def update(self, racers, play_choose, camera_follow):
        self.GAME.SCREEN.blit(self.img_minimap, (self.x, self.y))
        a = self.GAME.GAME_WIDTH/3
        for r in racers:
            if r.num != play_choose:
                x = self.x + self.size[0]*(1 - (self.GAME.DISTANCE - r.x)/(self.GAME.DISTANCE_DEFAULT - a)) - \
                    self.size_p[0]/2
                y = self.y + self.size[1]/2
                self.GAME.SCREEN.blit(self.img_b_point, (x, y))
        for r in racers:
            if r.num == play_choose:
                x = self.x + self.size[0]*(1 - (self.GAME.DISTANCE - r.x)/(self.GAME.DISTANCE_DEFAULT - a)) - \
                    self.size_p[0]/2
                y = self.y + self.size[1]/2
                self.GAME.SCREEN.blit(self.img_r_point, (x, y))
        for r in racers:
            if r.num == camera_follow:
                x = self.x + self.size[0]*(1 - (self.GAME.DISTANCE - r.x)/(self.GAME.DISTANCE_DEFAULT - a)) - \
                    self.size_p[0]/2 - self.size_c[0]/2 + self.size_p[0]/2
                y = self.y + self.size[1]/2 - self.size_c[1]/2 + self.size_p[1]/2
                self.GAME.SCREEN.blit(self.img_camera, (x, y))
    pass
