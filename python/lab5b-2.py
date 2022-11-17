#convert string value to ASCII code one character at a time
def asciiConvert (originalMsg):
    asciiList = []
    for i in range(len(originalMsg)):
        #print(original[i])
        asciiCharacter = ord(originalMsg[i])
        asciiList += [asciiCharacter]
    #print(asciiList)
    return asciiList

#convert ASCII to 0-25
def caesarConvert(asChar):
    characterX=0
    if (asChar >= 65) and (asChar <= 90): #upper-case
        characterX = asChar - 65
        setLetter = True
    elif (asChar >= 97) and (asChar <= 122): #lower-case
        characterX = asChar - 97
        setLetter=True
    else:
        setLetter=False
    return (characterX,setLetter)

#encrypt(x) = (x + n) % 26, where x = letter represented as 0-25 & n = shift
def caesarEncrypt (asciiList):
    counter=0
    for i in asciiList:
        caesarList = []
        characterX,setLetter = caesarConvert(i)
        if setLetter == True: #check for punct
            caesar = (characterX + shift) % 26 #shift
            caesarList += [caesar] #add to list
        else:
            caesarList += [i] #add punct to list
            print(caesarList)
        counter+=1
    return caesarList

#decrypt(x) = (x - n) % 26, where x = character represented as 0-25 & n = shift
def caesarDecrypt (asciiList):
    for i in asciiList:
        caesarList = []
        characterX,setLetter = caesarConvert(i)
        if setLetter == True: #check for punct
            caesar = (characterX - shift) % 26 #shift
            caesarList += caesar #add to list
        else:
            caesarList += i #add punct to list
    return caesarList

#convert values back to ASCII
def convertToAscii(encryptList):
    encryptAscii = []
    counter = 0
    for i in encryptList:
        asChar = encryptList[counter]
        if (asChar >= 65) and (asChar <= 90): #upper-case
            encryptChar = i + 65
        elif (asChar >= 97) and (asChar <= 122): #lower-case
            encryptChar = i + 97
        else:
            encryptChar = i #preserve punctuation
        encryptAscii += chr(encryptChar)
        counter+=1
    finalMessage = "".join(encryptAscii)
    return finalMessage

#take input //
original = input("Enter message: ")
shift = int(input("Number of characters to shift (1-26): "))
while (shift < 1) or (shift > 26):
    if (shift >= 1) or (shift <= 26):
        print("Invalid input")
    shift = int(input("Number of characters to shift (1-26): "))

encryptList = asciiConvert(original)
asciiEncrypt = caesarEncrypt(encryptList)
encryptMessage = convertToAscii(asciiEncrypt)

decryptMessage = original
print("Encrypted: " + encryptMessage)
print("Decrypted: " + decryptMessage)