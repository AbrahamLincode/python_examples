toplam = 0
sart = True
print("Toplama işlemi için lütfen sayı giriniz . Programdan çıkmak için 'ç' harfine basınız")

while sart:
    sayi = input("Toplam için sayı giriniz : ")
    if  sayi.isdigit():
        toplam += int(sayi) 
        print(f"yeni toplam : {toplam}")
    elif sayi == "ç":
        sart = False