numbers = 5, 8, 1, 4, 13
x, y, z = 9, 2, 4

# x, y ve z'nin toplamının mod 4'ü nedir?

print((x + y + z) %4)

# x'in z'ye kalansız bölümünü hesaplayın.
print(x//z)

# y'nin z. kuvvetini hesaplayın.
print(y ** z)

# Kullanıcıdan aldığınız iki sayının çarpımı ile x, y ve z toplamının farkı nedir?
num_bir = int(input("1. Sayıyı Giriniz: " ))
num_iki = int(input("2. Sayıyı Giriniz: " ))
multiply = num_bir * num_iki
print((num_bir * num_iki) - (x + y + z ))

# x, *y, z = numbers satırına göre z'nin karesi kaçtır?
x, *y, z = numbers
print(y)
print(z ** 2)

# x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?

toplam = y[0] + y[1] + y[2]
print(toplam)