names = ["Kenan", "Deniz", "Ayberk", "Rüzgar"]
dates = [1996, 1998, 1998, 1988]

# "Murat" ismini listenin sonuna ekleyin.
names.append("Murat")
print(names)
# Alternatif olarak names.insert(len(names),"Murat") ile sonuna eklenebilir
# "Toprak" değerini listenin başına ekleyin.
names.insert(0,"Toprak")
print(names)
# "Rüzgar" ismini listeden silin.
names.remove("Rüzgar")
print(names)
# names.pop() ile istenilen index'e göre silebilirsin.
# "Deniz" isminin indeksi nedir?
print(names.index("Deniz"))
# "Ayberk" listenin elemanı mıdır?
print("Ayberk" in names)
# index metodu ile de bulabilirsin.
# names liste elemanlarını ters çevirin.
names.reverse()
print(names)
# names liste elemanlarını alfabetik olarak sıralayın.
names.sort()
print(names)
# dates listesini rakamsal büyüklüğe göre sıralayın.
dates.sort
print(dates)
# str = "Audi,Opel" karakter dizisini listeye çevirin.
str = "Audi,Opel"
str = str.split(",")
print(str)
# dates dizisinin en büyük ve en küçük elemanını bulun.
print(max(dates))
print(min(dates))
# dates dizisinde kaç tane 1998 değeri vardır?
print(dates.count(1998))
# dates dizinin tüm elemanlarını silin.
dates.clear()
print(dates)
# Kullanıcıdan alacağınız 3 isim bilgisini bir listede saklayın.
markalar = []
marka = input("1. Markayı Girin: ")
markalar.append(marka)
marka = input("2. Markayı Girin: ")
markalar.append(marka)
marka = input("3. Markayı Girin: ")
markalar.append(marka)
print(markalar)