# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
numbers = [4, 6, 8, 4, 10, 16, 4]
letters = ["a", "y", "b", "e", "r", "k"]

print(min(numbers))               # Min. değeri yazdırır.         
print(max(numbers))               # Max. değeri yazdırır.         
print(max(letters))               # Alfabetik olarak yazar        
print(min(letters))

print(numbers[3:6])               # 4 10 16                        
print(numbers[4:])                # 10 16 4

numbers[4] = 40                   # İstediğimiz elemanı değiştirebiliriz.
print(numbers)

numbers.append("49")              # Eleman ekleme
print(numbers)

numbers.insert(3, 78)             # İstediğimiz yerden ekleme
print(numbers)

numbers.insert(-1,44)             # Insert ile en sona ekleme
print(numbers)
numbers.pop()                     # En sondaki elemanı siler (-1) de yazılabilir
print(numbers)
numbers.pop(0)                    # En baştakini siler
print(numbers)

numbers.remove(78)                # 78 i siler
print(numbers)

numbers.sort()                    # Sıralama yapmak için
letters.sort()
print(numbers)
print(letters)

numbers.reverse()                 # Tam tersine çevirmek
print(numbers)
letters.reverse()
print(letters)

print(len(numbers))               # Eleman sayısı bulmak
print(len(letters))

print(numbers.count(4))           # istediğimiz elemanı saymak
print(letters.count("a"))

numbers.clear()                   # Tüm elemanları siliyor.
print(numbers)