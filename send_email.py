import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "xxxx@gmail.com"
toaddr = "ccccc@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECTxxxx"

body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

filename = "Ecuador.txt"
attachment = open(r"C://Users/xxxx/Desktop/"+filename)
#open("C://Users/Luis/Desktop/", "r")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "xxxxxxx")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
