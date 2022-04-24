""" 

    Üç harften oluşan bir karakter dizisi tanımlayın ve bu karakter dizisinin ögelerine indeksler
yardımıyla baştan ve tersten olmak üzere iki ayrı şekilde ulaşıp ekrana yazdırın.

                                                                                """

s = "Pyt"

print(s[0])
print(s[1])
print(s[2])
print("--------------------")
print(s[-1])
print(s[-2])
print(s[-3])

"""
    Aşağıdaki değişkenin ilk 10 karakterini döngü kullanmadan ekrana bastırın.
                                                                                """
d = "Karakterler önemli değişkenlerdir"
print(d[:10])

"""
    Aşağıdaki paragrafta geçen kelimelerden en uzun olanı bulunuz ve görüntüleyiniz.
max() metotunu kullanın.
                                                                                """

paragraf = """Python'un son derece kolay okunabilir olması düşünülmüştür. Bu yüzden örneğin küme parantezleri yerine girintileme işlemi kullanılır. Hatta bazı durumlarda girintileme işlemine dahi gerek kalmadan kodun ilgili bölümü tek satırda yazılabilir. Böylece Python, program kodunuzu en az çaba ile ve hızlıca yazmanıza imkan tanır. Sade söz dizimi ile diğer programlama  dillerinden üstündür."""
paragraf = paragraf.split()
en_uzun_kelime = max(paragraf, key= len) 
print(en_uzun_kelime)

"""
    Aşağıdaki cümlede "programlama" kelimesinin hangi indekste başladığını bulun.
                                                                                """
cumle = " Bilgisayarların donanıma nasıl davranacağını anlatan, bilgisayara yön veren komutlar, kelimeler, aritmetik işlemlerdir. Diğer bir tanım verecek olursak programlama, bilgisayar programlarının yazılması, test edilmesi ve bakımının yapılması sürecine verilen isimdir."

print(cumle.index("programlama"))

"""" 
    Bir siteye üyelikte girilecek isimlerin veri tabanında tamamen büyük harflerden
oluşacak şekilde kaydedileceğini varsayalım. Bir kullanıcı ismi tanımlayın ve 
kullanıcının isminin bütün harflerini büyük harflere çeviren bir kod yazın.
                                                                                """
ad_soyad = "Ayberk Özkan"
ad_soyad = ad_soyad.upper()
print(ad_soyad)

""" Verilen cümlenin başındaki ve sonundaki özel sembolleri çıkarın. Daha sonra 
Türkçe ünlü harfler olan İ, Ö, Ü, ü, ö harflerini I, O, U, u ve o ile değiştirin.
                                                                                """
cumle2 = "<<Öz, İl, ülke, Ülkem, göl>>"
cumle2 = cumle2.lstrip("<<")
cumle2 = cumle2.rstrip(">>")
cumle2 = cumle2.replace("Ö","O").replace("İ","I").replace("Ü","U").replace("ü","u").replace("ö","o")
print(cumle2)
