#convert to ascii code one character at a time
def convertStringToAscii (originalMsg):
    characterList = []
    for i in range(len(originalMsg)):
        characterList += [ord(originalMsg[i])]
    return characterList

#convert 0-25 values back to ascii values
def convertCaesarToAscii(asciiList,oldList):
    newAscii = []
    counter = 0
    for i in oldList:
        asChar = asciiList[counter]
        if (asChar >= 65) and (asChar <= 90): #upper-case
            encryptChar = i + 65
        elif (asChar >= 97) and (asChar <= 122): #lower-case
            encryptChar = i + 97
        else:
            encryptChar = i #preserve punctuation
        newAscii += chr(encryptChar)
        counter+=1
    return newAscii

#take input //
original = input("Enter message: ")
shift = int(input("Number of characters to shift (1-26): "))
while (shift < 1) or (shift > 26):
    if (shift >= 1) or (shift <= 26):
        print("Invalid input")
    shift = int(input("Number of characters to shift (1-26): "))

asciiList=convertStringToAscii(original)
#print("Debug: asciiList - {}".format(asciiList))

#convert from ASCII to 0-25
caesarList = []
counter=0
for i in asciiList:
    asChar = asciiList[counter]
    #convert character ascii to 0-25
    if (asChar >= 65) and (asChar <= 90): #upper-case
        charX = asChar - 65
        isLetter=True
    elif (asChar >= 97) and (asChar <= 122): #lower-case
        charX = asChar - 97
        isLetter=True
    else:
        isLetter=False
    if isLetter == True: #check if letter
        caesarList += [charX] #add to list
    else:
        caesarList += [asChar] #add punct to list
    counter+=1
#print("Debug: caesarList - {}".format(caesarList))

encryptList = []
counter=0
for i in caesarList:
    asChar = caesarList[counter]
    if asChar <= 25:
        encrypt = (asChar + shift) % 26 #encrypt(x) = (x + n) % 26, where x = letter represented as 0-25
        encryptList += [encrypt]
    else:
        encryptList += [asChar]
    counter+=1
#print("Debug: encryptList - {}".format(encryptList))
encryptAscii = convertCaesarToAscii(asciiList,encryptList)
encryptMessage = "".join(encryptAscii)

decryptList = []
counter=0
for i in encryptList:
    asChar = encryptList[counter]
    if asChar <= 25:
        decrypt = (asChar - shift) % 26 #decrypt(x) = (x - n) % 26
        decryptList += [decrypt]
    else:
        decryptList += [asChar]
    counter+=1
#print("Debug: decryptList - {}".format(decryptList))
decryptAscii = convertCaesarToAscii(asciiList,decryptList)
decryptMessage = "".join(decryptAscii)

print("Encrypted: " + encryptMessage)
print("Decrypted: " + decryptMessage)