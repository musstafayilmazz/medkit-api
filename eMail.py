from email.message import EmailMessage
import ssl
import smtplib

def email_send(apikey,body,subject,receiver):
    if(apikey=="7cf8a317"):
        email_sender = "medkitdevteam@gmail.com"
        password = "gcibzzxrniedbcua"

        email_receiver = receiver
        subject = subject
        body = body

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        return {"message": "E-mail sent!"}
    else:
        return {"message": "Unauth access!"}