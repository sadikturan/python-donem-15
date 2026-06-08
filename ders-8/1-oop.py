"""
1. BÖLÜM: OOP Nedir? Neden İhtiyaç Duyarız?
Şu ana kadar yazdığımız tüm kodlar Prosedürel (Yapısal) mantıktaydı. Yani yukarıdan aşağıya değişkenler tanımlıyor, fonksiyonlar yazıyor ve bunları sırayla çalıştırıyorduk.

Prosedürel Kodun Tehlikesi: "Spagetti Kod"
Küçük projelerde bu harikadır. Ancak bir e-ticaret sisteminde 50 farklı ürün, 10.000 müşteri ve binlerce sipariş olduğunu hayal edin. Her ürünün fiyatını, stok bilgisini, rengini ayrı ayrı değişkenlerde tutmaya kalkarsak bir süre sonra kodlarımız birbirine girer, çorba olur (Spagetti Kod).

Çözüm: Nesne Tabanlı Programlama (OOP)
OOP, kodları ve verileri gerçek hayattaki nesneleri taklit ederek bir arada gruplama yöntemidir.

Gerçek hayatta etrafımıza baktığımızda gördüğümüz her şey birer nesnedir (Object): Bir Araba, bir Telefon, bir Müşteri veya bir Banka Hesabı...

OOP dünyasında her nesnenin iki temel bileşeni vardır:

* Attributes (Özellikler): O nesnenin sahip olduğu verilerdir. (Örn: Arabanın rengi, markası, hızı).
* Methods (Metotlar/Eylemler): O nesnenin yapabildiği işler, fonksiyonlardır. (Örn: Arabanın çalışması, fren yapması).

2. BÖLÜM: Class (Sınıf) ve Object (Nesne) İlişkisi

Öğrencilerin en çok bocaladığı yer bu iki kavramın farkıdır. Bunu tahtaya şu iki benzetmeyle kazıyın:

* Sınıf (Class): Bir nesnenin mimari taslak planı, çizimi veya fabrikadaki kalıbıdır. Somut olarak ortada henüz bir şey yoktur, sadece kurallar ve tasarım vardır.
* Nesne (Object / Instance): O kalıptan, o plandan üretilmiş gerçek, somut örnektir.

Benzetme: "Araba Mühendislik Çizimi" bir sınıftır. O çizime bakarak fabrikadan banttan indirilen, dokunabildiğimiz "Kırmızı renkli Toyota Corolla" ise bir nesnedir.
"""

# İlk Sınıfı Tanımlama (En Basit Hali)

# Sınıf isimleri Python standardı olarak her zaman büyük harfle başlar (CamelCase).
class Araba:
    pass # 'pass', şimdilik burayı boş bırak, hata verme demektir.

# Sınıftan nesne üretme (Yaratma)
benim_arabam = Araba()

print(type(benim_arabam)) 
# Çıktı: <class '__main__.Araba'> (Bakın kendi veri tipimizi yarattık!)

"""
3. BÖLÜM: __init__ Metodu ve self Kavramı (Anatomi)
Bir sınıftan yeni bir nesne üretildiği anda (yani nesne doğarken) arka planda otomatik olarak çalışan ilk fonksiyona __init__ metodu (Constructor / Yapıcı Metot) denir.

Görevi: Nesne dünyaya gözlerini açarken ona ait özellikleri peşin peşin yüklemektir.

** self Nedir?

self kelimesi, o an hafızada üretilmekte olan "nesnenin tam kendisini" temsil eden sihirli bir imleçtir. Sınıf içindeki özelliklerin o nesneye yapışmasını sağlar.

"""

class Dog:
    # 1. Adım: Nesne doğarken çalışacak kalıbı kuruyoruz
    def __init__(self, isim: str, cins: str):
        self.name = isim   # Gelen isim argümanını bu nesnenin 'name' özelliğine yapıştır
        self.breed = cins  # Gelen cins argümanını bu nesnenin 'breed' özelliğine yapıştır

# 2. Adım: Kalıbı kullanarak gerçek nesneler üretiyoruz
kopek1 = Dog("Karabaş", "Sivas Kangalı")
kopek2 = Dog("Pamuk", "Poodle")

# 3. Adım: Nesnelerin özelliklerine erişiyoruz
print(f"1. Köpeğin Adı: {kopek1.name} | Cinsi: {kopek1.breed}")
print(f"2. Köpeğin Adı: {kopek2.name} | Cinsi: {kopek2.breed}")

# Arka Planda Ne Oldu?
# Biz Dog("Karabaş", "Sivas Kangalı") yazdığımızda Python arka planda şunu yaptı:
# * Hafızada boş bir alan açtı.
# * __init__ fonksiyonunu çağırdı. self yerine o boş alanın adresini koydu.
# * self.name = "Karabaş" diyerek o adrese ismi kaydetti.

# 4. BÖLÜM: Pratik Örnek (Araba Sınıfı)
# Geliştirdiğimiz yapıyı parametre veri tiplerini de dahil ederek kurumsal standartta yazalım:

class Araba:
    # Marka, model ve renk özelliklerini başlangıçta zorunlu tutuyoruz
    def __init__(self, marka: str, model: str, renk: str):
        self.marka = marka
        self.model = model
        self.renk = renk

# Nesneleri oluşturuyoruz
araba1 = Araba("Toyota", "Corolla", "Sarı")
araba2 = Araba("BMW", "M5", "Siyah")

print(f"Seçilen Araç: {araba1.renk} renkli {araba1.marka} {araba1.model}")

# 5. BÖLÜM: Sınıf İçi Uygulama (Sosyal Medya Yorum Sistemi)

# Soru: Bir sosyal medya platformu (Instagram/YouTube gibi) için yorumları (Comment) yönetecek bir sınıf tasarlayınız. Her yorumun; kullanıcı adı, yorum metni, beğeni sayısı ve beğenmeme sayısı özellikleri olsun. Beğeni sayıları girilmezse varsayılan olarak 0 kabul edilsin. Ardından bu yorumları bir listede toplayıp döngüyle ekrana basın.

class Comment:
    # Likes ve Dislikes girilmezse varsayılan (Default) olarak 0 atanır
    def __init__(self, username: str, text: str, likes: int = 0, dislikes: int = 0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

# --- NESNELERİN (INSTANCE) OLUŞTURULMASI ---
c1 = Comment("sadikturan", "Harika bir OOP dersi başlangıcı olmuş.")
c2 = Comment("ahmetyilmaz", "Konuyu ilk defa bu kadar net anladım.")
c3 = Comment("cinarturan", "Örnekler biraz daha zorlaşabilir mi?", 50, 10)
c4 = Comment("ayse_yildiz", "Type hinting kullanılması çok profesyonelce.")
c5 = Comment("yazilim_geliştirici", "Emeğinize sağlık.", 120)

# Tüm nesneleri tek bir listede topluyoruz
comments_list: list[Comment] = [c1, c2, c3, c4, c5]

print("\n=== SOSYAL MEDYA YORUM RAPORU ===")
print("-" * 45)

# Nesne listesini döngüyle ekrana basıyoruz
for c in comments_list:
    print(f"Kullanıcı: @{c.username}")
    print(f"Yorum    : {c.text}")
    print(f"Beğeni   : {c.likes}  |  Beğenmeme: {c.dislikes}")
    print("-" * 45)
