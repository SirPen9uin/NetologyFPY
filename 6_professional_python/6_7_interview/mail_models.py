import email
import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class Mail():

    def __init__(self, smtpserver: str, imapserver: str, login: str, password: str):
        self.smtpserver = smtpserver
        self.imapserver = imapserver
        self.login = login
        self.password = password

    def send_mail(self, recipients: str, subject: str, message_content: str):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ','.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(message_content, 'plain'))

        try:
            with smtplib.SMTP(self.smtpserver, 587) as server:
                server.starttls()
                server.login(self.login, self.password)
                server.sendmail(self.login, recipients, message.as_string())
        except Exception as e:
            print(f'Ошибка при отправке. {e}')

    def receive_mail(self, header: str=None):
        try:
            mail = imaplib.IMAP4_SSL(self.imapserver)
            mail.login(self.login, self.password)
            mail.select('inbox')

            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            _, data = mail.uid('search', None, criterion)
            latest_email_uid = data[0].split()[-1]

            _, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)

            mail.logout()
            return email_message
        except Exception as e:
            print(f'Ошибка получения. {e}')