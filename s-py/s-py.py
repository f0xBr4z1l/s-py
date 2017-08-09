#!/usr/bin/python3
#spam Create by F0x_Br4zil
import smtplib
def _banner_():
    print("""
 _____       ________   __
/  ___|      | ___ \ \ / /
\ `--. ______| |_/ /\ V / 
 `--. \______|  __/  \ /  
/\__/ /      | |     | |  
\____/       \_|     \_/  
spam python
       create by F0x_Br4zil
       https://github.com/f0xBr4z1l                          
                          """)

def spam_msg(emailist, email, passwd, sub, mess):
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, passwd)
        you = email
        para = emailist
        msg = ("""from: %s
To: %s
Subject: %s

%s""" % (you, para, sub, mess))
        smtp.sendmail(you, para, msg)
        smtp.quit()
        print("spam enviado com sucesso")
    except:
        print("Não foi possivel envia spam\n")
_banner_()
email = input("Seu email, your email >> ")
passwd = input("Sua senha, your password >> ")
word = input("lista de email, e-mail list >> ")
sub = input("assunto, subject, >> ")
mess = input("mensagem, messege >> ")

emailist = open(word, "r").readlines()

for i in range(0,len(emailist)):
    spam_msg(emailist, email, passwd, sub, mess)




