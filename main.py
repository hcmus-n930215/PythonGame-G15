from libs.global_variables import *
from libs.Widgets import *
from libs.Pages import *
from libs.WARUserData import *
from libs.WARPlayHistory import *
import pygame
import time
import time
import math
import random


#history = []
def show_cusor(startx, starty):
    tv_cusor_X = TextView(startx, starty, 0, 0, "CUSOR X: ")
    tv_cusor_Y = TextView(startx, starty+60, 0, 0, "CUSOR Y: ")
    x, y = pygame.mouse.get_pos()
    tv_cusor_X.setText("CUSOR X: " + str(x))
    tv_cusor_Y.setText("CUSOR Y: " + str(y))
    tv_cusor_X.show()
    tv_cusor_Y.show()

def loginActivity(listUser):
    user = User()
    readSuccess = ReadUsersData.GetAllUsersData(listUser)

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

    #if file is edited
    #if(readSuccess == -1):
        ##warning.setText("You have deleted an important file so all your data is lost")

    if (readSuccess == -2):
        warning.setText("You have edit UsersData file so all your data is deleted")
    
    while True:
        #gameLancher.SCREEN.fill(20)
        #show_cusor(50,300)
        # sign in
        if btn_signin.is_clicked():
            showPass = loginPage.passWordInput.text
            exitCode = -3
            user.name = loginPage.userNameInput.text
            if loginPage.passWordInput.isPassword:
                user.password = loginPage.passWordInput.hidetext
            else:
                user.password = loginPage.passWordInput.text

            if (len(user.name) == 0) | (len(user.password) == 0):
                warning.setText("Please enter your username and password")

            elif len(user.password) != len(showPass):
                warning.setText("Please do not user your numpad to enter password")

            else:
                exitCode = LoginCore.FindUserName(listUser, user)
                if ((exitCode == -1)):
                    warning.setText("Account is not signed up yet.")

                elif ((exitCode == -2)):
                    warning.setText("Password is wrong.")
                else:
                    #print("Dung")
                    # btn_signin.setText("XIN CHAO")
                    # welcome user
                    welcome = "Welcome back " + str(user.name)
                    warning.setText(welcome)

                    # pygame.display.update(btn_signin.rect)
                    time.sleep(0.08)

                    gameLancher.IS_SIGNED_IN = True

                    loginPage.drawLoginPage()
                    pygame.display.flip()
                    return exitCode
        # sign up
        if btn_signup.is_clicked():

            if loginPage.passWordInput.isPassword:
                user.password = loginPage.passWordInput.hidetext
            else:
                user.password = loginPage.passWordInput.text

            showPass = loginPage.passWordInput.text

            user.name = loginPage.userNameInput.text
            if not LoginCore.CheckName(user):
                warning.setText("Your username and password cannot have \" symbol")

            # warning that user numpad to enter pass
            elif len(user.password) != len(showPass):
                warning.setText("Please do not user your numpad to enter password")

            elif len(user.password) < 4:
                warning.setText("Your password must have at least 4 character")

            elif (len(user.name) == 0) | (len(user.password) == 0):
                warning.setText("Please enter your username and password")

            #if account is not exist yet
            elif ((LoginCore.FindUserName(listUser, user) == -1)):

                # welcome user
                welcome = "Welcome " + str(user.name)
                warning.setText(welcome)

                # set ID if list empty
                if (len(listUser) == 0):
                    user.ID = str(100000)
                else:
                    user.ID = str(int(listUser[len(listUser) - 1].ID + 1))
                user.coins = "1000000"
                user.playTime = "0"
                user.winrate = "0"

                listUser.append(user)

                WriteUsersData.WriteAllUsersData(listUser)

                # gameplay
                # btn_signin.setText("XIN CHAO")

                loginPage.drawLoginPage()
                pygame.display.flip()
                return len(listUser) - 1

            else:
                warning.setText("Account is already exist.")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            loginPage.loginHandle(event)
        loginPage.drawLoginPage()

        for box in input_boxes:
            box.draw(gameLancher.SCREEN)

        pygame.display.flip()


def LoadUserHistory(user, history):
    ReadHistoryData.GetAllHistoryData(user.ID, history)
    '''
    i = 0
    while(i < len(history)):
        print(history[i].racerType)
        i += 1
    '''


