import requests

# 1. ADIM: Siteden aldığınız gizli anahtarı buraya string olarak yazmalısınız
API_KEY = "8f0037e1ff19487abe79b61577842389"

# f-string kullanarak anahtarımızı URL'in içine güvenle gömüyoruz
url = f'https://newsapi.org/v2/everything?language=tr&q=bitcoin&apiKey={API_KEY}'

try:
    response = requests.get(url)
    
    # 2. ADIM: HTTP durum kodunu kontrol edelim (200 ise her şey yolunda)
    if response.status_code == 200:
        news = response.json()
        print(f"Toplam {news['totalResults']} haber bulundu!\n")
        print("İlk 5 haber başlığı:")
        for article in news['articles'][:5]:
            print(f"- {article['title']}")
        print("Haberler başarıyla internetten çekildi!\n")
    else:
        print(f"Bir sorun oluştu! Durum Kodu: {response.status_code}")
        
except requests.exceptions.ConnectionError:
    print("Bağlantı Hatası: İnternetiniz kapalı olabilir.")