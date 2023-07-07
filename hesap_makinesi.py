while True:
    sayi1 = input("Birinci Sayı :")
    if sayi1.isdigit():
        sayi1 = int(sayi1)
        break
    else:
        print("lütfen geçerli bir sayı giriniz ")
while True:
    islem = input()
    while True:
        sayi2 = input("ikinci Sayı :")
        if sayi2.isdigit():
            sayi2 = int(sayi2)
            break
        else:
            print("lütfen geçerli bir sayı giriniz ")

    sonuc = 0
    match islem :
        case "+":
            sonuc = sayi1 + sayi2
            print(sonuc)
            sayi1 = sonuc
        case "-":
            sonuc = sayi1 - sayi2
            print(sonuc)
            sayi1 = sonuc
        case "*":
            sonuc = sayi1 * sayi2
            print(sonuc)
            sayi1 = sonuc
        case "/":
            sonuc = sayi1 / sayi2
            print(sonuc)
            sayi1 = sonuc
        case "**":
            sonuc = sayi1 ** sayi2
            print(sonuc)
            sayi1 = sonuc

            
