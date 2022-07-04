import hashlib
import time
import smtplib
import random
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

email_sender = "" # Enter your mail
password = ""# Enter your password

smtp_server = smtplib.SMTP("smtp.mail.ru", 2525) # Connected to smtp Mail.Ru server,with port 2525, you can also try 25,465,467,587 - for Gmail
smtp_server.starttls() # Starting
id = 4357 # Under maintance | I wanted to create random generation of code verification, maybe  i will do it soon
#id = random.randint(1000,10000)

msg = MIMEMultipart()
msg.attach(MIMEText("Your verification code \n\t\t\t\t\t4357 \n\n\n\nReply -> \n@help.feedback@mail.ru\n\n\n\n\t\t\t\t\t\t(C) StarEye Blockchain"))
# Just messages


# Creating hashGen main class

class Networkus_Blockchain: # Main Class


	def __init__(self,previous_block_hash,transaction_list): #initiliazing

		self.previous_block_hash = previous_block_hash #block hash
		self.transaction_list = transaction_list #transaction list

		self.block_data = "-".join(transaction_list) + "-" + previous_block_hash #random hash symbols
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



auth = str(input("[!] - Verify your identity by Mail (Enter your valid mail)  - "))

email_getter = auth



html2 = """\
<html>
 <head></head>
 <body>
   <a href="https://dribbble.com/shots/15750262-Success-Message-Verification">License</a>
</html>
"""

html = """\
<html>
 <head></head>
 <body>
   <a href="https://dribbble.com/shots/15750262-Success-Message-Verification">Secure my hash (SOON)</a>
</html>
"""

t1 = str(input("Enter string to generate hash: "))

print("~----------------HASH GENERATOR----------------~")


initial_block = Networkus_Blockchain(" StarEye Blockchain", [t1]) #initial block where we use transaction1 and transaction2
print(initial_block.block_data) # just printing this block
print("Generated hash > ", initial_block.block_hash)
print("-----------------------------------------------")



msg.attach(MIMEText(html2, "html"))

msg.attach(MIMEText("\n\nJOIN TO STAREYE DEVELOPERS"))
msg.attach(MIMEText(html, "html"))

# SENDING FILES TO MAIL
with open("readME.txt", "rb") as f:
    file = MIMEApplication(f.read(), Name=basename("readME.txt"))
msg.attach(file)

with open("ver.png", "rb") as f:
    file = MIMEApplication(f.read(), Name=basename("verify.png"))
msg.attach(file)

smtp_server.login(email_sender, password)
smtp_server.sendmail(email_sender, email_getter, msg.as_string())


# CODE CHECKING
# IF code not equal to id(4357), we give request to do it again.
# THIS CODE YOU CAN FIND IN YOUR MAIL, BUT IT IS UNDER DEVELOPMENT!!
# THERE IS ONLY ONE CODE YET. SOON IT WILL BE SENDING RANDOMLY.!!
# IF YOU WANT TO UPGRADE MY CODE  JUST FIND ME ON INSTAGRAM @alex.qmv
# ENJOY
while (True):
	print("Check your mail.")
	code = int(input("Enter verification code from your mail: "))
	if (code != id):
		print("[E:503 - verification code error!]")

	else:
		print("Successfully")
		break
