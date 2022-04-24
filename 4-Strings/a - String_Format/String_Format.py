name = "Ayberk"
surname = "Özkan"
age = 24
print("My name is {} {}".format(name, surname))                 # Sırası önemli !
print("My name is {1} {0}".format(name, surname))               # İndex numarası ile sıralayabilirsin.
print("My name is {s} {n}".format(n = name, s = surname))       # Değişken tanımlayabilirsin.
print("My name is {} {} and I'm {}".format(name, surname, age)) # Tür Dönüşümü yapmadık.

result = 22 / 7
print(" The result is {}".format(result))
print(" The result is {r:1.4}".format(r = result)) 
# 1.4' ün sol kısmı yani 1 basamak kaydır. 4 ise virgülden sonra alınacak değer "5714"

# f string
print(f"My name is {name} {surname} and I'm {age}.")
