import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# E-posta sunucusu ayarları
smtp_server = 'smtp.gmail.com'
smtp_port = 465  # E-posta sunucunuzun kullandığı port numarasını kullanın
smtp_username = '@gmail.com'
smtp_password = ''  # Şifreyi düz metin olarak kullanmak güvenlik açısından riskli olabilir

# E-posta bilgileri
sender_email = '@gmail.com'
receiver_email = '@gmail.com'
subject = 'Test E-posta'
message = 'Bu bir test e-postasıdır.'

# E-posta oluştur
email = MIMEMultipart()
email['From'] = sender_email
email['To'] = receiver_email
email['Subject'] = subject

# E-posta içeriğini ekleyin
email.attach(MIMEText(message, 'plain'))

# E-posta sunucusuna bağlanın ve e-postayı gönderin
try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, email.as_string())
    print("E-posta başarıyla gönderildi.")
except Exception as e:
    print("E-posta gönderme sırasında bir hata oluştu: ", str(e))
finally:
    server.quit()
