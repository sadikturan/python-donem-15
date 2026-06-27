import os
from analyzer import SentimentAnalyzer

analizci = SentimentAnalyzer()

dosya_yolu = "yorumlar.txt"
rapor_yolu = "analiz_raporu.txt"

print("Analiz sistemi başlatılıyor...")

basarili_sonuclar = []
hatali_yorum_sayisi = 0

if os.path.exists(dosya_yolu):
    with open(dosya_yolu, "r", encoding="utf-8") as file:
        satirlar = file.readlines()

    print(f"Toplam {len(satirlar)} adet yorum bulundu. İşleniyor...")

    for satir in satirlar:
        yorum = satir.strip()
        if not yorum:
            continue

        print(f"İnceleniyor: {yorum}")
        analiz_sonucu = analizci.analyze_text(yorum)

        # KRİTİK KONTROL: Eğer API hata döndüyse listeye ekleme, sayacı artır
        if analiz_sonucu.get("sentiment") == "Hata":
            print(f"Bu yorum yoğunluk nedeniyle analiz edilemedi, atlanıyor.")
            hatali_yorum_sayisi += 1
            continue

        analiz_sonucu["original_text"] = yorum
        basarili_sonuclar.append(analiz_sonucu)

    # DÖNGÜ BİTTİ - Raporlama aşamasına geçiyoruz
    print("\n[İşlem Tamamlandı] Tüm yorumlar incelendi. Rapor hazırlanıyor...")

    toplam_basarili = len(basarili_sonuclar)

    # Eğer hiçbir yorum başarıyla analiz edilemediyse rapor oluşturmayı engelle
    if toplam_basarili == 0:
        print(
            f"Hata: Hiçbir yorum başarıyla analiz edilemedi. (Tüm {hatali_yorum_sayisi} istek 503 hatasına takıldı)."
        )
    else:
        pozitif_sayisi = sum(
            1 for x in basarili_sonuclar if x["sentiment"] == "Pozitif"
        )
        negatif_sayisi = sum(
            1 for x in basarili_sonuclar if x["sentiment"] == "Negatif"
        )
        notr_sayisi = sum(
            1 for x in basarili_sonuclar if x["sentiment"] == "Nötr"
        )

        # Güvenli en yüksek/en düşük puan tespiti
        en_mutlu = max(basarili_sonuclar, key=lambda x: int(x["score"]))
        en_kizgin = min(basarili_sonuclar, key=lambda x: int(x["score"]))

        rapor_icerigi = f"""
        --- DUYGU ANALİZİ RAPORU ---

        Genel Durum
        -------------------
        Başarıyla Analiz Edilen Toplam Yorum: {toplam_basarili}
        Yoğunluk Nedeniyle Atlanan Yorum    : {hatali_yorum_sayisi}
        
        Dağılım:
        - Pozitif  : {pozitif_sayisi}
        - Negatif  : {negatif_sayisi}
        - Nötr     : {notr_sayisi}

        En Mutlu Müşteri Score: {en_mutlu['score']} Puan
        Yorum: {en_mutlu['original_text']}

        En Kızgın Müşteri Score: {en_kizgin['score']} Puan
        Yorum: {en_kizgin['original_text']}
        """

        with open(rapor_yolu, "w", encoding="utf-8") as f:
            f.write(rapor_icerigi)

        print(f"Rapor başarıyla '{rapor_yolu}' dosyasına yazıldı.")

else:
    print("Dosya bulunamadı.")