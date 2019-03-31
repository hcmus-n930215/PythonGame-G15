from libs.global_variables import *
from libs.decryptData import *
from libs.encryptdata import *

import os

#key to encript and decrip      from 1 to 127
key = 125

nameTitle = "username = \""
passTitle = "password = \""
coinsTitle = "coins = \""
playTimeTitle = "playTime = \""
winrateTitle = "winrate = \""

direct = os.getcwd()
currentDirrect = "/libs"
dataDirect = direct[0]

#change direction
i = 1
while(i < len(direct) - len(currentDirrect)):
    dataDirect = dataDirect + direct[i]
    i = i + 1

os.chdir(dataDirect)

aid = os.getcwd()

print(dataDirect)

endOfData = "\""

#create líst
#user = ["buiHuu Duc"]
#password = ["456"]
#coins = ["123"]
#playTime = ["789"]
#winrate =["100"]

user = []

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

    def GetUserData(data, startPoss):
        i = startPoss

        #get name
        if (ReadUsersData.StringCompare(data, nameTitle, i)):
            i = i + len(nameTitle)
            user.append(User())
            user[len(user) - 1].name = ReadUsersData.StringCopy(data, i)
            print(user[0].name)
        else:
            return -1

        #get pass
        i = i + len(user[len(user) - 1].name) + 2    #change poss to pass....
        if (ReadUsersData.StringCompare(data, passTitle, i)):
            i = i + len((passTitle))
            user[len(user) - 1].password = ReadUsersData.StringCopy(data, i)
            print(user[0].password)
        else:
            return -1

        #get coins
        i = i + len(user[len(user) - 1].password) + 2    #change poss to coins....
        if (ReadUsersData.StringCompare(data, coinsTitle, i)):
            i = i + len((coinsTitle))
            user[len(user) - 1].coins = ReadUsersData.StringCopy(data, i)
            print(user[0].coins)
        else:
            return -1

        #get playtime
        i = i + len(str(user[len(user) - 1].coins)) + 2    #change poss to playtime....
        if (ReadUsersData.StringCompare(data, playTimeTitle, i)):
            i = i + len((playTimeTitle))
            user[len(user) - 1].playTime = ReadUsersData.StringCopy(data, i)
            print(user[0].playTime)
        else:
            return -1

        # get winrate
        i = i + len(str(user[len(user) - 1].playTime)) + 2 # change poss to winrate....
        if (ReadUsersData.StringCompare(data, winrateTitle, i)):
            i = i + len((winrateTitle))
            user[len(user) - 1].winrate = ReadUsersData.StringCopy(data, i)
            print(user[0].winrate)
        else:
            return -1

        i = i + len(str(user[len(user) - 1].winrate)) + 2    #change poss to end of user
        return i

    #ham tra ve -1 neu khong doc duoc
    def  GetAllUsersData():

        f = open("data/usersData.txt", "rt")

        data = f.read()

        data = decrypt.DecyptData(data, key)

        dataLength = len(data)
        i = 0
        while(i < dataLength - 20):
            i = ReadUsersData.GetUserData(data,i)
            if(i == -1):
                print("loi")
                return -1

    pass

class WriteUsersData:

    def WriteAllUsersData():
        f = open("data/usersData.txt", "w")

        i = 0
        textToWrite = ""
        while(i < len(user)):
            textToWrite += nameTitle + user[i].name + "\" "

            textToWrite = textToWrite + passTitle + user[i].password + "\" "

            textToWrite = textToWrite + coinsTitle + user[i].coins + "\" "

            textToWrite = textToWrite + playTimeTitle + user[i].playTime + "\" "

            textToWrite = textToWrite + winrateTitle + user[i].winrate + "\" "

            #textToWrite = textToWrite + '\n'

            i = i + 1

        textToWrite = encypt.EncryptData(textToWrite, key)

        f.write(textToWrite)

    pass

ReadUsersData.GetAllUsersData()

WriteUsersData.WriteAllUsersData()



