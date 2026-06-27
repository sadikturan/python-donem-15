from database import get_connection

def urunleri_listele(limit=5):
    """Tüm ürünleri fiyatına göre azalan sırada listeler."""
    sorgu = """
        SELECT TOP (?) ProductID, ProductName, UnitPrice, UnitsInStock 
        FROM Products 
        ORDER BY UnitPrice DESC
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(sorgu, limit)
    sonuc = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return sonuc


def urun_getir_by_id(product_id):
    """ID değerine göre tek bir ürünün detayını getirir."""
    sorgu = """
        SELECT ProductID, ProductName, UnitPrice, UnitsInStock 
        FROM Products 
        WHERE ProductID = ?
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(sorgu, product_id)
    sonuc = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return sonuc


def urun_ekle(urun_adi, fiyat, stok):
    """Products tablosuna yeni bir ürün ekler."""
    sorgu = """
        INSERT INTO Products (ProductName, UnitPrice, UnitsInStock)
        VALUES (?, ?, ?)
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(sorgu, (urun_adi, fiyat, stok))
    conn.commit()  # Değişikliği veritabanına kaydet
    
    cursor.close()
    conn.close()
    print(f"✅ {urun_adi} ürünü başarıyla eklendi.")


def urun_guncelle_fiyat(product_id, yeni_fiyat):
    """ID değeri verilen ürünün fiyatını günceller."""
    sorgu = """
        UPDATE Products 
        SET UnitPrice = ? 
        WHERE ProductID = ?
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(sorgu, (yeni_fiyat, product_id))
    conn.commit()  # Değişikliği veritabanına kaydet
    
    cursor.close()
    conn.close()
    print(f"🔄 ID: {product_id} olan ürünün fiyatı ${yeni_fiyat} olarak güncellendi.")


def urun_sil(product_id):
    """ID değeri verilen ürünü tablodan siler."""
    sorgu = """
        DELETE FROM Products 
        WHERE ProductID = ?
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(sorgu, product_id)
    conn.commit()  # Değişikliği veritabanına kaydet
    
    cursor.close()
    conn.close()
    print(f"🗑️ ID: {product_id} olan ürün silindi.")


if __name__ == "__main__":
    
    print("--- 1. YENİ ÜRÜN EKLEME TESTİ ---")
    urun_ekle(urun_adi="Kablosuz Kulaklık", fiyat=89.99, stok=50)

    print("\n" + "="*50 + "\n")

    print("--- 2. EN PAHALI ÜRÜNLERİ LİSTELEME TESTİ ---")
    for row in urunleri_listele(limit=3):
        print(f"ID: {row.ProductID} | {row.ProductName} - Fiyat: ${row.UnitPrice:.2f} | Stok: {row.UnitsInStock}")

    print("\n" + "="*50 + "\n")

    print("--- 3. FİYAT GÜNCELLEME TESTİ ---")
    # Eklediğimiz veya var olan bir ürünün fiyatını değiştirelim (Örn ID: 78)
    urun_guncelle_fiyat(product_id=78, yeni_fiyat=95.50)

    print("\n" + "="*50 + "\n")

    print("--- 4. TEK VERİ DETAYI TESTİ ---")
    urun = urun_getir_by_id(78)
    if urun:
        print(f"Güncel Durum -> Ürün: {urun.ProductName} | Yeni Fiyat: ${urun.UnitPrice:.2f}")

    print("\n" + "="*50 + "\n")

    print("--- 5. ÜRÜN SİLME TESTİ ---")
    urun_sil(product_id=78)