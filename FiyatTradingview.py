#tradingview de belirli bir yatırım ensturumanını takip etme

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def get_crypto_price(symbol):
    try:
        xpath = f"//*[@id='js-category-content']/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]"
        fiyat = driver.find_element(By.XPATH, xpath).text
        print(f"{symbol} :", fiyat)
    except Exception as e:
        print(f"Hata ({symbol}):", e)

# Selenium için Chrome tarayıcı seçeneklerini ayarlamak için bir nesne oluşturuyoruz.
chromeOptions = webdriver.ChromeOptions()
# Tarayıcıyı gizli (incognito) modda çalıştırmak ve arka planda (headless) çalıştırmak
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--headless")
# WebDriver'ı bu ayarlarla başlatıyoruz.
driver = webdriver.Chrome(options=chromeOptions)

# Tarayıcıda belirtilen web sitelerine yönlendiriyoruz.
driver.get("https://tr.tradingview.com/symbols/JUPUSDT/")
driver.implicitly_wait(10)

while True:
  get_crypto_price("JUP")
  sleep(2)
    
