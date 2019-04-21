from libs.global_variables import *
from libs.Widgets import *
from libs.Pages import *
from libs.WARUserData import *
from libs.WARPlayHistory import *
import pygame
import time

def show_cusor(startx, starty):
    tv_cusor_X = View(startx, starty, 0, 0, "CUSOR X: ")
    tv_cusor_Y = View(startx, starty + 60, 0, 0, "CUSOR Y: ")
    x, y = pygame.mouse.get_pos()
    tv_cusor_X.setText("CUSOR X: " + str(x))
    tv_cusor_Y.setText("CUSOR Y: " + str(y))
    tv_cusor_X.show()
    tv_cusor_Y.show()


def loginActivity():
    listUser = []
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
    if (readSuccess == -2):
        warning.setText("You have edit UsersData file so all your data is deleted")
        listUser = []
    while True:
        # gameLancher.SCREEN.fill(20)
        # show_cusor(50,300)
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
                    # print("Dung")
                    # btn_signin.setText("XIN CHAO")
                    # welcome user
                    welcome = "Welcome back " + str(user.name)
                    warning.setText(welcome)

                    # pygame.display.update(btn_signin.rect)
                    time.sleep(0.08)

                    gameLancher.IS_SIGNED_IN = True

                    loginPage.drawLoginPage()
                    pygame.display.flip()
                    return exitCode, listUser
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

            # if account is not exist yet
            elif ((LoginCore.FindUserName(listUser, user) == -1)):

                # welcome user
                welcome = "Welcome " + str(user.name)
                warning.setText(welcome)
                user.ID = int(gameLancher.DEFAULT_ACCOUNT_POS)
                gameLancher.DEFAULT_ACCOUNT_POS = str(user.ID + 1)
                gameLancher.update_setting_pref()

                user.coins = "1000000"
                user.playTime = "0"
                user.winrate = "0"

                listUser.append(user)

                WriteUsersData.WriteAllUsersData(listUser)

                # gameplay
                # btn_signin.setText("XIN CHAO")

                loginPage.drawLoginPage()
                pygame.display.flip()
                return len(listUser) - 1, listUser

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

