"""
SELENIUM NEDİR VE NEDEN İHTİYAÇ DUYARIZ?

Şu ana kadar web kazıma (Web Scraping) işlemlerimizi requests ve BeautifulSoup kütüphanelerini kullanarak yaptık. Bu ikili, statik web sitelerinden veri çekmek için harika ve çok hızlı bir çözümdür.

Ancak modern web dünyasında her site düz HTML kodlarından oluşmaz. İşte bu noktada karşımıza çıkan büyük bir engeli aşmak için Selenium kütüphanesine ihtiyaç duyarız.

1. Selenium Nedir?
Selenium; aslında web uygulamalarını test etmek için geliştirilmiş, ancak veri kazıma dünyasında da sıklıkla kullanılan bir tarayıcı otomasyon aracıdır.

Yazdığınız Python koduyla bilgisayarınızdaki gerçek bir tarayıcıyı (Google Chrome, Firefox vb.) canlı olarak ayağa kaldırır; sitelere otomatik tıklama, form doldurma, sayfayı aşağı kaydırma ve butonları tetikleme gibi bir insanın yapabileceği tüm hareketleri simüle eder.

2. Neden İhtiyaç Var? requests ile İşleri Çözemez miyiz?

Sorunun kısa cevabı: Hayır, her sitede çözemezsiniz. requests kütüphanesi sadece bir sitenin sunucusuna gider, o an duran ham HTML kodunu indirir ve işi biter. requests bir tarayıcı değildir. Dolayısıyla sayfanın içindeki JavaScript (JS) kodlarını çalıştıramaz.

requests Kütüphanesinin Çaresiz Kaldığı 3 Senaryo:

** 1- Dinamik İçerikler (JavaScript/AJAX): Modern web siteleri (Örn: Twitter, Sahibinden, Trendyol, Akakçe, borsa siteleri) ilk açıldıklarında boş bir HTML sayfası yüklerler. Sayfa yüklendikten saliseler sonra arka plandaki JavaScript kodları çalışır ve verileri (fiyatları, tweetleri) ekrana getirir. requests bu sitelere gittiğinde sadece o ilk boş sayfayı indirir, verileri asla göremez.

** 2- Sonsuz Kaydırma (Infinite Scroll): Sayfayı aşağı kaydırdıkça yeni ürünlerin veya gönderilerin yüklendiği sitelerde requests sadece ilk ekranı görür. Aşağı kaydırma hareketini taklit edemez.

** 3- Giriş ve Etkileşim Zorunluluğu: Bir veriye ulaşmak için önce bir butona tıklamanız, bir açılır menüden (Dropdown) seçim yapmanız veya kullanıcı adı/şifre yazıp giriş yapmanız gerekiyorsa requests burada kilitlenir.


"""