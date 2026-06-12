# 1. Tehlikeli Ama Güçlü Mod: 'w' (Write - Yeniden Yazma)

# 'w' modu, belirtilen isimde bir dosya yoksa sıfırdan boş bir dosya oluşturur. Ancak en önemli özelliği şudur: Eğer o isimde bir dosya zaten varsa, içindeki tüm eski verileri saniyeler içinde kalıcı olarak siler ve tertemiz, boş bir sayfa açar.

# 'w' modu eski verileri temizler ve yeni veri yazar
with open("günlük_rapor.txt", "w", encoding="utf-8") as file:
    file.write("--- GÜNLÜK SATIŞ RAPORU ---\n")
    file.write("Laptop Satış Adedi: 15\n")
    file.write("Mouse Satış Adedi: 42\n")

print("Dosya başarıyla oluşturuldu ve veriler yazıldı.")

# 2. Güvenli Mod: 'a' (Append - Sona Ekleme)

# Mevcut bir veri setimiz veya log dosyamız olduğunda, içindeki eski verilere dokunmadan en alt satırdan itibaren yeni veriler eklemek isteriz. İşte bu durumlarda 'a' modunu kullanırız. Dosya yoksa sıfırdan oluşturur, varsa kaldığı yerden devam eder.

# 'a' modu dosyanın sonuna ekleme yapar
with open("günlük_rapor.txt", "a", encoding="utf-8") as file:
    file.write("Klavye Satış Adedi: 28\n")

print("Yeni veriler eski dosyanın sonuna başarıyla eklendi.")

# 3. Toplu Veri Yazma Metodu: writelines()

# Eğer elimizde bir dize veya liste (list) dolusu veri varsa ve bunları döngüye sokmadan tek seferde dosyaya basmak istiyorsak writelines() metodunu kullanırız.

yeni_kayitlar = [
    "Kulaklık Satış Adedi: 12\n",
    "Monitör Satış Adedi: 5\n",
    "Kamera Satış Adedi: 8\n"
]

with open("günlük_rapor.txt", "a", encoding="utf-8") as file:
    file.writelines(yeni_kayitlar)

print("Listenin tüm elemanları dosyaya topluca yazıldı.")