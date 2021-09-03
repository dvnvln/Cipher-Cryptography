from standardvigenere import StandardVigenere
from fullvigenere import FullVigenere
from autokeyvigenere import AutoKeyVigenere
from extendedvigenere import ExtendedVigenere
from playfair import PlayFair

if __name__ =="__main__":
    keyword = "viking"
    text = "vIkIngBOnekSamAsaJA"
    standar = StandardVigenere(keyword, text)
    full = FullVigenere(keyword,text)
    autokey = AutoKeyVigenere(keyword,text)
    playfair = PlayFair(keyword,text)
    print('----standar----')
    print("Cypher text : ", standar.getCipherText())
    print("Origin text : ", standar.getOriginText())
    # QQUQAMWWXMXYVUKANPV
    print('----autokey----')
    print("Cypher text : ", autokey.getCipherText())
    print("Origin text : ", autokey.getOriginText())
    # QQUQAMWWXMXYBANWKBA
    print('----full----')
    print("Cypher text : ", full.getCipherText())
    print("Origin text : ", full.getOriginText())
    # HEVENVONSQGCVDBFBKV
    print('----playfair----')
    print("Cypher text : ", playfair.getCipherText())
    print("Origin text : ", playfair.getOriginText())
    # IKNKGVEHGDNRDFDPBVCU
    print('----Extended----')
    keyword_ext = "BONek88"
    text_ext = "viking69JAYAjayaJAYA"
    ext = ExtendedVigenere(keyword_ext,text_ext)
    ext.printAll()
    # ¸¸¹ÎÙn{¾¬¢»°¦Äy
