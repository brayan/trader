import smtplib


def send_email():
    sender = 'brayan.bedritchuk@gmail.com'
    receivers = ['brayan.bedritchuk@gmail.com']

    message = """From: From Person <brayan.bedritchuk@gmail.com>
    To: To Brayan Bedritchuk <brayan.bedritchuk@gmail.com>
    Subject: SMTP e-mail test
    
    This is a test e-mail message.
    """

    try:
        smtp_obj = smtplib.SMTP('localhost')
        smtp_obj.sendmail(sender, receivers, message)
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
