from libs.global_variables import *
from libs.Widgets import *

import pygame

class LoginPage():
    def __init__(self, gameLancher):
        #load gameplay from main
        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()
        self.loginForm = self.GAME.load_img("img/pg_mainpage_no_title.png", -1, self.GAME.GAME_HEIGHT_DEFAULT//2)
        self.rect = self.loginForm.get_rect()
        self.rect.center = (self.GAME.GAME_WIDTH//2, self.GAME.GAME_HEIGHT//2)
        #add text and input
        self.TITLE = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.067, text="LOG IN/SIGN UP", gravity="center")
        self.userNameInput = InputBox(self.rect.x +self.rect.w*0.4, self.rect.y + self.rect.h*0.274, 250*self.GAME.SCALE_X, 50*self.GAME.SCALE_Y)
        self.passWordInput = InputBox(self.rect.x +self.rect.w*0.4, self.rect.y + self.rect.h*0.467, 250*self.GAME.SCALE_X, 50*self.GAME.SCALE_Y)
        self.userNameText = View(self.rect.x +self.rect.w*0.2, self.rect.y + self.rect.h*0.274, text="Username: ", gravity="center_left")
        self.passWordText = View(self.rect.x +self.rect.w*0.2, self.rect.y + self.rect.h*0.467, text="Password: ", gravity="center_left")
        self.btn_signin = View(self.rect.x +self.rect.w*0.2234, self.rect.y + self.rect.h*0.86, "Sign in", gravity="center")
        self.btn_signup = View(self.rect.x +self.rect.w*0.745, self.rect.y + self.rect.h*0.86, "Sign up", gravity="center")
        self.warningText = View(self.rect.x +self.rect.w*0.511, self.rect.y + self.rect.h*0.7, "")
        self.showView = [self.TITLE, self.userNameText, self.passWordText, self.btn_signup, self.btn_signin, self.warningText]
        pass
    def drawLoginPage(self):
        self.SCREEN.blit(self.loginForm, self.rect)
        self.SCREEN.blit(self.GAME.IC_APP_NAME, (self.rect.x + self.rect.w//2 - self.GAME.IC_APP_NAME.get_rect().w//2, 100*self.GAME.SCALE_Y))
        self.userNameInput.draw(self.SCREEN)
        self.passWordInput.draw(self.SCREEN)
        for v in self.showView:
            v.show()
        pass
    def loginHandle(self, event):
        ev_name = self.userNameInput.handle_event(event)
        if ev_name == 0:
            self.warningText.setText("Username is not longer than 10 character")
        elif ev_name == 1:
            self.warningText.setText("")
        ev_pass = self.passWordInput.handle_event(event)
        if ev_pass == 0:
            self.warningText.setText("Password is not longer than 10 character")
        elif ev_pass == 1:
            self.warningText.setText("")

class MainPage():
    def __init__(self, gameLancher):
        #load screen from main
        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()
        self.mainForm = gameLancher.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH_DEFAULT//4, self.GAME.GAME_HEIGHT_DEFAULT//2)
        self.rect = self.mainForm.get_rect()
        self.rect.center = (self.GAME.GAME_WIDTH//2, self.GAME.GAME_HEIGHT//2)
        self.reloadBtn()
        pass

    def reloadBtn(self):
        self.TITLE = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.067, text="MAIN MENU", gravity="center")
        self.btn_start = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.252, "START", gravity="center")
        self.btn_setting = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.412, "SETTING", gravity="center")
        self.btn_history = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.57, "HISTORY", gravity="center")
        self.btn_store = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.73, "SHOP", gravity="center")
        self.btn_logout = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.9, "LOG OUT", gravity="center")
        self.button = (self.btn_start, self.btn_setting,self.btn_store, self.btn_logout, self.btn_history)

    def drawMainPage(self):
        self.SCREEN.blit(self.mainForm, self.rect)
        self.TITLE.show()
        for btn in self.button:
            btn.show()
        pass

    def drawInitStart(self, user, racers):
        self.mainForm = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH_DEFAULT//3*2, self.GAME.GAME_WIDTH_DEFAULT//2)
        self.rect = self.mainForm.get_rect()
        self.rect.center = (self.GAME.GAME_WIDTH//2, self.GAME.GAME_HEIGHT//2)

        TITLE = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.05, text="CONFIGURING INIT", gravity="center")
        btn_save = View(self.rect.x + self.rect.w*0.25 ,self.rect.y+self.rect.h - 20*self.GAME.SCALE_Y, text="LET'S GO!", gravity="mid_bottom")
        btn_back = View(self.rect.x + self.rect.w*0.738 , self.rect.y+self.rect.h - 20*self.GAME.SCALE_Y, text="BACK!", gravity="mid_bottom")
        tv_coin = View(self.rect.x + self.rect.w*0.428, self.rect.y + self.rect.h*0.225, text="Enter coins:", gravity="mid_left")
        tv_distance = View(self.rect.x + self.rect.w*0.428, self.rect.y + self.rect.h*0.35, text="Range of map:", gravity="mid_left")
        ip_coin = InputBox(self.rect.x + self.rect.w*0.77 - 100*self.GAME.SCALE_X, self.rect.y + self.rect.h*0.225 - 25*self.GAME.SCALE_Y,
                           200*self.GAME.SCALE_X, 50*self.GAME.SCALE_Y, "", isdigit=True)
        ip_distance = InputBox(self.rect.x + self.rect.w*0.77 - 100*self.GAME.SCALE_X, self.rect.y + self.rect.h*0.35 - 25*self.GAME.SCALE_Y,
                           200*self.GAME.SCALE_X, 50*self.GAME.SCALE_Y, "", isdigit=True)
        self.warrningText = View(self.rect.x + self.rect.w*0.665, self.rect.y + self.rect.h*0.457, "", gravity="center")
        self.warrningText2 = View(self.rect.x + self.rect.w*0.573, self.rect.y + self.rect.h*0.842, "", gravity="center")
        tv_star = View(self.rect.x + self.rect.w*0.486, self.rect.y + self.rect.h*0.758, text="Star Amulet", gravity="center")
        tv_shield = View(self.rect.x + self.rect.w*0.79, self.rect.y + self.rect.h*0.758, text="Shield", gravity="center")
        list_tv = [tv_coin, tv_distance, self.warrningText, self.warrningText2, tv_shield, tv_star, TITLE, btn_save, btn_back]
        list_ip = [ip_coin, ip_distance]

        list_imgRacer = []
        imgArrow = self.GAME.IC_ARROW
        imgTick = self.GAME.IC_TICK

        imgStar = ImageView(self.GAME, self.rect.x + self.rect.w*0.428, self.rect.y + self.rect.h*0.522, 100, 100, "img/ic_star.png")
        imgShiled = ImageView(self.GAME, self.rect.x + self.rect.w*0.721, self.rect.y + self.rect.h*0.522, 100, 100, "img/ic_shield.png")
        list_imgExtend = [imgStar, imgShiled]
        use_star = False
        use_shield = False

        for i in range(0, 6):
            list_imgRacer.append(ImageView(self.GAME, self.rect.x+self.rect.w*0.075, self.rect.y+self.rect.h*0.215 + (racers[i].img.get_rect().h+14)*i, -1, 60, racers[i].ic_name))
        list_imgRacer[0].setActive(True)
        active_pos = 0

        while True:
            self.SCREEN.blit(self.mainForm, self.rect)
            self.SCREEN.blit(imgArrow, (self.rect.x+self.rect.w*0.075+ list_imgRacer[active_pos].rect.w + 5, self.rect.y+self.rect.h*0.215 +(list_imgRacer[active_pos].rect.h+3)*active_pos))
            for tv in list_tv:
                tv.show()
            for imgE in list_imgExtend:
                imgE.draw(self.SCREEN)
            use_star and self.SCREEN.blit(imgTick, (self.rect.x + self.rect.w*0.54, self.rect.y + self.rect.h*0.509))
            use_shield and self.SCREEN.blit(imgTick, (self.rect.x + self.rect.w*0.831, self.rect.y + self.rect.h*0.509))
            for ip in list_ip:
                ip.draw(self.SCREEN)
            for rc in list_imgRacer:
                rc.draw(self.SCREEN)
                if rc.is_clicked():
                    list_imgRacer[active_pos].setActive(False)
                    active_pos = list_imgRacer.index(rc)
                    rc.setActive(True)
            if imgStar.is_clicked():
                if not use_star and len(str(ip_coin.text)) > 0 and int(ip_coin.text) >= int(user.coins)/2:
                    use_star = not use_star
                    imgStar.setActive(use_star)
                    self.warrningText2.setText("Important: You've choose Star Amulet")
                elif not use_star:
                    self.warrningText2.setText("Can't choose while your bets half less than your coins")
                else:
                    use_star = not use_star
                    imgStar.setActive(use_star)
                    self.warrningText2.setText("")
                time.sleep(0.1)
            if imgShiled.is_clicked():
                if user.item_shield > 0:
                    use_shield = not use_shield
                    imgShiled.setActive(use_shield)
                else:
                    self.warrningText2.setText("You need buy shield in shop")
                time.sleep(0.1)
            if use_star and len(str(ip_coin.text)) > 0 and int(ip_coin.text) < int(user.coins)/2:
                self.warrningText2.setText("Can't chosse while your bets half less than your coins")
                use_star = False
                imgStar.setActive(use_star)
            if btn_back.is_clicked(gameLancher=self.GAME):
                self.mainForm = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH_DEFAULT//4, self.GAME.GAME_HEIGHT_DEFAULT//2)
                self.rect = self.mainForm.get_rect()
                self.rect.center = (self.GAME.GAME_WIDTH//2, self.GAME.GAME_HEIGHT//2)
                return False, None, None, active_pos, False, False
            if btn_save.is_clicked(gameLancher=self.GAME):
                if len((list_ip[0].text))==0 or len((list_ip[1].text))==0:
                    self.warrningText.setText("Please enter data to the box")
                elif int(list_ip[0].text) > int(user.coins):
                    self.warrningText.setText("You've not enough coins")
                elif int(list_ip[1].text) > 9000 or int(list_ip[1].text) < 2500:
                    self.warrningText.setText("Please enter distance between 2500 and 9000")
                else:
                    self.mainForm = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH_DEFAULT//4, self.GAME.GAME_HEIGHT_DEFAULT//2)
                    self.rect = self.mainForm.get_rect()
                    self.rect.center = (self.GAME.GAME_WIDTH//2, self.GAME.GAME_HEIGHT//2)
                    # return coin - distance
                    return True, list_ip[0].text, int(list_ip[1].text), active_pos, use_star, use_shield

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                for box in list_ip:
                    box.handle_event(event)
            pygame.display.flip()
class SettingPage():
    def __init__(self, gameLancher):
        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()
        self.settingForm = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH_DEFAULT//2, self.GAME.GAME_HEIGHT_DEFAULT//2)
        self.rect = self.settingForm.get_rect()
        self.rect.center = (self.GAME.GAME_WIDTH//2, self.GAME.GAME_HEIGHT//2)

        self.TITLE = View(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.0535, text="SETTINGS", gravity="center")
        self.btn_setplayer = View(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.217, text="Choose set of player", gravity="center")
        self.btn_setmap = View(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.4, text="Choose set of map", gravity="center")
        self.btn_modsound = View(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.625, text="Sounds", gravity="center")
        self.btn_back = View(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.8226, text="Back", gravity="center")
        self.button = (self.btn_setplayer, self.btn_setmap, self.btn_back, self.TITLE, self.btn_modsound)

    def drawSettingPage(self):
        self.TITLE.setText("SETTINGS")
        self.SCREEN.blit(self.settingForm, self.rect)
        for btn in self.button:
            btn.show()
        pass
    def drawChooseRacer(self):
        self.TITLE.setText("RACER CHOOSER")
        self.LIST_RC = []
        self.listRacer = ["rc_turtle", "rc_lead", "rc_snail", "rc_parrot", "rc_player"]
        last_active = 0
        btn_save = View(self.rect.x + self.rect.w//2, self.rect.y + self.rect.h - 30*self.GAME.SCALE_X, text="SAVE", gravity="center")
        for i in range(0, len(self.listRacer)):
            self.LIST_RC.append(ImageView(self.GAME, 150*self.GAME.SCALE_X*(i % 3) + self.GAME.GAME_WIDTH/3, 100*self.GAME.SCALE_Y*(i//3) + self.GAME.GAME_HEIGHT/3, 60*self.GAME.SCALE_X, 60*self.GAME.SCALE_Y, "img/" + self.listRacer[i] + "1.png"))
            if self.listRacer[i] == (self.GAME.DEFAULT_RACERS_CODE):
                self.LIST_RC[i].setActive(True)
                last_active = i
        while True:
            self.SCREEN.blit(self.settingForm, self.rect)
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
            if btn_save.is_clicked(gameLancher=self.GAME):
                return self.listRacer[last_active]
            pygame.display.flip()
    def drawChooseMap(self):
        self.TITLE.setText("MAPS CHOOSER")
        self.LIST_BG = []
        last_active = 0
        btn_save = View(self.rect.x + self.rect.w//2, self.rect.y + self.rect.h - 30*self.GAME.SCALE_Y,text="SAVE", gravity="center")
        img_info = []
        # create table of maps element
        row = 2
        collum = 2
        for i in range(0, row):
            for j in range(0, collum):
                fname = "img/Background"+str(i*2+j)+".png"
                try:
                    open(fname, 'r').close()
                    self.LIST_BG.append(ImageView(self.GAME, self.rect.x + self.rect.w*0.15 + (170 + 60)*self.GAME.SCALE_X*j, self.rect.y + self.rect.h*0.18 + (95.625+ 35)*self.GAME.SCALE_Y *i, 170, -1, fname))
                    img_info.append(View(self.rect.x + self.rect.w*0.15 + (170+60)*self.GAME.SCALE_X*j + 170/2*self.GAME.SCALE_X,
                                           self.rect.y + self.rect.h*0.18 + (95.625+35)*self.GAME.SCALE_Y *(i+1) - 35/2*self.GAME.SCALE_Y, "", gravity="center"))
                    if i*2+j == int(self.GAME.DEFAULT_MAP_CODE):
                        self.LIST_BG[i*2+j].setActive(True)
                        last_active = i*2+j
                except FileNotFoundError:
                    break
        img_info[0].setText("Spring")
        img_info[1].setText("The winter")
        img_info[2].setText("Summer vacation")
        img_info[3].setText("The Autumn")
        while True:
            self.SCREEN.blit(self.settingForm, self.rect)
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
            if btn_save.is_clicked(self.GAME):
                return last_active
            pygame.display.flip()
    def drawOptionSound(self):
        self.TITLE.setText("SOUND OPTIONS")
        btn_save = View(self.rect.x + self.rect.w//2, self.rect.y + self.rect.h - 30*self.GAME.SCALE_Y, text="SAVE", gravity="center")
        btn_theme = View(self.rect.x + self.rect.w//2, self.rect.y + self.rect.h*(1 - 0.6), text="THEME SONG:", gravity="center")
        btn_racing = View(self.rect.x + self.rect.w//2, self.rect.y + self.rect.h*(1 - 0.5), text="RACING SONG:", gravity="center")
        btn_effect = View(self.rect.x + self.rect.w//2, self.rect.y + self.rect.h*(1 - 0.4), text="EFFECT SOUND:", gravity="center")
        if self.GAME.DEFAULT_SOUND_CODE[0] == 1:
            btn_theme.text += " ON"
        else:
            btn_theme.text += " OFF"
        if self.GAME.DEFAULT_SOUND_CODE[1] == 1:
            btn_racing.text += " ON"
        else:
            btn_racing.text += " OFF"
        if self.GAME.DEFAULT_SOUND_CODE[2] == 1:
            btn_effect.text += " ON"
        else:
            btn_effect.text += " OFF"
        time.sleep(0.1)
        while True:
            self.SCREEN.blit(self.settingForm, self.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            self.TITLE.show()
            btn_save.show()
            btn_theme.show()
            btn_effect.show()
            btn_racing.show()
            if btn_save.is_clicked(self.GAME):
                return (btn_theme.text == "THEME SONG: ON",
                        btn_racing.text == "RACING SONG: ON",
                        btn_effect.text == "EFFECT SOUND: ON")
            if btn_theme.is_clicked(self.GAME):
                if btn_theme.text == "THEME SONG: ON":
                    btn_theme.text = "THEME SONG: OFF"
                else:
                    btn_theme.text = "THEME SONG: ON"
                time.sleep(0.2)
            if btn_racing.is_clicked(self.GAME):
                if btn_racing.text == "RACING SONG: ON":
                    btn_racing.text = "RACING SONG: OFF"
                else:
                    btn_racing.text = "RACING SONG: ON"
                time.sleep(0.2)
            if btn_effect.is_clicked(self.GAME):
                if btn_effect.text == "EFFECT SOUND: ON":
                    btn_effect.text = "EFFECT SOUND: OFF"
                else:
                    btn_effect.text = "EFFECT SOUND: ON"
                time.sleep(0.2)
            pygame.display.flip()

class InfoZone():
    def __init__(self, gameLancher, user):
        self.GAME = gameLancher
        self.USER = user
        self.SCREEN = pygame.display.get_surface()
        self.player_name = View(60*self.GAME.SCALE_X, 35*self.GAME.SCALE_Y, text=user.name, gravity="center_horizontal")
        self.coin = View(60*self.GAME.SCALE_X, 80*self.GAME.SCALE_Y, text=str(user.coins), gravity="center_horizontal")
        self.rect = pygame.Rect((10*self.GAME.SCALE_X, 10*self.GAME.SCALE_Y),(200*self.GAME.SCALE_X, 70*self.GAME.SCALE_Y))
        pass
    def drawInfoZone(self):
        self.SCREEN.blit(self.GAME.IC_PROFILE, (10*self.GAME.SCALE_X, 10*self.GAME.SCALE_Y))
        self.SCREEN.blit(self.GAME.IC_COIN, (10*self.GAME.SCALE_X, 60*self.GAME.SCALE_Y))
        self.player_name.show()
        self.coin.show()
    def drawInfoZoneExpand(self):
        self.SCREEN.blit(self.GAME.IC_PROFILE, (10*self.GAME.SCALE_X, 10*self.GAME.SCALE_Y))
        self.SCREEN.blit(self.GAME.IC_COIN, (10*self.GAME.SCALE_X, 60*self.GAME.SCALE_Y))
        self.SCREEN.blit(self.GAME.IC_SHIELD_MINI, (20*self.GAME.SCALE_X, 110*self.GAME.SCALE_Y))
        self.SCREEN.blit(self.GAME.IC_PLAYED_TIME, (15*self.GAME.SCALE_X, 150*self.GAME.SCALE_Y))
        self.SCREEN.blit(self.GAME.IC_WINRATE, (15*self.GAME.SCALE_X, 200*self.GAME.SCALE_Y))
        self.shield = View(70*self.GAME.SCALE_X, 125*self.GAME.SCALE_Y, text=str(self.USER.item_shield), gravity="center_horizontal")
        self.playedTime = View(60*self.GAME.SCALE_X, 170*self.GAME.SCALE_Y, text="time played: "+str(self.USER.playTime), gravity="center_horizontal")
        self.winrate = View(60*self.GAME.SCALE_X, 220*self.GAME.SCALE_Y, text="win rate: "+str(self.USER.winrate)+"%", gravity="center_horizontal")
        list = [self.winrate, self.playedTime, self.shield, self.playedTime, self.player_name, self.coin]
        for v in list:
            v.show()
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
class HistoryPage():
    def __init__(self, gameLancher):
        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()
        self.i = 0
        #add img
        self.historyForm = self.GAME.load_img("img/pg_history_board.png", self.GAME.GAME_WIDTH_DEFAULT//2, self.GAME.GAME_HEIGHT_DEFAULT//2)
        self.size = self.historyForm.get_rect().size
        self.scroll = self.GAME.load_img("img/ic_scroll.png", self.size[0]*7/150, -1)
        self.scroll_y = self.GAME.GAME_HEIGHT//4
        self.scroll_y_step = 0
        self.scroll_x = self.GAME.GAME_WIDTH//4 + self.size[0]*(1 - 7/150)
        self.size_scroll = self.scroll.get_rect().size
        #add text
        self.btn_back = View(gameLancher.GAME_WIDTH//2, 520*self.GAME.SCALE_Y, "Back", color="#3ae300", gravity="center")
        self.listRacerTypeText = []
        self.listCoinResultText = []
        i = 0
        while i < 5:
            self.listRacerTypeText.append(gameLancher.load_img("img/rc_snail1.png", -1, 50))
            self.listCoinResultText.append(View(self.GAME.GAME_WIDTH/1.6, self.GAME.GAME_HEIGHT/2.6 + (i + 1)*50*self.GAME.SCALE_Y, color="#FFFFFF"))
            i += 1
        self.typeTitle = View(self.GAME.GAME_WIDTH/3.5, self.GAME.GAME_HEIGHT/2.6, text="Type", color="#FFFFFF")
        self.coinTitle = View(self.GAME.GAME_WIDTH/1.6, self.GAME.GAME_HEIGHT/2.6, text="Result", color="#FFFFFF")

        self.warning = View(self.GAME.GAME_WIDTH//2, self.GAME.GAME_HEIGHT/2.6, text="You have not played yet", color="#FFFFFF", gravity="center")
        pass

    def Up(self):
        self.i -= 1
        self.scroll_y -= self.scroll_y_step

    def Down(self):
        self.i += 1
        self.scroll_y += self.scroll_y_step

    def setHistory(self, history):
        #ensure self.i is valid
        if (self.i < 0):
            self.i = 0
            self.scroll_y += self.scroll_y_step
        elif self.i + 2 >= len(history):
            self.i = max(len(history) - 3, 0)
            self.scroll_y -= self.scroll_y_step
            # set len of scroll
        len_h = len(history) - 2
        if len_h <= 0:
            len_h = 1
        self.scroll = pygame.transform.scale(self.scroll, (self.size_scroll[0], int(self.size[1]/len_h)))
        self.scroll_y_step = self.size[1]/len_h
        for i in range(0, 3):
            if(i < len(history)):
                self.listRacerTypeText[i] = self.GAME.load_img("img/"+history[len(history) - (self.i + i + 1)].racerType + ".png", -1, 50)
                #self.listRacerNumText[i].setText(history[len(history) - i].racerNum)
                self.listCoinResultText[i].setText(history[len(history) - (self.i + i + 1)].coinResult)

    def draw(self, history):
        self.SCREEN.blit(self.historyForm, (self.GAME.GAME_WIDTH//4, self.GAME.GAME_HEIGHT//4))

        if (len(history) == 0):
            self.warning.show()
            self.btn_back.show()
        else:
            for i in range(0,3):
                if (i < len(history)):
                    self.SCREEN.blit(self.listRacerTypeText[i],(self.GAME.GAME_WIDTH//3.6, self.GAME.GAME_HEIGHT//2.7 + (i + 1)*50*self.GAME.SCALE_Y))
                    self.listCoinResultText[i].show()
            self.coinTitle.show()
            self.typeTitle.show()
            self.btn_back.show()
            # show scroll bar
            self.SCREEN.blit(self.scroll, (self.scroll_x, self.scroll_y))
        pass
class Shoppage():
    def __init__(self, gameLancher,user):
        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()
        self.SHOP = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH_DEFAULT//2,self.GAME.GAME_HEIGHT_DEFAULT//2)
        self.SHIELD = self.GAME.load_img("img/ic_shield.png", self.GAME.GAME_WIDTH_DEFAULT//10, self.GAME.GAME_HEIGHT_DEFAULT//7)
        self.rect = self.SHOP.get_rect()
        self.rect.center = (self.GAME.GAME_WIDTH//2, self.GAME.GAME_HEIGHT//2)
        self.TITLE = View(self.rect.x + self.rect.w*0.5, self.rect.y + self.rect.h*0.0535, text="SHOP", gravity="center")
        self.btn_back = View(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.8226, text="Back", gravity="center")
        self.val_price_shield = 1000
        self.tv_shield = View(self.rect.x +self.rect.w*0.32, self.rect.y + self.rect.h*0.279, "SHIELD", gravity="center_horizontal")
        self.tv_shield_val = View(self.rect.x +self.rect.w*0.32, self.rect.y + self.rect.h*0.455, text="You own: "+str(user.item_shield), gravity="center_horizontal")
        self.price_shield = View(self.rect.x +self.rect.w*0.743, self.rect.y + self.rect.h*0.455, str(self.val_price_shield)+"$")

        self.tv_coin = View(self.rect.x + self.rect.w*0.084, self.rect.y + self.rect.h*0.7, "ADD MONEY", gravity="center_horizontal")
        self.buy_coin = View(self.rect.x + self.rect.w*0.743, self.rect.y + self.rect.h*0.7, "BUY 10000$", gravity="center")
        self.list_view = [self.TITLE, self.btn_back, self.tv_shield_val, self.tv_shield, self.price_shield, self.tv_coin, self.buy_coin]
        pass
    def DrawShop(self, user):
        self.TITLE.setText("SHOP")
        self.tv_shield_val.setText("You own: "+str(user.item_shield))
        self.SCREEN.blit(self.SHOP, self.rect)
        self.SCREEN.blit(self.SHIELD, (self.rect.x + self.rect.w*0.084, self.rect.y + self.rect.h*0.2178))
        if int(user.coins) >= self.val_price_shield:
            self.price_shield.setBackground(gameLancher=self.GAME, img_link="img/S_price1.png")
        else:
            self.price_shield.setBackground(gameLancher=self.GAME, img_link="img/S_price.png")
        self.buy_coin.setBackground(gameLancher=self.GAME, img_link="img/S_price1.png")
        for v in self.list_view:
            v.show()
    pass
