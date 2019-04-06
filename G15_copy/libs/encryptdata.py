import itertools
import random

#define
numBitsRanded = 3

class encypt:
    def FindNeedLength(a, b):
        i = 1

        while(((a * i) % b) != 0):
            i += 1
        return i

    def ConvertAndXor(a, key, xoredData):
        bitA = ord(a)
        bitA ^= key

        #add to string
        i = 0
        temp = bitA
        while(i < 8):
            temp = bitA >> (8 - i - 1)
            a = str(temp)
            xoredData += a
            temp = temp << (8 - i - 1)
            bitA ^= temp
            i += 1

        return xoredData

    def RandBits(bits):

        bitRand = random.randrange(1, 4)

        i = 0
        while(i < len(bits)):
            bitRand = bitRand << 1
            bitRand += int(bits[i])
            i += 1

        #convert to char
        a = str(chr(bitRand))
        return a

    def EncryptData(data, key):
        lengthNeed = encypt.FindNeedLength(8, 8 - numBitsRanded)     #8 is bits per byte
        while(len(data) % lengthNeed != 0):
            data += ' '

        xoredData = ""

        #convert data to bit and xor with key
        i = 0
        while(i < len(data)):
            xoredData = encypt.ConvertAndXor(data[i], key, xoredData)
            #print(xoredData)
            i += 1

        encryptedData = ""
        currentBits = []

        #encrypt
        i = 0
        l = len(xoredData)
        while(i < len(xoredData)):
            if((i % (8 - numBitsRanded) == 0) & (i != 0)):
                encryptedData += encypt.RandBits(currentBits)
                currentBits = []

            currentBits.append(int(xoredData[i]))
            i += 1

        encryptedData += encypt.RandBits(currentBits)

        #print(encryptedData)
        return encryptedData

    #EncryptData("BUI", 123)

    pass