def main_game(listUser, userIndex, history):
    startTime = time.time()
    user = listUser[userIndex]
    timenow = int(round(time.time() * 1000))
    lasttime = timenow
    gameLancher.START_POS = gameLancher.GAME_WIDTH / 3
    racers = gameLancher.assign_racers()
    ranking = Ranking(gameLancher, racers)
    minimap = Minimap(gameLancher)
    camera = Camera(gameLancher)
    mainpage = MainPage(gameLancher)
    settingPage = SettingPage(gameLancher)
    historyPage = HistoryPage(gameLancher)
    shoppage = Shoppage(gameLancher, user)

    finish = False
    play = False
    isPressed = False
    rollback = 100
    gameLancher.draw_map(100) and pygame.display.flip()
    time_count = 2001
    isScrolling = True
    coin_input = 0
    COUNT_AMULET = 0
    sound_result = False
    time_amulet_appear = 3
    count = 6
    time_amulet = 0
    racer_play_pos = 0

    use_star = False
    use_shield = False
    used_shield = False

    while not finish:
        ###########################
        timenow = int(round(time.time() * 1000))
        if timenow - lasttime > gameLancher.TIME_INTERVAL:
            # Xu ly giao dien sau moi Frame (FPS)
            time_count += gameLancher.TIME_INTERVAL
            if time_count > 1000:
                # Xu ly su kien sau moi 1 giay (thay doi toc do racer)
                time_count -= 1000

                for r in racers:
                    r.updatespeed()

            if play:
                rollback += camera.delta

            gameLancher.draw_map(rollback)
        ###########################
        if gameLancher.IS_IN_SHOP:
            shoppage.DrawShop(user)
            if shoppage.price_shield.is_clicked() and int(user.coins) >= shoppage.val_price_shield:
                if not isPressed:
                    user.coins = str(int(user.coins) - shoppage.val_price_shield)
                    user.item_shield += 1
                    listUser[userIndex] = user
                    WriteUsersData.WriteAllUsersData(listUser)
                    time.sleep(0.08)
                    isPressed = True
                else:
                    isPressed = False
            if shoppage.buy_coin.is_clicked():
                if not isPressed:
                    user.coins = str(int(user.coins) + 10000)
                    listUser[userIndex] = user
                    WriteUsersData.WriteAllUsersData(listUser)
                    time.sleep(0.1)
                    isPressed = True
                else:
                    isPressed = False
            if shoppage.btn_back.is_clicked():
                gameLancher.IS_IN_SHOP = False
        infoZone = InfoZone(gameLancher, listUser[userIndex])
        infoZone.drawInfoZoneExpand() if infoZone.is_clicked() else infoZone.drawInfoZone()

        if play and use_shield:
            gameLancher.IC_SHIELD.draw(gameLancher.SCREEN)
            if gameLancher.IC_SHIELD.is_clicked() and not used_shield:
                used_shield = True
                print("SHIELD CLICKED!")

        if use_shield and used_shield:
            racers[racer_play_pos].exist_shield_amulet = True
            use_shield = False

        if play and use_star:
            racers[racer_play_pos].exist_star_amulet = True
            use_star = False
            user.use_star = True

        show_cusor(30, 300)
        ###################
        if gameLancher.IS_IN_SETTINGS:
            settingPage.drawSettingPage()
            if settingPage.btn_setplayer.is_clicked():
                if not isPressed:
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
                if gameLancher.DEFAULT_SOUND_CODE[0]:
                    pygame.mixer.music.load("sound/theme_song_cut.mp3")
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
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
        if not gameLancher.IS_GAME_PLAYING and not gameLancher.IS_IN_SETTINGS and not gameLancher.IS_IN_HISTORY and not gameLancher.IS_IN_SHOP:
            mainpage.drawMainPage()
            if mainpage.btn_start.is_clicked():
                if not isPressed:
                    if not play:
                        isOK, coin_input, distance, racer_play_pos, use_star, use_shield = mainpage.drawInitStart(user,
                                                                                                                   racers)
                        camera.follow = racer_play_pos
                        if isOK:
                            gameLancher.IS_GAME_PLAYING = True
                            play = True
                            pygame.mixer.music.load("sound/fast_lane.mp3")
                            if gameLancher.DEFAULT_SOUND_CODE[1]:
                                pygame.mixer.music.play(-1)
                            gameLancher.DISTANCE = distance
                            gameLancher.DISTANCE_DEFAULT = distance

                            if use_shield:
                                user.item_shield -= 1
                        else:
                            coin_input = 0
                        time.sleep(0.08)
                    isPressed = True
            else:
                isPressed = False
            if mainpage.btn_logout.is_clicked():
                if not isPressed:
                    if not play:
                        listUser[userIndex] = user
                        WriteUsersData.WriteAllUsersData(listUser)
                        gameLancher.IS_SIGNED_IN = False
                        time.sleep(0.08)
                        play = False
                        user = User()
                        return main()
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
            if mainpage.btn_setting.is_clicked():
                if not isPressed:
                    if not play:
                        # gameLancher.IS_SIGNED_IN = False
                        gameLancher.IS_IN_SETTINGS = True
                        time.sleep(0.1)
                        play = False

                    isPressed = True
            else:
                isPressed = False

            if mainpage.btn_history.is_clicked():
                if not play:
                    # if(len(history) != 0):
                    gameLancher.IS_IN_HISTORY = True
                    historyPage.setHistory(history)
                    play = False
        ###################
        if gameLancher.IS_IN_HISTORY:
            if (len(history) != 0):
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
                    gameLancher.IS_IN_HISTORY = False
                    time.sleep(0.08)
                    isPressed = True
            else:
                isPressed = False
            historyPage.draw(history)

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
                    r.exist_star_amulet = False
                if r.rank == 1:
                    winner = r
                if r.rank == 6 and r.x >= gameLancher.DISTANCE:
                    last_racer = True
                r.draw_amulet(camera.delta)
                # Kiem tra ket thuc cuoc dua
                isScrolling = r.update(camera) or isScrolling
        # Check to show shield
        use_shield = use_shield and racers[racer_play_pos].update(camera)
        if gameLancher.IS_GAME_PLAYING:
            ranking.update(racers)
            minimap.update(racers, racer_play_pos, camera.follow)
            camera.update(racers[camera.follow])
            if not isScrolling:
                ranking.show_top1 = True
                if ranking.y < gameLancher.GAME_HEIGHT / 3.5:
                    ranking.y += 3
                coinResult, finish_r, temp_user = finish_race(gameLancher, winner, racers[racer_play_pos], user,
                                                              coin_input)


                if finish_r:
                    gameLancher.IS_GAME_PLAYING = isScrolling
                    play = isScrolling
                    win = 0
                    lose = 0
                    for i in history:
                        if (i.coinResult[0] == '+'):
                            win += 1
                        else:
                            lose += 1
                    if (coinResult[0] == '+'):
                        win += 1
                    else:
                        lose += 1
                    temp_user.winrate = str(int((win / (win + lose)) * 100))
                    user = temp_user
                    listUser[userIndex] = user
                    WriteUsersData.WriteAllUsersData(listUser)
                    # THEM DU LIEU VAO FILE CHO NAY
                    currentPlay = History()
                    currentPlay.racerType = str(gameLancher.DEFAULT_RACERS_CODE) + str(racer_play_pos)
                    currentPlay.coinResult = coinResult
                    history.append(currentPlay)
                    WriteHistoryData.WriteAllHistoryData(user.ID, history)
                    return main_game(listUser, userIndex, history)
        if last_racer:
            ranking.show_top1 = True
            if ranking.y < gameLancher.GAME_HEIGHT / 3.5:
                ranking.y += 3
            if not sound_result:
                sound_result = True
                # music
                pygame.mixer.music.load("sound/all_stop_now.mp3")
                if gameLancher.DEFAULT_SOUND_CODE[0]:
                    pygame.mixer.music.play(-1)
                # /music
                if gameLancher.DEFAULT_SOUND_CODE[2]:
                    if winner.num == racer_play_pos:
                        sound = pygame.mixer.Sound('sound/win.wav')
                        sound.play()
                    else:
                        sound = pygame.mixer.Sound('sound/lose.wav')
                        sound.play()
        if play:
            gameLancher.DISTANCE += camera.delta
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        pygame.display.flip()

