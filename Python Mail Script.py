from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# send Emails 
def mail(subject1,body1):
    smtp_server = 'smtp.office365.com'
    smtp_port = 587  
    smtp_username = ''
    smtp_password =""                                                 #get_email_password(tenant_id, client_id, client_secret, key_vault_url)
    # Sender and recipient details
    sender = ''
    recipient = ''
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject1
    body = body1
    message.attach(MIMEText(body, 'html'))
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)


subject1='test'
body1='python'
mail(subject1,body1)