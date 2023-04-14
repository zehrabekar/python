#döngüler(tekrarlı yapılar)
"""
*döngüler, sayaçlı ve koşullu olmak üzere ikiye ayrılır.

*koşullu döngüler:
-koşulun başta kontrol edildiği döngüler(while). (biz bunu göreceğiz)
-koşulun sonda kontrol edildiği döngüler(do-while). (bunu görmeyeceğiz)

*sayaçlı döngüler:
-sayacı bizim belirlediğimiz döngüler(for). (bunu görmeyeceğiz)
-sayacın otomatik belirlendiği döngüler.(bunu göreceğiz)

while kullanım :
while koşul:
    işlem
-koşul sağlandığı sürece döngü çalışır
"""
cevap="evet"
while cevap=="evet":
    print("merhaba")
    cevap=input("tekrar yazdırmak için evet yaz ")

#while ile sayaçlı döngü
#1den 10a kadar olan sayıları ekrana yazdırma:
i=1
while i<=10:
    print(i)
    i+=1

"""
sayaçlı döngü için for:
for sayaç in range(başlangıç değeri , bitiş değerinin bir fazlası , artış miktarı):
    işlemler
*bu listedeki değerler sırayla sayaç isimli değişkene aktarılır

-bir listenin içindeki değerleri okumak için kullanlır
-başlangıç değeri belirlenmezse 0dan başlar
-artış miktarı belirlenmezse bir bir artar
-range komutu 1,2 ya da 3 parametre alabilir
örnek:
range(10)= [0,1,2,3,4,5,6,7,8,9] (buradaki 10 bitiş değerinin bir fazlası)
range(2,10)= [2,3,4,5,6,7,8,9] (buradaki 2 başlangıç değeri)
range(2,10,3)= [2,5,8] (buradaki 3 artış değeri)
"""