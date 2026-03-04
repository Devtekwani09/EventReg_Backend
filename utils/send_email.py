import smtplib
from email.mime.text import MIMEText
from config import settings

def send_verification_email(to_email: str, otp: str):
    subject = "Email Verification OTP"
    body = f"Your OTP is: {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = settings.SMTP_USER
    msg["To"] = to_email

    server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
    server.starttls()
    server.login(settings.SMTP_USER, settings.SMTP_PASS)
    server.sendmail(settings.SMTP_USER, to_email, msg.as_string())
    server.quit()