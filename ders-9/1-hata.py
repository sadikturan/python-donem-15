"""
Python programlama dilinde kod yazarken her şeyin her zaman kusursuz çalışmasını bekleyemeyiz. Kullanıcılar hatalı veriler girebilir, internet bağlantısı kopabilir, aradığımız bir dosya silinmiş olabilir veya tamamen mantıksal hatalar yapmış olabiliriz.

Bir programın bu tarz beklenmedik durumlarda çökmesini engellemek ve kodun çalışmaya devam etmesini sağlamak için Hata Yönetimi (Exception Handling) ve kodlardaki böcekleri temizlemek için Hata Ayıklama (Debugging) mekanizmalarını kullanırız.

1. Hata ve Hata Yönetimi Nedir?

Python'da hatalar genel olarak iki ana gruba ayrılır:

Sözdizimi Hataları (Syntax Errors): Kod yazım kurallarına uymadığımızda (örneğin iki nokta : koymayı unutmak veya parantezi kapatmamak) ortaya çıkan hatalardır. Bu hatalar varsa kod hiç çalışmaz.

İstisnalar (Exceptions): Kodun yazımında hiçbir sorun yoktur, kod çalışmaya başlar ancak çalışma esnasında (Runtime) beklenmedik bir durumla karşılaşır ve çöker. İşte bizim "Yöneteceğimiz" hatalar bu istisnalardır.

Hata Yönetimi, bu istisnai durumlar gerçekleştiğinde programın kırmızı hata ekranı verip aniden kapanması yerine, hatayı yakalayıp kullanıcıya kibar bir mesaj gösterme ve programın akışını güvenle sürdürme işlemidir.
"""


# En Sık Karşılaşılan İstisna Tipleri (Exception Types): 

# ValueError: Beklenen türde olmayan bir değerle karşılaşıldığında ortaya çıkar. Örneğin, bir sayısal değer beklenirken metin girilmesi.
# TypeError: Bir işlemin beklenmedik türde bir nesneyle karşılaştığında ortaya çıkar. Örneğin, bir sayıyı bir metinle toplamak.
# FileNotFoundError: Aranılan bir dosya bulunamadığında ortaya çıkar. Örneğin, var olmayan bir dosyayı açmaya çalışmak.
# ZeroDivisionError: Bir sayıyı sıfıra bölmeye çalıştığınızda ortaya çıkar.
# KeyError: Bir sözlükte var olmayan bir anahtara erişmeye çalıştığınızda ortaya çıkar.
# IndexError: Bir dizinin veya listenin geçersiz bir indeksine erişmeye çalıştığınızda ortaya çıkar.

# Hata Yönetimi için try-except blokları kullanılır.

try:
    # Hata riski barındıran tehlikeli bölge
    ham_girdi = input("Lütfen bir sayı girin: ")
    sayi: int = int(ham_girdi)
    
    sonuc: float = 10 / sayi

except ValueError:
    # Kullanıcı sayı yerine harf/metin girerse burası çalışır
    print("[HATA]: Lütfen geçerli bir tam sayı giriniz!")

except ZeroDivisionError:
    # Kullanıcı 0 girerse burası çalışır
    print("[HATA]: Bir sayı sıfıra bölünemez!")

else:
    # EĞER HİÇBİR HATA OLMADAYSA burası çalışır. 
    print(f"İşlem Başarılı! Bölüm Sonucu: {sonuc}")

finally:
    # Hata olsa da olmasa da HER HALÜKARDA çalışacak bölge.
    # Genelde veritabanı bağlantılarını kapatmak veya dosyaları güvenle kilitlemek için kullanılır.
    print("[SİSTEM]: İşlem adımı sonlandırıldı.")

# Hata yönetimi, programın beklenmedik durumlarda bile çalışmaya devam etmesini sağlar ve kullanıcı deneyimini iyileştirir. Hataları doğru şekilde yönetmek, yazdığınız kodun daha güvenilir ve kullanıcı dostu olmasına yardımcı olur.

# Bilerek Hata Fırlatmak (raise)

# Bazen Python teknik olarak bir hata görmez ama bizim iş mantığımıza (Business Logic) göre o durum bir hatadır. Örneğin: Bir kullanıcının şifresi 6 karakterden azsa Python buna kızmaz ama bizim sistemimiz için bu bir güvenlik açığıdır. Bu durumlarda raise kelimesiyle el bombasının pimini biz çekeriz.

# Gelen parametrelerin tiplerini ve dönüş tipini (None) belirtiyoruz
def kayit_ol(kullanici_adi: str, sifre: str) -> None:
    if len(sifre) < 6:
        # Şart uymuyorsa kendi ValueError istisnamızı oluşturup fırlatıyoruz
        raise ValueError("Şifre güvenliği yetersiz! En az 6 karakter olmalıdır.")
    
    print(f"{kullanici_adi} başarıyla sisteme kaydedildi.")

# --- SİSTEMİN TEST EDİLMESİ ---
try:
    kayit_ol("python_can", "123") # Şifre kısa, hata fırlatacak!
except ValueError as e:
    # 'as e' diyerek raise ile fırlatılan o özel mesajı yakalayıp ekrana basıyoruz
    print(f"[KAYIT ENGELLENDİ]: {e}")


    


