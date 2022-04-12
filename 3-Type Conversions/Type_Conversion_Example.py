"""
    Kullanıcının girmiş olduğu değerlere bağlı olarak bir daire'nin alanını ve çevresini
bulan bir program yazınız. 
(π = 3.14)

"""
π = 3.14
r = float (input("Yarıçapı giriniz:")) # String bir bilgi verecektir. O yüzden başına float getirdim

alan = π * (r ** 2)
cevre = 2 * π * r

print("Daire'nin Alanı =", alan)
print("Daire'nin Çevresi =", cevre)

# Yan yana yazmak istersek, string birleştirme işlemini yapmamız gerekiyor.

print("Daire'nin Alanı =" + str(alan) + " Daire'nin Çevresi =" + str(cevre))
