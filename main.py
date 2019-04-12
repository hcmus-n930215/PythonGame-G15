from libs.global_variables import *
from libs.Widgets import *
from libs.Pages import *
from libs.WARUserData import *
import pygame
import time
import time
import math
import random



listUser = []

readSuccess = ReadUsersData.GetAllUsersData(listUser)

user = User()
"""
for a in listUser:

    print(a.ID)

    print(a.name)

    print(a.password)

    print(a.coins)

    print(a.playTime)

    print(a.winrate)
"""


def loginActivity():
    gameLancher.draw_map(2)
    loginPage = LoginPage(gameLancher)
    loginPage.drawLoginPage()
    btn_signin = loginPage.btn_signin
    btn_signup = loginPage.btn_signup
    warning = loginPage.warningText
    pygame.display.flip()
    loginPage.passWordInput.isPassword = True
    input_boxes = [loginPage.userNameInput, loginPage.passWordInput]

    NoneClick = True

    while True:
        
        #if file is edited
        if(readSuccess == -1):
            warning.setText("You have deleted an important file so all your data is lost")

        elif(readSuccess == -2):
            warning.setText("You have edit UsersData file so all your data is deleted")

        # sign in
        if btn_signin.is_clicked():


            user.name = loginPage.userNameInput.text
            if loginPage.passWordInput.isPassword:
                user.password = loginPage.passWordInput.hidetext
            else:
                user.password = loginPage.passWordInput.text

            if(len(user.name) == 0) | (len(user.password) == 0):
                warning.setText("Please enter your username and password")

            elif ((LoginCore.FindUserName(listUser, user) == -1)):
                warning.setText("Account is not signed up yet.")

            elif ((LoginCore.FindUserName(listUser, user) == -2)):
                warning.setText("Password is wrong.")


            else:
                print("Dung")
                btn_signin.setText("XIN CHAO")
                pygame.display.update(btn_signin.rect)
                time.sleep(0.08)
                gameLancher.IS_SIGNED_IN = True
                return
        # sign up
        if btn_signup.is_clicked():

            if loginPage.passWordInput.isPassword:
                user.password = loginPage.passWordInput.hidetext
            else:
                user.password = loginPage.passWordInput.text

            user.name = loginPage.userNameInput.text
            if not LoginCore.CheckName(user):
               warning.setText("Your username and password cannot have \" symbol")

            elif len(user.password) < 4:
                warning.setText("Your password must have at least 4 character")

            elif(len(user.name) == 0) | (len(user.password) == 0):
                warning.setText("Please enter your username and password")

            #if account is not exist yet
            elif ((LoginCore.FindUserName(listUser, user) == -1)):

                # set ID if list empty
                if (len(listUser) == 0):
                    user.ID = str(100000)
                else:
                    user.ID = str(int(listUser[len(listUser) - 1].ID + 1))
                user.coins = "100000"
                user.playTime = "0"
                user.winrate = "0"

                listUser.append(user)

                WriteUsersData.WriteAllUsersData(listUser)

                # gameplay
                btn_signin.setText("XIN CHAO")
                pygame.display.update(btn_signin.rect)
                time.sleep(0.08)
                gameLancher.IS_SIGNED_IN = True
                return

            else:
                warning.setText("Account is already exist.")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            for box in input_boxes:
                box.handle_event(event)
        loginPage.drawLoginPage()
        for box in input_boxes:
            box.update()


        #gameLancher.SCREEN.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(gameLancher.SCREEN)

        pygame.display.flip()


