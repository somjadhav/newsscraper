import smtplib, ssl

port=465
context=ssl.create_default_context()

sender_email="team17finalproject@gmail.com"
receiver_email="somjadhav787@gmail.com"
receiver_names = "Som"
message = "\nTHis is a test!"

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
    server.login(sender_email,"Abcd123!")
    server.sendmail(sender_email,receiver_email,message.encode("UTF-8"))

