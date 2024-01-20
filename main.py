import smtplib
import datetime as dt
import random
import pandas

my_email = 'email@gmail.com'
my_password = 'password'

now = dt.datetime.now()
current_month = now.month
current_day = now.day
data = pandas.read_csv('birthdays.csv')

# ****************************CHECKING FOR BIRTHDAYS*****************************
for x in range(0, len(data)):
    test = data.loc[x]
    if int(test['month']) == current_month and int(test['day']) == current_day:

        # *****************************CREATING THE LETTER TO SEND*****************************
        with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as letter:
            email_body = letter.read()
            email_body = email_body.replace('[NAME]', test['name'])

        # *****************************SENDING THE EMAIL*****************************
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=f'{test["email"]}',
                                msg=f'Subject:Happy Birthday!\n\n{email_body}')
