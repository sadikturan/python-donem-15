"""
Set Nedir?

1- Benzersiz Elemanlar (Unique): Bir set içinde aynı eleman sadece bir kez var olabilir. Aynı elemanı defalarca eklemeye çalışsanız bile Python bunu tek bir eleman olarak görür.

2- Sırasızdır (Unordered): Listeler gibi elemanların belirli bir indeksi (0, 1, 2) yoktur. Elemanlar hafızada karmaşık bir düzende tutulur. Bu yüzden liste[0] yazarak bir elemana erişemezsiniz.

3- Değiştirilebilir Ama Elemanları Sabittir (Mutable but Unchangeable): Kümenin kendisine yeni elemanlar ekleyip silebilirsiniz, ancak kümenin içindeki mevcut bir elemanı (örneğin "Elma"yı "Armut" olarak) güncelleyemezsiniz.

"""
# 1- Set Nasıl Oluşturulur?

# Basit bir set tanımlama
renkler = {"Kırmızı", "Mavi", "Yeşil", "Mavi", "Kırmızı"}

# Python mükerrer (tekrar eden) elemanları otomatik temizler:
print(renkler)  # Çıktı: {'Yeşil', 'Mavi', 'Kırmızı'} (Sıralama sizde farklı çıkabilir)

# EN KRİTİK NOKTA: Boş Küme Nasıl Tanımlanır?
# Boş bir süslü parantez {} Python tarafından BOŞ SÖZLÜK (dict) olarak algılanır.
bos_sozluk = {} 
print(type(bos_sozluk)) # <class 'dict'>

# Boş bir küme oluşturmak için mutlaka set() fonksiyonu kullanılmalıdır:
bos_kume = set()
print(type(bos_kume))   # <class 'set'>

# 2. Set Eleman Ekleme ve Silme Metotları

programlama_dilleri = {"Python", "R", "SQL"}

# 1. Eleman Ekleme: .add()
programlama_dilleri.add("Javascript")
programlama_dilleri.add("Python") # Zaten var olduğu için hiçbir şey değişmeyecek.
print(programlama_dilleri)

# 2. Eleman Silme: .remove() veya .discard()
# .remove() kullanırken silinecek eleman kümede yoksa Python hata verir (Sistem çöker).
programlama_dilleri.remove("R") 

# .discard() kullanırken eleman kümede yoksa hata vermez, sessizce devam eder (Daha güvenlidir).
programlama_dilleri.discard("Java") 
print(programlama_dilleri)

