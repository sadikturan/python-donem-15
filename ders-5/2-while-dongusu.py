"""
While döngüsü, belirli bir koşul sağlandığı sürece kod bloğunu tekrarlamaya devam eder. For döngüsünden farklı olarak, while döngüsü genellikle sayısal bir sayaç veya belirli bir koşulun sağlanmasıyla çalışır.
"""

# Başlangıç değeri
sayac = 1

# Sayac 5'ten küçük veya eşit olduğu sürece dön
while sayac <= 5:
    print(f"Döngü adım sayısı: {sayac}")
    
    # ÇOK ÖNEMLİ: Sayacı her adımda 1 artırıyoruz
    sayac += 1

# Uygulama: 1'den 10'a kadar olan sayıların toplamını hesaplayın.

toplam = 0
sayac = 1
while sayac <= 10:
    toplam += sayac
    sayac += 1

print(f"1'den 10'a kadar olan sayıların toplamı: {toplam}")

# Uygulama: Kullanıcı "çıkış" yazana kadar çalışan bir kelime tekrarlayıcı yapalım

kullanici_girdisi = ""

print("--- Çıkmak için 'çıkış' yazın ---")

# Kullanıcı 'çıkış' yazmadığı sürece bu döngü durmayacak
while kullanici_girdisi != "çıkış":
    kullanici_girdisi = input("Bir kelime yazın: ").lower().strip()
    
    if kullanici_girdisi != "çıkış":
        print(f"Yazdığınız kelime: {kullanici_girdisi}")

print("Program başarıyla sonlandırıldı.")

# Döngü Kontrol Komutları: break ve continue

# Hem for hem de while döngülerinin akışını değiştirmek için iki altın komutumuz vardır:
# break: Döngüyü o an, anında ve tamamen bitirir.
# continue: Döngünün o anki adımını pas geçer, altındaki kodları çalıştırmadan bir sonraki adıma (başa) atlar.


# break örneği
sayi = 1
while sayi <= 100:
    if sayi == 5:
        print("5 sayısına ulaşıldı, döngüden zorla çıkılıyor!")
        break # Döngü 100'e kadar gitmeden 5'te biter
    print(sayi)
    sayi += 1

# for mu, while mı? Ne Zaman Hangisi?

# Bir listenin içindeki elemanları gezecekseniz veya işlemin kaç kere döneceği net olarak belliyse (Örn: 10 kere): for döngüsü tercih edilir.

# Bir işlemin kaç kere döneceğini önceden kestiremiyorsanız, işlem bir durum gerçekleşene kadar sürecekse: while döngüsü tercih edilir.
