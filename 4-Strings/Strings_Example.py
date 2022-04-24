website = "https://github.com/AyberkOzkan"
amac = "Sıfırdan Python Programlama Öğreniyorum."

# 'amac' karakter dizisinde kaç karakter bulunmaktadır?

print(len(amac))
# 'website' içinden github karakterlerini alın.
print(website[8:14])
# 'website' içinden Ayberk karakterlerini alın.
print(website[19:25])
# 'amac' içinden ilk 15 ve son 15 karakteri alın.
print(amac[:15])
print(amac[25:40])
print(amac[-15:])
# 'amac' ifadesindeki karakterleri tersten yazdırın.
print(amac[::-1])
name, surname, age, job = "Ayberk", "Özkan", 24, "Mühendis"
# Verilen değişkenlerle aşağıdaki ifadeyi yazdırın.
# Benim adım Ayberk Özkan, Yaşım 24 ve mesleğim Mühendis.

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.") 

# Hello World ifadesindeki W harfini w ile değiştirin

hw = "Hello World"
hw = hw[0:6] + "w" + hw[7:11]
print(hw)
# hw.replace("W","w") 
# abc ifadesini yan yana 3 defa yazdırın

print("abc"*3)