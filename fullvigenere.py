import string
import random

class FullVigenere:
    def __init__(self, keyword, plain_text):
        self.keyword = keyword.upper()
        self.plain_text = plain_text.upper()
        self.generateKey()
        self.generateTable()
        self.encrypt()
        self.decrypt()

    def generateKey (self):
        new_key = list(self.keyword)
        if (len(self.plain_text) == len(self.keyword)):
            self.key = (self.keyword)
            return
        else:
            for i in range(len(self.plain_text) - len(new_key)):
                new_key.append(new_key[i % len(new_key)])
            self.key = "".join(new_key)

    def generateTable(self):
        table = []
        for i in range(26):
            order = list(string.ascii_uppercase)
            random.Random(i).shuffle(order)
            table.append(order)
        self.matrix = table

    def encrypt (self):
        text = []
        for i in range(len(self.plain_text)):
            j = ord(self.key[i]) - ord('A')
            k = ord(self.plain_text[i]) - ord('A')
            text.append(self.matrix[j][k])
        self.cipher_text = ("" . join(text))

    def decrypt (self):
        text = []
        for i in range(len(self.cipher_text)):
            j = ord(self.key[i]) - ord('A')
            k = self.matrix[j].index(self.cipher_text[i])
            text.append(chr(k + ord('A')))
        self.origin_text = ("" . join(text))

    def getCipherText(self):
      return self.cipher_text

    def getOriginText(self):
      return self.origin_text

    def printAll(self):
        print("Input plain_text user : ", self.plain_text)
        print("Input keyword user : ", self.keyword)
        print("New key : ", self.key)
        print("Ciphertext : ", self.cipher_text)
        print("Origin text : ", self.origin_text)