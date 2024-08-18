from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib

# googleでアプリパスワードを設定する必要がある
smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'test@mail.com'
to_email = 'メールアドレス'
username = 'メールアドレス'
password = 'パスワード'

msg = MIMEMultipart()
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(MIMEText('test message'))

# ファイル読み込み
with open('email/file.txt', 'rb') as f:
    attach = MIMEApplication(f.read())

attach.add_header('Content-Disposition', 'attachment', filename='file.txt')
msg.attach(attach)

server = smtplib.SMTP(smtp_host, smtp_port)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.close()

print('メールを送信しました。')
