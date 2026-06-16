# 1. Temel HTML Çekme Kodu
# Bir web sayfasının HTML kodunu metin formatında indirmek için requests.get() fonksiyonunun ardından .text özelliğini kullanırız.

import requests

# 1. Hedef web sitesinin adresini belirliyoruz
url = "https://example.com"

# 2. Sunucuya HTTP GET isteği gönderiyoruz
yanit = requests.get(url)

# 3. Bağlantının başarılı olup olmadığını kontrol ediyoruz (200 OK)
if yanit.status_code == 200:
    # 4. Sayfanın ham HTML kodlarını '.text' ile alıyoruz
    ham_html = yanit.text
    
    print("--- Siteden İndirilen Ham HTML Kodları ---")
    print(ham_html[0:500]) # Ekranı doldurmaması için sadece ilk 500 karakteri basıyoruz
else:
    print(f"Bağlantı hatası! Durum Kodu: {yanit.status_code}")



# 2. Gerçek Hayattaki Büyük Sorun: Bot Engelleri ve Güvenlik Duvarları

# Yukarıdaki kod example.com gibi korumasız sitelerde pürüzsüz çalışır. Ancak gerçek hayatta büyük e-ticaret, ilan veya haber sitelerini kazımaya çalıştığınızda sunucu size büyük ihtimalle 403 Forbidden (Erişim Engellendi) hatası fırlatır veya boş bir sayfa döndürür.

# Peki neden?
# Çünkü modern web siteleri kendilerini botlara ve siber saldırılara karşı korur. requests kütüphanesi varsayılan haliyle bir siteye istek attığında, sunucuya gizlice şu mesajı gönderir: "Ben bir Python yazılımıyım ve senin siteni kazımaya geldim." Sunucu da bot olduğunu anladığı an kapıyı yüzünüze kapatır.

# 3. Çözüm: headers (User-Agent) ile Kendini Tarayıcı Gibi Göstermek

# Bu engeli aşmak için istek paketimizin içine headers (Başlık Bilgileri) eklemeliyiz. Başlıkların içine yazacağımız User-Agent kimliği sayesinde Python kodumuzu sunucuya "Ben Python değilim; Google Chrome kullanan gerçek bir insanım" şeklinde tanıtırız.

# Gelin, gerçek bir web sitesine tarayıcı maskesi takarak güvenli bir şekilde istek atalım:

import requests

url = "https://www.n11.com/" 

# Sunucuyu gerçek bir insan olduğumuza ikna etmek için tarayıcı kimliği (User-Agent) tanımlıyoruz
tarayici_maskesi = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# İsteği fırlatırken 'headers' parametresine bu maskeyi bağlıyoruz
yanit = requests.get(url, headers=tarayici_maskesi)

if yanit.status_code == 200:
    print("Sunucu bizi gerçek bir tarayıcı sandı ve kapıyı açtı!")
    print("-" * 50)
    
    # HTML içeriğini ekrana basıyoruz
    html_icerik = yanit.text
    print(html_icerik[0:300]) # İlk 300 karakter
else:
    print(f"Engellendik veya Sayfa Bulunamadı! Kod: {yanit.status_code}")


# Özet Kural

# requests.get(url).text komutu, hedef web sayfasının sunucusunda duran tüm HTML iskeletini bir bütün halinde bilgisayarımızın hafızasına indirir.

# Gerçek ve korumalı web sitelerinde çalışırken sunucunun güvenlik duvarına takılmamak için her zaman headers={"User-Agent": "..."} maskesini kullanmak profesyonel bir zorunluluktur.

# Bu indirdiğimiz ham HTML metni şu an için çok karmaşık ve düzensizdir. Bir sonraki adımda, bu inen metnin içindeki etiketleri ayıklamak için öğrendiğimiz BeautifulSoup havuzuna bu içeriği boşaltacağız.