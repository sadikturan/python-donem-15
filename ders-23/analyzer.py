from google import genai
import json
from pydantic import BaseModel, Field
from google.genai import types

MY_API_KEY = "api_key"

class SentimentResponse(BaseModel):
    sentiment: str = Field(description="Pozitif, Negatif veya Nötr değerlerinden biri")
    score: int = Field(description="0 ile 100 arasında bir sayı. (100 = Çok olumlu)")
    summary: str = Field(description="Metnin ana fikri (Maksimum 10 kelime)")
    language: str = Field(description="Metnin dili (tr, en, de vb.)")

class SentimentAnalyzer:
    def __init__(self):
        try:
            self.client = genai.Client(api_key=MY_API_KEY)
            self.model = "gemini-2.5-flash"
        except Exception as e:
            print("Connection error:", e)

    def analyze_text(self, text):
        if not text:
            return {"error": "Boş metin gönderildi."}
        
        prompt = f"""
            Sen profesyonel bir duygu analizi ve dil uzmanısın.
            Aşağıdaki metni analiz et.

            {text}

            Lütfen yanıtı SADECE (başka hiç bir açıklama olmadan) aşağıdaki JSON formatında ver.

            {
                {
                    "sentiment": "Pozitif, Negatif veya Nötr",
                    "scora": "0 ile 100 arasında bir sayı. (100 = Çok olumlu)",
                    "summary": "Metnin ana fikri (Maksimum 10 kelime)",
                    "language": "Metnin dili (tr,en,de vb.)"
                }
            }
        """

        config = types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=SentimentResponse,
                temperature=0.1 # Daha kararlı ve kesin sonuçlar için sıcaklığı düşürüyoruz
            )

        try:
            response = self.client.models.generate_content(
                model=self.model, 
                contents=prompt,
                config=config
            )

            result = json.loads(response.text)

            return result
        
        except Exception as e:
            print("hata:", e)

            return {
                "sentiment": "Hata",
                "score": 0,
                "summary": "Bilinmiyor",
                "language": "Bilinmiyor",
                "error_detail": str(e)
            }


if __name__ == "__main__":
    analizci = SentimentAnalyzer()

    # ornek_yorum = "Ürünü beğendim ama kargo çok geç kaldı, biraz sinirlendim."
    # ornek_yorum = "Ürün harika, paketleme çok özenliydi. Teşekkürler!"
    ornek_yorum = "Hayatımda gördüğüm en kötü kargo deneyimi, sakın almayın."

    sonuc = analizci.analyze_text(ornek_yorum)

    print(sonuc)

