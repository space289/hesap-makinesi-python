import yedek
print("hesap makinesine hoşgeldiniz ")
print("toplama için t, çıkarma için ç,bölme için b harfine tıklayınız")
i =(input("yapmak istediğiniz işlemi giriniz \n "))
a=int (input("ilk sayınız: "))
f=int (input("ikinci sayınız: "))

t = yedek.toplama(a, f)        
#t= a+f
ç=a-f

b= a/f

if i== "t":
    print(t)
elif i== "ç":
    print(ç)  
elif i== "b":
    print(b)
else:
    print("böyle bir işlem mevcut değil")
print("işlem başarılı :)")
