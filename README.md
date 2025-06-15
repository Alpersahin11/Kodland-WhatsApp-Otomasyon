# 📲 Kodland WhatsApp Otomasyon

Kodland eğitmenleri için geliştirilmiş **otomatik WhatsApp mesaj gönderme** projesidir. Bu proje sayesinde sınıf gruplarına tanışma ve bilgilendirme mesajlarını kolayca gönderebilirsiniz.

## 🚀 Özellikler

- ✅ WhatsApp Web otomatik giriş (QR kod kaydetme desteği)
- 📱 Öğrenci velilerine otomatik tanışma mesajı gönderme
- 📂 Chrome kullanıcı profili kaydı (QR tekrar okutmaya gerek kalmaz)
- 🗂️ Grupta numara kontrolü
- 🎨 Kolay özelleştirilebilir yapı

## ⚙️ Kurulum

```bash
git clone https://github.com/alpersah11/Kodland-WhatsApp-Otomasyon.git
cd Kodland-WhatsApp-Otomasyon
pip install -r requirements.txt

## 📂 Ayarlar

Projenin davranışını `ayarlar.py` dosyası üzerinden değiştirebilirsiniz:

| Ayar          | Açıklama                                                          | Örnek                                |
|---------------|-------------------------------------------------------------------|--------------------------------------|
| `group_link`  | Kodland BackOffice grup linki                                     | `"https://backoffice.kodland.org/en/group_48859/"` |
| `grup_kontrol`| Numara grupta var mı kontrol edilsin mi? (True / False)           | `True`                               |
| `grup_davet`  | Tanışma mesajı gönderilsin mi? (True / False)                     | `False`                              |
| `message_detay` | Grup adı ve WhatsApp grubu linki                                  | `{"Grup":"TUR29....","Link":"https://chat.whatsapp.com/..."}` |
| `message`     | Gönderilecek tanışma mesajı                                       | Çok satırlı özel mesaj metni        |

## 🔧 Özelleştirme

- **Mesaj İçeriği:** `ayarlar.py` → `message` değişkeni içerisinde kendi mesajınızı yazabilirsiniz.
- **Emoji Desteği:** Mesaj içerisinde emojiler kullanılabilir.
- **Numara Listesi:** Numara listesini `.csv` veya başka formatlardan alacak şekilde geliştirebilirsiniz.

## 📎 Örnek Mesaj Formatı

```plaintext
Merhaba, ben Alper Şahin. Bilgisayar mühendisiyim ve çocuklara yönelik yazılım, algoritma ve teknoloji eğitimleri vermekteyim...

🎉 Kodland’a hoş geldiniz!
👉 WhatsApp Grubu Linki: https://chat.whatsapp.com/.....
