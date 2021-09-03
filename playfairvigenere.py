# import string
# import random

# class FullVigenere:
#     def __init__(self, keyword, plain_text):
#         self.keyword = keyword.upper()
#         self.plain_text = plain_text.upper()
#         self.generateKey()
#         self.encrypt()
#         self.decrypt()

#     def isSameRow(m, n, matrix):
#         return (matrix.find(m) // 5 == matrix.find(n) // 5)

#     def isSameCol(m, n, matrix):
#         return (matrix.find(m) % 5 == matrix.find(n) % 5)

#     def generateKey (self):
#         # new_key = list(self.keyword)
#         new_key = ""
#         for x in self.keyword:
#             if((x != 'J') and (new_key.find(x) == -1)):
#                 new_key += x
#         for i in range(26):
#             char = chr(i+65)
#             if ((char != 'J') and (new_key.find(char) == -1)):
#                 new_key += char
#         self.key = new_key

#     def encrypt (self):
#         text = []
#         for i in range(len(self.plain_text)):
#             j = ord(self.key[i]) - ord('A')
#             k = ord(self.plain_text[i]) - ord('A')
#             text.append(self.matrix[j][k])
#         self.cipher_text = ("" . join(text))

#     def decrypt (self):
#         text = []
#         for i in range(len(self.cipher_text)):
#             j = ord(self.key[i]) - ord('A')
#             k = self.matrix[j].index(self.cipher_text[i])
#             text.append(chr(k + ord('A')))
#         self.origin_text = ("" . join(text))

#     def printAll(self):
#         print("Input plain_text user : ", self.plain_text)
#         print("Input keyword user : ", self.keyword)
#         print("New key : ", self.key)
#         print("Ciphertext : ", self.cipher_text)
#         print("Origin text : ", self.origin_text)



# if __name__ =="__main__":
#     arr_test = [ 'a','b','c','d','e',
#             'f','g','h','i','k',
#             'l','m','n','o','p',
#             'q','r','s','t','u',
#             'v','w','x','y','z' ]
#     print(chr(97))
#     text = ("" . join(arr_test))
#     text_matrix = []
    
#     #print matrix key
#     # for i in range(5):
#     #     text_matrix.append([])
#     #     for j in range(5):
#     #         text_matrix[i].append(text[5 * i + j])
#     #     print(text_matrix[i])

# # def generateKeyTable(keyword):
# #     new_key = list(self.keyword)
# #     if (len(self.plain_text) == len(self.keyword)):
# #         self.key = (self.keyword)
# #         return
# #     else:
# #         for i in range(len(self.plain_text) - len(new_key)):
# #             new_key.append(self.plain_text[i])
# #         self.key = "".join(new_key)
# #     return

# # print(isSameRow('s','e',text))
# # print(isSameCol('a','f',text))