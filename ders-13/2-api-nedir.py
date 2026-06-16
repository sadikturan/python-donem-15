"""
API Nedir?

Python'da dış dünyadaki verilere ulaşmak ve requests kütüphanesini kullanmak için öncelikle modern yazılım dünyasının ana iletişim köprüsü olan API kavramını bilmemiz gerekir.

1. API Nedir?
API (Uygulama Programlama Arayüzü), iki farklı yazılımın, uygulamanın veya sunucunun belirli kurallar çerçevesinde birbiriyle konuşmasını ve güvenli bir şekilde veri alışverişi yapmasını sağlayan bir köprüdür.

İnsanların web sitelerini kullanabilmesi için butonlar ve menülerden oluşan görsel arayüzler (UI) tasarlanır. API'ler ise kodların ve programların birbiriyle anlaşabilmesi için tasarlanmış sistemsel arayüzlerdir.

2. Restoran Benzetmesi ile API Mantığı
API'nin çalışma prensibini anlamak için bir restorandaki işleyişi inceleyelim:

* Müşteri (İstemci / Sizin Kodunuz): Masada oturan ve yemek siparişi vermek isteyen kişidir.
* Mutfak (Sunucu / Veritabanı): Siparişlerin hazırlandığı, tüm malzemelerin ve ham verilerin bulunduğu güvenli bölgedir. Bir müşteri olarak mutfağa doğrudan girip malzemeleri alamazsınız.
* Garson (API): Sizin masanıza gelir, siparişinizi (isteğinizi) alır, mutfağa götürür. Mutfakta hazırlanan yemeği (yanıtı) alıp tekrar size pürüzsüzce teslim eder.
* Bu senaryoda Garson, tam olarak bir API gibi davranır. Arka plandaki veritabanını dış dünyaya karşı korur ama kurallara uygun bir istek (Request) götürdüğünüzde size istediğiniz veriyi (Response) servis eder.

3. Gerçek Hayatta API'ler Nerede Karşımıza Çıkar?

* Hava Durumu Uygulamaları: Akıllı telefonunuzdaki hava durumu uygulaması kendi uydusuna sahip değildir. Arka planda uluslararası bir meteoroloji merkezinin API'sine bağlanarak anlık hava verilerini çeker ve ekranınıza basar.

* "Google ile Giriş Yap" Butonları: Bir web sitesine üye olurken bu butona tıkladığınızda, o site sizin Google şifrenizi göremez. Google'ın giriş API'sine sorar: "Bu kullanıcı gerçekten o mu?". API'den onay gelirse sisteme girişiniz yapılır.

* Ödeme Sistemleri: Bir e-ticaret sitesinden alışveriş yaparken kart bilgilerinizi girdiğinizde, site kartı kendi veritabanına kaydetmez. Arka planda bir bankanın Ödeme API'sine veriyi gönderir, bankadan onay yanıtı gelirse siparişi tamamlar.

4. API'lerin Ortak Dili: JSON Formatı

API'ler sistemler arası köprü olduğu için tüm programlama dillerinin (Python, C#, Java, PHP vb.) ortaklaşa anlayabileceği evrensel bir veri formatı kullanırlar. Bu formata JSON (JavaScript Object Notation) denir.

JSON yapısı, Python derslerimizde öğrendiğimiz Sözlük (Dictionary) yapısının neredeyse birebir aynısıdır:

{
  "durum": "basarili",
  "sehir": "Istanbul",
  "sicaklik": 24.5,
  "hava_durumu": "Gunesli"
}

Python kodlarımızla bir API'ye istek attığımızda, bize yukarıdaki gibi bir JSON paketi döner. Biz de Python'ın veri analiz gücünü kullanarak bu sözlük yapısını çözümler ve projelerimizde kullanırız.

"""