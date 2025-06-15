from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_whatsapp_group(driver, group_name):
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 30)

    # Arama ikonuna tıkla
    search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="search"]')))
    search_icon.click()
    time.sleep(1)

    # Arama kutusuna grup adını yaz
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]')))
    search_box.clear()
    search_box.send_keys(group_name)
    time.sleep(1)

    try:
        # Grup listede varsa → tıkla
        group = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{group_name}"]')))
        group.click()
        print(f"✅ Grup bulundu: {group_name}")
        return True
    except:
        print(f"❌ Grup bulunamadı: {group_name}")
        return False


def wp_kontrol_et(driver,telefonlar,group_title):
# Grup adını bul ve tıkla
    if open_whatsapp_group(driver, group_title):

        time.sleep(1)
        # Grup bilgilerini aç
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//header//div[@role="button"]'))).click()
        search_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@aria-hidden="true"][@data-icon="search"]'))
        )
        time.sleep(1)
        search_icon.click()


        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
        )
        time.sleep(1)
        print("Wp grubunda numaralar aranıyor.")
        toplam = 0
        for i in telefonlar:

            search_box.click()
            search_box.send_keys(Keys.CONTROL, 'a')  # Tüm metni seç
            search_box.send_keys(Keys.BACKSPACE)  # Sil

            search_box.send_keys(i)
            time.sleep(0.4)  # Yazdıktan sonra sonuçların gelmesi için biraz bekle
            try:
                # "Kişi bulunamadı" yazısı varsa kişi YOK
                not_found_element = driver.find_element(By.XPATH, '//span[text()="Kişi bulunamadı"]')
                print(f"❌ {i} bulunamadı.")
                toplam +=1
            except:
                print("✅ Kişi bulundu.")


        print(f"Wp grubunda numara arama tamamlandı. {toplam} kişi eksik")
