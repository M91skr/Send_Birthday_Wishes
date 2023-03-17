"""---------------------------------------- Send birthday wishes ----------------------------------------
In this code, the name, date of birth and email of the audience are received. On the other hand, some beautiful texts
for happy birthday are also received from the user.

The program is simply implemented daily, and if it was the birthday of one of the people in the list,
one of the messages will be randomly emailed to the addressee.

Note:
Please:
1. enter your email information in the main application.
2. In the contacts file, put examples with real data and appropriate format.
3. And put your name or signature at the end of **each text** from the letter templates.
Otherwise you'll get an error.

You can run this code in the cloud, defined for that daily task, and enjoy your reminder.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

import datetime as dt
import os
import smtplib
from random import randint

import pandas

# ---------------------------------------- Specific Parameters Definition ----------------------------------------

my_email = "MY_EMAIL"
my_password = "MY_PASSWORD"

# ---------------------------------------- Read Audience File ----------------------------------------

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# ---------------------------------------- Read Text File ----------------------------------------

with open(f"./letter_templates/letter_{randint(1, 9)}.txt") as letter:
    text = letter.read()

# ---------------------------------------- CALL TODAY ----------------------------------------

today = (dt.datetime.now().month, dt.datetime.now().day)

# ---------------------------------------- CHECK BIRTHDAY ----------------------------------------

if today in birthday_dict:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv(my_email), password=os.getenv(my_password))
        text = text.replace("[NAME]", birthday_dict[today]["name"])
        connection.sendmail(from_addr=os.getenv(my_email), to_addrs=birthday_dict[today]["email"],
                            msg=f"Subject: Happy Birthday\n\n{text}")
