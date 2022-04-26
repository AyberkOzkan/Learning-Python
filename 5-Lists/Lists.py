# A list contains items separated by commas and enclosed within square brackets[]
# Lists are almos similar to arrays in C
# One difference is that all the items belonging to a list can be of different data type.

message = " Hello there. I will be a list".split() # Split ile listeye çeviririz.
print(message)
print(message[0])
print(message[1])
print(message[2])

my_list = [1, 2.4,"üç", True]
print(my_list)

list1 =["one", "two", "three"]
list2 =["four", "five", "six"]
numbers = list1 + list2
print(numbers)                  # ['one', 'two', 'three', 'four', 'five', 'six']
print(len(numbers))             # 6
userA = ["Ayberk", 24]
userB = ["Kenan", 22]
print(userA)
print(userB)
users = [userA, userB]           # Dizi içerisinde dizi saklamak yani liste içinde liste.
print(users)
print(users[0])
print(users[1])
x = users[1]
print(x[0])                      # Dizinin içerisindeki elemana ulaşırız. Böyle yazmak yerine;
print(users[1][0])               # Users'ın önce 2. elemanı daha sonra içerisindek dizinin 1. elemanı
