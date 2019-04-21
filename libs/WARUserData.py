import os
direct = os.getcwd()
#change direction

flag = True
currentDirrect = "\libs"
for i in range(1,len(currentDirrect)+1):
    a = direct[-i]
    b = currentDirrect[-i]
    if direct[-i] != currentDirrect[-i]:
        flag = False
if flag:
    dataDirect = ""
    i = 0
    while(i < len(direct) - len(currentDirrect)):
        dataDirect = dataDirect + direct[i]
        i = i + 1
    os.chdir(dataDirect)

    from global_variables import *
    from decryptData import *
    from encryptdata import *
else:
    from libs.global_variables import *
    from libs.decryptData import *
    from libs.encryptdata import *

#key to encript and decrip      from 1 to 127
key = 125
dataLocation = "data/usersData.txt"
userIDTitle = "ID = \""
nameTitle = "username = \""
passTitle = "password = \""
coinsTitle = "coins = \""
playTimeTitle = "playTime = \""
winrateTitle = "winrate = \""
shieldTitle = "shield = \""
endOfData = "\""    #to define where to stop read data

class ReadUsersData:

    def StringCompare(a, b, startPossOfA):
        i = startPossOfA
        j = 0
        while((i < len(a)) & (j < len(b))):
            if(a[i] != b[j]):
                return False
            i = i + 1
            j = j + 1
        return True

    def StringCopy(src, startPoss):
        if(startPoss < len(src) - 1):
            dest = src[startPoss]
            i = startPoss + 1
            while((src[i] != endOfData)):
                dest = dest + src[i]
                i = i + 1
                if(i == len(src)):
                    break;
            return dest

    def GetUserData(data, startPoss, user):
        i = startPoss
        # get ID
        if (ReadUsersData.StringCompare(data, userIDTitle, i)):
            i = i + len(userIDTitle)
            user.append(User())
            ID = ReadUsersData.StringCopy(data, i)
            if (ID == ""):
                return -1
            user[len(user) - 1].ID = int(ID)
        else:
            return -1
        #get name
        i = i + len(ID) + 2
        if (ReadUsersData.StringCompare(data, nameTitle, i)):
            i = i + len(nameTitle)
            user[len(user) - 1].name = ReadUsersData.StringCopy(data, i)
            if(user[len(user) - 1].name == ""):
                return -1
        else:
            return -1
        #get pass
        i = i + len(user[len(user) - 1].name) + 2    #change poss to pass....
        if (ReadUsersData.StringCompare(data, passTitle, i)):
            i = i + len((passTitle))
            user[len(user) - 1].password = ReadUsersData.StringCopy(data, i)
            if (user[len(user) - 1].password == ""):
                return -1
        else:
            return -1
        #get coins
        i = i + len(user[len(user) - 1].password) + 2    #change poss to coins....
        if (ReadUsersData.StringCompare(data, coinsTitle, i)):
            i = i + len((coinsTitle))
            user[len(user) - 1].coins = ReadUsersData.StringCopy(data, i)
            if (user[len(user) - 1].coins == ""):
                return -1
        else:
            return -1
        #get playtime
        i = i + len(str(user[len(user) - 1].coins)) + 2    #change poss to playtime....
        if (ReadUsersData.StringCompare(data, playTimeTitle, i)):
            i = i + len((playTimeTitle))
            user[len(user) - 1].playTime = ReadUsersData.StringCopy(data, i)
            if (user[len(user) - 1].playTime == ""):
                return -1
        else:
            return -1
        # get winrate
        i = i + len(str(user[len(user) - 1].playTime)) + 2 # change poss to winrate....
        if (ReadUsersData.StringCompare(data, winrateTitle, i)):
            i = i + len((winrateTitle))
            user[len(user) - 1].winrate = ReadUsersData.StringCopy(data, i)
            if (user[len(user) - 1].winrate == ""):
                return -1
        else:
            return -1
        # get shell number
        i = i + len(str(user[len(user) - 1].winrate)) + 2  # change poss to shell....
        if (ReadUsersData.StringCompare(data, shieldTitle, i)):
            i = i + len((shieldTitle))
            shield = ReadUsersData.StringCopy(data, i)
            if(shield == None):
                return -1
            user[len(user) - 1].item_shield = int(shield)
        else:
            return -1
        i = i + len(shield) + 2    #change poss to end of user
        return i

    #ham tra ve -1 neu khong doc duoc
    def  GetAllUsersData(user):
        try:
            f = open(dataLocation, "rt")
        except FileNotFoundError:
            return -1
        data = f.read()
        data = decrypt.DecyptData(data, key)
        dataLength = len(data)
        i = 0
        while(i < dataLength - 20):
            i = ReadUsersData.GetUserData(data, i, user)
            if(i == -1):
                # ERROR
                return -2
    pass

class WriteUsersData:

    def WriteAllUsersData(user):
        f = open(dataLocation, "w")
        i = 0
        textToWrite = ""
        while(i < len(user)):
            textToWrite += userIDTitle + str(user[i].ID) + "\" "
            textToWrite += nameTitle + user[i].name + "\" "
            textToWrite += passTitle + user[i].password + "\" "
            textToWrite += coinsTitle + user[i].coins + "\" "
            textToWrite += playTimeTitle + user[i].playTime + "\" "
            textToWrite += winrateTitle + user[i].winrate + "\" "
            textToWrite += shieldTitle + str(user[i].item_shield) + "\" "
            i = i + 1
        textToWrite = encypt.EncryptData(textToWrite, key)
        f.write(textToWrite)
    pass

class LoginCore:
    def FindUserName(listUser, x):   #return -1 if not exist    -2 if wrong pass    or poss of user in list
        if(len(listUser) == 0):
            return -1
        i = 0
        exist = False
        rightPass = False
        poss = 0
        while i < len(listUser):
            if((ReadUsersData.StringCompare(listUser[i].name, x.name, 0)) & (len(listUser[i].name) == len(x.name))):
                exist = True
                poss = i
                break
            i += 1
        if not exist:
            return -1

        if ((ReadUsersData.StringCompare(listUser[i].password, x.password, 0)) & (len(listUser[i].password) == len(x.password))):
            rightPass = True
        if not rightPass:
            return -2
        return poss

    def CheckName(user):
        i = 0
        while i < len(user.name):
            if(user.name[i] == endOfData):
                return False
            i += 1
        i = 0
        while i < len(user.password):
            if(user.password[i] == endOfData):
                return False
            i += 1
        return True
    pass
