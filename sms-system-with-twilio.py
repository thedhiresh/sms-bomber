import os
from twilio.rest import Client

# Your Twilio account credentials
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

# Send the SMS
message = client.messages.create(
    from_=twilio_number,
    to=recipient_number,
    body=message
)

print(f'SMS sent successfully! SID: {message.sid}')
