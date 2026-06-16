import requests

# 1. ADIM: Fixer.io base URL'i ve sizin üyelik anahtarınız
# Ücretsiz planda istek adresi 'http' olmalıdır, 'https' ücretli planlar içindir.
BASE_URL = "http://data.fixer.io/api/latest"
API_KEY = "d29ddb067a61c433fd62c9fa39c450d5"

# Kullanıcı girdilerini alıyoruz (Standart olması için büyük harfe çeviriyoruz)
bozulan_doviz = input("Bozulan döviz türü (Örn: USD, TRY, EUR): ").strip().upper()
alinan_doviz = input("Alınan döviz türü (Örn: USD, TRY, EUR): ").strip().upper()
miktar = float(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

# URL'e access_key parametresini ekleyerek isteğimizi atıyoruz
url = f"{BASE_URL}?access_key={API_KEY}"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        result = response.json()  # json.loads(result.text) yerine bu yöntem daha pratik ve moderndir.
        
        # API'nin başarılı dönüp dönmediğini kontrol ediyoruz (Key yanlışsa veya limit bittiyse false döner)
        if result.get("success"):
            rates = result["rates"]
            
            # 2. ADIM: Ücretsiz plan kısıtlamasını çözen Matematiksel Formül (EUR Çapraz Kuru)
            # Fixer bize sadece EUR tabanlı kur verdiği için; bozulan ve alınan parayı önce EUR değerine oranlıyoruz.
            eur_to_bozulan = rates[bozulan_doviz]
            eur_to_alinan = rates[alinan_doviz]
            
            # 1 birim bozulan paranın alınan para cinsinden değeri
            tekli_kur = eur_to_alinan / eur_to_bozulan
            toplam_karislik = miktar * tekli_kur
            
            # 3. ADIM: Çıktıları Ekrana Yazdırma
            print("\n" + "-"*45)
            # Sizin kullandığınız .format() yöntemi yerine yeni nesil f-string kullanımı kodu daha okunabilir kılar:
            print(f" Canlı Kur: 1 {bozulan_doviz} = {round(tekli_kur, 4)} {alinan_doviz}")
            print(f" İşlem Sonucu: {miktar} {bozulan_doviz} = {round(toplam_karislik, 2)} {alinan_doviz}")
            print("-"*45)
            
        else:
            print("\n API Hatası:", result["error"]["info"])
            
    else:
        print(f"\n Sunucuya bağlanılamadı. HTTP Durum Kodu: {response.status_code}")

except KeyError:
    print("\n HATA: Girdiğiniz döviz türlerinden biri geçersiz veya desteklenmiyor!")
except requests.exceptions.ConnectionError:
    print("\n BAĞLANTI HATASI: İnternet bağlantınızı kontrol edin.")
except Exception as e:
    print(f"\n Beklenmedik bir hata oluştu: {e}")