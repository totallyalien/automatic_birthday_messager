import smtplib
import datetime as dt
import random
import pandas as pd

YOUR_NAME = "TAMIO"
MY_MAIL = "xyz@gmail.com"
PASSWORD = "XXXXXXXX"

now = dt.datetime.now()
df = pd.read_csv("birthdays.csv")



details = (df.loc[(df["month"]==now.month) & (df["day"]==now.day)])


if not (details.empty):
    letter = random.choice(["letter_1.txt","letter_2.txt","letter_3.txt"])
    with open(f"./letter_templates/{letter}") as template:
        message = template.read()
        message = message.replace("[NAME]",str(details["name"][0]))
        message = message.replace("[YOUR_NAME]",YOUR_NAME)

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_MAIL,password=PASSWORD)
    connection.sendmail(from_addr=MY_MAIL,to_addrs=details["email"][0],msg=f"Subject:Happy birthday\n\n {message}")
    connection.close()



