#sayı tahmin etme
import random
sayi= random.randint(1, 10)
print("üç tahmin hakkınız var \n lütfen ilk tahmininizi yapınız: ")
tahmin = 0
while tahmin< 3 :
    yeni=int(input())
    tahmin+=1
    if yeni < sayi:
        print ("lütfen daha büyük sayı giriniz")
    if yeni> sayi:
        print("lütfen daha büyük sayi giriniz")
    if yeni== sayi:
        break
if yeni== sayi:
    print ("tahminiz doğru seçtiğim sayi{}dir".format(sayi))
else :
    print("tahmin hakkınız bitmiştir by") 