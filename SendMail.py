import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.ehlo()
#this is security script
s.starttls()
s.login()
#write own login and password
s.login("login","password")
message="salam men huseyn:-software programmer"
s.sendmail("kimden:","kime",message)
