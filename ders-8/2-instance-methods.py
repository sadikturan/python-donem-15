"""
Instance Methods (Nesne Metotları)

Geçen dersimizde bir sınıfın özelliklerini (Attributes) __init__ ile nasıl tanımlayacağımızı gördük. Ancak gerçek hayattaki nesneler sadece veri tutmaz, aynı zamanda eylemler gerçekleştirirler.

Bir sınıfın içinde tanımlanan ve o sınıftan üretilen nesnelerin yapabileceği eylemleri / işleri içeren fonksiyonlara Instance Method (Nesne Metodu) denir.

** En Büyük Kural: self Zorunluluğu
Sıradan fonksiyonlardan en büyük farkı şudur: Bir nesne metodunun parantezi içine ilk parametre olarak HER ZAMAN self yazılmak zorundadır.

* Neden self Yazıyoruz? 
Çünkü metot çağrıldığı an, hangi nesne üzerinde çalışıyorsa o nesnenin özelliklerine (self.name, self.bakiye vb.) erişebilmek ve onları güncelleyebilmek için o nesnenin adresine (kendisine) ihtiyaç duyar.

"""

# Temel Nesne Metodu Uygulaması

class Person:
    # Nesnenin özelliklerini başlatıyoruz
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Bu bir Instance Method'dur. İlk parametresi self'tir.
    def greet(self) -> str:
        # self.name ve self.age sayesinde bu nesnenin kimlik bilgilerine ulaşıyoruz
        return f"Merhaba, benim adım {self.name} ve ben {self.age} yaşındayım."
    
# --- ÇALIŞTIRMA ---
person1 = Person("Ahmet", 30)

# Metodu çağırırken parantez içine self için bir şey yazmayız. 
# Python arka planda person1'i self yerine otomatik gönderir.
print(person1.greet()) 
# Çıktı: Merhaba, benim adım Ahmet ve ben 30 yaşındayım.

# Nesne Durumunu Değiştiren Metotlar (Banka Hesabı)

# Metotlar sadece ekrana yazı basmaz veya değer döndürmez; nesnenin içindeki veriyi (durumu) kalıcı olarak değiştirebilir ve güncelleyebilir. Dökümanınızdaki banka hesabı örneği bunu göstermek için harikadır:

class BankaHesabi:
    def __init__(self, sahip: str, bakiye: float | int):
        self.sahip = sahip
        self.bakiye = bakiye
        
    # Bu metot dışarıdan bir 'miktar' alır ve nesnenin bakiyesini kalıcı olarak günceller
    def para_yatir(self, miktar: float | int) -> None:
        self.bakiye += miktar # Nesnenin kendi içindeki bakiye güncelleniyor!
        print(f" Sayın {self.sahip}, hesabınıza {miktar} TL yatırıldı.")
        print(f" Güncel Bakiye: {self.bakiye} TL")

# --- SENARYO ---
hesap = BankaHesabi("Ahmet Yılmaz", 5000)

# Para yatırma eylemini gerçekleştiriyoruz
hesap.para_yatir(1500) 
# Çıktı: Güncel Bakiye: 6500 TL

# Doğrulama: Nesnenin bakiyesine doğrudan baktığımızda da değiştiğini görüyoruz:
print(f"Nesnenin Son Bakiye Durumu: {hesap.bakiye} TL") # 6500

# Sınıf İçi İleri Seviye Uygulama (Akıllı Sepet Sistemi)

# Senaryo: Bir e-ticaret sitesi için Sepet sınıfı tasarlayalım. Bu sepetin içinde ürünleri tutan bir liste olsun. Sepete ürün ekleme (urun_ekle), sepeti listeleme (sepeti_goster) ve toplam tutarı hesaplama (toplam_tutar) eylemlerini nesne metotları olarak yazalım.

class Sepet:
    def __init__(self, musteri_adi: str):
        self.musteri_adi = musteri_adi
        self.urunler: list[dict] = [] # Başlangıçta sepetin içi boş bir listedir

    # Eylem 1: Sepete yeni bir ürün sözlüğü ekler
    def urun_ekle(self, urun_adi: str, fiyat: float | int) -> None:
        yeni_urun = {"urun": urun_adi, "fiyat": fiyat}
        self.urunler.append(yeni_urun)
        print(f"🛒 {urun_adi} ({fiyat} TL) sepete eklendi.")

    # Eylem 2: Sepetteki toplam tutarı hesaplar ve döndürür
    def toplam_hesapla(self) -> float | int:
        toplam = sum(item["fiyat"] for item in self.urunler)
        return toplam

    # Eylem 3: Sepet raporunu şık bir şekilde ekrana basar
    def sepeti_goster(self) -> None:
        print(f"\n--- @{self.musteri_adi} İÇİN SEPET RAPORU ---")
        if not self.urunler:
            print("Sepetiniz henüz boş.")
            return
            
        for sira, item in enumerate(self.urunler, start=1):
            print(f"{sira}. {item['urun']} - {item['fiyat']} TL")
            
        print(f"➡️ Toplam Ödenecek: {self.toplam_hesapla()} TL")
        print("-" * 35)

# --- UYGULAMA AKIŞI ---

# 1. Ahmet için boş bir sepet nesnesi oluşturuyoruz
ahmet_sepeti = Sepet("ahmet_yazilimci")

# 2. Sepete ürünler ekliyoruz (Metotlar nesne hafızasını güncelliyor)
ahmet_sepeti.urun_ekle("Kablosuz Mouse", 450)
ahmet_sepeti.urun_ekle("Mekanik Klavye", 1200)
ahmet_sepeti.urun_ekle("Oyuncu Kulaklığı", 2500)

# 3. Sepetin son durumunu raporlayan metodu çağırıyoruz
ahmet_sepeti.sepeti_goster()