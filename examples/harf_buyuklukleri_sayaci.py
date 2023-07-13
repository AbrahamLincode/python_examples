def metin_kontrol(metin):
    denetim_Sonucu = {"buyuk_harfler": 0 ,"kucuk_harfler": 0}
    for i in metin:
        if i.islower():
            denetim_Sonucu["kucuk_harfler"] +=1
        elif i.isupper():
            denetim_Sonucu["buyuk_harfler"] += 1
        else:
            pass
    print("Asıl metin : ", metin)
    print("Büyük harf sayısı : ",denetim_Sonucu["buyuk_harfler"])
    print("Küçük harf sayısı : ",denetim_Sonucu["kucuk_harfler"])

metin = input("Lütfen Bir metin giriniz : ")

metin_kontrol(metin)