# Girilen bir sayının 0 - 100 arasında olup olmadığını kontrol ediniz.

sayi = int(input('Bir sayı giriniz: '))
print(f'Bu sayının ({sayi}), 0 ile 100 arasında olma durumu: {sayi > 0 and sayi < 100}')

# Aynı sayının pozitif ve çift sayı olup olmadığını kontrol ediniz.

print(f'Bu sayının ({sayi}), pozitif ve çift olma durumu: {(sayi % 2 == 0) and (0 < sayi)}')

# E-mail ve parola bilgileri ile giriş kontrolü yapın.

email ='kenan.ayberk@github.com'    # Sanki database'de kayıtlıymış gibi düşünelim.
paswrd = 'Abc2134!'
inputEmail = input('E-mail: ')
inputPswrd = input('Password: ')
print(f'Girilen Bilgilerinizin Doğruluğu: {email == inputEmail.strip() and paswrd == inputPswrd}')

# Girilen 3 sayıyı büyüklük olarak karşılaştırın

num_bir = float(input('1. sayıyı giriniz: ')) 
num_iki = float(input('2. sayıyı giriniz: ')) 
num_uc  = float(input('3. sayıyı giriniz: ')) 

print(f'1. Sayı({num_bir}) en büyüktür: {num_bir > num_iki and num_bir > num_uc}')
print(f'2. Sayı({num_iki}) en büyüktür: {num_bir < num_iki and num_iki > num_uc}')
print(f'3. Sayı({num_uc}) en büyüktür: {num_bir < num_uc and num_iki < num_uc}')

# Kullanıcıdan vize (%40) ve final (%60) notunu alıp ortalama hesabı yapın ve geçme durumunu karşılaştırın.
# Ortalama 50 olsa bile final notu en az 50 olmalıdır !
# Finalden eğer 70 ve üstü alınırsa ortalamanın hiçbir önemi olmasın !

vize = float(input('Vize Notunu Girin: '))
final = float(input('Final Notunu Girin: '))
vize1 = vize * 0.4
final1 = final * 0.6
ort = (vize1 + final1)
print(f'Not ortalaması: {ort}\nDersten geçme durumu: {(ort >= 50) or (final >=70)} ')
# Kişinin ad, soyad ve kilo bilgilerini alıp kilo indekslerini hesaplayın
# Formül = (Kilo / Boy^2)
# 0 - 18.4      --> Zayıf
# 18.5 - 24.9   --> Normal
# 25.0 - 29.9   --> Kilolu
# 30.0 - 34.9   --> Obez
name = input('Adınızı giriniz: ')
surname = input('Soyadınızı giriniz: ')
tall = float(input('Boyunuzu giriniz (metre): '))
kg = float(input('Kilonuzu giriniz: '))
formul = kg / (tall ** 2)
zayif = (formul >= 0) and (formul <=18.4)
normal = (formul > 18.4) and (formul <= 24.9)
kilolu = (formul > 24.9) and (formul <= 29.9)
obez = (formul > 29.9) and (formul <= 34.9)
print(f'{name +" "+ surname} kilo indeksiniz: {formul}\nKilo değerlendirmeniz zayıf: {zayif}')
print(100*'-')
print(f'{name +" "+ surname} kilo indeksiniz: {formul}\nKilo değerlendirmeniz normal: {normal}')
print(100*'-')
print(f'{name +" "+ surname} kilo indeksiniz: {formul}\nKilo değerlendirmeniz kilolu: {kilolu}')
print(100*'-')
print(f'{name +" "+ surname} kilo indeksiniz: {formul}\nKilo değerlendirmeniz obez: {obez}')
print(100*'-')
