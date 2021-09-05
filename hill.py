import numpy as np
from sympy import Matrix

class Hill:
    def __init__(self, keyword, keyNumber, plain_text):
        self.keyword = keyword.upper()
        self.keyNumber = keyNumber
        self.plain_text = plain_text.upper()
        self.plainTextList = [char for char in self.plain_text]
        self.cipherTextString = ""
        self.plainTextLength = len(plain_text)

        if(len(self.plainTextList) % self.keyNumber != 0):
            for i in range (self.keyNumber - (len(self.plainTextList) % self.keyNumber)):
                self.plain_text += 'X'
                self.plainTextList.append('X')

        self.cipherMatrix = [[0] for i in range(self.keyNumber)]
        self.decipherMatrix = [[0] for i in range(self.keyNumber)]
        self.messageVector = [[0] for i in range(self.keyNumber)]
        self.encryptedVector = [[0] for i in range(self.keyNumber)]

        self.keyMatrix = [[0] * self.keyNumber for i in range(self.keyNumber)]
        self.generateKey()

        self.keyMatrixInverse = Matrix(self.keyMatrix)
        self.keyMatrixInverse = self.keyMatrixInverse.inv_mod(26)
        # print('-----')
        # print(self.keyMatrixInverse[0,0])
        self.encrypt()
        self.decrypt()

    def generateKey (self):
        k = 0
        for i in range(self.keyNumber):
            for j in range(self.keyNumber):
                self.keyMatrix[i][j] = ord(self.keyword[k]) % 65
                k += 1

    def encrypt (self):
        # Generate vector for the message
        for k in range(int(len(self.plainTextList) / self.keyNumber)):
            for i in range(self.keyNumber):
                self.messageVector[i][0] = ord(self.plainTextList[i]) % 65

            for i in range(self.keyNumber):
                for j in range(1):
                    self.cipherMatrix[i][j] = 0
                    for x in range(self.keyNumber):
                        self.cipherMatrix[i][j] += (self.keyMatrix[i][x] *
                                            self.messageVector[x][j])
                    self.cipherMatrix[i][j] = self.cipherMatrix[i][j] % 26

            # Generate the encrypted text
            # from the encrypted vector
            for i in range(self.keyNumber):
                self.cipherTextString += chr(self.cipherMatrix[i][0] + 65)

            for i in range(self.keyNumber):
                self.plainTextList.pop(0)
            self.encryptedTextList = [char for char in self.cipherTextString]

    def decrypt(self):
        self.decryptedText = ''
        for k in range(int(len(self.encryptedTextList) / self.keyNumber)):
            for i in range(self.keyNumber):
                    self.encryptedVector[i][0] = ord(self.encryptedTextList[i]) % 65

            for i in range(self.keyNumber):
                for j in range (1):
                    self.decipherMatrix[i][j] = 0
                    for x in range(self.keyNumber):
                        self.decipherMatrix[i][j] += (self.keyMatrixInverse[i,x] * self.encryptedVector[x][j])
                    self.decipherMatrix[i][j] = self.decipherMatrix[i][j] % 26
            
            for i in range(self.keyNumber):
                self.decryptedText += chr(self.decipherMatrix[i][0] + 65)

            for i in range(self.keyNumber):
                self.encryptedTextList.pop(0)

        if(self.plainTextLength % self.keyNumber != 0):
            for i in range (self.keyNumber - (self.plainTextLength % self.keyNumber)):
                self.decryptedText = self.decryptedText[:-1]
    
    def getCipherText(self):
        return self.cipherTextString

    def getDecipherText(self):
        return self.decryptedText

# Driver Code
def main():
    message = "PAYMOREMONE"
    key = "CFAIBECGHIJDBFHI"

    hill = Hill(key, 4, message)
    print(message)
    print(hill.getCipherText())
    print(hill.getDecipherText())
 
if __name__ == "__main__":
    main()