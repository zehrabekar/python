"""
yorumlama = interprete
yorumlayıcı = interpreter
derleme = compile
derleyici = compiler

derleme işlemi bir kere yapar,yorumlama işlemleri tekrar tekrar yapar.
derleme işlemi daha hızlı çalışır
yorumlama işleminde hangi satırdaysak o satırın komutu belleğe alınır,derleyicide tüm komut belleğe alınır. bu yüzden yorumlayıcıda daha az 
belleğe ihtiyaç vardır.
dosya uzantısı : .py
"""

#ekrana yazdırma komutu = print. örnek : 
print("merhaba")
#başka örnek :
a=5
b=10
c=a+b
print(c) #15 yazdırdı

"""
\t : tab tuşu kadar boşluk bırakır
\n : enter'a karşılık gelir. print ile yazdırdığımız ifadeden sonra \n nedeniyle imleç alt satıra geçer
"""

# çok satırlı yorum satırı yazmak için -> """  """  ya da '''  ''' kullanılır
# tek satır yorum yazmak için # kullanılır
#python dili büyük küçük harf duyarlıdır
"""
değişken tanımlama kuralları :
-ilk karakter _ ya da harflerden oluşabilir
-ilk karakter dışında sayısal değer kullanılabilir
-python dilindeki komut ve ifadeler değişken ismi olarak kullanılamaz
-birden fazla kelimeden oluşuyorsa arasında boşluk bırakılamaz
- _ dışında - / vs gibi başka karakterler kullanaMAyız.
"""
#örnek :
_ad ="zehra"
Soyad = "bekar"
print(_ad,Soyad) #zehra bekar
f1=5e3 #( 5*10^3 demektir) 
f2=15e-3 #(15i 1000e böler = 0.015)
m1=True
karsilastirma = 5<6
print(f1,f2,m1,karsilastirma) # 5000.0 0.015 True True

#bir değişkenin veri türünü öğrenmek için  : type(değişkenadı) . örnek :
print(type(_ad)) # <class 'str'> çıktısını verdi


#kullanıcıdan bilgi almak için : input(ekranda görünecek mesaj). klavyeden girilen her değer stringdir.
deger = input("klavyeden değer gir : ")
sonuc=deger*20
print(sonuc)
#5 girdim çıktı olarak 55555555555555555555 verdi.çünkü klavyeden girilen değer string olduğu için * çarpma işlemi olarak kullanılamadı.
#int'e dönüştürürsek çarpma işlemini yapar :
deger = int(input("klavyeden değer gir : "))
sonuc=deger*20
print(sonuc)
#8 grdim 160 çıktısını verdi


#eğer girilen değerin veri türünün int olmasını (veya başka bir şey) istiyorsak tür değişimi yapmalıyız :
mesaj = int(input("bir değer giriniz"))
print(mesaj)


#birden fazla değeri aynı anda yazdırırken aralarında varsayılan olarak gelen boşluk yerine istediğimiz bir ayırıcıyı koymak için : sep=" istediğimiz ayırıcı mesela |"
print(f1,f2,m1,sep="|") # çıktı : 5000.0|0.015|True

#en sondaki değerin sonunda varsayılan olarak gelen \n kaçış değeri yerine sonuna da | koysun (veya başka bir şey koysun)istersek : 
print(f1,f2,m1,sep="|",end="|") # çıktı : 5000.0|0.015|True|

# eğer " \ " (ters slash) kullanacaksak yanyana iki tane kullanmalıyız -> \\ 

"""
kaçış karakterleri : 
\b : boşluk karakteri kadar boşluk bırakır
\t : tab tuşu kadar boşluk bırakır
\n : bir alt satıra geçer 
"""

#end kullandığımızda peş peşe olan printlerin çıktısını yanyana verir. örnek : 
print(f1,f2,sep=",",end=";")
print(m1,karsilastirma,sep=":")
# çıktı : 5000.0,0.015;True:True
# end kullanıdğımızda çıktıların alt alta gelmesi için end ile belirttiğimiz karakterin yanına \n eklemeliyiz :
print(f1,f2,sep=",",end=";\n")
print(m1,karsilastirma,sep=":")
""" çıktı :
5000.0,0.015;
True:True
"""



































