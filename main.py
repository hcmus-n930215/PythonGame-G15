from libs.gobal_variables import INIT_GAME , Racer, Amulet, GameController, Player
import pygame
import time
import math
import random

gameLancher = INIT_GAME()

gameLancher.draw_map()

def data_manager():
    """Xu li file, du lieu"""


# main code
player = Player()

racers = (Racer(0, 170+0*50,gameLancher), Racer(0, 170+1*50,gameLancher), Racer(0, 170+2*50,gameLancher),
          Racer(0, 170+3*50,gameLancher), Racer(0, 170+4*50,gameLancher), Racer(0, 170+5*50,gameLancher))

finish = False



while not finish:

    gameLancher.draw_map()
    for r in racers:
        r.update()
        r.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    pygame.display.update()
    gameLancher.clock.tick(gameLancher.FPS)


pygame.quit()
exit()