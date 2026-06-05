# 1. if Yapısı (Eğer)

if True:
    print("true")

yas = 20

kosul = (yas >= 18)

if kosul:
    print("Ehliyet alabilirsiniz.") # Bu satır sadece yaş 18 veya büyükse çalışır.
print("Bu kod if'ten bağımsız.")    # Girintisiz: Şart ne olursa olsun her zaman çalışır.

username = "sadikturan"
password = "12345"

if (username == "sadikturan" and password == "12345"):
    print("Giriş başarılı")

# 2. else Yapısı (Değilse)

hava_yagmurlu_mu = False

if hava_yagmurlu_mu == True:
    print("Şemsiyeni al.")
else:
    print("Şemsiyeye gerek yok, hava güzel.")

# 3. elif Yapısı (Eğer Değilse Ama Şöyleyse)

ogrenci_notu = 75

if ogrenci_notu >= 85:
    print("Harf Notu: AA")
elif ogrenci_notu >= 70:
    print("Harf Notu: BB") # 75 bu şarta uyduğu için sadece burası çalışır.
elif ogrenci_notu >= 50:
    print("Harf Notu: CC")
else:
    print("Maalesef kaldınız.")


yas = int(input("Yaşınızı giriniz: "))

if yas >= 18:
    # Bu blok sadece yaş 18 veya daha büyükse çalışır
    print("Ehliyet alabilirsiniz! 🎉")
    
elif yas == 17:
    # İlk şart uymadıysa ama yaş tam 17 ise burası çalışır
    print("Ehliyet alamazsınız ama sürücü kursuna kaydolabilirsiniz. 🚗")
    
else:
    # Yukarıdaki şartların hiçbiri uymadıysa (yaş 17'den küçükse) burası çalışır
    kalan_yil = 18 - yas
    print("Ehliyet alamazsınız. Büyümek için", kalan_yil, "yıl daha beklemelisiniz. 🛑")