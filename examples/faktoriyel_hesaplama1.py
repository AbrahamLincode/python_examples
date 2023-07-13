def faktoriyel(giris):
    giris = int(giris)
    sayi_new = giris-1
    gosterim ="{}".format(giris)
    for i in range(1,giris):
        gosterim += " x "+str(sayi_new)
        giris = giris*(sayi_new)
        sayi_new -= 1
    return gosterim, giris

giris = input("faktoriyeli hesaplanacak pozitif sayıyı giriniz :")
if int(giris) < 0 :
    print("Lütfen sadece Pozitif tam sayı değeri giriniz")

faktoriyel_goserim , sonuc = faktoriyel(giris)
print(f"{giris} faktoriyelin gösterimi : {faktoriyel_goserim} , Sonucu : {sonuc} ")




