"""
Bu bölümde, Python kodlarımızın içinden uzak sunuculara nasıl bağlanacağımızı, nasıl veri isteyeceğimizi (GET) ve gelen verileri nasıl işleyeceğimizi Python'ın en popüler kütüphanesi olan requests ile öğreneceğiz.

1. requests Kütüphanesi Kurulumu
requests, Python'ın içinde gömülü olarak gelmez. Harici bir üçüncü parti (third-party) modül olduğu için projemize başlamadan önce terminal veya komut satırına şu komutu yazarak bilgisayarımıza indirmeliyiz:

pip install requests

Kurulum tamamlandıktan sonra, kod dosyamızın en üstüne import requests yazarak kütüphaneyi kullanmaya hazır hale geliriz.

"""

# 2. İlk HTTP İsteğini Fırlatmak (requests.get)

import requests

# 1. İstek atacağımız API adresini (URL) belirliyoruz
url = "https://jsonplaceholder.typicode.com/todos/1"

# 2. GET isteğini fırlatıyoruz ve gelen yanıtı bir değişkene eşliyoruz
yanit = requests.get(url)

# 3. Sunucudan gelen Durum Kodunu (Status Code) kontrol ediyoruz
print(f"Durum Kodu: {yanit.status_code}") # Çıktı: 200 (Yani her şey başarılı)

# 3. Gelen Yanıtı JSON (Sözlük) Formatına Çevirmek

# Sunucu bize 200 durum koduyla olumlu döndüğünde, gönderdiği paketlerin içindeki ham veriyi Python'da işleyebilmek için .json() metodunu kullanırız. Bu metot, gelen veriyi anında bir Python Sözlüğüne (Dictionary) dönüştürür.

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
yanit = requests.get(url)

if yanit.status_code == 200:
    # Gelen ham metni Python sözlüğüne çeviriyoruz
    veri = yanit.json()
    
    print("--- API'den Gelen Sözlük Verisi ---")
    print(veri)
    print(type(veri)) # Çıktı: <class 'dict'>
    
    # Artık standart sözlük metotlarıyla verileri cımbızla çekebiliriz:
    print(f"Görev Başlığı: {veri['title']}")
    print(f"Tamamlandı mı?: {veri['completed']}")
else:
    print(f"HATA: Veri çekilemedi. Hata kodu: {yanit.status_code}")

# 4. Tüm Listeyi Çekmek ve Döngü ile Dönmek

import requests

# 🎯 Sonunda ID yok, yani tüm listeyi istiyoruz
url = "https://jsonplaceholder.typicode.com/todos"

yanit = requests.get(url)

if yanit.status_code == 200:
    # Gelen veri bir liste (list) formatındadır
    gorevler_listesi = yanit.json()
    
    print(f"Toplam Çekilen Görev Sayısı: {len(gorevler_listesi)}\n")
    print("--- İLK 5 GÖREVİN RAPORU ---")
    print("-" * 40)
    
    # Listenin çok uzun olup ekranı doldurmaması için sadece ilk 5 elemanı [0:5] dönüyoruz
    for gorev in gorevler_listesi[0:5]:
        print(f"Görev ID : {gorev['id']}")
        print(f"Başlık   : {gorev['title']}")
        print(f"Durum    : {'Tamamlandı' if gorev['completed'] else 'Bekliyor'}")
        print("-" * 40)
        
else:
    print(f"HATA: Bağlantı başarısız. Kod: {yanit.status_code}")

# 5. Çekilen Liste Üzerinde Veri Analizi Yapmak

import requests

url = "https://jsonplaceholder.typicode.com/todos"
yanit = requests.get(url)

if yanit.status_code == 200:
    gorevler = yanit.json()
    
    # Analiz A: List Comprehension ile sadece tamamlanmış görevleri süzüyoruz
    tamamlanmis_gorevler = [g for g in gorevler if g["completed"] == True]
    
    # Analiz B: Bekleyen görevlerin sayısını matematiksel olarak buluyoruz
    toplam_gorev = len(gorevler)
    tamamlanan_sayisi = len(tamamlanmis_gorevler)
    bekleyen_sayisi = toplam_gorev - tamamlanan_sayisi
    
    # Başarı yüzdesini hesaplayalım
    basari_yuzdesi = (tamamlanan_sayisi / toplam_gorev) * 100
    
    print("=== API GÜN SONU PERFORMANS RAPORU ===")
    print(f"Toplam Görev Sayısı     : {toplam_gorev}")
    print(f"Tamamlanan Görev Sayısı : {tamamlanan_sayisi}")
    print(f"Bekleyen Görev Sayısı    : {bekleyen_sayisi}")
    print(f"Şirket Başarı Yüzdesi   : %{basari_yuzdesi:.2f}")