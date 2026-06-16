import requests

url = "https://jsonplaceholder.typicode.com/todos"

# Sunucuya diyoruz ki: "Sadece kullanıcı ID'si 3 olan VE tamamlanmış olanları getir."
coklu_filtre = {
    "userId": 3,
    "completed": "true" # API standartları gereği boolean değerler bazen string olarak gönderilir
}

# Arka planda oluşacak URL:
# https://jsonplaceholder.typicode.com/todos?userId=3&completed=true
yanit = requests.get(url, params=coklu_filtre)

if yanit.status_code == 200:
    gelen_veriler = yanit.json()
    print(f"Filtreye Uyan Toplam Kayıt Sayısı: {len(gelen_veriler)}\n")
    
    print("--- 3 Numaralı Kullanıcının Tamamlanmış Görevleri ---")
    print("-" * 60)
    for g in gelen_veriler:
        print(f"ID: {g['id']} | Durum: ✔️ | Başlık: {g['title']}")