from libs.global_variables import *
from libs.Widgets import *

import pygame

class LoginPage():
    def __init__(self, gameLancher):
        #load gameplay from main
        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()
        #add img
        self.loginForm = self.GAME.load_img("img/pg_mainpage_no_title.png", -1, self.GAME.GAME_HEIGHT // 2)
        self.rect = self.loginForm.get_rect()
        self.rect.center = (self.GAME.GAME_WIDTH //2, self.GAME.GAME_HEIGHT//2)
        #add text and input
        self.TITLE = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.067, 0, 0, text="LOG IN/SIGN UP", gravity="center")
        self.userNameInput = InputBox(self.rect.x +self.rect.w*0.4, self.rect.y + self.rect.h*0.274, 250, 50)
        self.passWordInput = InputBox(self.rect.x +self.rect.w*0.4, self.rect.y + self.rect.h*0.467, 250, 50)
        self.userNameText = Button(self.rect.x +self.rect.w*0.2, self.rect.y + self.rect.h*0.274, 0, 0, text="Username: ", gravity="center_left")
        self.passWordText = Button(self.rect.x +self.rect.w*0.2, self.rect.y + self.rect.h*0.467, 0, 0, text="Password: ", gravity="center_left")
        self.btn_signin = Button(self.rect.x +self.rect.w*0.2234, self.rect.y + self.rect.h*0.86, 100, 100, "Sign in", gravity="center")
        self.btn_signup = Button(self.rect.x +self.rect.w*0.745, self.rect.y + self.rect.h*0.86, 100, 100, "Sign up", gravity="center")
        self.warningText = Button(self.rect.x +self.rect.w*0.511, self.rect.y + self.rect.h*0.7, 100, 100, "")
        self.showView = [self.TITLE, self.userNameText, self.passWordText, self.btn_signup, self.btn_signin, self.warningText]
        pass
    def drawLoginPage(self):
        self.SCREEN.blit(self.loginForm, self.rect)
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
        self.mainForm = gameLancher.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH // 4, self.GAME.GAME_HEIGHT // 2)
        self.rect = self.mainForm.get_rect()
        self.rect.center = (self.GAME.GAME_WIDTH // 2, self.GAME.GAME_HEIGHT // 2)
        self.reloadBtn()
        pass

    def reloadBtn(self):
        self.TITLE = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.067, 0, 0, text="MAIN MENU",
                            gravity="center")
        self.btn_start = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.252, 100, 100, "START",
                                gravity="center")
        self.btn_setting = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.412, 100, 100,
                                  "SETTING", gravity="center")
        self.btn_history = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.57, 100, 100,
                                  "HISTORY", gravity="center")
        self.btn_store = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.73, 100, 100,
                                  "SHOP", gravity="center")
        self.btn_logout = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.9, 100, 100,
                                 "LOG OUT", gravity="center")
        self.button = (self.btn_start, self.btn_setting,self.btn_store, self.btn_logout, self.btn_history)

    def drawMainPage(self):
        self.SCREEN.blit(self.mainForm, self.rect)
        self.TITLE.show()
        for btn in self.button:
            btn.show()
        pass

    def drawInitStart(self, user, racers):
        self.mainForm = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH // 3 * 2, self.GAME.GAME_WIDTH // 2)
        self.rect = self.mainForm.get_rect()
        # set x, y to rect
        self.rect.center = (self.GAME.GAME_WIDTH // 2, self.GAME.GAME_HEIGHT // 2)
        TITLE = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.05, 0, 0, text="CONFIGURING INIT", gravity="center")
        btn_save = Button(400,self.rect.y+self.rect.h - 20, 100, 100, text="LET'S GO!", gravity="mid_bottom")
        btn_back = Button(700, self.rect.y+self.rect.h - 20, 100, 100, text="BACK!", gravity="mid_bottom")
        tv_coin = Button(self.rect.x + self.rect.w * 0.428, self.rect.y + self.rect.h * 0.225, 0, 0, text="Enter coins:", gravity="mid_left")
        tv_distance = Button(self.rect.x + self.rect.w * 0.428, self.rect.y + self.rect.h * 0.35, 0, 0, text="Range of map:", gravity="mid_left")
        ip_coin = InputBox(self.rect.x + self.rect.w * 0.77 - 100, self.rect.y + self.rect.h * 0.225 - 25, 200, 50, "", isdigit=True)
        ip_distance = InputBox(self.rect.x + self.rect.w * 0.77 - 100, self.rect.y + self.rect.h * 0.35 - 25, 200, 50, "", isdigit=True)
        self.warrningText = Button(self.rect.x + self.rect.w * 0.665, self.rect.y + self.rect.h * 0.457, 0, 0, "", gravity="center")
        self.warrningText2 = Button(self.rect.x + self.rect.w * 0.573, self.rect.y + self.rect.h * 0.842, 0, 0, "", gravity="center")
        tv_lucky = Button(self.rect.x + self.rect.w * 0.486, self.rect.y + self.rect.h * 0.758, 0, 0, text="Lucky Amulet", gravity="center")
        tv_shield = Button(self.rect.x + self.rect.w * 0.79, self.rect.y + self.rect.h * 0.758, 0, 0, text="Shield", gravity="center")
        list_tv = [tv_coin, tv_distance, self.warrningText, self.warrningText2, tv_shield, tv_lucky, TITLE, btn_save, btn_back]
        list_ip = [ip_coin, ip_distance]

        list_imgRacer = []
        imgArrow = self.GAME.IC_ARROW
        imgTick = self.GAME.IC_TICK

        imgLucky = ImageView(self.GAME, self.rect.x + self.rect.w * 0.428, self.rect.y + self.rect.h * 0.522, 100, 100, "img/ic_hope.png")
        imgShiled = ImageView(self.GAME, self.rect.x + self.rect.w * 0.721, self.rect.y + self.rect.h * 0.522, 100, 100, "img/ic_shield.png")
        list_imgExtend = [imgLucky, imgShiled]
        use_lucky = False
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
            use_lucky and self.SCREEN.blit(imgTick, (self.rect.x + self.rect.w * 0.54, self.rect.y + self.rect.h * 0.509))
            use_shield and self.SCREEN.blit(imgTick, (self.rect.x + self.rect.w * 0.831, self.rect.y + self.rect.h * 0.509))
            for ip in list_ip:
                ip.draw(self.SCREEN)
            for rc in list_imgRacer:
                rc.draw(self.SCREEN)
                if rc.is_clicked():
                    list_imgRacer[active_pos].setActive(False)
                    active_pos = list_imgRacer.index(rc)
                    rc.setActive(True)
            if imgLucky.is_clicked():
                if not use_lucky and len(str(ip_coin.text)) > 0 and int(ip_coin.text) >= int(user.coins)/2:
                    use_lucky = not use_lucky
                    imgLucky.setActive(use_lucky)
                    self.warrningText2.setText("Important: You've choose Lucky Amulet")
                elif not use_lucky:
                    self.warrningText2.setText("Can't chosse while your bets half less than your coins")
                else:
                    use_lucky = not use_lucky
                    imgLucky.setActive(use_lucky)
                    self.warrningText2.setText("")
                time.sleep(0.1)


            if imgShiled.is_clicked():
                if user.item_shield > 0:
                    use_shield = not use_shield
                    imgShiled.setActive(use_shield)
                else:
                    self.warrningText2.setText("You need buy shield in shop")
                time.sleep(0.1)
            if use_lucky and len(str(ip_coin.text)) > 0 and int(ip_coin.text) < int(user.coins) / 2:
                self.warrningText2.setText("Can't chosse while your bets half less than your coins")
                use_lucky = False
                imgLucky.setActive(use_lucky)
            if btn_back.is_clicked():
                self.mainForm = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH // 4, self.GAME.GAME_HEIGHT // 2)
                self.rect = self.mainForm.get_rect()
                self.rect.center = (self.GAME.GAME_WIDTH // 2, self.GAME.GAME_HEIGHT // 2)
                return False, None, None, active_pos, False, False
            if btn_save.is_clicked():
                if len((list_ip[0].text))==0 or len((list_ip[1].text))==0:
                    self.warrningText.setText("Please enter data to the box")
                elif int(list_ip[0].text) > int(user.coins):
                    self.warrningText.setText("You've not enough coins")
                elif int(list_ip[1].text) > 9000 or int(list_ip[1].text) < 2500:
                    self.warrningText.setText("Please enter distance between 2500 and 9000")
                else:
                    self.mainForm = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME.GAME_WIDTH // 4, self.GAME.GAME_HEIGHT // 2)
                    self.rect = self.mainForm.get_rect()
                    self.rect.center = (self.GAME.GAME_WIDTH // 2, self.GAME.GAME_HEIGHT // 2)
                    # return coin - distance
                    return True, list_ip[0].text, int(list_ip[1].text), active_pos, use_lucky, use_shield

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                for box in list_ip:
                    box.handle_event(event)
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

        self.settingForm = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME_WIDTH //2, self.GAME_HEIGHT // 2)
        self.rect = self.settingForm.get_rect()
        self.rect.center = (self.GAME_WIDTH //2, self.GAME_HEIGHT//2)

        self.TITLE = Button(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.0535, 0, 0, text="SETTINGS", gravity="center")
        self.btn_setplayer = Button(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.217, 110, 60, text="Choose set of player", gravity="center")
        self.btn_setmap = Button(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.4, 110, 60, text="Choose set of map", gravity="center")
        self.btn_modsound = Button(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.625, 110, 60, text="Sounds", gravity="center")
        self.btn_back = Button(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.8226, 100, 100, text="Back", gravity="center")
        self.button = (self.btn_setplayer, self.btn_setmap, self.btn_back, self.TITLE, self.btn_modsound)

        pass

    def drawSettingPage(self):
        self.TITLE.setText("SETTINGS")
        self.SCREEN.blit(self.settingForm, self.rect)
        for btn in self.button:
            btn.show()
        pass
    def drawChooseRacer(self):
        self.TITLE.setText("RACER CHOOSER")
        self.LIST_RC = []
        self.listRacer = ["rc_turtle", "rc_lead", "rc_snail", "rc_parrot"]
        last_active = 0
        btn_save = Button(self.rect.x + self.rect.w //2, self.rect.y + self.rect.h - 20, 70, 70, text="SAVE", gravity="center")
        img_info = []
        for i in range(0, len(self.listRacer)):

            self.LIST_RC.append(ImageView(self.GAME, 150 * (i % 3) + self.GAME_WIDTH / 3, 100 * (i // 3) + self.GAME_HEIGHT / 3, 60, 60, "img/" + self.listRacer[i] + "1.png"))
            #img_info.append(Button(320 + 230 * i, 400, 0, 0, "btn"))
            if self.listRacer[i] == (self.GAME.DEFAULT_RACERS_CODE):
                self.LIST_RC[i].setActive(True)
                last_active = i

        while True:

            self.SCREEN.blit(self.settingForm, self.rect)
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
        btn_save = Button(self.rect.x + self.rect.w //2, self.rect.y + self.rect.h - 20, 70, 70,text="SAVE", gravity="center")
        img_info = []
        # create table of maps element
        row = 2
        collum = 2
        for i in range(0, row):
            for j in range(0, collum):
                fname = "img/Background"+str(i*2+j)+".png"
                try:
                    f = open(fname, 'r')
                    f.close()
                    self.LIST_BG.append(ImageView(self.GAME, self.rect.x + self.rect.w*0.15 + (170 + 60) * j, self.rect.y + self.rect.h*0.18 + (95.625+ 35) *i, 170, -1, fname))
                    img_info.append(Button(self.rect.x + self.rect.w*0.15 + (170+60) * j + 170/2,
                                           self.rect.y + self.rect.h*0.18 + (95.625+35) *(i+1) - 35/2, 0, 0, "", gravity="center"))
                    if i == int(self.GAME.DEFAULT_MAP_CODE):
                        self.LIST_BG[i].setActive(True)
                        last_active = i
                except FileNotFoundError:
                    break

        img_info[0].setText("Spring")
        img_info[1].setText("The winter")
        img_info[2].setText("Summer vacation")
        while True:

            self.GAME.SCREEN.fill(20)
            show_cusor(20,300)
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
            if btn_save.is_clicked():
                return last_active
            pygame.display.flip()
    def drawOptionSound(self):
        self.TITLE.setText("SOUND OPTIONS")
        btn_save = Button(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h - 20, 70, 70, text="SAVE",
                          gravity="center")

        while True:
            self.GAME.SCREEN.fill(20)
            show_cusor(20,300)
            self.SCREEN.blit(self.settingForm, self.rect)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            self.TITLE.show()
            btn_save.show()
            if btn_save.is_clicked():
                # return something
                return
            pygame.display.flip()


class InfoZone():
    def __init__(self, gameLancher, user):
        self.GAME = gameLancher
        self.USER = user
        self.SCREEN = pygame.display.get_surface()
        self.player_name = Button(60, 35, 0, 0, text=user.name, gravity="center_horizontal")
        self.coin = Button(60, 80, 0, 0, text=str(user.coins), gravity="center_horizontal")
        self.shield = Button(60, 125, 0 , 0, text=str(user.item_shield), gravity="center_horizontal")

        pass
    def drawInfoZone(self):
        self.SCREEN.blit(self.GAME.IC_PROFILE, (10, 10))
        self.SCREEN.blit(self.GAME.IC_COIN, (10, 60))
        self.SCREEN.blit(self.GAME.IC_SHIELD_MINI, (10, 110))
        self.player_name.show()
        self.coin.show()
        self.shield.show()

class HistoryPage():
    def __init__(self, gameLancher):

        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()
        self.i = 0
        #add img
        self.historyForm = self.settingForm = self.GAME.load_img("img/pg_history_board.png", self.GAME.GAME_WIDTH //2, self.GAME.GAME_HEIGHT // 2)
        self.size = self.historyForm.get_rect().size
        self.scroll = self.GAME.load_img("img/ic_scroll.png", self.size[0]*7/150, -1)
        self.scroll_y = self.GAME.GAME_HEIGHT // 4
        self.scroll_y_step = 0
        self.scroll_x = self.GAME.GAME_WIDTH // 4 + self.size[0] * (1 - 7/150)
        self.size_scroll = self.scroll.get_rect().size
        #add text
        self.btn_back = Button(gameLancher.GAME_WIDTH // 2, 500, 100, 100, "Back", color="#3ae300", gravity="center")
        self.listRacerTypeText = []
        self.listCoinResultText = []
        i = 0
        while i < 5:
            self.listRacerTypeText.append(gameLancher.load_img("img/rc_snail1.png", -1, 50))
            self.listCoinResultText.append(TextView(self.GAME.GAME_WIDTH / 1.6, self.GAME.GAME_HEIGHT / 2.6 + (i + 1) * 50, 100, 50, color="#FFFFFF"))
            i += 1
        # set title
        self.typeTitle = TextView(self.GAME.GAME_WIDTH / 3.5, self.GAME.GAME_HEIGHT / 2.6, 100, 50, text="Type", color="#FFFFFF")
        #self.listRacerNumText[0].setText("Number")
        self.coinTitle = TextView(self.GAME.GAME_WIDTH / 1.6, self.GAME.GAME_HEIGHT / 2.6, 100, 50,text="Result", color="#FFFFFF")

        self.warning = TextView(self.GAME.GAME_WIDTH / 3, self.GAME.GAME_HEIGHT / 2.6, 100, 50,text="You have not played yet", color="#FFFFFF")
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
        elif self.i + 2 > len(history):
            self.i = len(history) - 3
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
        self.SCREEN.blit(self.historyForm, (self.GAME.GAME_WIDTH // 4, self.GAME.GAME_HEIGHT // 4))

        if (len(history) == 0):
            self.warning.show()
            self.btn_back.show()
        else:
            for i in range(0,3):
                if (i < len(history)):
                    self.SCREEN.blit(self.listRacerTypeText[i],(self.GAME.GAME_WIDTH // 3.5, self.GAME.GAME_HEIGHT // 2.6 + (i + 1) * 50))
                    self.listCoinResultText[i].show()
            self.coinTitle.show()
            self.typeTitle.show()
            self.btn_back.show()
            # show scroll bar
            self.SCREEN.blit(self.scroll, (self.scroll_x, self.scroll_y))
        pass
class Shoppage():
    def __init__(self, gameLancher,user):
        # load screen from main
        self.INFOR_DISPLAY = gameLancher.INFOR_DISPLAY

        self.SCREEN_SIZE = gameLancher.SCREEN_SIZE
        self.GAME_WIDTH = gameLancher.GAME_WIDTH
        self.GAME_HEIGHT = gameLancher.GAME_HEIGHT
        self.GAME = gameLancher
        self.SCREEN = pygame.display.get_surface()

        self.SHOP = self.GAME.load_img("img/pg_mainpage_no_title.png", self.GAME_WIDTH // 2,self.GAME_HEIGHT // 2)
        self.LUCKY = self.GAME.load_img("img/ic_hope.png", self.GAME_WIDTH//10, self.GAME_HEIGHT//7)
        self.SHIELD = self.GAME.load_img("img/ic_shield.png", self.GAME_WIDTH//10, self.GAME_HEIGHT//7)
        self.PRICE = self.GAME.load_img("img/S_price.png", self.GAME_WIDTH*(5/54), self.GAME_WIDTH*(5/144))
        self.PRICE1 = self.GAME.load_img("img/S_price1.png", self.GAME_WIDTH*(5/54), self.GAME_WIDTH*(5/144))
        self.ADD = self.GAME.load_img("img/S_price.png", self.GAME_WIDTH*(1/9), self.GAME_HEIGHT*(1/18))
        self.ADD1 = self.GAME.load_img("img/S_price1.png", self.GAME_WIDTH*(1/9), self.GAME_HEIGHT*(1/18))
        self.rect = self.SHOP.get_rect()
        self.size_shield = self.SHIELD.get_rect()
        self.size_price = self.PRICE1.get_rect()
        self.rect.center = (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2)

        self.TITLE = Button(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.0535, 0, 0, text="SHOP",
                            gravity="center")
        self.btn_back = Button(self.rect.x +self.rect.w*0.9, self.rect.y + self.rect.h*0.9, 100, 100, text="Back!", gravity="center")
        self.ADD_MONEY = TextView(self.rect.x +self.rect.w*0.5, self.rect.y + self.rect.h*0.65, 0 , 0 ,"ADD MONEY")
        self.BTN_SHIELD = Button(self.rect.x + self.rect.w * 0.5 - self.size_price.w * 0.5,self.rect.y + self.rect.h * 0.45, self.size_price.w, self.size_price.h)
        self.BTN_ADD_MONEY = Button(self.rect.x + self.rect.w * 0.5 - self.size_price.w * 0.5,self.rect.y + self.rect.h * 0.7, self.size_price.w, self.size_price.h)
        self.price_shield = 1000
        self.Price_shield = TextView(self.rect.x + self.rect.w * 0.5 ,self.rect.y + self.rect.h * 0.5, self.size_price.w, self.size_price.h, str(self.price_shield))
        self.MONEY = TextView(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.75, self.size_price.w, self.size_price.h, "+1000")
        pass

    def DrawShop(self):
        self.TITLE.setText("SHOP")
        self.SCREEN.blit(self.SHOP, self.rect)
        self.SCREEN.blit(self.SHIELD, (self.rect.x + self.rect.w * 0.5-self.size_shield.w*0.5, self.rect.y + self.rect.h * 0.15))
        self.SCREEN.blit(self.PRICE1, (self.rect.x + self.rect.w * 0.5-self.size_price.w*0.5, self.rect.y + self.rect.h * 0.45))
        self.SCREEN.blit(self.PRICE1, (self.rect.x + self.rect.w * 0.5 - self.size_price.w * 0.5, self.rect.y + self.rect.h * 0.7))
        self.TITLE.show()
        self.ADD_MONEY.show()
        self.Price_shield.show()
        self.MONEY.show()
        self.btn_back.show()
    def Warning_Text(self):
        self.WARNING = TextView(self.rect.x + self.rect.w * 0.5, self.rect.y + self.rect.h * 0.9, 0, 0, "If your money is less than $1,000")
        self.WARNING.show()
def show_cusor(startx, starty):
    tv_cusor_X = TextView(startx, starty, 0, 0, "CUSOR X: ")
    tv_cusor_Y = TextView(startx, starty+60, 0, 0, "CUSOR Y: ")
    x, y = pygame.mouse.get_pos()
    tv_cusor_X.setText("CUSOR X: " + str(x))
    tv_cusor_Y.setText("CUSOR Y: " + str(y))
    tv_cusor_X.show()
    tv_cusor_Y.show()