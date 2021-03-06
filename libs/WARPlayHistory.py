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
if flag: # correct
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

endOfData = "\""    #to define where to stop read data
racerTypeTitle = "racerType = \""
racerNumTitle = "racerNum = \""
coinResulTitle = "coinResult = \""
key = 123

class ReadHistoryData:
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
            while(src[i] != endOfData):
                dest = dest + src[i]
                i = i + 1
            return dest

    def GetData(data, startPoss, history):
        i = startPoss
        # get type
        if (ReadHistoryData.StringCompare(data, racerTypeTitle, i)):
            i = i + len(racerTypeTitle)
            history.append(History())
            history[len(history) - 1].racerType = ReadHistoryData.StringCopy(data, i)
        else:
            return -1
        #get number
        i = i + len(history[len(history) - 1].racerType) + 2
        if (ReadHistoryData.StringCompare(data, racerNumTitle, i)):
            i = i + len(racerNumTitle)
            history[len(history) - 1].racerNum = ReadHistoryData.StringCopy(data, i)
        else:
            return -1
        #get result
        i = i + len(history[len(history) - 1].racerNum) + 2    #change poss to pass....
        if (ReadHistoryData.StringCompare(data, coinResulTitle, i)):
            i = i + len((coinResulTitle))
            history[len(history) - 1].coinResult = ReadHistoryData.StringCopy(data, i)
        else:
            return -1
        i = i + len(str(history[len(history) - 1].coinResult)) + 2    #change poss to end of history
        return i
    #ham tra ve -1 neu khong doc duoc
    def  GetAllHistoryData(userID, history):
        dataLocation = "data/" + str(userID) + ".txt"
        try:
            f = open(dataLocation, "rt")
        except FileNotFoundError:
            # ERROR ACCESS FILE
            return

        data = f.read()
        dataLength = len(data)
        i = 0
        while(i < dataLength - 20):
            i = ReadHistoryData.GetData(data, i, history) + 1
            if(i == -1): # HISTORY ERROR
                return -1
        return history
    pass

class WriteHistoryData:
    def WriteAllHistoryData(userID, history):
        dataLocation = "data/" + str(userID) + ".txt"
        f = open(dataLocation, "w")
        i = 0
        textToWrite = ""
        while(i < len(history)):
            textToWrite += racerTypeTitle + history[i].racerType + "\" "
            textToWrite += racerNumTitle + history[i].racerNum + "\" "
            textToWrite += coinResulTitle + history[i].coinResult + "\" "
            textToWrite = textToWrite + '\n'
            i = i + 1
        f.write(textToWrite)
    pass
'''
history = []
ReadHistoryData.GetAllHistoryData("100000", history)
'''
