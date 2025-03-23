import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg = MIMEMultipart()
msg["From"] = "shiowmei.hg@gmail.com"
msg["To"] = "shiowmei_huang@seed.net.tw"
msg["Subject"] = Header("Test send mail" , "utf-8").encode()
msg_content = MIMEText("this is test")
msg.attach(msg_content)

ssl_context = ssl.create_default_context()
"""
server = smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context)
server.login("shiowmei.hg@gmail.com","usbu eede drmv oriw")
server.sendmail("shiowmei.hg@gmail.com","shiowmei_huang@seed.net.tw", msg.as_string())
server.close()
"""
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
    server.login("shiowmei.hg@gmail.com","usbu eede drmv oriw")
    server.sendmail("shiowmei.hg@gmail.com","shiowmei_huang@seed.net.tw", msg.as_string())

print("success send mail")

