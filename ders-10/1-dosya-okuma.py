"""
Dosya Okuma: Python'da dosya okuma işlemi, `open()` fonksiyonu kullanılarak gerçekleştirilir. Dosya okuma modunda açmak için `'r'` parametresi kullanılır. Dosya açıldıktan sonra, içeriği okumak için çeşitli yöntemler vardır:

- `read()`: Dosyanın tamamını okur.
- `readline()`: Dosyanın sadece bir satırını okur.
- `readlines()`: Dosyanın tüm satırlarını bir liste olarak döndürür.

Dosya okuma işlemi tamamlandıktan sonra, dosyayı kapatmak önemlidir. Bu, `close()` yöntemi ile yapılır veya `with` ifadesi kullanılarak otomatik olarak yapılabilir.
"""

# 1. Geleneksel Yöntem: open() ve close()

# Bir dosyayı açtığımızda, işletim sisteminde gereksiz kilitlenmeler ve bellek sızıntıları yaşanmaması için işimiz bittiğinde close() metodu ile dosyayı kapatmak zorundayız.

# 1. Dosyayı okuma modunda açma
file = open('ornek.txt', 'r', encoding='utf-8')

# 2. Dosyanın tamamını tek bir metin (string) olarak okuma
content = file.read()
print("--- Geleneksel Okuma Çıktısı ---")
print(content)

# 3. Dosyayı kapatma (Zorunlu adım)
file.close()

# Kontrol: Dosya kapandı mı? (True döner)
print(f"Dosya kapandı mı?: {file.closed}")

# 2. Profesyonel ve Güvenli Yöntem: with open

# Büyük projelerde close() komutunu unutmak büyük bir risktir. with yapısı altındaki kod bloğu bittiği an dosyayı arka planda otomatik olarak kapatır.

# Ayrıca dosyanın sistemde bulunamaması riskine karşı bu yapıyı Hata Yönetimi (try-except) ile sarmalamak en doğru yaklaşımdır.

try:
    with open('ornek.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("\n--- 'with' Bloğu Okuma Çıktısı ---")
        print(content)
except FileNotFoundError as e:
    print(f"HATA: Okunmak istenen dosya bulunamadı! Detay: {e}")
finally:
    print("Dosya okuma süreci tamamlandı.")

# 3. Satır Satır Okuma ve Hafıza Yönetimi

# Çok büyük boyutlu dosyaları (Örn: 2 GB'lık bir log dosyası) read() ile tek seferde RAM belleğe yüklemek bilgisayarı kilitleyebilir. Bunun yerine satır satır okuma teknikleri kullanılır:

# A) readline() Yöntemi
# Dosyayı baştan başlayarak sadece tek bir satır okur. Her çağrıldığında bir sonraki satıra geçer.

with open('ornek.txt', 'r', encoding='utf-8') as file:
    print("\n--- Sadece İlk İki Satır ---")
    print(file.readline(), end="") # 1. Satır
    print(file.readline(), end="") # 2. Satır

# B) En Verimli Yol: Dosya Üzerinde for Döngüsü

# Büyük veri setlerinde dosyayı RAM'e yüklemeden, diskten satır satır akıtarak okumanın en performanslı yoludur.

with open('ornek.txt', 'r', encoding='utf-8') as file:
    print("\n--- For Döngüsü İle Performanslı Okuma ---")
    for satir in file:
        # end="" parametresi, dosyadaki gizli \n karakterinin üzerine 
        # print'in kendi alt satıra geçme özelliğinin eklenmesini engeller.
        print(satir, end="")

# 4. Veri Analizi için readlines() ve List Comprehension

# readlines() metodu dosyadaki tüm satırları okur ve bize bir liste (list) verir. Ancak her satırın sonundaki görünmez \n (alt satıra geçme) karakterini de listeye dahil eder.

# Veri analitiğinde bu \n karakterlerini temizlemek için List Comprehension ve .strip() metodu harika bir ikilidir:

# Temizlenmemiş Ham Liste Çıktısı
with open('ornek.txt', 'r', encoding='utf-8') as file:
    ham_icerik = file.readlines()
    print("\n\n--- Temizlenmemiş Ham Liste (readlines) ---")
    print(ham_icerik) 
    # Çıktı: ['Satır 1\n', 'Satır 2\n', 'Satır 3'] gibi kirli olur.

# List Comprehension İle Temizlenmiş Liste Çıktısı
with open('ornek.txt', 'r', encoding='utf-8') as file:
    # line.strip() metodu satırın başındaki ve sonundaki tüm boşlukları/gizli karakterleri uçurur.
    temiz_icerik = [line.strip() for line in file.readlines()]
    
    print("\n--- List Comprehension İle Temizlenmiş Liste ---")
    print(temiz_icerik)
    # Çıktı: ['Satır 1', 'Satır 2', 'Satır 3'] şeklinde tertemiz olur.

