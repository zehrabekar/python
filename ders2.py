#alıştırmalar

#1 - klavyeden girilen km değerini mm değerine çevirme :
#print(f1,f2,m1,sep="\n") komutu ile f2,f2,m1'in değerleri alt alta yazdırılır. seperator olarak alt satıra geçmeyi kullandık
kmToM = int(input("metreye çevirilecek km değeri giriniz "))
metre = kmToM * 100
print("metre değeri: " , metre)

#2 - klavyeden grilen fahrenheit değerini santigrat değerine çevirme :
fahrenheit = float(input("bir fahrenheit değeri giriniz"))
santigrat =(fahrenheit-32)/1.8
print(fahrenheit,"fahrenheit",santigrat,"santigrat derecedir ")
print(type(santigrat))
"""
300 fahrenheit 148.88888888888889 santigrat derecedir
<class 'float'>
"""

#3 - öğrencinin vize ve final notunun ortalamasını hesaplama :
vize = int(input("vize notunu giriniz "))
final = int(input("final notunu giriniz "))
ortalama = (vize*0.4) + (final*0.6)
print("ortalama : ", ortalama)
