from libs.global_variables import *
from libs.Widgets import *
import pygame
import time
import time
import math
import random

def main():
    timenow = int(round(time.time() * 1000))
    lasttime = timenow
    gameLancher.draw_map(0)

    # main code
    player = Player()

    racers = (Racer(0, 170 + 0 * 50, gameLancher, "ic_snail", 0),
              Racer(0, 170 + 1 * 50, gameLancher, "ic_snail", 1),
              Racer(0, 170 + 2 * 50, gameLancher, "ic_snail", 2),
              Racer(0, 170 + 3 * 50, gameLancher, "ic_snail", 3),
              Racer(0, 170 + 4 * 50, gameLancher, "ic_snail", 4),
              Racer(0, 170 + 5 * 50, gameLancher, "ic_snail", 5))

    ranking = Ranking(gameLancher, racers)
    finish = False

    btn = Button(400, 200, 100, 100, "START")

    tv_cusor_X = TextView(200, 200, 100, 50, "CUSOR X: ")
    tv_cusor_Y = TextView(200, 300, 100, 50, "CUSOR Y: ")
    tv_data = TextView(200, 400, 100, 50)

    subScreen = btn.setSurface(gameLancher.SCREEN)

    play = False
    isPressed = False
    rollback = 0
    list_area_to_be_update_display = []
    gameLancher.draw_map(0)

    pygame.display.flip()
    time_count = 0
    while not finish:
        list_area_to_be_update_display = []
        # gameLancher.SCREEN.fill(180)
        ###########################
        timenow = int(round(time.time() * 1000))

        if timenow-lasttime> gameLancher.TIME_INTERVAL:
            # Xu ly giao dien sau moi Frame (FPS) (draw lai giao dien o dong #57-58
            time_count+=gameLancher.TIME_INTERVAL
            if time_count > 2000:
                # Xu ly su kien sau moi 2 giay (thay doi toc do racer)
                time_count-=2000
                for r in racers:
                    r.updatespeed()
            if play:
                rollback -= gameLancher.ROLLBACK_STEP
            gameLancher.draw_map(rollback)

        ###########################
        btn.show()
        x, y = pygame.mouse.get_pos()
        tv_cusor_X.setText("CUSOR X: " + str(x))
        tv_cusor_Y.setText("CUSOR Y: " + str(y))

        tv_data.setText(str(gameLancher.SCREEN.get_clip()) + " == ")

        if btn.is_clicked():
            if not isPressed:
                if play:

                    btn.setText("RESUME")
                    play = False
                else:
                    btn.setText("STOP")
                    play = True
                    btn.stop()
                isPressed = True
        else:
            isPressed = False

        if tv_cusor_X.is_clicked():
            tv_cusor_X.setText()
            time.sleep(0.08)
        if play:
            for r in racers:
                r.update()

                list_area_to_be_update_display.append(r.clear())
                list_area_to_be_update_display.append(r.draw())

            ranking.update(racers)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

        pygame.display.flip()
        # pygame.display.update(list_area_to_be_update_display)
        # time.sleep(1) # sleep 1 sec
gameLancher = INIT_GAME()
main()
pygame.quit()
del gameLancher
exit()