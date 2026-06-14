"""
JSON Nedir?

CSV satırlar ve sütunlardan oluşan iki boyutlu bir tablo yapısı sunarken, JSON bize çok daha esnek, karmaşık ve iç içe geçmiş (hierarchical) veri yapılarını saklama imkanı tanır.

Adım 1: JSON Nedir ve Kuralları Nelerdir?

JSON, okunması ve yazılması son derece kolay olan metin tabanlı bir veri değişim formatıdır. Python'daki Sözlük (Dictionary) yapısa benzerdir.

JSON Yazım Kuralları (Kritik Bilgiler):

Veriler Anahtar-Değer (Key-Value) çiftleri halinde tutulur.

* Çift Tırnak Zorunluluğu: JSON içinde tüm anahtarlar (keys) ve metinsel değerler (strings) mutlaka çift tırnak ("...") ile yazılmalıdır. Tek tırnak ('...') kullanımı JSON formatında geçersizdir ve hata verir.

* Veri Tipleri: JSON; metin, sayı, boolean (true/false), liste (array) ve başka JSON nesnelerini içerebilir. (Python'daki None değeri JSON'da null olarak karşılık bulur).

Adım 2: Temel Metotlar ve İki Altın Kural

Serialization (Diske Yazma / Paketleme): Python sözlüğünü veya listesini JSON formatına çevirip bir dosyaya kaydetme işlemidir. json.dump() metodu kullanılır.

Deserialization (Diskten Okuma / Çözme): Bir JSON dosyasındaki metni okuyup Python'ın anlayacağı dict veya list yapısına geri çevirme işlemidir. json.load() metodu kullanılır.

"""

kitap_detay = {
    "trend_mi": True,
    "kategori": "Fiction",
    "istatistik": {
        "toplam_inceleme": 21625,
        "puan": 4.8
    },
    "etiketler": ["Bestseller", "Edebiyat", "Palacio"]
}
