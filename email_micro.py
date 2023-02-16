import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

# Credentials for sender
gm_user = 'cs361testmicro@gmail.com'
gm_user_pw = 'TESTINGpassword541!'

# Credentials for reciever
gm_reciever = 'cs361recievetest@gmail.com'

# Outline message contents for email
msg = MIMEMultipart()
msg['From'] = gm_user
msg['To'] = gm_reciever
msg['Subject'] = 'Generated QR Code'
message = 'This will be a QR code eventually'
msg.attach(MIMEText(message))

# Creating our server object
mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
# sign in to our email account
mailserver.login(gm_user, gm_user_pw)
# Send the email
mailserver.sendmail(gm_user,gm_reciever,msg.as_string())
# quit our email server
mailserver.quit()