def fatura_toplam():
    toplam = 0
    while True:
        odenek = input("Ödenek giriniz ('ç' için çıkış): ")
        if odenek == "ç":
            break
        toplam += float(odenek)
    return toplam

def kdv(toplam):
    kdv = toplam*0.18
    kdv_dahil = kdv + toplam
    return(kdv,kdv_dahil)

fatura = fatura_toplam()
kdv_tutari, kdv_dahil_toplam = kdv(fatura)

print(f"Fatura toplam değeri: {fatura}, %18 KDV tutarı: {kdv_tutari}, KDV dahil toplam fatura tutarı: {kdv_dahil_toplam}")