def main_game(listUser, userIndex, history):
    user = listUser[userIndex]
    timenow = int(round(time.time() * 1000))
    lasttime = timenow

    gameLancher.draw_map(0)

    # main code
    #player = Player()

    racers = gameLancher.assign_racers()

    ranking = Ranking(gameLancher, racers)
    minimap = Minimap(gameLancher)
    camera = Camera(gameLancher)
    mainpage = MainPage(gameLancher)
    settingPage = SettingPage(gameLancher)
    historyPage = HistoryPage(gameLancher)
    shoppage = Shoppage(gameLancher, user)
    finish = False

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
    coin_input = 0
    COUNT_AMULET = 0
    sound_result = False
    time_amulet_appear = 3
    count = 6
    time_amulet = 0
    racer_play_pos = 0
    use_lucky = False
    use_shield = False


    while not finish:



        list_area_to_be_update_display = []

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

        if play and use_shield :
            rc = racers[racer_play_pos]

            if rc.button_shield_amulet :
                # Tạo nút shield
                rc.INFOR_DISPLAY = pygame.display.Info()
                rc.SCREEN_SIZE = (rc.INFOR_DISPLAY.current_w, rc.INFOR_DISPLAY.current_h)
                rc.GAME_WIDTH = int(rc.SCREEN_SIZE[1])
                rc.GAME_HEIGHT = int(rc.GAME_WIDTH / 3 * 2)
                rc.btn_use_shield_amulet = Button(rc.GAME_WIDTH / 2,
                                                    rc.GAME_HEIGHT / 5,
                                                    rc.GAME_WIDTH / 10, rc.GAME_HEIGHT / 10, ' ')
                rc.btn_use_shield_amulet.show()
                rc.game.SCREEN.blit(rc.IC_shield, (rc.GAME_WIDTH / 2,
                                                       rc.GAME_HEIGHT / 5))
            # Xử lí khi nhấp
            if rc.btn_use_shield_amulet.is_clicked():
                rc.button_shield_amulet = False
                rc.exist_shield_amulet = True







            """"# Tạo nút hope
            rc.INFOR_DISPLAY = pygame.display.Info()
            rc.SCREEN_SIZE = (rc.INFOR_DISPLAY.current_w, rc.INFOR_DISPLAY.current_h)
            rc.GAME_WIDTH = int(rc.SCREEN_SIZE[1])
            rc.GAME_HEIGHT = int(rc.GAME_WIDTH / 3 * 2)
            rc.btn_use_hope_amulet = Button(rc.GAME_WIDTH / 2 + 2 * (rc.GAME_WIDTH / 5),
                                              rc.GAME_HEIGHT / 5,
                                              rc.GAME_WIDTH / 10, rc.GAME_HEIGHT / 10, ' ')
            rc.btn_use_hope_amulet.show()
            rc.game.SCREEN.blit(rc.IC_HOPE, (rc.GAME_WIDTH / 2 + 2 * (rc.GAME_WIDTH / 5),
                                                 rc.GAME_HEIGHT / 5 - 10))
            if rc.btn_use_hope_amulet.is_clicked():
                # Xử lí khi nhấp"""









        #if use_shield and used_shield:
            #gameLancher.IC_USED_SHIELD.draw(gameLancher.SCREEN)

        if play and use_lucky:
            rc = racers[racer_play_pos]
            rc.exist_hope_amulet = True
            use_hope=False
            user.use_star = True



        show_cusor(30, 300)
        ###################

        if gameLancher.IS_IN_SHOP:
            shoppage.DrawShop()
            if not isPressed:
                if shoppage.BTN_LUCKY.is_clicked() and not shoppage.use_lucky:
                    shoppage.use_lucky = True
                    if shoppage.use_lucky:
                        user.coins = str(int(user.coins) - shoppage.price_lucky)
                        user.item_lucky = True
                if shoppage.BTN_SHIELD.is_clicked() and not shoppage.use_shield:
                    shoppage.use_shield = True
                    if shoppage.use_shield:
                        user.coins = str(int(user.coins) - shoppage.price_shield)
                        user.item_shield = True
                if shoppage.BTN_BUY.is_clicked() and not shoppage.buy:
                    shoppage.buy = True
                if not shoppage.buy:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit(0)
                        shoppage.add_money.handle_event(event)
                    shoppage.add_money.draw(gameLancher.SCREEN)
                    pygame.display.flip()
                else:
                    shoppage.addmoney = shoppage.add_money.text
                if not shoppage.add and shoppage.buy:
                    user.coins = str(int(shoppage.addmoney) + int(user.coins))
                    print(shoppage.addmoney)
                    print(user.coins)
                    shoppage.add = True
                if shoppage.BTN_BACK.is_clicked():
                    gameLancher.IS_IN_SHOP = False
                isPressed = True
            else:
                isPressed = False
        infoZone = InfoZone(gameLancher, user)
        infoZone.drawInfoZone()
        if gameLancher.IS_IN_SETTINGS:
            settingPage.drawSettingPage()
            if settingPage.btn_setplayer.is_clicked():
                if not isPressed:
                    # gameLancher.IS_SIGNED_IN = False
                    gameLancher.DEFAULT_RACERS_CODE = str(settingPage.drawChooseRacer())
                    gameLancher.update_setting_pref()
                    racers = gameLancher.assign_racers()
                    gameLancher.IS_IN_SETTINGS = True
                    time.sleep(0.08)

                    isPressed = True
            else:
                isPressed = False
            if settingPage.btn_setmap.is_clicked():
                gameLancher.DEFAULT_MAP_CODE = str(settingPage.drawChooseMap())

                gameLancher.update_setting_pref()
                gameLancher.assign_map()
                gameLancher.IS_IN_SETTINGS = True
                time.sleep(0.1)
            if settingPage.btn_modsound.is_clicked():
                gameLancher.DEFAULT_SOUND_CODE = settingPage.drawOptionSound()
                # save DEFAULT_SOUND_CODE  to setting_pref
                gameLancher.update_setting_pref()

                # refresh sound option from setting to main_game
                # create this funtion: gameLancher.assign_sound()
                gameLancher.IS_IN_SETTINGS = True
                time.sleep(0.08)
            if settingPage.btn_back.is_clicked():
                if not isPressed:
                    # gameLancher.IS_SIGNED_IN = False

                    gameLancher.IS_IN_SETTINGS = False
                    time.sleep(0.08)

                    isPressed = True
            else:
                isPressed = False
        ###########################
        if not gameLancher.IS_GAME_PLAYING and not gameLancher.IS_IN_SETTINGS and not gameLancher.IS_IN_HISTORY:
            mainpage.drawMainPage()
            if mainpage.btn_start.is_clicked():
                if not isPressed:
                    if not play:
                        isOK, coin_input, distance, racer_play_pos, use_lucky, use_shield  = mainpage.drawInitStart(user, racers)
                        camera.follow = racer_play_pos
                        if isOK:
                            gameLancher.IS_GAME_PLAYING = True
                            gameLancher.IS_START_OPTIONS = True
                            pygame.mixer.music.load("sound/fast_lane.mp3")
                            pygame.mixer.music.play(-1)
                            gameLancher.DISTANCE = distance
                            gameLancher.DISTANCE_DEFAULT = distance

                        else:
                            coin_input = 0
                        time.sleep(0.08)

                        #mainpage.btn_start.stop()
                    isPressed = True
            else:
                isPressed = False
            if mainpage.btn_logout.is_clicked():
                if not isPressed:
                    if not play:
                        gameLancher.IS_SIGNED_IN = False
                        time.sleep(0.08)
                        play = False
                        user = User()
                        return main()

                    isPressed = True
            else:
                isPressed = False
            if mainpage.btn_setting.is_clicked():
                if not isPressed:
                    if not play:
                        #gameLancher.IS_SIGNED_IN = False
                        gameLancher.IS_IN_SETTINGS = True
                        time.sleep(0.1)
                        play = False


                    isPressed = True
            else:
                isPressed = False
            if mainpage.btn_store.is_clicked():
                if not isPressed:
                    if not play:
                        gameLancher.IS_IN_SHOP = True
                        play = False
                    isPressed = True
            else:
                isPressed = False
            if mainpage.btn_history.is_clicked():
                if not isPressed:
                    if not play:
                        if(len(history) != 0):
                            gameLancher.IS_IN_HISTORY = True
                            historyPage.setHistory(history)
                            time.sleep(0.08)
                            play = False


                    isPressed = True
            else:
                isPressed = False

        ###################E
        if gameLancher.IS_START_OPTIONS:
            play = True
            gameLancher.IS_START_OPTIONS = False


        ###################
        if gameLancher.IS_IN_HISTORY:
            if(len(history) != 0):
                if pygame.key.get_pressed()[pygame.K_UP]:
                    historyPage.Up()
                    time.sleep(0.08)
                    historyPage.setHistory(history)
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    historyPage.Down()
                    time.sleep(0.08)
                    historyPage.setHistory(history)

                if historyPage.btn_back.is_clicked():
                    if not isPressed:
                        # gameLancher.IS_SIGNED_IN = False

                        gameLancher.IS_IN_HISTORY = False
                        time.sleep(0.08)

                        isPressed = True
                else:
                    isPressed = False
                historyPage.draw(history)
        ###################
        #max_speed = 0
        max_racer = 0
        # doan nay chua lam gi ca
        if isScrolling:
            for r in racers:
                if r.x > max_racer:
                    #max_speed = r.speed
                    max_racer = r.x
        isScrolling = False
        last_racer = False
        winner = racers[0]
        for r in racers:
            if play:
                if (time.clock() > time_amulet_appear and COUNT_AMULET < count):
                    if not r.exist_amulet:
                        r.Amulet_appear()
                    COUNT_AMULET += 1

                    if (COUNT_AMULET == count):
                        time_amulet_appear += 8
                        count += 6

                if (r.exist_amulet):
                    if (r.x > r.amulet_x and r.time > 0):
                        r.active()
                        time_amulet = time.clock() + 2
                elif (r.time > 0):
                    if (time.clock() < time_amulet):
                        r.active()
                    else:
                        r.kind = 0
                        r.exist_turn = False

                else:
                    r.kind = 0
                    r.exist_turn = False

                #else:
                #    r.update(camera)

                if r.rank == 1:
                    winner = r
                if r.rank == 6 and r.x >= gameLancher.DISTANCE:
                    last_racer = True

                r.draw_amulet(camera.delta)
                # Kiem tra ket thuc cuoc dua


                isScrolling = r.update(camera) or isScrolling

            # list_area_to_be_update_display.append(r.clear())
            if gameLancher.IS_GAME_PLAYING:
                list_area_to_be_update_display.append(r.draw())
                # Check to show result board
        if last_racer:
            ranking.show_top1 = True
            if ranking.y < gameLancher.GAME_HEIGHT / 3.5:
                ranking.y += 3
            if not sound_result:
                sound_result = True
                # music
                pygame.mixer.music.load("sound/theme_song_cut.mp3")
                pygame.mixer.music.play(-1)
                # /music
                if winner.num == racer_play_pos:
                    sound = pygame.mixer.Sound('sound/win.wav')
                    sound.play()
                else:
                    sound = pygame.mixer.Sound('sound/lose.wav')
                    sound.play()
            #finish = finish_race(gameLancher, winner, racers[3])
        if gameLancher.IS_GAME_PLAYING:
            ranking.update(racers)

            minimap.update(racers, racer_play_pos, camera.follow)
            camera.update(racers[camera.follow])

            if not isScrolling:
                #play = isScrolling
                ranking.show_top1 = True
                if ranking.y < gameLancher.GAME_HEIGHT / 3.5:
                    ranking.y += 3
                coinResult, finish_r, temp_user = finish_race(gameLancher, winner, racers[racer_play_pos], user, coin_input)
                if finish_r:
                    gameLancher.IS_GAME_PLAYING = isScrolling
                    play = isScrolling
                    #user = temp_user
                    listUser[userIndex] = temp_user
                    WriteUsersData.WriteAllUsersData(listUser)
                    # THEM DU LIEU VAO FILE CHO NAY
                    currentPlay = History()
                    currentPlay.racerType = str(gameLancher.DEFAULT_RACERS_CODE) + str(racer_play_pos)

                    currentPlay.coinResult = coinResult

                    history.append(currentPlay)
                    WriteHistoryData.WriteAllHistoryData(user.ID, history)
                    return main_game(listUser, userIndex, history)

                    #gameLancher.IS_START_OPTIONS = True
               #if finish:
                    #return main_game(user)
        #else:

        if play:
            gameLancher.DISTANCE += camera.delta


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

        pygame.display.flip()
        gameLancher.clock.tick(gameLancher.FPS)
        # pygame.display.update(list_area_to_be_update_display)
        # time.sleep(1) # sleep 1 sec

