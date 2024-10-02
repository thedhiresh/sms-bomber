import os
from twilio.rest import Client

# Your Twilio account credentials
# AC9e3c6cf298cc90466d3a5f1a82336806
# b3c0185abcfb236fb7ef2f6665f6e801

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Your Twilio phone number
twilio_number = os.environ['TWILIO_PHONE_NUMBER']

# Create a Twilio client object
client = Client(account_sid, auth_token)

# Define the recipient's phone number (in international format, e.g., +1234567890)
recipient_number = '+9779826259899'

# Define the SMS message
message = 'Happy Birthday to You'

Copy code block
Open code block in new page
from twilio.rest import Client

# account_sid = 'AC9e3c6cf298cc90466d3a5f1a82336806'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16673032833',
body='Happy Birthday to you '
  to='+9779826259899'
)

print(message.sid)
# Send the SMS
message = client.messages.create(
    from_=twilio_number,
    to=recipient_number,
    body=message
)

print(f'SMS sent successfully! SID: {message.sid}')
