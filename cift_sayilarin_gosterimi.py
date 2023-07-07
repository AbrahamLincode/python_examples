sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

if sayi1 > sayi2:
    sayi1, sayi2 = sayi2, sayi1  # Sayıları yer değiştir

for sayi in range(sayi1+1, sayi2):
    if sayi % 2 == 0:
        print(sayi)
