def splitText(text):
    return [char for char in text]

def affineCipher(plainText, move):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    n = 26 #jumlah alfabet
    m = 7 #key
    b = move

    plainTextList = splitText(plainText)

    encryptedText = ""

    for char in plainTextList:
        if (char in alphabet):
            cipher = ((m * (alphabet.index(char))) + b) % n
            encryptedText += alphabet[cipher]

    return encryptedText

def findDecipherKey(m):
    found = False
    decipherKey = 0
    n = 26 #jumlah alfabet
    i = 1

    while found == False:
        if ((m * i) % n == 1):
            found = True
        else:
            i += 1
    
    return i

def affineDecipher(encryptedText, move):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    encryptedTextList = splitText(encryptedText)
    decipherKey = findDecipherKey(7)
    b = move #jumlah pergeseran
    decryptedText = ""

    for char in encryptedTextList:
        decipher = (decipherKey * (alphabet.index(char) - b)) % 26
        decryptedText += alphabet[decipher]

    return decryptedText 
