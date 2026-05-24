# Uygulama 1: Kullanıcı Kayıt Paneli (Veri Tiplerini Tanıma)

# Farklı veri tiplerinde değişkenler tanımlayalım
kullanici_adi = "yazilimci_dostu"      # str (Metin)
takipci_sayisi = 1250                  # int (Tam Sayı)
hesap_puani = 4.8                      # float (Ondalıklı Sayı)
onayli_hesap_mi = True                 # bool (Mantıksal)

# Veri tiplerini kontrol edelim
print("--- Kullanıcı Profili ---")
print("Kullanıcı Adı Tipi:", type(kullanici_adi))
print("Takipçi Sayısı Tipi:", type(takipci_sayisi))
print("Hesap Puanı Tipi:   ", type(hesap_puani))
print("Onay Durumu Tipi:   ", type(onayli_hesap_mi))

# Uygulama 2: Yaş Hesaplayıcı (String -> Integer Dönüşümü)

dogum_yili_metin = input("Doğum yılınızı giriniz: ")

dogum_yili = int(dogum_yili_metin)
su_anki_yil = 2026
yas = su_anki_yil - dogum_yili

# Sonucu ekrana yazdırırken tekrar metne çevirelim (str + str birleşimi için)
print("Tahmini yaşınız: " + str(yas))

# Uygulama 3: İndirim Hesaplayıcı (Float -> String Dönüşümü)

# 1. Adım: Kullanıcıdan metinsel (String) veri alma
# input() varsayılan olarak string döndürdüğü için ekstra bir işleme gerek yoktur.
isim = input("Lütfen adınızı giriniz: ")

# 2. Adım: Kullanıcıdan ondalıklı sayı (Float) veri alma
# Fiyat kuruşlu olabileceği için input'u float() ile sarmalıyoruz.
ham_fiyat = float(input("Almak istediğiniz ürünün fiyatını girin (TL): "))

# 3. Adım: Kullanıcıdan tam sayı (Integer) veri alma
# Adet miktarı buçuklu olamayacağı için input'u int() ile sarmalıyoruz.
adet = int(input("Kaç adet satın almak istiyorsunuz?: "))

# Eğer yukarıda float() ve int() dönüşümlerini yapmasaydık, 
# Python metinlerle matematiksel çarpma yapamayacağı için sistem çökecekti.
toplam_tutar = ham_fiyat * adet

# 4. Adım: Sonuçları kullanıcıya dinamik olarak gösterme
print("\n" + "-"*40)
# Virgül kullandığımızda Python araya otomatik olarak bir adet boşluk bırakır

print("Hoş geldin,", isim, "!")
print("-> Seçtiğiniz ürünün birim fiyatı:", ham_fiyat, "TL")
print("-> Talep ettiğiniz miktar:", adet, "adet")
print("Toplam Ödemeniz Gereken Tutar:", toplam_tutar, "TL")

print("-"*40)
