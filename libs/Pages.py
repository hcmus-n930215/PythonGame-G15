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
        self.warningText = Button(self.GAME_WIDTH / 3.1, self.GAME_HEIGHT / 1.9, 100, 100, "")
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
        self.GAME = gameLancher
        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH =  gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT

        self.SCREEN = pygame.display.get_surface()
        self.loginForm = gameLancher.load_img("img/pg_mainpage_no_title.png", -1, self.GAME_HEIGHT // 2)

        self.TITLE = Button(self.GAME_WIDTH // 5 + self.loginForm.get_rect().w//3, self.GAME_HEIGHT // 5 + 20, 0, 0, text="MAIN MENU")
        #add img
        #self.IC_RACETRACK = gameLancher.IC_RACETRACK
        #self.loginForm = gameLancher.load_img("img/pg_loginForm.png", 0.5, 0.5)

        #self.wrongPass = pygame.transform.scale(pygame.image.load("img/pg_wrongPass.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        #self.accNotExist = pygame.transform.scale(pygame.image.load("img/pg_notExistAccount.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))

        #add text
        #self.userNameInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.6, 100, 50)
        #self.passWordInput = InputBox(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.1, 100, 50)
        '''
        self.btn_start = Button(gameLancher.GAME_WIDTH // 2 - 30, 200, 100, 100, "START")
        self.btn_setting = Button(gameLancher.GAME_WIDTH // 2 - 30, 300, 100, 100, "SETTING")
        self.btn_exit = Button(gameLancher.GAME_WIDTH // 2 - 30, 400, 100, 100, "LOG OUT")
        
        
        self.btn_start.setSurface(gameLancher.SCREEN)
        self.button = (self.btn_start, self.btn_setting, self.btn_exit)
        '''
        self.btn_start = Button(gameLancher.GAME_WIDTH // 2, 200, 100, 100, "START")
        self.btn_setting = Button(gameLancher.GAME_WIDTH // 2, 275, 100, 100, "SETTING")
        self.btn_history = Button(gameLancher.GAME_WIDTH // 2, 350, 100, 100, "HISTORY")
        self.btn_exit = Button(gameLancher.GAME_WIDTH // 2, 425, 100, 100, "LOG OUT")
        self.button = (self.btn_start, self.btn_setting, self.btn_exit, self.btn_history)
        self.pos_form = (self.GAME_WIDTH // 5, self.GAME_HEIGHT // 5)
        #self.OKText = Button(self.GAME_WIDTH / 2.05, self.GAME_HEIGHT / 2.43, 10, 10, "OK")
        pass

    def drawMainPage(self):
        self.TITLE.setText("MAIN MENU")
        self.SCREEN.blit(self.loginForm, self.pos_form)
        self.TITLE.show()
        for btn in self.button:
            btn.show()
        pass
    def drawInitStart(self, user, racers):
        self.TITLE.setText("CONFIGURING INIT")

        btn_save = Button(400, 400, 100, 100, "LET'S GO!")
        btn_back = Button(700, 400, 100, 100, "BACK!")
        list_tv = []
        list_ip = []

        for i in range(1,3):
            list_tv.append(Button(self.GAME_WIDTH / 20 * 9 - self.GAME_WIDTH / 20,
                                  self.GAME_HEIGHT / 4 + self.GAME_HEIGHT / 8 * i + 15, 0, 0, ""))
            list_ip.append(InputBox(self.GAME_WIDTH / 20 * 12 - self.GAME_WIDTH / 20,
                                  self.GAME_HEIGHT / 4 + self.GAME_HEIGHT / 8 * i, 200, 50, "", isdigit=True))


        list_tv[0].setText("Enter coins:")
        list_tv[1].setText("Range of map:")
        # add warning text

        list_tv.append(Button(self.GAME_WIDTH / 6 * 2 - self.GAME_WIDTH / 20,
                                  self.GAME_HEIGHT / 4 + self.GAME_HEIGHT / 10 * 3 + 30, 0, 0, ""))
        list_imgRacer = []
        imgArrow = self.GAME.load_img("img/arrow.png", 50, -1)
        for i in range(0, 6):
            list_imgRacer.append(ImageView(self.GAME, self.pos_form[0]+30,
                                           self.pos_form[1]+(racers[i].img.get_rect().h+3)*(i+1)  ,-1,40,
                                           racers[i].ic_name))


        list_imgRacer[0].setActive(True)

        active_pos = 0
        while True:

            self.SCREEN.blit(self.loginForm, (self.GAME_WIDTH // 5, self.GAME_HEIGHT // 5))
            for tv in list_tv:
                tv.show()
            self.SCREEN.blit(imgArrow, (self.pos_form[0]+90,self.pos_form[1]+(racers[active_pos].img.get_rect().h+3)*(active_pos+1)))
            for ip in list_ip:
                ip.draw(self.SCREEN)
            for rc in list_imgRacer:
                rc.draw(self.SCREEN)
                if rc.is_clicked():
                    list_imgRacer[active_pos].setActive(False)
                    active_pos = list_imgRacer.index(rc)
                    rc.setActive(True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                for box in list_ip:
                    box.handle_event(event)

            self.TITLE.show()
            btn_save.show()
            btn_back.show()
            if btn_back.is_clicked():
                return False, None, None, active_pos
            if btn_save.is_clicked():
                if len((list_ip[0].text))==0 or len((list_ip[1].text))==0:
                    list_tv[2].setText("Please enter data to the box")
                    continue
                if int(list_ip[0].text) > int(user.coins):
                    list_tv[2].setText("You've not enough coins")
                    continue
                if int(list_ip[1].text) > 7000 or int(list_ip[1].text) < 1000:
                    list_tv[2].setText("Please enter distance between 1000 and 7000")
                    continue
                # return coin - distance
                return True, list_ip[0].text, int(list_ip[1].text), active_pos
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

            self.LIST_RC.append(ImageView(self.GAME, 150 * (i % 3) + self.GAME_WIDTH / 3, 100 * (i // 3) + self.GAME_HEIGHT / 3, 60, 60, "img/" + self.listRacer[i] + "1.png"))
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

            self.LIST_BG.append(ImageView(self.GAME, 320+230*i,250,0.1,0.1, "img/Background"+str(i)+".png"))
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


class HistoryPage():
    def __init__(self, gameLancher):

        #load screen from main
        self.INFOR_DISPLAY = gameLancher.INFOR_DISPLAY

        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH =  gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT
        self.game = gameLancher
        self.SCREEN = pygame.display.get_surface()
        self.i = 0

        #add img

        self.historyForm = pygame.transform.scale(pygame.image.load("img/pg_history_board.png").convert_alpha(),
                                                  (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        self.size = self.historyForm.get_rect().size
        self.scroll = self.game.load_img("img/ic_scroll.png", self.size[0]*7/150, -1)
        self.scroll_y = self.GAME_HEIGHT // 4
        self.scroll_y_step = 0
        self.scroll_x = self.GAME_WIDTH // 4 + self.size[0] * (1 - 7/150)
        self.size_scroll = self.scroll.get_rect().size

        #add text
        self.btn_back = Button(gameLancher.GAME_WIDTH // 2-100, 450, 100, 100, "Back")

        self.listRacerTypeText = []
        #self.listRacerNumText = []
        self.listCoinResultText = []
        i = 0
        while i < 5:
            self.listRacerTypeText.append(gameLancher.load_img("img/rc_snail1.png", -1, 50))
            self.listCoinResultText.append(TextView(self.GAME_WIDTH / 1.6, self.GAME_HEIGHT / 2.6 + (i + 1) * 50, 100, 50, color="#FFFFFF"))
            i += 1
        # set title
        self.typeTitle = TextView(self.GAME_WIDTH / 3.5, self.GAME_HEIGHT / 2.6, 100, 50, text="Type", color="#FFFFFF")
        #self.listRacerNumText[0].setText("Number")
        self.coinTitle = TextView(self.GAME_WIDTH / 1.6, self.GAME_HEIGHT / 2.6, 100, 50,text="Result", color="#FFFFFF")

        pass

    def Up(self):
        self.i -= 1
        self.scroll_y -= self.scroll_y_step

    def Down(self):
        self.i += 1
        self.scroll_y += self.scroll_y_step


    def setHistory(self, history):

        #ensure self.i is valid
        if(self.i < 0):
            self.i = 0
            self.scroll_y += self.scroll_y_step
        elif self.i >= len(history):
            self.i = len(history) - 1
            self.scroll_y -= self.scroll_y_step
        # set len of scroll
        len_h = len(history)
        if len_h <= 0:
            len_h = 1
        self.scroll = pygame.transform.scale(self.scroll, (self.size_scroll[0], int(self.size[1]/len_h)))

        self.scroll_y_step = self.size[1]/len_h


        for i in range(0, 3):
            if(i < len(history)):
                self.listRacerTypeText[i] = self.game.load_img("img/"+history[len(history) - (self.i + i + 1)].racerType + ".png", -1, 50)
                #self.listRacerNumText[i].setText(history[len(history) - i].racerNum)
                self.listCoinResultText[i].setText(history[len(history) - (self.i + i + 1)].coinResult)


    def draw(self, history):
        self.SCREEN.blit(self.historyForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))
        for i in range(0,3):
            if (i < len(history)):
                self.SCREEN.blit(self.listRacerTypeText[i],(self.GAME_WIDTH // 3.5, self.GAME_HEIGHT // 2.6 + (i + 1) * 50))
                self.listCoinResultText[i].show()
        self.coinTitle.show()
        self.typeTitle.show()
        self.btn_back.show()
        # show scroll bar
        self.SCREEN.blit(self.scroll, (self.scroll_x, self.scroll_y))
        # pygame.display.flip()
        pass

        