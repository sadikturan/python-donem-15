# Uygulama 1: 
# Kullanıcı Bilgi Düzenleyici (Temel Metotlar)
# Bu uygulama, kullanıcıdan gelen "hatalı" veya "düzensiz" verileri profesyonel bir görünüme kavuşturur.

# Kullanıcıdan gelen düzensiz veri
kirli_veri = "   pYtHon pRoGRamLaMa dİli   "

# 1. Başındaki ve sonundaki boşlukları temizleyelim
temiz_veri = kirli_veri.strip()

# 2. Hepsini küçük harfe çevirelim
kucuk_harf = temiz_veri.lower()

# 3. Sadece kelimelerin baş harflerini büyük yapalım
baslik_format = temiz_veri.title()

# 4. Belirli bir kelimeyi değiştirelim
yeni_metin = temiz_veri.replace("dİli", "Dünyası")

print(f"Ham Veri: '{kirli_veri}'")
print(f"Temizlenmiş: {temiz_veri}")
print(f"Başlık Formatı: {baslik_format}")
print(f"Değiştirilmiş: {yeni_metin}")


# Uygulama 2: Otomatik E-posta Oluşturucu (Birleştirme ve İndeksleme)
# Bu senaryoda, bir şirkete yeni giren personelin adı ve soyadından otomatik kurumsal e-posta adresi oluşturuyoruz.

ad = "Yusuf"
soyad = "Arslan"
sirket_uzantisi = "teknoloji.com"

# E-postayı adın baş harfi + soyad şeklinde oluşturalım
# ad[0] -> İsmin ilk harfini alır
# .lower() -> E-posta karakterlerini küçük harfe çevirir
eposta = (ad[0] + soyad).lower() + "@" + sirket_uzantisi

print(f"Personel Adı: {ad} {soyad}")
print(f"Oluşturulan E-posta: {eposta}")

# Uygulama 3: URL Temizleyici ve Analiz (Parçalama ve Kontrol)
# Bir web scraping veya otomasyon projesinde, gelen bağlantı adreslerini analiz etmeniz gerekebilir.

web_sitesi = "https://www.google.com"

# 1. URL güvenli mi? (https ile mi başlıyor?)
guvenli_mi = web_sitesi.startswith("https")

# 2. Sitenin sonu .com ile mi bitiyor?
com_mu = web_sitesi.endswith(".com")

# 3. URL uzunluğu nedir?
uzunluk = len(web_sitesi)

# 4. 'www' kısmını metinden ayıklayalım
temiz_url = web_sitesi.replace("https://www.", "")

print(f"Site: {web_sitesi}")
print(f"Güvenli Bağlantı: {guvenli_mi}")
print(f"Temizlenmiş Adres: {temiz_url}")
print(f"Karakter Sayısı: {uzunluk}")