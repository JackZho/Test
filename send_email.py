import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


def send_email(host, port, use_tls, username, password, to, subject):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = os.environ.get('EMAIL_FROM', 'GitHub Actions <github-actions@example.com>')
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)

    msg.attach(MIMEText("Workflow logs:\n\nArtifacts link:\n\nCheck the attached file for more details.\n", 'plain'))

    part = MIMEBase('application', "octet-stream")
    with open('logs.txt', 'rb') as f:
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="logs.txt"')

    msg.attach(part)

    server = smtplib.SMTP(host, port)
    if use_tls:
        server.starttls()
    server.login(username, password)
    server.sendmail(os.environ.get('EMAIL_FROM', 'GitHub Actions <github-actions@example.com>'), [to], msg.as_string())
    server.quit()


if __name__ == "__main__":
    host = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
    port = int(os.environ.get('EMAIL_PORT', '587'))
    use_tls = bool(os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true')
    username = os.environ.get('EMAIL_USERNAME', 'your-gmail-address')
    password = os.environ.get('EMAIL_PASSWORD', 'your-gmail-password')
    to = os.environ.get('EMAIL_TO', 'your-gmail-address')
    subject = os.environ.get('EMAIL_SUBJECT', 'GitHub Actions Log')

    send_email(host, port, use_tls, username, password, to, subject)
