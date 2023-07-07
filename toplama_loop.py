while True:
    sayi1 = int(input(" :"))
    islem = input()
    sonuc = 0
    match islem:
        case "+":
            sayi2 =int(input(":"))
            sonuc = sayi1 + sayi2
        case "-":
            sayi2 =int(input(":"))
            sonuc = sayi1 - sayi2
        case "*":
            sayi2 =int(input(":"))
            sonuc = sayi1 * sayi2
        case "/":
            sayi2 =int(input("/"))
            sonuc = sayi1 + sayi2
        case "ç":
            break
    print(sonuc)