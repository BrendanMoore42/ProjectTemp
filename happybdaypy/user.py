"""
date: December 11, 2018
author: @BrendanMoore42

Send a message to yourself to
remember family birthdays.

Or any semi-annual important dates you'd
like to remember by text--meaning you'll
always see it.

"""
from credentials import credentials
from friends import friends
from twilio.rest import Client
import datetime

# account info
account = credentials['account']
token = credentials['token']
twi_phone = credentials['twi_phone']
phone = credentials['phone']

# set sms client
client = Client(account, token)

# set date variables
now = datetime.datetime.now()
now_string = str(now.day) + '/' + str(now.month)

# search date in friends list for a match
for friend, date in friends.items():
    # if someone's birthday, will send a text to selected phone
    if now_string == date:
        message = client.messages.create(
            body=f"Text Happy Birthday to {friend}!",  # change message here
            from_=twi_phone,  # twilio account number
            to=phone  # personal or target outgoing number
        )









# message = client.messages.create(
#     body=f"Text Happy Birthday to {name}!",
#     from_=phone,
#     to=phone
# )
