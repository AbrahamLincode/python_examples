dizi = input("ters çevirilecek metni giriniz :")
def ters_cevir():
    ters_metin =""
    indx = len(dizi)
    for i in range(indx):
        ters_metin += dizi[indx-1]
        indx -= 1
    
    return ters_metin

print(ters_cevir())