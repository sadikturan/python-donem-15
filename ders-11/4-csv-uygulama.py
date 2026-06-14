import csv
import os

# --- GİRDİ VE KONTROL AŞAMASI ---
print("====== İLERİ DÜZEY KİTAP ANALİZ SİSTEMİ ======")

hedef_yil = input("Analiz etmek istediğiniz yılı girin (2009-2019): ").strip()
hedef_tur = input("Kitap türünü girin (Fiction / Non Fiction): ").strip().title()

# Filtreleme için boş kaplar hazırlıyoruz
filtrelenmis_kitaplar = []
toplam_fiyat = 0

try:
    # 1. ADIM: CSV Dosyasını Sözlük Biçiminde Okuma (Extract)
    with open("bestselling-books.csv", "r", encoding="utf-8") as file:
        okuyucu = csv.DictReader(file)
        
        # 2. ADIM: Satır Satır Gezme ve Filtreleme (Transform)
        for satir in okuyucu:
            # Dosyadan gelen verileri kendi filtrelerimizle kıyaslıyoruz
            if satir["Year"] == hedef_yil and satir["Genre"] == hedef_tur:
                
                # Sayısal hesaplamalar yapacağımız için veri tiplerini dönüştürüyoruz
                fiyat = int(satir["Price"])
                yorum = int(satir["Reviews"])
                puan = float(satir["User Rating"])
                
                # Filtreye uyan kitabı listeye ekliyoruz
                filtrelenmis_kitaplar.append({
                    "Name": satir["Name"],
                    "Author": satir["Author"],
                    "User Rating": puan,
                    "Reviews": yorum,
                    "Price": fiyat
                })
                
                # Ortalama için kümülatif toplam alıyoruz
                toplam_fiyat += fiyat

    # 3. ADIM: Metriklerin Hesaplanması (Analiz)
    kitap_sayisi = len(filtrelenmis_kitaplar)
    
    if kitap_sayisi == 0:
        print(f"\n UYARI: {hedef_yil} yılında '{hedef_tur}' türünde hiçbir kitap bulunamadı!")
    else:
        # A) Ortalama Fiyat Hesaplama
        ortalama_fiyat = round(toplam_fiyat / kitap_sayisi, 2)
        
        # B) En Çok Yorum Alan (En Popüler) Kitabı Bulma
        # max() fonksiyonuna 'key' olarak bir lambda vererek en yüksek 'Reviews' değerine sahip sözlüğü seçiyoruz
        en_populer_kitap = max(filtrelenmis_kitaplar, key=lambda x: x["Reviews"])
        
        # C) Analiz Sonuçlarını Ekrana Yazdırma (Raporlama)
        print("\n" + "="*45)
        print(f"{hedef_yil} - {hedef_tur} ANALİZ SONUÇLARI")
        print("="*45)
        print(f"Filtreye Uyan Toplam Kitap Sayısı : {kitap_sayisi}")
        print(f"Bu Grubun Ortalama Kitap Fiyatı  : {ortalama_fiyat} USD")
        print(f"En Popüler (En Çok Yorumlanan) Kitap:")
        print(f" -> İsim  : {en_populer_kitap['Name']}")
        print(f" -> Yazar : {en_populer_kitap['Author']}")
        print(f" -> Yorum : {en_populer_kitap['Reviews']} adet")
        print("="*45)
        
        # 4. ADIM: Sonuçları Yeni Bir CSV Dosyasına Noktalı Virgülle Yazma (Load)
        # Sütun isimlerimizi belirliyoruz
        alanlar = ["Kitap_Adi", "Yazar", "Puan", "Yorum_Sayisi", "Fiyat_USD", "Analiz_Yili", "Tur"]
        
        # Excel'in doğrudan tablo yapabilmesi için delimiter=";" kullanıyoruz
        with open("analiz_raporu.csv", "w", encoding="utf-8", newline="") as rapor_dosyasi:
            yazar = csv.DictWriter(rapor_dosyasi, fieldnames=alanlar, delimiter=";")
            
            # Başlıkları yazalım
            yazar.writeheader()
            
            # Verilerimizi DictWriter'ın beklediği formata (alanlar ile eşleşen sözlüklere) dönüştürüp yazıyoruz
            for k in filtrelenmis_kitaplar:
                yazar.writerow({
                    "Kitap_Adi": k["Name"],
                    "Yazar": k["Author"],
                    "Puan": k["User Rating"],
                    "Yorum_Sayisi": k["Reviews"],
                    "Fiyat_USD": k["Price"],
                    "Analiz_Yili": hedef_yil,
                    "Tur": hedef_tur
                })
                
        print("\n✔️ 'analiz_raporu.csv' dosyası noktalı virgül ayırıcısı ile başarıyla diske kaydedildi.")

except FileNotFoundError:
    print("\n HATA: 'bestselling-books.csv' kaynak dosyası bulunamadı! Lütfen dosya adını kontrol edin.")
except Exception as e:
    print(f"\n Beklenmedik bir hata oluştu: {e}")