def finish_race(game, racer, player_choose, user, coin_input):
    size = game.IC_RESULT_BOARD.get_rect().size
    game.SCREEN.blit(game.IC_RESULT_BOARD, (game.GAME_WIDTH/2 - size[0]/2, game.GAME_HEIGHT/2 - size[1]/2))
    img_racer = player_choose.img.get_rect().size
    game.SCREEN.blit(pygame.transform.scale(player_choose.img, (int(img_racer[0]*2), int(img_racer[1]*2))),
                     (game.GAME_WIDTH/2 - size[0]/2.5, game.GAME_HEIGHT/2 - size[1]/4))
    size_result = game.IC_WIN.get_rect().size
    last_coin = int(user.coins)
    change_coin= int(coin_input)
    current_coin = int(user.coins)
    if racer.num == player_choose.num:
        game.SCREEN.blit(game.IC_WIN,
                         (game.GAME_WIDTH / 2, game.GAME_HEIGHT / 2 - size[1] / 2.25))
        # set win state include VAT 10%
        if user.use_star:
            change_coin = change_coin*3
        current_coin = str(last_coin+change_coin-change_coin//10)
        last_coin = str(last_coin)
        change_coin = "+" + str(change_coin-change_coin//10)
    else:
        game.SCREEN.blit(game.IC_LOSE,
                         (game.GAME_WIDTH / 2, game.GAME_HEIGHT / 2 - size[1] / 2.25))
        # set lose state
        if user.use_star:
            change_coin = int(change_coin*(0.5))
        current_coin = str(max(last_coin-change_coin, 0))
        change_coin = "-" + str(last_coin-int(current_coin))
        last_coin = str(last_coin)

    list_tv = (Button(game.GAME_WIDTH / 3 - game.GAME_WIDTH / 20, game.GAME_HEIGHT / 2 + game.GAME_HEIGHT / 20*1,
                      0, 0, "LAST COIN: "+ last_coin, color="#FFFFFF"),
               Button(game.GAME_WIDTH / 3 - game.GAME_WIDTH / 20, game.GAME_HEIGHT / 2 + game.GAME_HEIGHT / 20*2,
                      0, 0, "CHANGE: "+ change_coin, color="#FFFFFF"),
               Button(game.GAME_WIDTH / 3 - game.GAME_WIDTH / 20, game.GAME_HEIGHT / 2 + game.GAME_HEIGHT / 20*3,
                      0, 0, "CURRENT COINS: "+current_coin, color="#FFFFFF"))
    for tv in list_tv:
        tv.show()
    gameLancher.btn_end.show()
    gameLancher.btn_play_again.show()

    if gameLancher.btn_end.is_clicked():
        new_user = User()
        user.cloneTo(temp_user=new_user)
        new_user.coins=current_coin
        return change_coin, True, new_user
    if gameLancher.btn_play_again.is_clicked():
        gameLancher.IS_GAME_PLAYING = False
        gameLancher.IS_IN_SETTINGS = False
        gameLancher.IS_IN_HISTORY = False
        new_user = User()
        user.cloneTo(temp_user=new_user)
        new_user.coins = current_coin
        return change_coin, True, new_user
    return change_coin, False, None

def main():
    # music
    pygame.mixer.music.load("sound/theme_song_cut.mp3")
    pygame.mixer.music.play(-1)
    # /music
    user = User()
    #user.ID = "100000"
    listUser = []
    #listUser.append(user)
    userIndex = 0
    if not gameLancher.IS_SIGNED_IN:

        userIndex = loginActivity(listUser)
        user = listUser[userIndex]

        time.sleep(1)

    else:
        listUser.append(user)
    #if not gameLancher.IS_PLAYING:
    #	mainActivity()
    #time.sleep(2)

    history = []
    LoadUserHistory(user, history)
    main_game(listUser, userIndex, history)



gameLancher = INIT_GAME()

main()

pygame.quit()
del gameLancher
exit()