github = "https://github.com/AyberkOzkan"
ataturk = "Zafer, 'Zafer benimdir' diyebilenindir. Başarı ise, 'Başaracağım' diye başlayarak sonunda 'Başardım' diyebilenindir."

# " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
hw = " Hello World "
print(hw.strip())
#  "https://github.com/AyberkOzkan" AyberkOzkan dışındaki her karakteri silin.
github1 = "https://github.com/AyberkOzkan"
github1 = github1.strip("https://github.com/")
print(github1)
# "ataturk" karakter dizisinin tüm karakterlerini büyük harf yapın.
print(ataturk.upper())
# "github" içinde kaç tane "a" harfi vardır?
print(github.count("a"))
# "github", "https" ile başlayıp "com" ile bitiyor mu?
print(github.startswith("https"))
print(github.endswith("com"))
# "github" içinde .com ifadesi var mı?
print(github.find(".com"))
print(github.index(".com"))
# "ataturk" içindeki karakterlerin hepsi alfabetik mi? (Harflerden mi oluşur?)
print(ataturk.isalpha())
print(ataturk.isspace())
print(ataturk.istitle())
print(ataturk.islower())
print(ataturk.isupper())
print(ataturk.isalnum())
print(ataturk.isdigit())    # Rakamlar için
# "Python" ifadesini satırda 50 karakter içine yerleştirip sağına ve soluna "-" ekleyin
py = "Python"
print(py.center(50,"-"))
print(py.ljust(50,"-"))
print(py.rjust(50,"-"))
# "ataturk" karakter dizisindeki tüm boşluk karakterlerini "*" ile değiştirin.
print(ataturk.replace(" ","*"))
print(ataturk.replace(" ","*",6))
# "Hello World" karakter dizisin "Hello" ifadesini "This" olarak değiştirin.
print(hw.replace("Hello","This"))
# "ataturk" karakter dizisini boşluk karakterlerinden ayırın.
print(ataturk.split(" "))
