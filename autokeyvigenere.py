class AutoKeyVigenere:
    def __init__(self, keyword, plain_text):
        self.keyword = keyword.upper()
        self.plain_text = plain_text.upper()
        self.generateKey()
        self.encrypt()
        self.decrypt()

    def generateKey (self):
        new_key = list(self.keyword)
        if (len(self.plain_text) == len(self.keyword)):
            self.key = (self.keyword)
            return
        else:
            for i in range(len(self.plain_text) - len(new_key)):
                new_key.append(self.plain_text[i])
            self.key = "".join(new_key)

    def encrypt (self):
        text = []
        for i in range(len(self.plain_text)):
            c = ((ord(self.plain_text[i]) + ord(self.key[i])) % 26) + 65
            text.append(chr(c))
        self.cipher_text = ("" . join(text))

    def decrypt (self):
        text = []
        for i in range(len(self.cipher_text)):
            c = ((ord(self.cipher_text[i]) - ord(self.key[i])) % 26) + 65
            text.append(chr(c))
        self.origin_text = ("" . join(text))

    def printAll(self):
        print("Input plain_text user : ", self.plain_text)
        print("Input keyword user : ", self.keyword)
        print("New key : ", self.key)
        print("Ciphertext : ", self.cipher_text)
        print("Origin text : ", self.origin_text)
