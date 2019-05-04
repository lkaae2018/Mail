import smtplib
import config

def send_email(subject, msg):
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject: {}\n\n{}".format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS_rx, message)
        server.quit()
        print("Mail sendt med succes")

    except:
        print("Fejl mail ikke sendt")


subject ="Test"
msg="Hej med dig"
send_email(subject, msg)