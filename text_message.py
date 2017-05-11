# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio import rest

# Find these values at https://twilio.com/user/account
account_sid = "AC17a2055e638db03269ee9896fcb88d3f"
auth_token = "e399bc1b57a8544c2378c1ea5b62b3d4"
client = rest.Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+254712123456",
                                             from_="+17473335882",
                                             body="This is a trial message")

# print message.sid