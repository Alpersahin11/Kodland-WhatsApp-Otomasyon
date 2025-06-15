##########################################
#     Kodland Bot Ayarları       #
##########################################

# 📌 Kodland Backoffice Grup Linki
# Örnek: "https://backoffice.kodland.org/en/group_XXXXX/"
group_link = "https://backoffice.kodland.org/en/group_...."

# 📌 WhatsApp grubunda numaralar kontrol edilsin mi?
# True → Kontrol eder, False → Etmez
grup_kontrol = True

# 📌 Tanışma mesajı gönderilsin mi?
# True → Aşağıdaki message içeriğini gönderir
# False → Mesaj gönderilmez, sadece kontrol yapılır
grup_davet = False


##########################################
#             Mesaj İçeriği              #
##########################################

# ℹ️ Grup bilgileri → Mesaj içinde otomatik yerleştirilecek
message_detay = {
    "Grup": "TUR2...",  # Buraya grup kodunu yazın
    "Link": "https://chat.whatsapp.com/Cvzk6.....",  # WhatsApp grup linki
    "Isim": "Alper Şahin", # Buraya adınızı yazın
    "Title": "Bilgisayar Mühendisi & Kodland Python Eğitmeni" # Buraya title yazın
}

# 📌 Gönderilecek Tanışma Mesajı
message = f"""
Merhaba, ben {message_detay["Isim"]}. Çocuklara yönelik yazılım, algoritma ve teknoloji eğitimleri vermekteyim. Bu alanda uzun süredir çalışıyor, aynı zamanda Python, yapay zeka ve oyun geliştirme gibi konularda da eğitmenlik yapıyorum.

Bu dönem Kodland ailesinde, *{message_detay["Grup"]}* kodlu sınıfta çocuğunuzun eğitmeni olacağım. Hep birlikte keyifli ve öğretici bir dönem geçireceğimize inanıyorum.

🎉 Kodland’a hoş geldiniz!
Kodland, çocukların yaratıcılığını geliştirmeyi ve teknolojiyi eğlenceli bir şekilde öğrenmelerini amaçlayan global bir eğitim platformudur.

👨‍💻 Bu 8 aylık kursta öğrencilerimiz şunları öğrenecek:

🔹 Temel Python Kavramları
🔹 Değişkenler ve veri tipleri (sayı, metin, mantıksal)
🔹 Koşul ifadeleri (if-elif-else)
🔹 Döngüler (for, while)
🔹 Mantıksal operatörler ve karşılaştırmalar
🔹 Fonksiyonlar 
🔹 2D Oyun Geliştirme (Pgzero kullanarak)
🔹 Proje Geliştirme Süreci
🔸 Final projesi: Öğrencinin kendi tasarladığı bir 2D oyun

🧠 Bu kurs, sadece kodlamayı öğretmekle kalmayacak; çocuklarımızın algoritmik düşünme, problem çözme, yaratıcılık, ve özgüven gibi 21. yüzyıl becerilerini geliştirmelerine de katkı sağlayacaktır.

📢 Süreç boyunca siz velilerimizle iletişimde kalmak bizler için çok önemli. Bu nedenle bir WhatsApp grubu oluşturduk. Duyurular, hatırlatmalar ve genel bilgilendirmeler bu grup üzerinden paylaşılacaktır.

👉 WhatsApp Grubu Linki: {message_detay["Link"]}

Lütfen bağlantıya tıklayarak gruba katılım sağlayınız.
Herhangi bir sorunuz olursa bana yazmaktan çekinmeyin. Size yardımcı olmaktan memnuniyet duyarım. 😊

Saygılarımla,
{message_detay["Isim"]} – {message_detay["Title"]}
"""
