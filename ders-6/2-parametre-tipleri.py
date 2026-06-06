"""
Python'da fonksiyon tanımlarken parametrelerin yanına "bu parametre hangi veri tipinde olmalı" ya da "bu fonksiyon geriye ne döndürecek" bilgisini ekleme işlemine Type Hinting (Tip İpuçları) denir.

Python dinamik bir dildir; yani değişkenlerin tiplerini zorunlu tutmaz. Ancak büyük veri projelerinde ve kurumsal yazılımlarda, kodun okunabilirliğini artırmak, hataları erkenden yakalamak ve kod editörlerinin bize doğru ipuçları (autocomplete) vermesini sağlamak için parametre veri tiplerini tanımlamak sektör standardıdır.

Gelin bu yapıyı temel seviyeden ileri seviyeye kadar adım adım inceleyelim.
"""

# 1. Temel Veri Tipleri ile Parametre Tanımlama

# Parametre isimlerinin hemen yanına iki nokta üst üste (:) koyarak beklenen veri tipini yazarız. Fonksiyonun geriye döndüreceği veri tipini ise parantezin dışına -> işareti koyarak belirtiriz.

# sayi1 ve sayi2'nin int (tam sayı) olmasını bekliyoruz.
# Fonksiyonun ise geriye int bir sonuç döndüreceğini (-> int) belirtiyoruz.
def toplama_yap(sayi1: int, sayi2: int) -> int:
    return sayi1 + sayi2

# String ve Float parametre örneği:
def maas_hesapla(isim: str, ham_maas: float) -> str:
    net_maas = ham_maas * 0.80
    return f"{isim} isimli personelin net maaşı: {net_maas} TL"

# 2. Liste, Sözlük ve Küme (List, Dict, Set) Tiplerini Tanımlama

# Bir sayı listesi alıp, geriye ondalıklı sayı (float) döndüren fonksiyon
def ortalama_hesapla(notlar: list[int]) -> float:
    return sum(notlar) / len(notlar)

# Sözlük (Dictionary) parametre örneği:
# Anahtarlar str (string), değerler int (tam sayı) olmalı
def stok_kontrol(katalog: dict[str, int]) -> None:
    for urun, adet in katalog.items():
        print(f"{urun} ürününden {adet} adet var.")

# 3. Birden Fazla Veri Tipi İhtimali (Union / | Operatörü)

# Bir sütun hem tam sayı (int) hem de ondalıklı sayı (float) barındırabilir. Veya bir fonksiyon bazen str bazen de veri bulunamadığında None döndürebilir. Bu gibi durumlarda Veya (|) operatörünü kullanırız.

# 'fiyat' parametresi int VEYA float olabilir
def vergi_ekle(fiyat: int | float) -> float:
    return fiyat * 1.20

# Müşteri ID'sini arayan, bulursa str bulamazsa None dönen fonksiyon
def musteri_bul(id: int) -> str | None:
    veritabanı = {101: "Ahmet", 102: "Zeynep"}
    
    if id in veritabanı:
        return veritabanı[id]
    else:
        return None # Müşteri yoksa None döner
    
# 4. Default (Varsayılan) Değer ile Tip Tanımlama Birlikte Nasıl Yazılır?

# Eğer bir parametreye hem veri tipi belirtmek hem de varsayılan bir değer atamak istiyorsak sıralama şu şekilde olmalıdır: parametre_adi: veri_tipi = varsayilan_deger

# 'mesaj' bir string'dir ve girilmezse varsayılan değeri "Hata!" metnidir.
def alarm_ver(kod: int, mesaj: str = "Sistemsel Hata!") -> None:
    print(f"KOD: {kod} - MESAJ: {mesaj}")

alarm_ver(404) # mesaj girilmedi, varsayılanı kullandı.

