message = "Hey ! My name's Ayberk Özkan"
message = message.upper()           # Bütün karakterler BÜYÜK
print(message)
message = message.lower()           # Bütün karakterler küçük
print(message)
message = message.title()           # Her Kelimenin Baş Harfi Büyük
print(message)
message = message.capitalize()      # Bir karakter dizisinin sadece ilk harfi büyük
print(message)
print(message.swapcase())           # Büyük harfleri küçük harflere, küçük harfleri büyük harflere dönüştürür.
message = message.split()           # Herhangi bir string ifadeyi parçalara ayırır.
print(message)                      # Boşluk karakterlerinden bölünür ve ayrı string ifade olur. (Dizi)     
print(message[4])
print(message[5])
message ="*".join(message)          # Birleştirirken araya "yıldız" gelsin.   
print(message)                      # Bölünmüş karakter dizilerini tekrar bir araya getirmek için. Bölünmüş karakter dizileri "list" veri tipine girer
print(message.find("Ayberk"))       # Aramak istenilen kelimeyi parantez içine yazıyoruz daha sonra bize index numarası veriyor.
print(message.find("ayberk"))       # Pozitif bir değer veriyorsa aradığımız kelime yada veri mevcut, -1 yok demektir.
# find() soldan aramaya başlarken rfind() sağdan aramaya başlar.
# index() ve rindex() find metotlarına benzerler. Aranılan karakter karakter dizisinde yoksa ValueError hatası verecektir.
isim = "AYBERK"
print(isim)
print(isim.isupper())               # Tamamen büyük harflerden mi oluşuyor
print(isim.islower())               # Tamamen küçük harflerden mi oluşuyor
print("-----------------------------")
message1 ="  Boşluk  "              # Başta ve sonda 2 boşluk var
print(message1.strip())             # Boşluk karakterini silmek için
print(message1.lstrip())            # Sadece soldaki boşlukları silmek için
print(message1.rstrip())            # Sadece sağdaki.
araba = "araba"
print(araba.strip("a"))
print(araba.lstrip("a"))
print(araba.rstrip("a"))
print("-----------------------------")
is_found = message.startswith("H")  # H ile mi başlıyor
print(is_found)                     # True
is_found = message.startswith("*")  # * ile mi başlıyor
print(is_found)                     # False
is_found2 = message.endswith("n")   # n ile mi bitiyor
print(is_found2)
message = message.replace("*"," ")  # Cümle içerisinde bir arama yapar ve girilen veriyi değiştirir.
                                    # Yıldız karakterleri yerine boşluk kullansın
print(message)                      # .replace ard arda kullanabilirsin
print("-----------------------------")
message2 = "Kazandığınızdan en emin olduğunuz an, kaybetmeye en yakın olduğunuz andır."
message2 = message2.replace("an","zaman")
print(message2)                     # Her "an" geçen yeri "zaman"la değiştirecektir.
message = message.center(100)       # Verilen string ifadeyi 100 karakterlik bir bilgi içerisine alır ve tam ortalar
print(message)
message3 = "Beni 50 Karakter Ortala"
message3 = message3.center(50,"-")
print(message3)
print(message2.count("a"))          # Karakter dizisinin içerisinde belirlediği karakterden ya da karakter grubundan kaç tane olduğunu
sayılar = [1, 5, 10, 3, 20, 15, 1000, 2] # [1, 2, 3, 5, 10, 15, 20, 1000]
print(sorted(sayılar))              # Verileri küçükten büyüğe sıralamak için kullanılır
sırala = "harfler"                  # ['a', 'e', 'f', 'h', 'l', 'r', 'r']
print(sorted(sırala))
print(sorted("coğrafya"))           # Python sıralamayı kendi bünyesindeki sırasına göre yapıyor bu yüzden ğ en sonda.
import locale                       # locale kütüphanesini importladık
locale.setlocale(locale.LC_ALL,"Turkish_turkey.1254")
print(sorted("coğrafya", key = locale.strxfrm)) # ['a', 'a', 'c', 'f', 'ğ', 'o', 'r', 'y']
print("-----------------------------")
translation_table = str.maketrans("aeiou","12345")
message4 = "Bu bir karakter verisi!"
print(message4.translate(translation_table))
print("-----------------------------")
print(dir(""))                      # Bütün karakter dizisi yöntemlerini görmemizi sağlar