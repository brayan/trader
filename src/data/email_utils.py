# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# with open(textfile, 'rb') as fp:
    # Create a text/plain message
    # msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
email_from = "brayan.bedritchuk@gmail.com"
email_to = "brayan.bedritchuk@gmail.com"

msg['Subject'] = "My subject"
msg['From'] = email_from
msg['To'] = email_to

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(email_from, [email_to], msg.as_string())
s.quit()