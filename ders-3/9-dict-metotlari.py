"""
Sözlük Metotları

keys(): Sözlükteki tüm anahtarları bir liste gibi verir.
values(): Sözlükteki tüm değerleri bir liste gibi verir.
items(): Anahtar ve değerleri çiftler (tuple) halinde verir (Döngülerde çok işe yarar).
"""

araba = {"marka": "Tesla", "model": "Model Y", "yil": 2026}

print(araba.keys())   # dict_keys(['marka', 'model', 'yil'])
print(araba.values()) # dict_values(['Tesla', 'Model Y', 2026'])
print(araba.items())  # dict_items([('marka', 'Tesla'), ('model', 'Model Y'), ('yil', 2026)])

# Dictionary metotları:

# get(): Anahtara karşılık gelen değeri döndürür. Anahtar yoksa None döner veya belirtilen varsayılan değeri döndürür.
print(araba.get("marka"))  # Tesla
print(araba.get("renk", "Bilinmiyor"))  # Bilinmiyor

# pop(): Anahtara karşılık gelen değeri döndürür ve o anahtarı sözlükten kaldırır.
print(araba.pop("model"))  # Model Y
print(araba)  # {'marka': 'Tesla', 'yil': 2026}

# update(): Bir sözlüğü başka bir sözlükle günceller.
araba.update({"renk": "Sarı", "yil": 2027})
print(araba)  # {'marka': 'Tesla', 'yil': 2027, 'renk': 'Sarı'}

# popitem(): Sözlükten rastgele bir anahtar-değer çiftini kaldırır ve döndürür.
print(araba.popitem())  # ('renk', 'Sarı') veya ('yil', 2027) veya ('marka', 'Tesla')
print(araba)  # Kalan anahtar-değer çiftleri



