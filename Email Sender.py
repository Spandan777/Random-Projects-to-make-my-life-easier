import smtplib

email= input("Enter Sender's Email: ")
receiver_email= input("Enter Receiver's Email: ")

subject=input("Write the Subject: ")
message=input("Write the message: ")

text=f"Subject: {subject}\n\n{message}"

server= smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email,"vyun rrda baiw xzwp")
server.sendmail(email, receiver_email, text)
print("Email has been sent to "+ receiver_email)