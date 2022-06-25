<div align="center">

[<< Introduction](../0-Keywords,%20Variables,%20Notations%20and%20Data%20Types/Introductions.md) & [Python Operators >>](../2-Operators/Python_Operators.md)

</div>

## **print() Fonksiyonu**
```print()``` fonksiyonun amacı ekrana çıktı vermektir.<br>
--> 
```py
print("Hello World!")
print('Hello World!')
print("""Hello World!""")
#Yanlış yazımlar print("Hello')                                     X
# print('Python'un en önemli özelliği dinamik yapısıdır.')          X
#Eğer print() içerisindeki tırnak işaretleri birbirleriyle çakışırsa program hata verecektir.
print("Python'un en önemli özelliği dinamik yapısıdır.")
print('"Java Nesne Yönelimli bir dildir." diye açıkladı.')
# Çok satırlı
print("""I'm not in danger Skyler,
I'm the danger.
Say my name?
-Heisenberg""")
print('We\'ll get back to you later!')
print("Kenan Ayberk \n Özkan")
print(1000)
print(True)
print('2'+'2')
print(2+2)
```

## **input() Fonksiyonu**

```input()``` fonksiyonu kullanıcıdan girdi almamızı sağlar.
<br>
--> 
```py
x = input('İsminizi Girin:')
print('Merhaba, ' + x)
```

**Not:** input fonksiyonunu kullanarak kullanıcadan bir sayı girmesini isterseniz ve bunu direkt print fonksiyonu ile yazdırmaya kalkarsanız sayıyı string ifade olarak alacaktır. Bu yüzden ileride göreceğimiz Type dönüşümü yapmamız gerekiyor.

```py
sayi = input('Bir sayi giriniz: ')
print(sayi + 10)    # Kullanıcıdan aldığımız sayıya 10 ekleyelim.
# Type Error hatası verecektir.
```
<div align="center">

[<< Introduction](../0-Keywords,%20Variables,%20Notations%20and%20Data%20Types/Introductions.md) & [Python Operators >>](../2-Operators/Python_Operators.md)

</div>
