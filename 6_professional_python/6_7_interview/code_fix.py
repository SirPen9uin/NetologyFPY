from mail_models import Mail

if __name__ == '__main__':
    gmail_smtp = 'smtp.gmail.com'
    gmail_imap = 'imap.gmail.com'
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'

    email_client = Mail(gmail_smtp, gmail_imap, login, password)
    email_client.send_mail(recipients, subject, message)
