from standardvigenere import StandardVigenere
from fullvigenere import FullVigenere
from autokeyvigenere import AutoKeyVigenere
from extendedvigenere import ExtendedVigenere

if __name__ =="__main__":
    keyword = "viking"
    text = "vIkIngBOnekSamAsaJA"
    coba = StandardVigenere("AYUSH","GEEKSFORGEEKS")
    standar = StandardVigenere(keyword, text)
    full = FullVigenere(keyword,text)
    autokey = AutoKeyVigenere(keyword,text)
    standar.printAll()
    print('----standar----')
    full.printAll()
    print('----autokey----')
    autokey.printAll()
    print('----Extended----')
    keyword_ext = "BONek88"
    text_ext = "viking69JAYAjayaJAYA"
    ext = ExtendedVigenere(keyword_ext,text_ext)
    ext.printAll()