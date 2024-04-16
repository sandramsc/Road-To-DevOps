#!/usr/bin/python3

from email.message import EmailMessage
import smtplib
import ssl

email_sender = 'chewwwsome@gmail.com'
email_password = 'vhxb dlbe kwuk wxvm'
email_receiver = 'sandraashipala@gmail.com'

subject = 'Checkout my 15-Days-of-DevOps challenge repo'

body = """

I have created a 15 days of DevOps repo that will explain select DevOps tools and concepts in a very simple way. Created as a way to practice using the Feynman technique while learning DevOps, this has turned out to be a full fledged content piece that I have turned into an Open Source project that can be used by those who might find it useful.

"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 456, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
smtp.quit()
print("Message successfully sent!")
