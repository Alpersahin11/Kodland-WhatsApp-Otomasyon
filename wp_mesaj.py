from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pyperclip
import time

print("WhatsApp Web açıldı!")

def send_whatsapp_message(driver, phone_numbers, message):
    for phone_number in phone_numbers:
        url = f"https://web.whatsapp.com/send?phone={str(phone_number).replace('+','')}"
        driver.get(url)

        try:
            # Mesaj kutusunun açılması için bekle
            input_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
            msg_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, input_xpath))
            )
            time.sleep(1)


            # Kutunun içine tıkla
            pyautogui.click()
            time.sleep(1)

            pyperclip.copy(message)

            time.sleep(3)  # Kutunun yüklendiğinden emin ol, Selenium ile tıklandıysa 1-2 sn yetebilir
            pyautogui.hotkey("ctrl", "v")  # Yapıştır
            time.sleep(1)
            pyautogui.press("enter")
            
            time.sleep(1)

            print(f"✅ Mesaj gönderildi: {phone_number}")

        except Exception as e:
            print(f"❌ {phone_number} numarasına mesaj gönderilemedi → {e}")

        time.sleep(3)  # Diğer numaraya geçmeden önce kısa bekleme

