def kelimeleri_say(metin):
    liste = metin.split(" ")
    adet = len(liste)
    return adet

metin = input("Lütfen kelimeleri saymak istediğiniz metni giriniz : ")

print(f"Girdiğiniz metinde toplam {kelimeleri_say(metin)} adet kelime bulunuyor"  )