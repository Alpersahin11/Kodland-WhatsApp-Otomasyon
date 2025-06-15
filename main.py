from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
import pickle
import os

from  wp_kontrol import wp_kontrol_et
from wp_mesaj import send_whatsapp_message
import ayarlar

# Değişkenler
LOGIN_URL = "https://backoffice.kodland.org/en/login"

COOKIE_FILE = "cookies.pkl"


current_dir = os.getcwd()
profile_path = os.path.join(current_dir, "chrome_profile")

options = Options()
options.add_argument("--start-maximized")
options.add_argument(f"user-data-dir={profile_path}")

driver = webdriver.Chrome(options=options)

telefon = []

def bilgileri_al():

    try:
        group_link = ayarlar.group_link
    except:
        print("Grup Linki Bulunamadı.")
        group_link = "-1"

    try:
        message = ayarlar.message
    except:
        print("Mesaj Bilgisi Bulunamadı")
        message = "-1"

    try:
        grup_davet = ayarlar.grup_davet
    except:
        print("Grup daveti False Atandı")
        grup_davet = False

    try:
        grup_kontrol = ayarlar.grup_kontrol
    except:
        print("Grup Kontrolü False Atandı")
        grup_kontrol = False

    return group_link, message,grup_davet,grup_kontrol

def save_cookies():
    with open(COOKIE_FILE, "wb") as file:
        pickle.dump(driver.get_cookies(), file)

def load_cookies():
    with open(COOKIE_FILE, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

def telefon_bilgisi_al(TARGET_URL):

    if os.path.exists(COOKIE_FILE):
        # Cookie varsa yükle
        try:
            driver.get(TARGET_URL)
        except:
            print("group_link düzgün girilmemiş")
            return -1

        load_cookies()
        driver.refresh()
    else:
        # Cookie yoksa giriş yap
        driver.get(LOGIN_URL)
        input("Giriş Yaptıktan sonra Enter tuşuna basınız")
        save_cookies()
        try:
            driver.get(TARGET_URL)
        except:
            print("group_link düzgün girilmemiş")
            return -1
        print("✅ Cookie kaydedildi. Artık tekrar giriş yapmana gerek kalmayacak.")

    h4_elements = driver.find_elements(By.TAG_NAME, "h4")

    for h4 in h4_elements:
        text = h4.text.strip()
        if text.startswith("TUR"):
            grup_adi = text
            break

    # Tüm öğrenci linklerini bul
    time.sleep(1)

    # Öğrenci divlerini bul
    student_cards = driver.find_elements(By.CLASS_NAME, 'flex-grow-1')

    # Öğrenci linklerini listele
    student_links = []
    for card in student_cards:
        try:
            link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
            student_links.append(link)
        except:
            continue

    print(f"{len(student_links)} öğrenci bulundu.\n")
    print("Telefon numaraları alınıyor.")

    for url in student_links:
        driver.get(url)
        time.sleep(0.5)
        tried_again = False  # Tekrar deneme kontrolü

        while True:
            try:
                # Parent Information başlığı görünene kadar bekle
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//h2[text()="Parent Information"]'))
                )
                parent_info = driver.find_element(By.XPATH,
                                                  '//h2[text()="Parent Information"]/parent::div').get_attribute(
                    'textContent')

                match = re.search(r'\+\d{8,}', parent_info)
                if match:
                    phone = match.group()
                    telefon.append(phone)
                    break  # Telefon bulundu, döngüden çık
                else:
                    if not tried_again:
                        driver.refresh()
                        time.sleep(1)

                        tried_again = True
                    else:
                        print("Telefon bulunamadı",url)
                        break
            except Exception as e:
                if not tried_again:
                    driver.refresh()
                    time.sleep(1)
                    tried_again = True
                else:
                    print("Bilgi alınamadı, tekrar denendi ama hata devam ediyor:", e)
                    break

    print(f"{len(telefon)} Adet Telefon numarası alındı.")

    return {"telefon": telefon, "grup_adi": grup_adi}


group_link, message,grup_davet,grup_kontrol = bilgileri_al()


if grup_kontrol:
    bilgiler = telefon_bilgisi_al(group_link)
    if bilgiler != -1:
        wp_kontrol_et(driver,bilgiler["telefon"],bilgiler["grup_adi"])

if grup_davet and message != "-1":
    bilgiler = telefon_bilgisi_al(group_link)
    if bilgiler != -1:
        send_whatsapp_message(driver,bilgiler["telefon"],message)
