# Kimlik operatörleri eşit olup olmadıklarını değil aynı bellek konumuna veya 
# aynı nesne olup olmadıklarını karşılaştırmak için kullanılır.
# is        is not
# id() ---> Nesnelerin bilgisayar hafızasındaki kimlikleri gösterir.

isim = "Ayberk"
ad ="Ayberk"
yas = 20
print(id(isim))
print(id(yas))

print(yas is isim)      # False
print(ad is isim)       # True
print(ad is not yas)    # True
print(ad is not isim)   # False