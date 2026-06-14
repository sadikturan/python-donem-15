# muhasebe.py

sirket_adi = "Can Teknoloji A.Ş."

def maas_hesapla(ham_maas: float, mesai_saati: int) -> float:
    """Personelin mesai ücreti dahil net maaşını hesaplar."""
    mesai_ucreti = mesai_saati * 250
    return ham_maas + mesai_ucreti

def vergi_kesintisi(gelir: float) -> float:
    """Gelir üzerinden %20 vergi kesintisi hesaplar."""
    return gelir * 0.20

if __name__ == "__main__":
    print("maaş:", maas_hesapla(20000, 5))
    print("maaş:", maas_hesapla(30000, 15))
    print("vergi:", vergi_kesintisi(50000))