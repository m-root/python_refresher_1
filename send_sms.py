# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+12316851234",
                                             from_="+15555555555",
                                             body="Hello there!")