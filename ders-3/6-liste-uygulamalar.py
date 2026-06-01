# Uygulama 1: Öğrenci Kayıt ve Sıralama Sistemi (Temel Metotlar)
# Bu uygulama, bir öğretmenin sınıf listesini nasıl yöneteceğini simüle eder. 
# Eleman ekleme, silme, sayma ve alfabetik sıralama metotlarını içerir.

# 1. Başlangıçta boş bir sınıf listesi oluşturalım
sinif_listesi = ["Ahmet", "Zeynep", "Burak", "Ebru"]

# 2. Sınıfa yeni bir öğrenci kayıt oldu (Sona ekleme)
sinif_listesi.append("Can")

# 3. Listeye belirli bir sıradan (Araya) öğrenci ekleyelim (1. indekse)
sinif_listesi.insert(1, "Aslı")

# 4. Bir öğrenci okul değiştirdi, onu listeden silelim
sinif_listesi.remove("Burak")

# 5. Listeyi alfabetik olarak sıralayalım
sinif_listesi.sort()

# 6. Sınıf mevcudunu öğrenelim
mevcut = len(sinif_listesi)

print("----- SINIF RAPORU -----")
print(f"Mevcut Öğrenci Sayısı: {mevcut}")
print(f"Sıralı Liste: {sinif_listesi}")
print(f"İlk Sıradaki Öğrenci: {sinif_listesi[0]}")
print(f"Son Sıradaki Öğrenci: {sinif_listesi[-1]}")


# Uygulama 2: Sayısal Analiz ve Skor Tablosu (Matematiksel Fonksiyonlar)
# Bu uygulamada bir oyunun skorlarını tutuyoruz. 
# Listelerle kullanılan min(), max() ve sum() gibi gömülü fonksiyonların kullanımını göreceğiz.

# Oyuncuların aldıkları puanlar
skorlar = [150, 320, 85, 420, 210, 95]

# En yüksek ve en düşük skorları bulalım
en_yuksek = max(skorlar)
en_dusuk = min(skorlar)

# Toplam puanı ve ortalamayı hesaplayalım
toplam_puan = sum(skorlar)
oyuncu_sayisi = len(skorlar)
ortalama_skor = toplam_puan / oyuncu_sayisi

print("----- OYUN İSTATİSTİKLERİ -----")
print(f"Toplam Oyuncu: {oyuncu_sayisi}")
print(f"En Yüksek Skor: {en_yuksek}")
print(f"En Düşük Skor: {en_dusuk}")
print(f"Ortalama Skor: {ortalama_skor:.2f}") # Ondalık kısmı 2 basamağa sınırladık


# Uygulama 3: Dinamik Yapılacaklar Listesi (To-Do List)
# Bu uygulama, listenin en son elemanını koparıp alan .pop() metodunu ve bir elemanın listede olup 
# olmadığını kontrol eden in kontrolünü gösterir.

# Yapılacaklar listesi
gorevler = ["Python çalış", "E-postaları kontrol et", "Yürüyüş yap"]

# Listede belirli bir görevin olup olmadığını kontrol edelim
kontrol_edilecek = "Python çalış"
var_mi = kontrol_edilecek in gorevler
print(f"'{kontrol_edilecek}' listede var mı?: {var_mi}")

# Son görevi tamamladık varsayalım ve listeden çekelim (pop metodu)
tamamlanan_gorev = gorevler.pop() 

print("\n--- Güncelleme ---")
print(f"Tamamlanan ve Listeden Silinen Görev: {tamamlanan_gorev}")
print(f"Kalan Görevler: {gorevler}")