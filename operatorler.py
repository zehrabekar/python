#operatorlerin üzerinde işlem yaptığı değerlere operand denir
#örnek : sayi1 = sayi2 * sayi3. buradaki = ve * operatör; sayi1,sayi2 ve sayi3 operandır
"""
operatörler : 
- atama operatörler (=,)
- aritmetiksel operatörler
- karşılaştırma operatörler
- mantıksal operatörler( and , or , not) (not : true değeri false, false değeri true yapar.)
- metinsel operatörler
"""
s1,s2,m1=1,2,"ali"
#( // sembolü bize bölümü verir) mesela 14//4 sonucu 3'tür
# % sembölü bölümünden kalanı (mod) verir. 14%4 sonucu 2'dir

#metinsel operatörlerde + metinleri birleştirir ve yan yana yazar
#metinsel operatörlerde * metinleri yazılan değer kadar yanyana yazar. örnek :
metin="merhaba"
print(metin*2) # çıktı : merhabamerhaba

#karakter uzunluğunu bulmak için len kullanılır. örnek :
print(len(metin)) #7
#son karakterin indis numarasına ulaşmak için :
print(len((metin))-1) # indis no 6
#son indisdeki karaktere ulaşmak için :
print(metin[-1]) #a