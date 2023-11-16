import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr

# 发送方邮箱信息
sender_email = "2846150854@qq.com"
sender_name = "Jack_Test"
sender_password = "qcxblsaegurtdghb"

# 接收方邮箱信息
receiver_email = "2846150854@qq.com"
receiver_name = "测试"

# 邮件主题
subject = "GitHub Actions Logs"

# 构造邮件
message = MIMEMultipart()
message["From"] = formataddr((sender_name, sender_email))
message["To"] = formataddr((receiver_name, receiver_email))
message["Subject"] = subject

# 邮件正文
body = "GitHub Actions Logs"
message.attach(MIMEText(body, "plain"))

# 附件（logs.txt）
attachment_path = "artifacts/logs.txt"
attachment = MIMEApplication(open(attachment_path, "rb").read())
attachment.add_header("Content-Disposition", "attachment", filename="logs.txt")
message.attach(attachment)

# 连接 SMTP 服务器
smtp_server = "smtp.qq.com"
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# 登录邮箱
server.login(sender_email, sender_password)

# 发送邮件
server.sendmail(sender_email, receiver_email, message.as_string())

# 关闭连接
server.quit()
