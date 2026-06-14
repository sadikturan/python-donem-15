"""
Sanal Ortam (Virtual Environment - venv) Nedir?

Yazılıma yeni başlayanların en çok zorlandığı ama büyük projelerde hayat kurtaran kavram sanal ortamdır.

Problem: Bilgisayarınızda iki farklı proje üzerinde çalıştığınızı düşünün.
A Projesi (eski bir proje) eski bir kütüphane sürümü kullanıyor: pandas==1.0
B Projesi (yeni bir proje) en güncel özellikleri istiyor: pandas==2.2

Eğer kütüphaneleri doğrudan bilgisayarınızın ana sistemine (global) yüklerseniz, bu iki proje birbiriyle çelişir ve sürümler birbirini bozarak projelerin çökmesine neden olur.

Çözüm: Her proje için o projenin klasörüne özel, dış dünyadan izole edilmiş Sanal bir Python Odası (Virtual Environment) kurarız. Bu sayede A projesinin odasındaki kütüphane, B projesini asla etkilemez.

1- Sanal Ortam Nasıl Kurulur ve Yönetilir?

Yöntem 1: Vs Code Üzerinden Kurulum: Python eklentisiyle birlikte gelen "Python: Create Environment" komutunu kullanabilirsiniz. Bu komut, proje klasörünüzün içinde .venv adında, içinde temiz bir Python kopyası olan yeni bir klasör yaratır.

Yöntem 2: Terminal Üzerinden Kurulum (Windows, Linux, MacOS) 

python -m venv .venv

Bu komut, proje klasörünüzün içinde myenv adında, içinde temiz bir Python kopyası olan yeni bir klasör yaratır

2- Sanal Ortamı Aktif Etme

.venv\Scripts\activate
source .venv/bin/activate

** Aktif olduğunda terminal satırınızın en başında (.venv) ibaresini görürsünüz. Artık yapacağınız tüm pip install işlemleri sadece bu projeye özel kalır.

3- Sanal Ortamı Kapatma

deactivate

3- requirements.txt

Projenizi bir arkadaşınıza veya sunucuya (server) taşırken, devasa boyutlardaki sanal ortam klasörünü (.env) kopyalamazsınız. Bunun yerine sadece projenizin çalışması için hangi kütüphanelerin hangi sürümlerle yüklendiğini listeleyen küçük bir metin belgesi oluşturursunuz.

Sanal ortamınız aktifken listenin çıktısını almak için:

"pip freeze > requirements.txt"   => Bu komut otomatik olarak projenizin kök dizinine requirements.txt dosyasını oluşturur.
"pip install -r requirements.txt" => Bu komut ise requirements.txt dosyasındaki tüm kütüphaneleri tek seferde yükler.


"""





