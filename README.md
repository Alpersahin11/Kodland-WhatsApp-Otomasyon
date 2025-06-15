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
git clone https://github.com/alpersahin11/Kodland-WhatsApp-Otomasyon.git
cd Kodland-WhatsApp-Otomasyon
pip install -r requirements.txt
```

## 📂 Ayarlar

Projenin davranışını `ayarlar.py` dosyası üzerinden değiştirebilirsiniz:

| Ayar          | Açıklama                                                          | Örnek                                |
|---------------|-------------------------------------------------------------------|--------------------------------------|
| `group_link`  | Kodland BackOffice grup linki                                     | `"https://backoffice.kodland.org/en/group_..../"` |
| `grup_kontrol`| Numara grupta var mı kontrol edilsin mi? (True / False)           | `True`                               |
| `grup_davet`  | Tanışma mesajı gönderilsin mi? (True / False)                     | `False`                              |
| `message_detay` | Grup adı ve WhatsApp grubu linki                                  | `{"Grup":"TUR29....","Link":"https://chat.whatsapp.com/..."}` |
| `message`     | Gönderilecek tanışma mesajı                                       | Çok satırlı özel mesaj metni        |

## 🔧 Özelleştirme

- **Mesaj İçeriği:** `ayarlar.py` → `message` değişkeni içerisinde kendi mesajınızı yazabilirsiniz ve Metin biçimlendirme Yapabilirsiniz
  Metin biçimlendirme örnekleri:

- *İtalik metin* için:  `_metin_`  
  Örnek: *İtalik metin* veya _İtalik metin_

- **Kalın metin** için: `**metin**`  
  Örnek: **Kalın metin** 

- ~~Üstü çizili metin~~ için: `~~metin~~`  
  Örnek: ~~Üstü çizili metin~~
  
- **Emoji Desteği:** Mesaj içerisinde emojiler kullanılabilir.


## 🚀 Projeyi Çalıştırma

Projeyi çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

```bash
python main.py
```

- Lütfen otomasyonu etik ve yasal sınırlar içinde kullanınız.
