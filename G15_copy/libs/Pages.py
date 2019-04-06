from libs.global_variables import *
#from libs.WARUserData import *
from libs.Widgets import *

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
        #self.IC_RACETRACK = gameLancher.IC_RACETRACK
        #self.loginForm = gameLancher.load_img("img/pg_loginForm.png", 0.5, 0.5)
        self.loginForm = pygame.transform.scale(pygame.image.load("img/pg_mainpage_no_title.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        #self.wrongPass = pygame.transform.scale(pygame.image.load("img/pg_wrongPass.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        #self.accNotExist = pygame.transform.scale(pygame.image.load("img/pg_notExistAccount.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))

        #add text
        #self.userNameInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.6, 100, 50)
        #self.passWordInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.1, 100, 50)
        self.TITLE = Button(500, 200, 0, 0, "MAIN MENU")
        self.GAME = gameLancher
        self.btn_start = Button(gameLancher.GAME_WIDTH // 2, 250, 100, 100, "START")
        self.btn_start.setSurface(gameLancher.SCREEN)
        self.btn_setting = Button(gameLancher.GAME_WIDTH // 2, 350, 100, 100, "SETTING")
        self.btn_exit = Button(gameLancher.GAME_WIDTH // 2, 450, 100, 100, "LOG OUT")
        self.button = (self.btn_start, self.btn_setting, self.btn_exit)
        #self.OKText = Button(self.GAME_WIDTH / 2.05, self.GAME_HEIGHT / 2.43, 10, 10, "OK")
        pass

    def drawMainPage(self):
        self.TITLE.setText("MAIN MENU")
        self.TITLE.show()
        self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
        for btn in self.button:
            btn.show()
        pass
    def drawInitStart(self, user):
        self.TITLE.setText("CONFIGURING INFO")

        self.tv_in_coin = Button(320,275,0,0,"Enter COIN:")
        self.tv_in_distance = Button(320,350,0,0,"Enter distance of race:")
        self.IP_COIN = InputBox(550, 250, 200, 50, "")
        self.IP_DISTANCE = InputBox(550, 325, 200, 50, "")
        self.input_boxes = [self.IP_DISTANCE, self.IP_COIN]
        self.tv_warrning = Button(350,450,0,0,"")
        for box in self.input_boxes:
            box.isDigit = True
        btn_save = Button(500,450,100,100,"Let's go!")

        while True:

            self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
            self.tv_in_coin.show()
            self.tv_in_distance.show()
            self.IP_COIN.draw(self.SCREEN)
            self.IP_DISTANCE.draw(self.SCREEN)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                for box in self.input_boxes:
                    box.handle_event(event)
            self.TITLE.show()
            self.tv_warrning.show()
            btn_save.show()
            if btn_save.is_clicked():
                if len(self.IP_COIN.text) == 0 or len(self.IP_DISTANCE.text) == 0:
                    self.tv_warrning.setText("Please enter all field data")
                    continue
                if int(self.IP_COIN.text) > int(user.coins):
                    self.tv_warrning.setText("You've not enough coins")
                    continue
                if int(self.IP_DISTANCE.text) < 1000 or int(self.IP_DISTANCE.text) > 5000:
                    self.tv_warrning.setText("Warning: Distance is between 1000m and 5000m")
                    continue
                # checksomething here
                return int(self.IP_COIN.text), int(self.IP_DISTANCE.text)
            pygame.display.flip()

class SettingPage():

    def __init__(self, gameLancher):

        #load screen from main
        self.INFOR_DISPLAY = gameLancher.INFOR_DISPLAY

        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH =  gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT
        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()
        self.TITLE = Button(500,200,0,0,"SETTINGS")
        self.loginForm = pygame.transform.scale(pygame.image.load("img/pg_mainpage_no_title.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))


        self.btn_setplayer = Button(gameLancher.GAME_WIDTH // 2-100, 250, 110, 60, "Choose set of player")
        self.btn_setmap = Button(gameLancher.GAME_WIDTH // 2-100, 350, 110, 60, "Choose set of map")
        self.btn_back = Button(gameLancher.GAME_WIDTH // 2-100, 450, 100, 100, "Back")
        self.button = (self.btn_setplayer, self.btn_setmap, self.btn_back, self.TITLE)
        #self.OKText = Button(self.GAME_WIDTH / 2.05, self.GAME_HEIGHT / 2.43, 10, 10, "OK")
        pass

    def drawSettingPage(self):
        self.TITLE.setText("SETTINGS")
        self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
        for btn in self.button:
            btn.show()
        pass
    def drawChooseRacer(self):
        self.TITLE.setText("RACER CHOOSER")
        self.LIST_RC = []
        self.listRacer = ["rc_turtle", "rc_lead", "rc_catus", "rc_snail"]
        last_active = 0
        btn_save = Button(500, 450, 100, 100, "SAVE")
        img_info = []
        for i in range(0, 4):

            self.LIST_RC.append(ImageView(150 * (i % 3) + self.GAME_WIDTH / 3, 100 * (i // 3) + self.GAME_HEIGHT / 3, 60, 60, "img/" + self.listRacer[i] + "1.png"))
            #img_info.append(Button(320 + 230 * i, 400, 0, 0, "btn"))
            if self.listRacer[i] == (self.GAME.DEFAULT_RACERS_CODE):
                self.LIST_RC[i].setActive(True)
                last_active = i
        #img_info[0].setText("Summer vacation")
        #img_info[1].setText("The winter")
        while True:

            self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
            #for info in img_info:
            #    info.show()
            for rc in self.LIST_RC:
                rc.draw(self.SCREEN)

                if rc.is_clicked():
                    self.LIST_RC[last_active].setActive(False)
                    last_active = self.LIST_RC.index(rc)
                    self.LIST_RC[last_active].setActive(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            self.TITLE.show()

            btn_save.show()
            if btn_save.is_clicked():
                return self.listRacer[last_active]
            pygame.display.flip()

    def drawChooseMap(self):
        self.TITLE.setText("MAPS CHOOSER")
        self.LIST_BG = []
        last_active = 0
        btn_save = Button(500,450,100,100,"SAVE")
        img_info = []
        for i in range(0,2):

            self.LIST_BG.append(ImageView(320+230*i,250,0.1,0.1, "img/Background"+str(i)+".png"))
            img_info.append(Button(320+230*i,400,0,0,"btn"))
            if i == int(self.GAME.DEFAULT_MAP_CODE):
                self.LIST_BG[i].setActive(True)
                last_active = i
        img_info[0].setText("Summer vacation")
        img_info[1].setText("The winter")
        while True:

            self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
            for info in img_info:
                info.show()
            for bg in self.LIST_BG:
                bg.draw(self.SCREEN)


                if bg.is_clicked():
                    self.LIST_BG[last_active].setActive(False)
                    last_active = self.LIST_BG.index(bg)
                    self.LIST_BG[last_active].setActive(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            self.TITLE.show()
            btn_save.show()
            if btn_save.is_clicked():
                return last_active
            pygame.display.flip()

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


        