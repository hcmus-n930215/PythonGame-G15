from libs.global_variables import *
from libs.decryptData import *
from libs.encryptdata import *

import os

#key to encript and decrip      from 1 to 127
key = 125

dataLocation = "data/usersData.txt"

userIDTitle = "ID = \""
nameTitle = "username = \""
passTitle = "password = \""
coinsTitle = "coins = \""
playTimeTitle = "playTime = \""
winrateTitle = "winrate = \""


#change direction
direct = os.getcwd()
currentDirrect = "/libs"
dataDirect = direct[0]

i = 1
while(i < len(direct) - len(currentDirrect)):
    dataDirect = dataDirect + direct[i]
    i = i + 1

os.chdir(dataDirect)
print(dataDirect)

endOfData = "\""    #to define where to stop read data

#create líst
#user = ["buiHuu Duc"]
#password = ["456"]
#coins = ["123"]
#playTime = ["789"]
#winrate =["100"]

#user = []

class ReadUsersData:

    def StringCompare(a, b, startPossOfA):
        i = startPossOfA
        j = 0
        x= len(a)
        y= len(b)
        while((i < len(a)) & (j < len(b))):
            if(a[i] != b[j]):
                #c = a[i]
                #d = a[i+1]
                #u = a[i-1]
                return False
            i = i + 1
            j = j + 1
        return True

    def StringCopy(src, startPoss):
        if(startPoss < len(src) - 1):
            dest = src[startPoss]

            i = startPoss + 1
            while(src[i] != endOfData):
                dest = dest + src[i]
                i = i + 1
            return dest

    def GetUserData(data, startPoss, user):
        i = startPoss

        # get ID
        if (ReadUsersData.StringCompare(data, userIDTitle, i)):
            i = i + len(userIDTitle)
            user.append(User())
            user[len(user) - 1].ID = ReadUsersData.StringCopy(data, i)
            #a = user[0].ID
            #print(user[0].ID)
        else:
            return -1

        #get name
        i = i + len(user[len(user) - 1].name) + 2
        if (ReadUsersData.StringCompare(data, nameTitle, i)):
            i = i + len(nameTitle)
            user[len(user) - 1].name = ReadUsersData.StringCopy(data, i)
            #a = user[0].name
            #print(user[0].name)
        else:
            return -1

        #get pass
        i = i + len(user[len(user) - 1].name) + 2    #change poss to pass....
        if (ReadUsersData.StringCompare(data, passTitle, i)):
            i = i + len((passTitle))
            user[len(user) - 1].password = ReadUsersData.StringCopy(data, i)
            #a = user[0].password
            #print(user[0].password)
        else:
            return -1

        #get coins
        i = i + len(user[len(user) - 1].password) + 2    #change poss to coins....
        if (ReadUsersData.StringCompare(data, coinsTitle, i)):
            i = i + len((coinsTitle))
            user[len(user) - 1].coins = ReadUsersData.StringCopy(data, i)
            #a = user[0].coins
            #print(user[0].coins)
        else:
            return -1

        #get playtime
        i = i + len(str(user[len(user) - 1].coins)) + 2    #change poss to playtime....
        if (ReadUsersData.StringCompare(data, playTimeTitle, i)):
            i = i + len((playTimeTitle))
            user[len(user) - 1].playTime = ReadUsersData.StringCopy(data, i)
            #a = user[0].playTime
            #print(user[0].playTime)
        else:
            return -1

        # get winrate
        i = i + len(str(user[len(user) - 1].playTime)) + 2 # change poss to winrate....
        if (ReadUsersData.StringCompare(data, winrateTitle, i)):
            i = i + len((winrateTitle))
            user[len(user) - 1].winrate = ReadUsersData.StringCopy(data, i)
            #a = user[0].winrate
            #print(user[0].winrate)
        else:
            return -1

        i = i + len(str(user[len(user) - 1].winrate)) + 2    #change poss to end of user
        return i

    #ham tra ve -1 neu khong doc duoc
    def  GetAllUsersData(user):

        f = open(dataLocation, "rt")

        data = f.read()

        data = decrypt.DecyptData(data, key)

        dataLength = len(data)
        i = 0
        while(i < dataLength - 20):
            i = ReadUsersData.GetUserData(data, i, user)
            if(i == -1):
                print("loi")
                return -1

    pass

class WriteUsersData:

    def WriteAllUsersData(user):
        f = open(dataLocation, "w")

        i = 0
        textToWrite = ""
        while(i < len(user)):
            textToWrite += userIDTitle + user[i].ID + "\" "

            textToWrite += nameTitle + user[i].name + "\" "

            textToWrite += passTitle + user[i].password + "\" "

            textToWrite += coinsTitle + user[i].coins + "\" "

            textToWrite += playTimeTitle + user[i].playTime + "\" "

            textToWrite += winrateTitle + user[i].winrate + "\" "

            #textToWrite = textToWrite + '\n'

            i = i + 1

        textToWrite = encypt.EncryptData(textToWrite, key)

        f.write(textToWrite)

    pass

class FindUser:
    def FindUser(listUser, x):   #return -1 if not exist    -2 if wrong pass    or poss of user in list
        i = 0
        exist = False
        rightPass = False
        poss = 0
        while i < len(listUser):
            if(listUser[i].userName == x.userName):
                exist = True
                poss = i
                break

        if not exist:
            return -1

        if listUser[poss].password != x.password:
            return -2
        return poss

'''
user = []
if(ReadUsersData.GetAllUsersData(user) != -1):

    WriteUsersData.WriteAllUsersData(user)

for a in user:
    print(a.ID)
    print(a.name)
    print(a.password)
    print(a.coins)
    print(a.playTime)
    print(a.winrate)
'''



