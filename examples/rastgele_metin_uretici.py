import random
import string

metin = ""      # Boş metin oluşturuldu
harfler = string.ascii_lowercase   # string modülünden bütün küçük harfler alındı

for i in range(0,10):       # kaç tane kelime oluşturulacağı döngüsü
    kelime_uzunluk = random.randint(0,15)   # kelime oluştururken kaç harften oluşacağının rastgele değeri oluşturulup , her yeni kelimeden sonra bir alt döngüye bu bilgi gidiyor

    for _ in range(kelime_uzunluk):     # kelime oluşturan döngü
        harf = random.choice(harfler)  # harfler değişkeninden seçilen harf harf değişkenine atılıyor
        metin += harf   # harf değişkeni her defasında metine ekleniyor
    
    metin += " "    #her oluşturulan kelimeden sonra kelimeler arasına boşluk bırakılıyo

print(metin) # metin değeri yazdırılıyor