# Adım 1: CSV Nedir ve Yapısı Nasıldır?

# CSV (Comma-Separated Values), verilerin satırlar halinde tutulduğu ve her satırdaki hücrelerin birbirlerinden virgül (,), noktalı virgül (;) veya tab (\t) gibi ayırıcılarla ayrıldığı düz metin dosyalarıdır. Excel veya Google Sheets tablolarının en sade halidir.

# Adım 2: CSV Modülünü Dahil Etmek (import csv)

# Python'da CSV dosyalarıyla çalışmak için dışarıdan bir şey indirmeye gerek yoktur. Standart kütüphanede gelen csv modülü projeye dahil edilir:

# Adım 3: CSV Dosyasından Veri Okuma Yöntemleri

# A) Liste Olarak Okuma (csv.reader)

# Dosyadaki her bir satırı bize sırayla bir liste (list) olarak getirir. Verilere indeks numaralarıyla (satir[0], satir[1]) erişilir.

# import csv
# with open("bestselling-books.csv", "r", encoding="utf-8") as file:
#     okuyucu = csv.reader(file)
#     header = next(okuyucu) # Başlık satırını atlamak veya yakalamak için kullanılır
#     for satir in okuyucu:
#         print(f"Kitap: {satir[0]} - Yazar: {satir[1]}")

# B) Sözlük Olarak Okuma (csv.DictReader) En Çok Tercih Edilen

# Dosyadaki ilk satırı (sütun isimlerini) otomatik olarak anahtar (key) kabul eder ve sonraki her satırı birer sözlük (dict) olarak getirir. Verilere indeksle değil, direkt sütun adıyla erişilir.

import csv

with open("bestselling-books.csv", "r", encoding="utf-8") as file:
    okuyucu = csv.DictReader(file)
    for satir in okuyucu:
        print(f"Kitap: {satir['Name']} - Puan: {satir['User Rating']}")

