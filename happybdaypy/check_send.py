"""
Checks today's date and if there's a match it will
send a text message to your outgoing number.

Account and token access in credentials.py.
Phone numbers must be in E.164 formatting--"+, country code, number"

To modify text, replace "body=" variable with desired message.
"""
import json
import datetime
from twilio.rest import Client
from credentials import credentials

def check_send(test=False):
    """
    Sends a message if dates match with person's name.
    :param test: if True, test message will send to your phone
    """

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

    # import friend data
    with open('friends.json') as f:
        friends = json.load(f)

    # if user wants to test phone numbers
    if test:
        print('Sending test message...')
        message = client.messages.create(
            body=f"Test message!",  # change message here
            from_=twi_phone,  # twilio account number
            to=phone  # personal or target outgoing number
        )
    else:
        # search date in friends list for a match
        for name, date in friends.items():
            # if someone's birthday, will send a text to selected phone
            if date_now == date:
                print(f'Sending message to {name} on {date}')
                message = client.messages.create(
                    body=f"Remember to text Happy Birthday to {name}!",  # CHANGE HERE!!
                    from_=twi_phone,  # twilio account number
                    to=phone  # personal or target outgoing number
                )

if __name__ == '__main__':
    check_send()