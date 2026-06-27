from google import genai    # pip install google-genai
from dotenv import load_dotenv # pip install python-dotenv
from google.genai import types

# MY_API_KEY = "api_key"
# client = genai.Client(api_key=MY_API_KEY)

# .env dosyasındaki değişkenleri yükle
load_dotenv()

# client, .env içindeki GEMINI_API_KEY'i otomatik olarak algılar ve kullanır
client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Bana yazılımcılarla ilgili çok kısa,tek cümlelik bir komik bir şaka yap.",
        config=types.GenerateContentConfig(
            temperature=0.7  # Şaka daha yaratıcı olsun diye 0.7 bıraktık
        )
    )
    print(response.text)
    
except Exception as ex:
    print("hata oluştu")
    print(f"hata: {ex}")

