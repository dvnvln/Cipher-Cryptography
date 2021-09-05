from extendedvigenere import *
from tkinter.filedialog import askopenfilename

filepath = 'EcgvlJbWoAEzWXp.jpg'

readFile = open(filepath, 'rb')
fileReaded = readFile.read()
b = bytearray(fileReaded)
# print(b)
result = b.decode('latin-1')
# print(result)


keyword_ext = "BONek88"
text_ext = result
ext = ExtendedVigenere(keyword_ext,text_ext)
# print(ext.getOriginText())

decrypted_txt = ext.getOriginText()
b_decrypted = decrypted_txt.encode('utf8')
exportFileName = 'hasilDecrypted'
save_text = open(exportFileName, 'wb')
save_text.write(b_decrypted)
save_text.close()