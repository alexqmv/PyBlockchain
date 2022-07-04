import hashlib #importing hashlib library
import time
import smtplib
import random
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
email_sender = "YOURMAIL.RU"
password = "YOUR MAIL.RU PASSWORD"
 

smtp_server = smtplib.SMTP("smtp.mail.ru", 2525)
smtp_server.starttls()

msg = MIMEMultipart()
msg.attach(MIMEText("Hi, dear user!\n\nYou chose this mail for verification? Was that you?"))


class Networkus_Blockchain: # Main Class

	def __init__(self, previous_block_hash,transaction_list): #initiliazing
		self.previous_block_hash = previous_block_hash #block hash
		self.transaction_list = transaction_list #transaction list

		self.block_data = "-".join(transaction_list) + "-" + previous_block_hash #random hash symbols
		self.block_hash = hashlib.md5(self.block_data.encode()).hexdigest()

auth = str(input("[!] - Verify your identity by @mail  (Enter your valid mail)  - "))
email_getter = auth



html2 = """\
<html>
 <head></head>
 <body>
   <a href="https://dribbble.com/shots/15750262-Success-Message-Verification">No,it wasn't me!</a>
</html>
"""

html = """\
<html>
 <head></head>
 <body>
   <a href="https://dribbble.com/shots/15750262-Success-Message-Verification">Verify Account NOW.</a>
</html>
"""

t1 = str(input("Enter string to generate hash: "))

print("~----------------HASH GENERATOR----------------~")


initial_block = Networkus_Blockchain(" NetworkusChain", [t1]) #initial block where we use transaction1 and transaction2
print(initial_block.block_data) # just printing this block
print("Generated hash login ->> ", initial_block.block_hash)
print("-----------------------------------------------")


msg.attach(MIMEText(html2, "html"))

msg.attach(MIMEText("\n\nIf it's you, let's verify account by tapping here => "))
msg.attach(MIMEText(html, "html"))

smtp_server.login(email_sender, password)
smtp_server.sendmail(email_sender, email_getter, msg.as_string())
