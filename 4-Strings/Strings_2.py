name = "Ayberk"
surname = " Özkan"
age = 24
# String Birleştirme ile
introduce = "My name is " + name + surname + " and I'm " + str(age)+"."
print(introduce)
print(len(introduce))
length = len(introduce)
print(introduce[length - 1])  # Son ifadeyi yazdırmak için -1 yazıyoruz çünkü stringler 0'dan başlar. Yazmazsak "String index out of range hatası" verecektir.
print(introduce[-1])          # Böyle de yazabilirdik.
print(introduce[11:17])
print(introduce[20:])         # 20. karakterden başlar sonuna kadar gider.
print(introduce[:20])         # Baştan başlar 20. karakterde durur.
print(introduce[2:35:3])      # 2. karakterden başlayıp 35. karaktere gider. 3'er 3'er atlar.