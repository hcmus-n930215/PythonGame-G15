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


for a in listUser:

    print(a.ID)

    print(a.name)

    print(a.password)

    print(a.coins)

    print(a.playTime)

    print(a.winrate)



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

    #if file is edited
    if(readSuccess == -1):
        warning.setText("You have deleted an important file so all your data is lost")

    elif(readSuccess == -2):
        warning.setText("You have edit UsersData file so all your data is deleted")

    while True:
        # sign in
        if btn_signin.is_clicked():

            showPass = loginPage.passWordInput.text

            user.name = loginPage.userNameInput.text
            if loginPage.passWordInput.isPassword:
                user.password = loginPage.passWordInput.hidetext
            else:
                user.password = loginPage.passWordInput.text

            if(len(user.name) == 0) | (len(user.password) == 0):
                warning.setText("Please enter your username and password")

            elif len(user.password) != len(showPass):
                warning.setText("Please do not user your numpad to enter password")

            elif ((LoginCore.FindUserName(listUser, user) == -1)):
                warning.setText("Account is not signed up yet.")

            elif ((LoginCore.FindUserName(listUser, user) == -2)):
                warning.setText("Password is wrong.")
                


            else:
                print("Dung")
                #btn_signin.setText("XIN CHAO")
                #welcome user
                welcome = "Welcome back " + str(user.name) 
                warning.setText(welcome)
                
                #pygame.display.update(btn_signin.rect)
                time.sleep(0.08)
                
                gameLancher.IS_SIGNED_IN = True
                
                loginPage.drawLoginPage()
                pygame.display.flip()
                return
                
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

            #warning that user numpad to enter pass
            elif len(user.password) != len(showPass):
                warning.setText("Please do not user your numpad to enter password")

            elif len(user.password) < 4:
                warning.setText("Your password must have at least 4 character")

            elif(len(user.name) == 0) | (len(user.password) == 0):
                warning.setText("Please enter your username and password")

            #if account is not exist yet
            elif ((LoginCore.FindUserName(listUser, user) == -1)):
                
                #welcome user
                welcome = "Welcome " + str(user.name) 
                warning.setText(welcome)

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
                #btn_signin.setText("XIN CHAO")
                
                loginPage.drawLoginPage()
                pygame.display.flip()

                #pygame.display.update(btn_signin.rect)
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

    racers = (Racer(350, 170 + 0 * 50, gameLancher, "ic_snail", 0),
              Racer(350, 170 + 1 * 50, gameLancher, "ic_snail", 1),
              Racer(350, 170 + 2 * 50, gameLancher, "ic_snail", 2),
              Racer(350, 170 + 3 * 50, gameLancher, "ic_snail", 3),
              Racer(350, 170 + 4 * 50, gameLancher, "ic_snail", 4),
              Racer(350, 170 + 5 * 50, gameLancher, "ic_snail", 5))

    ranking = Ranking(gameLancher, racers)
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
                #print((r.x))
                #print(r.amulet_x)
                if (r.x > r.amulet_x and r.time > 0):
                    r.active()
                #else:
                #    r.update(camera)

                r.draw_amulet(camera.delta)
                if not r.update(camera):
                    max_speed = 0
                    isScrolling = False


            # list_area_to_be_update_display.append(r.clear())
            if gameLancher.IS_GAME_PLAYING:
                list_area_to_be_update_display.append(r.draw())
        if gameLancher.IS_GAME_PLAYING:
            ranking.update(racers)
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

def main():
    if not gameLancher.IS_SIGNED_IN:
        loginActivity()
        
        time.sleep(2)
    #if not gameLancher.IS_PLAYING:
    #	mainActivity()
    #	time.sleep(0.5)
    main_game()



gameLancher = INIT_GAME()
main()
pygame.quit()
del gameLancher
exit()