def main_game():
    timenow = int(round(time.time() * 1000))
    lasttime = timenow

    gameLancher.draw_map(0)

    # main code
    player = Player()

    h = 260
    k = 60
    s = gameLancher.GAME_WIDTH/3  # newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
    pack = "rc_catus"
    racers = (Racer(s, h + 0 * k, gameLancher, pack, 0),
              Racer(s, h + 1 * k, gameLancher, pack, 1),
              Racer(s, h + 2 * k, gameLancher, pack, 2),
              Racer(s, h + 3 * k, gameLancher, pack, 3),
              Racer(s, h + 4 * k, gameLancher, pack, 4),
              Racer(s, h + 5 * k, gameLancher, pack, 5))

    ranking = Ranking(gameLancher, racers)
    minimap = Minimap(gameLancher) # newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
    camera = Camera(gameLancher)
    mainpage = MainPage(gameLancher)
    finish = False


    tv_cusor_X = TextView(200, 200, 100, 50, "CUSOR X: ")
    tv_cusor_Y = TextView(200, 300, 100, 50, "CUSOR Y: ")
    tv_data = TextView(200, 400, 100, 50)

    #subScreen = []
    #for btn in button:
    #    subScreen.append(btn.setSurface(gameLancher.SCREEN))

    play = False
    isPressed = False
    rollback = 0
    list_area_to_be_update_display = []
    gameLancher.draw_map(0)

    pygame.display.flip()
    time_count = 2001
    max_speed = 0
    isScrolling = True
    COUNT_AMBULET = 0
    sound_result = False    # newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww

    while not finish:

        list_area_to_be_update_display = []
        gameLancher.SCREEN.fill(180)
        ###########################
        timenow = int(round(time.time() * 1000))

        if timenow - lasttime > gameLancher.TIME_INTERVAL:
            # Xu ly giao dien sau moi Frame (FPS) (draw lai giao dien o dong #57-58
            time_count += gameLancher.TIME_INTERVAL
            if time_count > 1000:
                # Xu ly su kien sau moi 2 giay (thay doi toc do racer)
                time_count -= 1000

                for r in racers:
                    r.updatespeed()

            if play:
                # rollback -= gameLancher.ROLLBACK_STEP
                rollback += camera.delta
            gameLancher.draw_map(rollback)

        ###########################
        if not gameLancher.IS_GAME_PLAYING:
            mainpage.drawMainPage()
            if mainpage.btn_start.is_clicked():
                if not isPressed:
                    if play:
                        mainpage.btn_start.setText("RESUME")
                        gameLancher.IS_GAME_PLAYING = False
                        time.sleep(0.08)
                        play = False
                    else:
                        mainpage.btn_start.setText("STOP")
                        gameLancher.IS_GAME_PLAYING = True
                        play = True
                        time.sleep(0.08)
                        mainpage.btn_start.stop()
                        pygame.mixer.music.load("sound/fast_lane.mp3")
                        pygame.mixer.music.play(-1)
                    isPressed = True
            else:
                isPressed = False
            
        ###################E
        max_speed = 0
        max_racer = 0
        if isScrolling:
            for r in racers:
                if r.x > max_racer:
                    max_speed = r.speed
                    max_racer = r.x

        last_racer = False
        winner = racers[0]

        for r in racers:
            if play:
                if (COUNT_AMBULET < 6):
                    r.Amulet_appear()
                    COUNT_AMBULET += 1
                """elif(r.x>1000and  COUNT_AMBULET <12):
                    r.Amulet_appear()
                    COUNT_AMBULET += 1
                elif(r.x>2000and  COUNT_AMBULET <18):
                    r.Amulet_appear()
                    COUNT_AMBULET += 1"""
                # print((r.x))
                # print(r.amulet_x)
                if (r.x > r.amulet_x and r.time > 0):
                    r.active()
                # else:
                #    r.update(camera)

                if r.rank == 1:
                    winner = r
                if r.rank == 6 and r.x >= gameLancher.DISTANCE:
                    last_racer = True



                r.draw_amulet(camera.delta)
                if not r.update(camera):
                    max_speed = 0
                    isScrolling = False


            # list_area_to_be_update_display.append(r.clear())
            if gameLancher.IS_GAME_PLAYING:
                list_area_to_be_update_display.append(r.draw())

        # Check to show result board
        if last_racer:
            ranking.show_top1 = True
            if ranking.y < gameLancher.GAME_HEIGHT/3.5:
                ranking.y += 3

            # newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
            if not sound_result:
                sound_result = True
                if winner.num == racers[3].num :
                    sound = pygame.mixer.Sound('sound/win.wav')
                    sound.play()
                else:
                    sound = pygame.mixer.Sound('sound/lose.wav')
                    sound.play()
            finish = finish_race(gameLancher, winner, racers[3])

        if gameLancher.IS_GAME_PLAYING:
            ranking.update(racers)
            minimap.update(racers, 3, camera.follow) # newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
            camera.update(racers[camera.follow])

        if play:
            gameLancher.DISTANCE += camera.delta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True


        pygame.display.flip()
        gameLancher.clock.tick(gameLancher.FPS)
        # pygame.display.update(list_area_to_be_update_display)
        # time.sleep(1) # sleep 1 sec


def finish_race(game, racer, player_choose):
    size = game.IC_RESULT_BOARD.get_rect().size
    game.SCREEN.blit(game.IC_RESULT_BOARD, (game.GAME_WIDTH/2 - size[0]/2, game.GAME_HEIGHT/2 - size[1]/2))
    img_racer = player_choose.img.get_rect().size
    game.SCREEN.blit(pygame.transform.scale(player_choose.img, (int(img_racer[0]*2), int(img_racer[1]*2))),
                     (game.GAME_WIDTH/2 - size[0]/2.5, game.GAME_HEIGHT/2 - size[1]/4))
    size_result = game.IC_WIN.get_rect().size

    if racer.num == player_choose.num:
        game.SCREEN.blit(game.IC_WIN,
                         (game.GAME_WIDTH / 2, game.GAME_HEIGHT / 2 - size[1] / 2.25))
    else:
        game.SCREEN.blit(game.IC_LOSE,
                         (game.GAME_WIDTH / 2, game.GAME_HEIGHT / 2 - size[1] / 2.25))

    gameLancher.btn_end.show()
    gameLancher.btn_play_again.show()

    if gameLancher.btn_end.is_clicked():
        return True
    if gameLancher.btn_play_again.is_clicked():
        gameLancher.RESTART = True
        return True
    return False


def main():
    # newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
    pygame.mixer.music.load("sound/theme_song_cut.mp3")
    pygame.mixer.music.play(-1)
    if not gameLancher.IS_SIGNED_IN:
        loginActivity()
        time.sleep(1)
    # if not gameLancher.IS_PLAYING:
    #	mainActivity()
    #	time.sleep(0.5)
    main_game()


gameLancher = INIT_GAME()
main()
while gameLancher.RESTART:
    gameLancher.RESTART = False

    gameLancher.IS_GAME_PLAYING = False
    gameLancher.IS_GAME_ENDED = False

    gameLancher.DISTANCE = 3000
    main()

pygame.quit()
del gameLancher

exit()