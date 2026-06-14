"""
1. Modül ve Paket Nedir?

Modül (Module): Python'da .py uzantılı her bir kod dosyası aslında bir modüldür. İçinde fonksiyonlar, sınıflar veya değişkenler barındırır.

Paket (Package): Birden fazla modülün (kod dosyasının) bir klasör altında toplanmış halidir. Örneğin, bir proje içinde veri işleme, görselleştirme ve modelleme gibi farklı görevler için ayrı modüller oluşturup bunları tek bir paket altında toplayabiliriz.

Kütüphane (Library): Belirli bir büyük problemi çözmek için yazılmış, içinde onlarca paket ve modül barındıran devasa kod koleksiyonlarıdır. Örneğin, veri bilimi için pandas, makine öğrenmesi için scikit-learn gibi.

Framework: Kütüphanelerden daha büyük ve kapsamlı yapılar olup, belirli bir uygulama türü (web, oyun, veri bilimi) geliştirmek için gerekli araçları ve kuralları sağlarlar. Örneğin: Django (web), TensorFlow (makine öğrenmesi), Unity (oyun).

Python kütüphaneleri temel olarak ikiye ayrılır:

1- Yerleşik (Built-in) Kütüphaneler: Python'ı bilgisayara kurduğumuzda kendiliğinden hazır gelen, internet bağlantısı veya indirme gerektirmeyen kütüphanelerdir (math, random, json, csv, os, datetime).

2- Harici (External) Kütüphaneler: Dünyadaki diğer yazılımcılar tarafından geliştirilen ve internetten bilgisayarımıza indirmemiz gereken kütüphanelerdir (pandas, numpy, requests).

"""

# Kütüphaneleri Projeye Dahil Etme Yöntemleri (import)

# 1- import modül_adı
import math

sonuc = math.sqrt(25) # math modülünün içindeki sqrt (karekök) fonksiyonunu kullandık.
print(sonuc) # 5.0

# 2- from modül_adı import fonksiyon_adı

from math import sqrt, pi

# Doğrudan fonksiyon adıyla çağırıyoruz, math.sqrt() yazmaya gerek yok
print(sqrt(36)) # 6.0
print(pi)       # 3.141592653589793

# 3- from modül_adı import *
from math import *
print(factorial(5)) # 120

# 4- import modül_adı as takma_ad
import datetime as dt
su_an = dt.datetime.now() # datetime yerine artık 'dt' yazabiliyoruz.




