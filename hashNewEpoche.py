"""
	* CODE BY @alex.qmv
	find in github, instagram and twitter

	* IF YOU HAVE ANY QUESTIONS:
		help.feedback@mail.ru


"""

import hashlib
import time
import smtplib
import random
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

email_sender = " " # Enter your mail
password = ""
smtp_server = smtplib.SMTP("smtp.mail.ru", 2525) # Connected to smtp Mail.Ru server,with port 2525, you can also try 25,465,467,587 - for Gmail
smtp_server.starttls() # Starting
id = random.randint(1000000,9000000) # Under maintance | I wanted to create random generation of code verification, maybe  i will do it soon

msg = MIMEMultipart()
msg.attach(MIMEText("Your verification code - {} \n\n\nIf you did not send the code, we advise you to delete it immediately or not to tell anyone this code.\n\n\n".format(id)))
# Just messages


# Creating hashGen main class

class Networkus_Blockchain: # Main Class


	def __init__(self,previous_block_hash,transaction_list): #initiliazing

		self.previous_block_hash = previous_block_hash #block hash
		self.transaction_list = transaction_list #transaction list

		self.block_data = "-".join(transaction_list) + "-" + previous_block_hash #random hash symbols
		self._block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



auth = str(input("[!] - Verify your identity by Mail (Enter your valid mail)  - "))

email_getter = auth





html2 = """\
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<title>Atom</title>
</head>
<body>
<!--Создаём таблицу контейнер, которой задаём следующее
оформление:
border="1" - рамка вокруг контейнера. Увеличив число, можно увеличить толщину рамки.
align="center" - размещаем контейнер по центру экрана.
rules="rows" - убираем двойную рамку.
style="width:60%;" - добавляем стилевое свойства, делающее
контейнер и весь сайт "резиновым".
Сделать полноценный адаптивный дизайн, этим способом невозможно.-->
<table
border="1"
align="center"
rules="rows"
style="width:12%;">
<!--Создаём строку-->
<tr>
<!--Создаём ячейку строки-->
<td>

<!--ШАПКА САЙТА-->

<!--В ячейке строки создаём ещё одну таблицу для шапки сайта.
Оформление:
border="1" - двойная рамка толщиной в 1px
background="images/168.png" - картинка в шапке сайта, если требуется.
Адрес картинки вы должны вставить свой.
bgcolor="#7FFFD4" - фоновый цвет в шапке, если нет картинки.
cellpadding="10" - отступ содержимого от рамки не менее 10px.
style="width:100%; border-radius:5px;" - добавляем "резиновость"

и закругляем уголки рамки-->


<table
border="1"
background="atom.png"
bgcolor="#7FFFD4"
cellpadding="10"
style="width:100%; border-radius:5px;">
<!--Создаём строку таблицы-->
<tr>
<!--Создаём столбец таблицы-->
<th>
<!--Содержание ячейки столбца-->
<h1>Atom</h1>
<h3>Smart,Fast & Secure</h3>
<!--Закрываем таблицу-->
</th>
</tr>
</table>

<!--ОСНОВНОЙ КОНТЕНТ-->

<!--В этой же ячейке контейнера создаём ещё одну таблицу
для основного контента.
Оформление как и в предыдущей таблице-->

<table
border="1"
bgcolor="#e6e6fa"
cellpadding="10"
style="width:100%; border-radius:5px;">
<!--Создаём строку-->
<tr>
<!--Создаём ячейку
Оформление:
rowspan="2" - объединяем две ячейки в одну.
Число объединяемых ячеек по числу ячеек в сайдбаре.
style="width:80%" - основной контент занимает 80% всей площади,
оставшиеся 20% для сайдбара-->
<td
rowspan="2"
style="width:80%">
<h2>Home</h2>
<!--Начинаем абзац с красной строки-->
<p style="text-indent:40px">
<table>

<label for="fname">Username:</label>
<input type="email"><br><br>
<label for="sname">MailName:</label>
<input type="email"><br><br>
<label for="vcode">Verif.Code:</label>
<input type="password"><br><br>

<a href="https://gmail.com/">Need Help?</a><br>
<span style='font-size:100px;'>&#9989;</span><br>
<p>Verified &#9989;</p><br>
<p>Get rewards for registrations and verifications &#x2B50;</p><br>
<!-- <p>I will display &#x2705;</p> -->

</table>
</p>

<p style="text-indent:20px">Register to make sure that this account is not SPAM. The data is completely safe. If you need help, click on "Need Help?" or contact us directly - help.feedback@mail.ru</p>
<!--Закрываем ячейку-->
</td>

<!--САЙДБАР-->

<!--Создаём ячейку сайдбара-->
<td bgcolor="#e6e6fa">
<h3>Menus</h3>
<!--Абзац для ссылки на страницу сайта-->
<p>
<!--Ссылка на страницу сайта-->
<a href="">
<!--Картинка маркера перед названием страницы-->
<img src="atom.png">
<!--Название страницы
style="margin-left:5px;" - отступ названия от маркера-->
<span style="margin-left:5px;">Messages [0]</span></a>
<!--Закрываем абзац-->
</p>
<p>
<a href="">
<img src="http://trueimages.ru/img/31/ab/4dcb087c2ae4305edcd15171696.jpg">
<span style="margin-left:5px;">Home Page</span;></a>
</p>
<p>
<a href="">
<img src="http://trueimages.ru/img/31/ab/4dcb087c2ae4305edcd15171696.jpg">
<span style="margin-left:5px;">Change Password</span></a>
</p>
<!--Закрываем строку Меню-->
</td>
</tr>
<!--Создаём строку с дополнительной информацией-->
<tr>
<!--Ячейка с дополнительной информацией-->
<td
bgcolor="#e6e6fa"
align="center">
<h3>Support & Help</h3>
<p>help.feedback@gmail.com</p>
<!--Закрываем ячейку с общей информацией
и таблицу основного контента-->
</td>
</tr>
</table>

<!--ПОДВАЛ-->

<!--Создаём таблицу подвала-->
<table
border="1"
bgcolor="#7FFFD4"
height="100"
cellpadding="10"
style="width:100%; border-radius:5px;">
<!--Создаём строку.-->
<tr>
<!--Создаём столбец-->
<th>
<h3>(Copyright by AtomIT Inc | 2022)</h3>
<!--Закрываем таблицу подвала. При желании в подвале можно
сделать несколько строк и столбцов-->
</th>
</tr>
</table>
<!--Закрываем таблицу контейнера-->
</td>
</tr>
</table>
</body>
</html>

"""



