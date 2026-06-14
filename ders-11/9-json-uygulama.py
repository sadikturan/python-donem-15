import json
import os

# Veritabanı olarak kullanılacak dosya adı
DB_FILE = "kitaplik.json"

# --- 1. YARDIMCI FONKSİYONLAR (OKUMA VE YAZMA) ---

def veritabani_oku():
    """Diskteki JSON dosyasını okur ve Python listesi olarak döner."""
    if not os.path.exists(DB_FILE):
        # Dosya henüz yoksa, başlangıç için boş bir liste oluştur ve kaydet
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []
    
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Dosya bozuk veya boş kalmışsa sıfırla
        return []

def veritabani_yaz(veri):
    """Gelen Python listesini JSON formatına çevirip diske kalıcı olarak yazar."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        # indent=4 ile dosyayı okunabilir yapıyoruz, ensure_ascii=False ile Türkçe karakterleri koruyoruz
        json.dump(veri, f, indent=4, ensure_ascii=False)


# --- 2. ANA İŞLEM FONKSİYONLARI (CRUD & FILTER) ---

def kitap_ekle(isim, yazar, fiyat, tur):
    """Veritabanına benzersiz ID ile yeni bir kitap ekler."""
    kitaplar = veritabani_oku()
    
    # Basit bir benzersiz ID mekanizması (Eğer liste boşsa ID: 1, değilse son ID + 1)
    yeni_id = kitaplar[-1]["id"] + 1 if kitaplar else 1
    
    yeni_kitap = {
        "id": yeni_id,
        "isim": isim.strip().title(),
        "yazar": yazar.strip().title(),
        "fiyat": float(fiyat),
        "tur": tur.strip().title()
    }
    
    kitaplar.append(yeni_kitap)
    veritabani_yaz(kitaplar)
    print(f"\n✔️ '{isim}' başarıyla kitaplığa eklendi! (ID: {yeni_id})")

def kitaplari_listele():
    """Tüm kitaplığı ekrana tablo benzeri bir düzende basar."""
    kitaplar = veritabani_oku()
    
    if not kitaplar:
        print("\n📭 Kitaplığınız şu an tamamen boş.")
        return
    
    print("\n" + "="*60)
    print(f"{'ID':<5} | {'KİTAP ADI':<20} | {'YAZAR':<15} | {'FİYAT':<8} | {'TÜR':<10}")
    print("="*60)
    for k in kitaplar:
        print(f"{k['id']:<5} | {k['isim'][:20]:<20} | {k['yazar'][:15]:<15} | {k['fiyat']:<8.2f} | {k['tur']:<10}")
    print("="*60)

def kitap_guncelle(kitap_id, yeni_fiyat):
    """ID numarası verilen kitabın fiyatını günceller."""
    kitaplar = veritabani_oku()
    bulundu_mu = False
    
    for k in kitaplar:
        if k["id"] == kitap_id:
            k["fiyat"] = float(yeni_fiyat)
            bulundu_mu = True
            print(f"\n✔️ ID: {kitap_id} olan kitabın yeni fiyatı {yeni_fiyat} TL olarak güncellendi.")
            break
            
    if not bulundu_mu:
        print(f"\n❌ HATA: ID: {kitap_id} olan bir kitap bulunamadı!")
    else:
        veritabani_yaz(kitaplar)

def kitap_sil(kitap_id):
    """ID numarası verilen kitabı veritabanından tamamen siler."""
    kitaplar = veritabani_oku()
    # List comprehension kullanarak, silinecek ID hariç tüm kitapları yeni listeye alıyoruz
    yeni_liste = [k for k in kitaplar if k["id"] != kitap_id]
    
    if len(kitaplar) == len(yeni_liste):
        print(f"\n❌ HATA: ID: {kitap_id} olan bir kitap bulunamadı, silme başarısız.")
    else:
        veritabani_yaz(yeni_liste)
        print(f"\n🗑️ ID: {kitap_id} olan kitap başarıyla sistemden silindi.")

def kitap_filtrele(arama_turu, kelime):
    """Türe göre (Genre) veya Yazara göre filtreleme yapar."""
    kitaplar = veritabani_oku()
    arama_turu = arama_turu.lower()
    kelime = kelime.lower().strip()
    
    # Şarta uyanları ayıklıyoruz
    filtrelenmis = [k for k in kitaplar if kelime in k[arama_turu].lower()]
    
    if not filtrelenmis:
        print(f"\n⚠️ Kriterlere uygun hiçbir kitap bulunamadı.")
        return
        
    print(f"\n🔍 Filtre Sonuçları ({arama_turu.upper()} içinde '{kelime}' geçenler):")
    print("-" * 50)
    for k in filtrelenmis:
        print(f"-> {k['isim']} - Yazar: {k['yazar']} | Tür: {k['tur']} | Fiyat: {k['fiyat']} TL")
    print("-" * 50)


# --- 3. KULLANICI ARAYÜZÜ (MENÜ DÖNGÜSÜ) ---

while True:
    print("\n📚 KİTAPLIK YÖNETİM SİSTEMİ 📚")
    print("1 - Kitap Ekle")
    print("2 - Kitapları Listele")
    print("3 - Fiyat Güncelle")
    print("4 - Kitap Sil")
    print("5 - Kitap Filtrele (Yazar/Tür)")
    print("6 - Çıkış")
    
    secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-6): ").strip()
    
    if secim == "1":
        isim = input("Kitap Adı: ")
        yazar = input("Yazar Adı: ")
        fiyat = input("Fiyat (TL): ")
        tur = input("Kitap Türü (Roman/Bilim/Tarih vb.): ")
        try:
            kitap_ekle(isim, yazar, fiyat, tur)
        except ValueError:
            print("\n❌ HATA: Fiyat kısmına lütfen sadece sayısal değer girin!")
            
    elif secim == "2":
        kitaplari_listele()
        
    elif secim == "3":
        try:
            k_id = int(input("Fiyatını güncellemek istediğiniz kitabın ID'si: "))
            y_fiyat = float(input("Yeni Fiyat (TL): "))
            kitap_guncelle(k_id, y_fiyat)
        except ValueError:
            print("\n❌ HATA: Lütfen ID ve Fiyat bilgilerini sayısal olarak girin!")
            
    elif secim == "4":
        try:
            k_id = int(input("Silmek istediğiniz kitabın ID'si: "))
            kitap_sil(k_id)
        except ValueError:
            print("\n❌ HATA: Geçersiz ID formatı!")
            
    elif secim == "5":
        tip = input("Neye göre filtrelemek istersiniz? ('yazar' veya 'tur'): ").strip().lower()
        if tip in ["yazar", "tur"]:
            kelime = input(f"Aramak istediğiniz {tip} bilgisini girin: ")
            kitap_filtrele(tip, kelime)
        else:
            print("\n❌ HATA: Geçersiz arama kriteri! Sadece 'yazar' veya 'tur' yazabilirsiniz.")
            
    elif secim == "6":
        print("\n👋 Sistem kapatılıyor, kitaplığınız güvenle diske kaydedildi. İyi günler!")
        break
    else:
        print("\n❌ HATA: Geçersiz seçim! Lütfen 1-6 arasında bir rakam girin.")