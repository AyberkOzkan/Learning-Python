# Girilen 2 sayıdan hangisi büyüktür?
bir = int(input('1. Sayıyı Giriniz: '))
iki = int(input('2. Sayıyı Giriniz: '))
print(f'1. Sayı ({bir}) 2. Sayıdan ({iki}) büyüktür: {bir > iki}')
# if bloklarını henüz öğrenmedik. Öğrendiklerimizden yola çıkarak yapıyoruz.
# Kullanıcıdan Vize (%40) ve Final(%60) notunu alıp ortalama hesaplayın.

vize = float(input('Vize Notunu Girin: '))
final = float(input('Final Notunu Girin: '))
vize = vize * 0.4
final = final * 0.6
ort = (vize + final)
print(f'Not Ortalamanız: {ort} \nDersten Geçme Durumunuz: {ort >=50}')

# Girilen bir sayının tek mi çift mi olduğunu yazdırın.
a = int(input('Bir sayı giriniz: '))
cift = (a % 2 == 0)
print(f'Girilen sayının Çift olma durumu: {cift}')
# Aynı sayının negatif mi pozitif mi olduğunu yazdırın.
print(f'Girilen sayının pozitif olma durumu: {a > 0}')
# Parola ve E-mail bilgisini isteyip doğruluğunu kontrol edin.
# (email: kenan.ayberk@github.com parola: Abc2134!)     

email ='kenan.ayberk@github.com'    # Sanki database'de kayıtlıymış gibi düşünelim.
paswrd = 'Abc2134!'
inputEmail = input('E-mail: ')
inputPswrd = input('Password: ')
print(f'Girilen E-mail adresi: {email == inputEmail.strip()}\nŞifre: {paswrd == inputPswrd}')
# Eğer kullanıcı mail adresini girerken yanlışlıkla başına veya sonuna boşluk girerse False değeri karşımıza çıkacaktır.
# Bunu önlemek için .strip() kullandık