t1 = str(input("Enter string to generate hash: "))

print("~__________________HASH GENERATOR__________________~\n\n")


_initial_block = Networkus_Blockchain(" Networkus_Blockchain", [t1]) #initial block where we use transaction1 and transaction2
print(_initial_block.block_data) # just printing this block
print("Generated hash > ", _initial_block._block_hash)
msg.attach(MIMEText("\n\n\nGenerated Hash {0}".format(_initial_block._block_hash)))

print("\n\n______________ BETA VERSION_____________________")



msg.attach(MIMEText(html2, "html"))




# SENDING FILES TO MAIL
with open("readME.txt", "rb") as f:
    file = MIMEApplication(f.read(), Name=basename("readME.txt"))
msg.attach(file)

# with open("ver.png", "rb") as f:
#     file = MIMEApplication(f.read(), Name=basename("verify.png"))
# msg.attach(file)

smtp_server.login(email_sender, password)
smtp_server.sendmail(email_sender, email_getter, msg.as_string())


# CODE CHECKING
# IF code not equal to id(4357), we give request to do it again.
# THIS CODE YOU CAN FIND IN YOUR MAIL, BUT IT IS UNDER DEVELOPMENT!!
# THERE IS ONLY ONE CODE YET. SOON IT WILL BE SENDING RANDOMLY.!!
# IF YOU WANT TO UPGRADE MY CODE  JUST FIND ME ON INSTAGRAM @alex.qmv
# ENJOY

while (True):
	print("[!] Check your mail:")
	code = int(input("Enter verification code from your mail: "))

	print("Checking...")
	time.sleep(2)
	if (code != id):
		print("[E:503] - Verification Code Error")

	else:
		print("Successfully verified. ")
		break
