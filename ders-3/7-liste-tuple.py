""" Tuple (Demetler): Değiştirilemezler (Immutable).

* Bir Tuple'ı tanımladıktan sonra üzerinde hiçbir değişiklik yapamazsınız.

Peki Neden Tuple Kullanırız?
Veri Güvenliği: Kodunuzda kesinlikle değişmesini istemediğiniz verileri (gün isimleri, aylar, matematiksel sabitler, GPS koordinatları) koruma altına alır.

Performans (Hız): Python, değiştirilemeyeceğini bildiği için Tuple'ları bellekte çok daha hızlı işler. Büyük verilerle çalışırken Tuple kullanmak programı hızlandırır.
"""

# 1. Tuple Tanımlama

# Basit bir Tuple tanımlama
renkler = ("Kırmızı", "Mavi", "Yeşil")

# Farklı veri tipleri barındırabilir
kullanici = ("admin", 12345, True)

# Parantez kullanmadan da Tuple tanımlanabilir (Tuple Packing)
koordinat = 41.0082, 28.9784

hatali_tuple = ("Elma")  # Tipi 'str' (String) olur
dogru_tuple  = ("Elma",) # Tipi 'tuple' olur

# 2. Elemanlara Erişme (Indexing)

gunler = ("Pazartesi", "Salı", "Çarşamba")

print(gunler[0])  # "Pazartesi"
print(gunler[-1]) # "Çarşamba"

# 3. Tuple Metotları

# Değiştirilemez oldukları için Tuple'ların sadece iki adet metodu vardır:

# count(): Bir elemanın Tuple içinde kaç defa geçtiğini sayar.

# index(): Belirtilen elemanın kaçıncı indekste olduğunu söyler.

rakamlar = (1, 2, 3, 2, 4, 2, 5)

print(rakamlar.count(2))  # 3 (2 sayısı 3 defa geçiyor)
print(rakamlar.index(4))  # 4 (4 sayısı 4. indekste)
