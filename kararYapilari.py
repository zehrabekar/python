import math
"""
karar yapıları ikiye ayrılır : 
* doğru - yanlış karar yapısı (tek koşulun kontrol edildiği karar yapısı = if, birden fazla koşulun kontrol edildiği karar yapısı = if-else)
* çoklu seçim karar yapısı(if-elif-else)

"""
#if döngüsü ile vize ve final notuna bakarak öğrencinin sınıftan geçip geçmediğini yazdırma
vize=int(input("vizeniz : "))
final=int(input("finaliniz : "))
ort= (vize * 0.4) + (final * 0.6)
print("ortalamanız : ",ort)
if (ort>50) : 
    print("sınıftan geçtiniz")
    print("tebrikler")
print("çıkış")

# : -> anlamını ise olarak düşünebiliriz. :'dan sonra en az bir karakter boşluk bırakmamız gerekiyor
"""if'den sonra başka bir komut daha çalışsın istersek "print("sınıftan geçtiniz")" ile aynı hizada yazmak zorundayız. fakat yazacağımız komutun ifdeki
şartla bir ilgisi yoksa yani ortalamanın 50nin altında olduğu zamanda bile çalışmasını istersek  "print("sınıftan geçtiniz")" ile aynı hizada yazmamalıyız
(print("çıkış"))
"""

"""
if-else :
    if koşul:
        işlem1
    else :
        işlem2
"""

# matematik kütüphanesini dahil etmek için -> import math yazılır

"""çoklu seçim karar yapısı: art arda yazılan else if bloklarının birleştirilmiş hali 
if koşul :
    işlem
else :
    if koşul:
        işlem
    else : 
        if koşul:
            işlem
        else
            işlem 

yukarıdaki şekilde art arda if-else kullanımında sürekli sağa doğru bir kayma var . bunu engellemek için else ile sonraki if birleştirilerek elif oluşturulur :

if koşul :
    işlem
elif koşul :
   işlem
elif koşul : 
    işlem
else
    işlem
"""
#örnek :
sayi=int(input("0-5 arasında bir sayı giriniz "))
if sayi==0:
    print("sıfır")
elif sayi==1:
    print("bir")
elif sayi==2:
    print("iki")
elif sayi==3:
    print("üç")
elif sayi==4:
    print("dört")
elif sayi==5:
    print("beş")
else:
    print("geçersiz sayı girdiniz")

#ideal kilo ile güncel kilo farkını bulma:
boy=int(input("boyunuz : "))
yas=int(input("yaşınız : "))
cinsiyet=(input("cinsiyetiniz : "))
kilo=int(input("kilonuz : "))
if cinsiyet == "kadın":
    ik=(boy-100)*0.8+(yas/10)
else:
    ik=(boy-100)*0.9+(yas/10)
ik=round(ik) #ideal kilo sonucunu yuvarladık
print("ideal kilonuz : " , ik)
fark=ik-kilo
if fark<0:
    print(abs(fark)," kilo vermelisiniz")
elif fark>0 :
    print(fark," kilo almalısınız")
else:
    print("tebrikler ideal kilonuzdasınız.")