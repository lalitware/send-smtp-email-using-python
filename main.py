import getpass
import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

# To check the connection
# smtp_object.ehlo()

# if port is 587 then we need to call start TLS.
smtp_object.starttls()

# To input an app password and email from user for authentication
email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your app password")
smtp_object.login(email, password)

# send email using .sendemail() method
from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter receiver's email: ")
subject = input("Enter the subject: ")
message = input("Enter the message: ")
body = "Subject: " + subject + "\n" + message
result = smtp_object.sendmail(from_address, to_address, body)

if result == {}:
    print("Email sent successfully!")
else:
    print("Error occured")
