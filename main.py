import random
karakterler = '!^+%&/()=QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç'

uzunluk = int(input("Şifre uzunluğunu giriniz."))

sifre = ""

for i in range(uzunluk):
    sifre =  sifre + random.choice(karakterler)


print(sifre)
