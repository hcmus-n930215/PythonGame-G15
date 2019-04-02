from libs.global_variables import *
from libs.WARUserData import *
from libs.Widgets import *

import pygame

class LoginPage():

    def __init__(self):
        pygame.init()

        #init screen
        self.INFOR_DISPLAY = pygame.display.Info()
        self.SCREEN_SIZE = (self.INFOR_DISPLAY.current_w, self.INFOR_DISPLAY.current_h)
        self.GAME_WIDTH = int(self.SCREEN_SIZE[1])
        self.GAME_HEIGHT = int(self.GAME_WIDTH / 3 * 2)
        self.screen = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))

        #add img
        self.IC_RACETRACK = pygame.transform.scale(pygame.image.load("img/ic_way.png"), (200,150))
        self.loginForm = pygame.transform.scale(pygame.image.load("img/pg_loginForm.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        self.wrongPass = pygame.transform.scale(pygame.image.load("img/pg_wrongPass.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))
        self.accNotExist = pygame.transform.scale(pygame.image.load("img/pg_notExistAccount.png"), (self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2))

        #add text
        self.userNameInput = TextView(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.5, 10, 10, "Enter your name")
        self.passWordInput = TextView(self.GAME_WIDTH / 2.5, self.GAME_HEIGHT / 2.1, 10, 10, "Enter your password")
        self.signinText = TextView(self.GAME_WIDTH / 3, self.GAME_HEIGHT / 1.656, 10, 10, "Sign in")
        self.signupText = TextView(self.GAME_WIDTH / 1.7, self.GAME_HEIGHT / 1.656, 10, 10, "Sign up")
        self.OKText = Button(self.GAME_WIDTH / 2.05, self.GAME_HEIGHT / 1.8, 10, 10, "OK")

        pass

    def drawLoginPage(self):
        finish = False
        while not finish:

            self.screen.fill(100)
            self.screen.blit(self.loginForm, (self.GAME_WIDTH // 4, self.GAME_HEIGHT // 4))

            self.userNameInput.show()
            self.passWordInput.show()
            self.signinText.show()
            self.signupText.show()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True

            pygame.display.flip()

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

a = LoginPage()
a.drawWrongPassPage()