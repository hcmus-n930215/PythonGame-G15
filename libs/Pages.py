from libs.global_variables import *
#from libs.WARUserData import *
from libs.Widgets import *

import time

import pygame

class LoginPage():

    def __init__(self, gameLancher):

        #load screen from main
        self.INFOR_DISPLAY = gameLancher.INFOR_DISPLAY

        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH =  gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT

        self.SCREEN = pygame.display.get_surface()


        #add img
        self.IC_RACETRACK = gameLancher.IC_RACETRACK
        self.loginForm = pygame.transform.scale(pygame.image.load("img/pg_loginForm.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        self.wrongPass = pygame.transform.scale(pygame.image.load("img/pg_wrongPass.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        self.accNotExist = pygame.transform.scale(pygame.image.load("img/pg_notExistAccount.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))

        #add text
        self.userNameInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.6, 100, 50)
        self.passWordInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.1, 100, 50)
        self.btn_signin = Button(self.GAME_WIDTH / 3.2, self.GAME_HEIGHT / 1.656, 100, 100, "Sign in")
        self.btn_signup = Button(self.GAME_WIDTH / 1.75, self.GAME_HEIGHT / 1.656, 100, 100, "Sign up")
        self.OKText = Button(self.GAME_WIDTH / 2.05, self.GAME_HEIGHT / 2.43, 10, 10, "OK")
        self.warningText = Button(self.GAME_WIDTH / 2.9, self.GAME_HEIGHT / 1.9, 100, 100, "")
        pass

    def drawLoginPage(self):
        self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
        self.userNameInput.draw(self.SCREEN)
        self.passWordInput.draw(self.SCREEN)
        self.btn_signin.show()
        self.btn_signup.show()
        self.warningText.show()
        pass

    def drawWrongPassPage(self):
        finish = False
        while not finish:

            self.screen.fill(100)
            self.screen.blit(self.wrongPass, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))

            self.OKText.show()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True

            pygame.display.flip()

        pass

    def drawAccNotExistPage(self):
        finish = False
        while not finish:

            self.screen.fill(100)
            self.screen.blit(self.accNotExist, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))

            self.OKText.show()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True

            pygame.display.flip()

        pass

