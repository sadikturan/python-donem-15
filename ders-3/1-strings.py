# String Tanımlama

isim = 'Ahmet'
soyisim = "Yılmaz"

yas = 30
adres = """Atatürk Caddesi,
No: 5, Çankaya
Ankara"""

cumle = "İstanbul'un havası bugün çok güzel."

# String Slicing

programlama_dili = "Python Dersleri"

print(programlama_dili[0]) # 'P' harfini verir
print(programlama_dili[3]) # 'h' harfini verir
print(programlama_dili[-1]) # En sondaki harfi ('i') verir
print(programlama_dili[0:6]) # 'Python' verir
print(programlama_dili[:]) # Tüm string'i verir
print(programlama_dili[:6]) # 'Python' verir (başlangıçtan 6. index'e kadar)
print(programlama_dili[2:5]) # 'tho' verir (2. index'ten 5. index'e kadar)
print(programlama_dili[::2]) # 'PtoDrsri' verir (2 karakter atlayarak)
print(programlama_dili[::-1]) # 'iresrDnohtyP' verir (string'i ters çevirir)

# String Birleştirme (Concatenation)

ad = "Yusuf"
soyad = "Arslan"

tam_isim = ad + " " + soyad
print(tam_isim) # Çıktı: Yusuf Arslan

# String Formatlama

urun = "Laptop"
fiyat = 25000

print("Aldığınız " + urun + " için " + str(fiyat) + " TL ödeme yapıldı.")
print(f"Aldığınız {urun} için {fiyat} TL ödeme yapıldı.")
