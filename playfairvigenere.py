import string
import random

class PlayFairVigenere:
    def __init__(self, keyword, plain_text):
      self.keyword = keyword.upper()
      self.plain_text = plain_text.upper()
      self.generateKey()
      self.generateText()
      self.encrypt()
      self.decrypt()

    def isSameRow(self, m, n):
      return (self.key.find(m) // 5 == self.key.find(n) // 5)

    def isSameCol(self, m, n):
      return (self.key.find(m) % 5 == self.key.find(n) % 5)

    def generateKey(self):
      new_key = ""
      for x in self.keyword:
          if((x != 'J') and (new_key.find(x) == -1)):
              new_key += x
      for i in range(26):
          char = chr(i+65)
          if ((char != 'J') and (new_key.find(char) == -1)):
              new_key += char
      self.key = new_key

    def generateText(self):
      self.new_text = self.plain_text.replace('J', 'I')
      temp = self.new_text[0]
      text = self.new_text[0]
      for i in range(1, len(self.new_text)):
          if (self.new_text[i] == temp):
              if (self.new_text[i] == 'X'):
                  text += 'Z'
              else:
                  text += 'X'
          text += self.new_text[i]
          temp = self.new_text[i]
      if (len(text) % 2 != 0):
          text += 'X'
      self.new_text = text

    def shiftRight(self, char):
      if (self.key.find(char) % 5 == 4):
        return self.key[self.key.find(char)-4]
      else:
        return self.key[self.key.find(char)+1]
    
    def shiftLeft(self, char):
      if(self.key.find(char) % 5 == 0):
        return self.key[self.key.find(char)+4]
      else:
        return self.key[self.key.find(char)-1]
    
    def shiftDown(self, char):
      if(self.key.find(char) // 5 == 4):
        return self.key[self.key.find(char) % 5]
      else:
        return self.key[self.key.find(char) + 5]
      
    def shiftUp(self, char):
      if (self.key.find(char) // 5 == 0):
        return self.key[self.key.find(char) + 20]
      else:
        return self.key[self.key.find(char) -5]
      
    def shiftCustom(self, char1, char2):
      char1_x = self.key.find(char1) % 5
      char1_y = self.key.find(char1) // 5
      char2_x = self.key.find(char2) % 5
      char2_y = self.key.find(char2) // 5
      return (self.key[char1_y * 5 + char2_x] + self.key[char2_y * 5 + char1_x])

    def encrypt (self):
      text = ""
      for i in range(0, len(self.new_text)-1, 2):
        char1 = self.new_text[i]
        char2 = self.new_text[i+1]
        if (self.isSameRow(char1,char2)):
          text += self.shiftRight(char1)
          text += self.shiftRight(char2)
        elif (self.isSameCol(char1,char2)):
          text += self.shiftDown(char1)
          text += self.shiftDown(char2)
        else:
          text += self.shiftCustom(char1,char2)
      self.cipher_text = text

    def decrypt (self):
      text = ""
      for i in range(0, len(self.cipher_text),2):
        char1 = self.cipher_text[i]
        char2 = self.cipher_text[i+1]
        if (self.isSameRow(char1,char2)):
          text += self.shiftLeft(char1)
          text += self.shiftLeft(char2)
        elif (self.isSameCol(char1,char2)):
          text += self.shiftUp(char1)
          text += self.shiftUp(char2)
        else:
          text += self.shiftCustom(char1,char2)
      self.origin_text = text

    def printAll(self):
        print("Input plain_text user : ", self.plain_text)
        print("Input customtext  : ", self.new_text)
        print("Input keyword user : ", self.keyword)
        print("New key : ", self.key)
        print("Ciphertext : ", self.cipher_text)
        print("Origin text : ", self.origin_text)

    def getCipherText(self):
      return self.cipher_text

    def getOriginText(self):
      return self.origin_text

if __name__ =="__main__":
    keyword = "JALANGANESHASEPULUH"
    text = "temuiibunantimalam"
    coba = PlayFairVigenere(keyword,text)
    coba.printAll()