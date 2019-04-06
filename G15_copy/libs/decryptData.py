import itertools

#define
numBitsRanded = 3

class decrypt:
    def Convert(a, strBit):
        bitA = ord(a)

        #add to string
        i = 0
        tempt = bitA

        #get rid randedBit
        temp = bitA >> (8 - numBitsRanded)
        temp = temp << (8 - numBitsRanded)
        bitA ^= temp


        while(i < (8 - numBitsRanded)):
            temp = bitA >> (8 - i - numBitsRanded - 1)
            a = str(temp)
            strBit += a
            temp = temp << (8 - i - numBitsRanded - 1)
            bitA ^= temp
            i += 1

        return strBit

    def XorData(currentBits, key):
        i = 0
        bits = 0

        while(i < len(currentBits)):
            bits = bits << 1
            bits += int(currentBits[i])
            i += 1

        #xored key
        bits ^= key

        a = str(chr(bits))
        return a


    def DecyptData(data, key):
        strBit = ""

        i = 0
        while(i < len(data)):
            strBit = decrypt.Convert(data[i], strBit)
            i += 1

        decryptedData = ""
        currentBits = []
        i = 0
        while(i < len(strBit)):
            if((i != 0) & (i % 8 == 0)):
                decryptedData += decrypt.XorData(currentBits, key)
                currentBits = []

            currentBits.append(int(strBit[i]))
            i += 1

        decryptedData += decrypt.XorData(currentBits, key)
        #print(decryptedData)
        return decryptedData

    #DecyptData("G$7#DVZ[", 123)
    pass