class MainPage():

    def __init__(self, gameLancher):

        #load screen from main
        self.INFOR_DISPLAY = gameLancher.INFOR_DISPLAY

        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH =  gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT

        self.SCREEN = pygame.display.get_surface()


        #add img
        self.IC_RACETRACK = gameLancher.IC_RACETRACK
        #self.loginForm = gameLancher.load_img("img/pg_loginForm.png", 0.5, 0.5)
        self.loginForm = pygame.transform.scale(pygame.image.load("img/pg_mainpage.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        #self.wrongPass = pygame.transform.scale(pygame.image.load("img/pg_wrongPass.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        #self.accNotExist = pygame.transform.scale(pygame.image.load("img/pg_notExistAccount.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))

        #add text
        #self.userNameInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.6, 100, 50)
        #self.passWordInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.1, 100, 50)

        self.btn_start = Button(gameLancher.GAME_WIDTH // 2, 250, 100, 100, "START")
        self.btn_start.setSurface(gameLancher.SCREEN)
        self.btn_setting = Button(gameLancher.GAME_WIDTH // 2, 350, 100, 100, "SETTING")
        self.btn_exit = Button(gameLancher.GAME_WIDTH // 2, 450, 100, 100, "LOG OUT")
        self.button = (self.btn_start, self.btn_setting, self.btn_exit)
        #self.OKText = Button(self.GAME_WIDTH / 2.05, self.GAME_HEIGHT / 2.43, 10, 10, "OK")
        pass

    def drawMainPage(self):
        self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
        for btn in self.button:
            btn.show()
        pass

class SettingPage():

    def __init__(self, gameLancher):

        #load screen from main
        self.INFOR_DISPLAY = gameLancher.INFOR_DISPLAY

        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH =  gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT

        self.SCREEN = pygame.display.get_surface()


        #add img
        self.IC_RACETRACK = gameLancher.IC_RACETRACK
        #self.loginForm = gameLancher.load_img("img/pg_loginForm.png", 0.5, 0.5)
        self.loginForm = pygame.transform.scale(pygame.image.load("img/pg_mainpage.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        #self.wrongPass = pygame.transform.scale(pygame.image.load("img/pg_wrongPass.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        #self.accNotExist = pygame.transform.scale(pygame.image.load("img/pg_notExistAccount.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))

        #add text
        #self.userNameInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.6, 100, 50)
        #self.passWordInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.1, 100, 50)
        #self.SCREEN.setSurface(gameLancher.SCREEN)

        self.btn_setplayer = Button(gameLancher.GAME_WIDTH // 2-100, 250, 100, 100, "Choose set of player")
        self.btn_setmap = Button(gameLancher.GAME_WIDTH // 2-100, 350, 100, 100, "Choose set of map")
        self.btn_back = Button(gameLancher.GAME_WIDTH // 2-100, 450, 100, 100, "Back")
        self.button = (self.btn_setplayer, self.btn_setmap, self.btn_back)
        #self.OKText = Button(self.GAME_WIDTH / 2.05, self.GAME_HEIGHT / 2.43, 10, 10, "OK")
        pass

    def drawSettingPage(self):
        self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
        for btn in self.button:
            btn.show()
        pass

class InfoZone():

    def __init__(self, gameLancher, user):

        #load screen from main
        self.INFOR_DISPLAY = gameLancher.INFOR_DISPLAY

        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH =  gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT
        self.USER = user
        self.SCREEN = pygame.display.get_surface()


        #add img
        self.IC_PLAYER = gameLancher.load_img("img/ic_profile1.png", 40, 40)
        self.IC_COIN = gameLancher.load_img("img/ic_coin.png", 40, 40)
        #self.loginForm = gameLancher.load_img("img/pg_loginForm.png", 0.5, 0.5)
        
        #self.wrongPass = pygame.transform.scale(pygame.image.load("img/pg_wrongPass.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        #self.accNotExist = pygame.transform.scale(pygame.image.load("img/pg_notExistAccount.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))

        #add text
        #self.userNameInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.6, 100, 50)
        #self.passWordInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.1, 100, 50)
		
        self.player_icon = Button(10, 5, 40, 40, "START")
        self.coin_icon = Button(10, 105, 100, 40, "START")
        #self.btn_start.setSurface(gameLancher.SCREEN)
        self.player_name = Button(60, 10, 30, 40, user.name)
        self.coin = Button(50, 60, 30, 40, str(user.coins))
        #self.button = (self.btn_start, self.btn_setting, self.btn_exit)
        #self.OKText = Button(self.GAME_WIDTH / 2.05, self.GAME_HEIGHT / 2.43, 10, 10, "OK")
        pass

    def drawInfoZone(self):
        self.SCREEN.blit(self.IC_PLAYER, (10, 10))
        self.SCREEN.blit(self.IC_COIN, (10, 60))
        self.player_name.show()
        self.coin.show()

class SelectRacerType():
    def __init__(self, gameLancher):
        #load screen from main
        self.INFOR_DISPLAY = gameLancher.INFOR_DISPLAY

        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH =  gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT
        self.game = gameLancher

        self.SCREEN = pygame.display.get_surface()


        #add img
        self.IC_RACETRACK = gameLancher.IC_RACETRACK
        self.selectRacerForm = pygame.transform.scale(pygame.image.load("img/pg_selectRacer.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        self.selectBG = pygame.transform.scale(pygame.image.load("img/bg_racerCurrent.png"), (60, 60))
        self.current = 0        #possion of choose racer
        self.listRacer = ["rc_turtle", "rc_lead", "rc_catus", "rc_snail"]
        self.listRacerImg = []
        img = ""
        i = 0
        while i < len(self.listRacer):
            img = "img/" + str(self.listRacer[i] + "1") + ".png"
            self.listRacerImg.append(pygame.transform.scale(pygame.image.load(img), (60, 60)))
            i += 1


        #add text
        self.introText = TextView(self.GAME_WIDTH / 3.2, self.GAME_HEIGHT / 1.8, 100, 100, "Use W, A, S, D to move, Enter to choose")

    def draw(self):
        self.SCREEN.blit(self.selectRacerForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
        self.introText.show()
        self.game.SCREEN.blit(self.selectBG, (150 * (self.current % 3) +  self.GAME_WIDTH / 3, 100 * (self.current // 3) + self.GAME_HEIGHT / 3))
        

        i = 0
        while i < len(self.listRacerImg):
            self.game.SCREEN.blit(self.listRacerImg[i], (150 * (i % 3) +  self.GAME_WIDTH / 3, 100 * (i // 3) + self.GAME_HEIGHT / 3))
            i += 1

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True

        pygame.display.flip()
        pass
        
    def update(self):
        
        pygame.key.get_pressed()
        if pygame.key.get_pressed()[pygame.K_w]:
            if(self.current > 2):
                self.current-= 3
            time.sleep(0.08)
        if pygame.key.get_pressed()[pygame.K_a]:
            if(self.current % 3 > 0):
                self.current-= 1
            time.sleep(0.08)
        if pygame.key.get_pressed()[pygame.K_s]:
            if(self.current < 3):
                self.current+=3
            time.sleep(0.08)
        if pygame.key.get_pressed()[pygame.K_d]:
            if(self.current % 3 < 2):
                self.current+=1
            time.sleep(0.08)
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            #print(self.listRacer[self.current])
            return self.listRacer[self.current]
        return ""
        