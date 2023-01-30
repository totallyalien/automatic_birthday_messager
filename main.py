import smtplib
import datetime as dt
import random
import pandas as pd

MY_MAIL = "XXXXXX@gmail.com"
PASSWORD = "xxxxxxxxxxxxxxx"

now = dt.datetime.now()
df = pd.read_csv("birthdays.csv")



details = (df.loc[(df["month"]==now.month) & (df["day"]==now.day)])

if not (details.empty):
    letter = random.choice(["letter_1.txt","letter_2.txt","letter_3.txt"])
    with open(f"./letter_templates/{letter}") as template:
        message = template.read()


