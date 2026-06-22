from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.github.com"
    
driver.get(url)

time.sleep(2)

# driver.maximize_window()
# driver.set_window_size(400, 400)
# driver.minimize_window()

print("Sayfa Başlığı:", driver.title)
print("Sayfa URL'si:", driver.current_url)
print("Sayfa Kaynağı:", driver.page_source)
# driver.set_screenshot("github_screenshot.png")

username = "sadikturan"
driver.get(f"{url}/{username}")

if username in driver.title.lower():
    print("GitHub profiline başarıyla ulaşıldı.")
    driver.set_screenshot("github_screenshot.png")
else:
    print("GitHub profiline ulaşılamadı.")

driver.back()

print("Geri gidildi. Şu anki URL:", driver.current_url)
time.sleep(2)

username = "sadikturan"
driver.get(f"{url}/{username}")

# driver.forward()
# driver.refresh()

time.sleep(5)
driver.quit()