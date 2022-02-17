from random import randint
 
rand=randint(1, 10)
say=0
 
while True:
    say+=1
    sayi=int(input("1 ile 10 arasında değer girin (0 Çıkış):"))
    if(sayi==0):
        print("Çıkış Yapıldı")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı : {0}".format(rand))
        print("Tahmin sayısı : {0}".format(say))
