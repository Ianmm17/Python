import smtplib
import ssl
from email.message import EmailMessage
from getpass import getpass

subject = 'Email From Python'
body = 'This is a test email from Python!'
sender_email = 'ianmm0917@gmail.com'
receiver_email = 'Jacob.Zacha@wwt.com'
password = getpass('Enter Password: ')

message = EmailMessage()
print(message)
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
# message.set_content(body)

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
        <p><img src='
    </body>
</html>
"""

message.add_alternative(html, subtype='html')

context = ssl.create_default_context()

print('sending email')

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    try:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email Sent!')
    except:
        print('Login Failed')
