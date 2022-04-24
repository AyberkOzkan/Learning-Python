karakter_dizisi = "Bu bir karakter dizisidir."
print(karakter_dizisi[0])       # Stringler 0'dan başlar
print(karakter_dizisi[1])
print(karakter_dizisi[-4])      # Sondan istenilen karakteri kullanmak için
print(karakter_dizisi[-3])
print(karakter_dizisi[-2])
print(karakter_dizisi[-1])
# print(karakter_dizisi[100]) karakter sayısını aşarsak hata verir.
print(karakter_dizisi[:10])     # Parçalar halinde çekebiliriz.

# Stringlerin karakterleri modifiye edilemez çünkü stringler değiştirilebilir değildir. Denenirse typeError
# karakter_dizisi[0] = "b"  Kısaca listeler gibi değiştirilemiyor