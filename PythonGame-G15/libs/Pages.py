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
        self.warningText = TextView(self.GAME_WIDTH / 2.2, self.GAME_HEIGHT / 1.9, 100, 100, "")
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


