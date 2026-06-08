# Kapsamlı Proje: OOP ile Quiz Uygulaması
# Şimdi iki farklı sınıf tasarlayacağız:

# Soru Sınıfı: Her bir sorunun metnini, şıklarını ve doğru cevabını tutacak.
# Quiz Sınıfı: Soru listesini yönetecek, skoru tutacak ve sırayla soruları ekrana getirecek.


# --- 1. SORU SINIFI ---
class Soru:
    def __init__(self, soru_metni, secenekler, dogru_cevap):
        self.soru_metni = soru_metni
        self.secenekler = secenekler
        self.dogru_cevap = dogru_cevap

    def cevabi_kontrol_et(self, kullanici_cevabi):
        """Kullanıcının cevabı doğruysa True, yanlışsa False döner."""
        return self.dogru_cevap.upper() == kullanici_cevabi.upper()
    

# --- 2. QUIZ SINIFI ---
class Quiz:
    def __init__(self, sorular_listesi):
        self.sorular = sorular_listesi
        self.skor = 0
        self.soru_indeksi = 0 # Şu an kaçıncı soruda olduğumuzu tutar

    def soru_getir(self):
        """Sıradaki soru nesnesini döner."""
        return self.sorular[self.soru_indeksi]

    def quizi_baslat(self):
        """Quiz döngüsünü başlatır ve sırayla soruları sorar."""
        print("====== PYTHON BİLGİ YARIŞMASINA HOŞ GELDİNİZ ======")
        
        # Soru listesi bitene kadar while döngüsü çalışsın
        while self.soru_indeksi < len(self.sorular):
            mevcut_soru = self.soru_getir()
            
            print(f"\nSoru {self.soru_indeksi + 1}: {mevcut_soru.soru_metni}")
            for secenek in mevcut_soru.secenekler:
                print(secenek)
                
            cevap = input("Cevabınız (A/B/C/D): ").strip()
            
            # Soru sınıfındaki metodu çağırarak kontrol ediyoruz
            if mevcut_soru.cevabi_kontrol_et(cevap):
                print("🎉 Doğru Cevap!")
                self.skor += 10
            else:
                print(f"❌ Yanlış Cevap! Doğru cevap: {mevcut_soru.dogru_cevap}")
                
            self.soru_indeksi += 1 # Sonraki soruya geç
            
        self.raporu_goster()

    def raporu_goster(self):
        """Yarışma bittiğinde skor raporunu ekrana basar."""
        print("\n================ YARIŞMA BİTTİ ================")
        print(f"Toplam Doğru Sayısı: {self.skor // 10} / {len(self.sorular)}")
        print(f"Toplam Puanınız    : {self.skor}")
        print("===============================================")


# --- 3. UYGULAMA AKIŞI (SORULARI HAZIRLAMA) ---

# Soru nesnelerini oluşturup bir liste içinde topluyoruz
havuz = [
    Soru(
        "Python'da listeye eleman ekleyen metot hangisidir?",
        ["A) pop()", "B) append()", "C) insert()", "D) remove()"],
        "B"
    ),
    Soru(
        "Sözlüklerde (Dictionary) veriler hangi mantıkla saklanır?",
        ["A) İndeks-Değer", "B) Sadece Değer", "C) Anahtar-Değer", "D) Rastgele"],
        "C"
    ),
    Soru(
        "Aşağıdakilerden hangisi 'değiştirilemez' (immutable) bir veri tipidir?",
        ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
        "D"
    )
]

# Quiz nesnemizi oluşturup yarışmayı tetikliyoruz
python_quiz = Quiz(havuz)
python_quiz.quizi_baslat()



"""
Modülerlik: Sorunun nasıl kontrol edileceği (cevabi_kontrol_et), Soru sınıfının kendi sorumluluğundadır. Skorun ne olacağı ve sıranın nasıl ilerleyeceği ise Quiz sınıfının sorumluluğundadır. Nesneler birbiriyle konuşarak çalışırlar.

Sürdürülebilirlik: Yarın bir gün 100 tane daha soru eklemek isterseniz, ana koda veya Quiz sınıfına dokunmanıza gerek kalmaz. Sadece havuz listesine yeni bir Soru(...) nesnesi eklemeniz yeterlidir.

"""