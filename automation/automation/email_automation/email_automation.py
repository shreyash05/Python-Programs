import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import os
import psutil
from sys import *
import time
def email_automation():
	# instance of MIMEMultipart
	msg = MIMEMultipart()

	msg['Subject'] = "Process schedule log"
	body = "this file contains log of running processess"
	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP_SSL("smtp.gmail.com",465)
	server.login("sender_email","password")
	filename = "Marvellous.log"
    #file path
	file_path = "C:\\Users\\shree\\Desktop\\Python Marvellous\\New folder\\abc\\Marvellous.log"
	file = open(file_path,"rb")

	# instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')
	  
	# To change the payload into encoded form
	p.set_payload((file).read())
	  
	# encode into base64
	encoders.encode_base64(p)
	   
	p.add_header('Content-Disposition', "file; filename= %s" % filename)

	# attach the instance 'p' to instance 'msg'
	msg.attach(p)

	text = msg.as_string()


	server.sendmail("sender_email",
								"reciever_email",
								text)

	server.quit()				
	print("email sent ")
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])
    #schedule.every().day.at("10:30").do(email_automation)
    schedule.every(int(argv[1])).seconds.do(email_automation)
    while True:
        schedule.run_pending()
        time.sleep(1)	

if __name__ == '__main__':
	main()        

    