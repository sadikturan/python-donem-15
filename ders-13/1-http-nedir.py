"""
HTTP (Hypertext Transfer Protocol), Türkçe karşılığıyla Hiper Metin Transfer Protokolü, internette tarayıcınız (istemci) ile web sitelerinin barındığı sunucu (server) arasındaki veri alışverişinin kurallarını belirleyen en temel iletişim protokolüdür.


HTTP Nasıl Çalışır? (İstek ve Yanıt Mimarisi)

HTTP, tamamen bir "İstek-Yanıt" (Request-Response) döngüsü üzerine kuruludur. Bu süreçte iki ana aktör vardır:

1- İstemci (Client): Genellikle sizin web tarayıcınızdır (Google Chrome, Safari, Edge vb.).

2- Sunucu (Server): Web sitesinin kodlarının, görsellerinin ve veritabanının tutulduğu uzak bilgisayardır.

Süreç tıpkı bir restoranda sipariş vermeye benzer:

1- İstek (Request): Tarayıcınızın adres çubuğuna www.google.com yazıp Enter'a bastığınızda, sunucuya bir garson gibi gidip "Bana Google'ın ana sayfa kodlarını getir" dersiniz.

2- Yanıt (Response): Sunucu bu isteği alır, mutfakta hazırlar (kodları işler) ve tarayıcınıza HTML, CSS, JavaScript ve görsel dosyalarını içeren bir yanıt paketleri fırlatır. Tarayıcınız da bu kodları birleştirerek karşınıza renkli web sayfasını çıkarır.

HTTP İstek Metotları (Methods)

Bir web sayfasına gittiğinizde sadece veri çekmezsiniz; bazen form doldurur, bazen bir fotoğraf silersiniz. HTTP, sunucuya ne yapmak istediğinizi anlatmanız için belirli fiiller (metotlar) kullanır:

1- GET: Sunucudan veri okumak/almak için kullanılır. (Örn: Bir haber sitesindeki makaleyi görüntülemek).

2- POST: Sunucuya yeni bir veri gönderip kaydetmek için kullanılır. (Örn: Bir siteye üye olurken şifre ve kullanıcı adı formunu göndermek).

3- PUT / PATCH: Sunucudaki mevcut bir veriyi güncellemek için kullanılır. (Örn: Profil resminizi değiştirmek).

4- DELETE: Sunucudaki bir veriyi silmek için kullanılır. (Örn: Attığınız bir tweet'i silmek).

HTTP Durum Kodları (Status Codes)

Sunucu, tarayıcınızın yaptığı isteğe karşılık gönderdiği yanıt paketinin içine 3 haneli bir durum kodu sıkıştırır. Bu kod, işlemin başarıyla tamamlanıp tamamlanmadığını söyler.

* 2xx (Başarı)	       => İstek başarıyla alındı ve işlendi.200 OK: Her şey yolunda, sayfa yükleniyor.
* 3xx (Yönlendirme)	   => Aradığınız sayfa başka bir adrese taşındı. 301 Moved Permanently: Sayfa kalıcı olarak taşındı.
* 4xx (İstemci Hatası) => Hata sizden (tarayıcıdan) kaynaklı.	404 Not Found: Aradığınız sayfa veya link web sitesinde yok!
* 5xx (Sunucu Hatası)  => Web sitesinin kendi bilgisayarı çöktü.500 Internal Server Error: Sunucunun yazılımında hata oluştu.

"""