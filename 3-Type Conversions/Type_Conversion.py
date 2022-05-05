# Veri Tipi Öğrenmek
x, y, z, w, bool = 0.04, 4j, "Dört", 4, True 
print(type(x), type(y), type(z), type(w), type(bool))

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
print(boolean(1))

cozum = a + b    # 9.123
print(cozum)
cozum2 = str(a) + str(b) # 45.123
print(cozum2)
print(type(cozum2))

# str() Bir veri tipini karakter dizisine dönüştürür.
sayi = 4444
print(type(sayi)) # Class INT
yeni_class = str(sayi) # STR oldu
print(type(yeni_class))

# int() Tam sayıya dönüştürülebilir veri tiplerini tam sayıya dönüştürür.
j = input("1. Sayıyı giriniz:")
k = input("2. Sayıyı giriniz:")
l = input("3. Sayıyı giriniz:")
toplam = j + k + l
print(toplam) 
# Girilen değerler String olduğu için matematik işlemine katmak için int dönüşümünü yaptım.
toplam2 = int(j) + int(k) + int(l)
print(toplam2) 