def main():
    # music
    if gameLancher.DEFAULT_SOUND_CODE[0]:
        pygame.mixer.music.load("sound/theme_song_cut.mp3")
        pygame.mixer.music.play(-1)
    # /music
    user = User()
    listUser = []
    userIndex = 0
    if not gameLancher.IS_SIGNED_IN:
        userIndex, listUser = loginActivity()
        user = listUser[userIndex]
        time.sleep(1)
    else:
        listUser.append(user)
    history = []
    LoadUserHistory(user, history)
    main_game(listUser, userIndex, history)

def finish_race(game, racer, player_choose, user, coin_input):
    game.SCREEN.blit(game.IC_RESULT_BOARD, resultRect)
    game.SCREEN.blit(player_choose.imgbig, (resultRect.x + resultRect.w*0.3,resultRect.y + resultRect.h*0.3))
    last_coin = int(user.coins)
    change_coin = int(coin_input)
    current_coin = int(user.coins)

    if racer.num == player_choose.num:
        game.SCREEN.blit(game.IC_WIN, (resultRect.x + resultRect.w//2, resultRect.y + resultRect.h*0.2))
        # set win state include VAT 10%
        if user.use_star:
            change_coin = change_coin * 2
        current_coin = str(last_coin + change_coin - change_coin // 10)
        last_coin = str(last_coin)
        change_coin = "+" + str(change_coin - change_coin // 10)
    else:
        game.SCREEN.blit(game.IC_LOSE, (resultRect.x + resultRect.w//2, resultRect.y + resultRect.h*0.2))
        # set lose state
        if user.use_star:
            change_coin = int(change_coin * 1.5)
        current_coin = str(max(last_coin - change_coin, 0))
        change_coin = "-" + str(last_coin - int(current_coin))
        last_coin = str(last_coin)

    game.list_tv[0].setText("LAST COIN: " + last_coin)
    game.list_tv[1].setText("CHANGE: " + change_coin)
    game.list_tv[2].setText("CURRENT COINS: " + current_coin)

    for tv in game.list_tv:
        tv.show()
    gameLancher.btn_end.show()
    gameLancher.btn_play_again.show()

    if gameLancher.btn_end.is_clicked():
        if gameLancher.DEFAULT_SOUND_CODE[0]:
            pygame.mixer.music.load("sound/theme_song_cut.mp3")
            pygame.mixer.music.play(-1)
        new_user = User()
        user.cloneTo(temp_user=new_user)
        new_user.coins = current_coin
        return change_coin, True, new_user
    if gameLancher.btn_play_again.is_clicked():
        if gameLancher.DEFAULT_SOUND_CODE[0]:
            pygame.mixer.music.load("sound/theme_song_cut.mp3")
            pygame.mixer.music.play(-1)
        gameLancher.IS_GAME_PLAYING = False
        gameLancher.IS_IN_SETTINGS = False
        gameLancher.IS_IN_HISTORY = False
        new_user = User()
        user.cloneTo(temp_user=new_user)
        new_user.coins = current_coin
        new_user.playTime = str(int(new_user.playTime)+1)

        return change_coin, True, new_user
    return change_coin, False, None

gameLancher = INIT_GAME()
resultRect = gameLancher.IC_RESULT_BOARD.get_rect()
resultRect.center = (gameLancher.GAME_WIDTH // 2, gameLancher.GAME_HEIGHT//2)


main()

pygame.quit()
del gameLancher
exit()