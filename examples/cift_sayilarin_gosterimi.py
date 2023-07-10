#--------------- for döngüsü ile ----------------#
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayilar = []
if sayi1 > sayi2:
    sayi1, sayi2 = sayi2, sayi1  # Sayıları yer değiştir
for sayi in range(sayi1+1, sayi2):
    if sayi % 2 == 0:
        sayilar.append(sayi)
      
print(sayilar)


#--------------------while döngüsü ile ------------#

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayilar = []
if sayi1 > sayi2:
    sayi1, sayi2 = sayi2, sayi1  # Sayıları yer değiştir

sayi = sayi1+1  # (sayi +1 ) aralığı belirten sayılar dahil edilmesin diye bir arttırıldı

while sayi < sayi2:
    if sayi % 2 == 0:
        sayilar.append(sayi)
    sayi += 1

print(sayilar)