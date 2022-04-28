# "Ferrari, BMW, Jaguar, TESLA" create a list with these elements.
cars = ["Ferrari", "BMW", "Jaguar", "TESLA"]
print(cars)
# This list has a how many elements?
print(len(cars))
# What is the list first and last element?
print(cars[0])
print(cars[-1])
# Change "jaguar" to "Lamborghini"
cars[2] = "Lamborghini"
print(cars)
# Is TESLA a element of the list?
print(cars.index("TESLA"))
print("TESLA" in cars)
# What is the value at index -2 of the list
print(cars[-2])
# Take the first three element in list
print(cars[:3])
# Substitute "Opel" and "Mercedes" for the last 2 elements of the list.
cars[-2:] = ["Opel", "Mercedes"]
print(cars)
#Add "Audi" and "Nissan" the top elements of the list.
cars.insert(0,"Audi")
cars.insert(0,"Nissan")
print(cars)
# Delete the last element of the list.
cars.pop(-1)
print(cars)
# Print the list elements in reverse
cars.reverse()
print(cars)
# Store the following data in a list.

        # student_A: SELEN ERTAN,       (70, 60, 60)
        # student_B: ZELİHA YARADILMIŞ, (80, 80, 70)
        # student_C: ESRA CAN OLMUŞ,    (60, 90, 70)
student_A = "SELEN ERTAN", [70, 60, 60]
student_B = "ZELİHA YARADILMIŞ", [80, 80, 70]
student_C = "ESRA CAN OLMUŞ", [60, 90, 70]
students = student_A + student_B + student_C
# Print the list elements to the screen.
print(students)
print(student_A[0])
print(student_B[1])
print(student_C[1])
print(student_C[1][1])
