<div align="center">

[<< Python Operators](../2-Operators/Python_Operators.md) & [Strings >>](../4-Strings/Strings.md)

</div>

# **Data Types**

Python'da birkaç veri türü vardır. Veri türünü tanımlamak için ```Type()``` fonksiyonunu kullanırız. Farklı veri türlerini çok iyi anlamaya odaklanmanızı rica ediyorum. Bir şeyleri programlama söz konusu olduğunda, neredeyse hemen her şey veri türleri ile ilgili olduğunu göreceksiniz.
Veri türleri, bellekte biraz yer ayırmak için kullandığınız değişkenlerden başka bir şey değildir.

</br>

```py
# Veri Tipi Öğrenmek
x, y, z, w, bool = 0.04, 4j, "Dört", 4, True 
print(type(x), type(y), type(z), type(w), type(bool))
# <class 'float'> <class 'complex'> <class 'str'> <class 'int'> <class 'bool'>
```

Peki veri türlerini birbirlerine nasıl dönüştüreceğiz? Detaylarla boğmak yerine gelin örneklerle basit bir şekilde anlayalım.

```py
# int --> float
int = 434
print('int: ',int)         # 434
float = float(int)
print('float: ', float)    # 434.0

# float --> int
yer_cekimi = 9.80665
print(int(yer_cekimi))     # 9

# int --> str
int2 = 1234
print(int2)                # 1234
str = str(int2)
print(str)                 #'1234'

# str --> int, float
str2 = '2022.2022'
print('float: ', float(str2))     # 2022.2022
print('int: ', int(float(str2)))  # 2022

```
<br/> 

________________________________
________________________________

<br/>
<br/>

```py
a = 4
b = 5.123
c = 3j
# Değişkenleri ekrana yazdırmak
print(a)
print(b)
print(c)

print(float(a))  # int ---> float
print(int(b))    # float ---> int
print(str(bool)) # bool ---> str
print(bool)
print(int(bool)) # bool ---> int


cozum = a + b    # 9.123
print(cozum)
cozum2 = str(a) + str(b) # 45.123
print(cozum2)
print(type(cozum2))

# str(): Bir veri tipini karakter dizisine dönüştürür.
sayi = 4444
print(type(sayi)) # Girilen sayi INT bir veri türüdür.
yeni_class = str(sayi) # STR oldu
print(type(yeni_class))

# int(): Tam sayıya dönüştürülebilir veri tiplerini tam sayıya dönüştürür.
j = input("1. Sayıyı giriniz:")
k = input("2. Sayıyı giriniz:")
l = input("3. Sayıyı giriniz:")
toplam = j + k + l
print(toplam) 
# Girilen değerler String olduğu için matematik işlemine katmak için int dönüşümünü yaptım.
toplam2 = int(j) + int(k) + int(l)
print(toplam2) 
```
-> **Bu örnekleri önce kendiniz yapmaya çalışın.**

> Kullanıcının girmiş olduğu değerlere bağlı olarak bir daire'nin alanını ve çevresini bulan bir program yazınız. 
(π = 3.14)

```py
π = 3.14
r = float(input("Yarıçapı giriniz:")) # String bir bilgi verecektir. O yüzden başına float getirdim

alan = π * (r ** 2)
cevre = 2 * π * r

print("Daire'nin Alanı =", alan)
print("Daire'nin Çevresi =", cevre)

# Yan yana yazmak istersek, string birleştirme işlemini yapmamız gerekiyor.

print("Daire'nin Alanı =" + str(alan) + " Daire'nin Çevresi =" + str(cevre))
```
<div align="center">

[<< Python Operators](../2-Operators/Python_Operators.md) & [Strings >>](../4-Strings/Strings.md)

</div>