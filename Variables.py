# Değişken tanımlarken Özel semboller kullanılmaz (!, #, $, £ ...)
# Değişken adları rakam ile başlamaz
# Değişkenler büyük KÜÇÜK harf duyarlıdır. Case sensetive
# degis-ken = "Ayberk"  --> YANLIŞ
# degis ken = "Ayberk"  --> YANLIŞ
# Türkçe karakter kullanmayın.

FirstName = "Ayberk"
LastName = " Özkan"
print(FirstName + LastName) # Ayberk Özkan


# Çift veya Tek tırnak fark eder mi?
w = "Ayberk"
print(w)
w = 'Ayberk'
print(w)

# Bir değer birden fazla değişkene atanabilir.
t = u = g ="Mavi"
print(t, u, g)

T = '500'
U = '400'
print(T+U) # String birleştirme 500400


#Unpacking
Meyveler = ["Armut", "Muz", "Portakal"]
s, d, f = Meyveler
print(s, d, f)

# Veri tiplerinin uzunluklarını elde etmek için len() kullanılır.
# Ancak sayısal değerlerde hata verir.
# Sayılar tekrarlanamayan yapılar olduğu için kullanılamıyor.
isim = "Kenan Ayberk Özkan"
print(len(isim)) # 18