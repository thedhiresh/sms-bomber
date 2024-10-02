import os
import logging
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your Twilio account credentials
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Your Twilio phone number
twilio_number = os.environ['TWILIO_PHONE_NUMBER']

# Create a Twilio client object
client = Client(account_sid, auth_token)

def send_sms(recipient_number, message):
    try:
        # Send the SMS
        message = client.messages.create(
            from_=twilio_number,
            to=recipient_number,
            body=message
        )
        logger.info(f'SMS sent successfully! SID: {message.sid}')
    except TwilioRestException as e:
        logger.error(f'Twilio error: {e}')

def main():
    # Define the recipient's phone number (in international format, e.g., +1234567890)
    recipient_number = '+1234567890'

    # Define the SMS message
    message = 'Hello from Python!'

    # Send the SMS
    send_sms(recipient_number, message)

if __name__ == '__main__':
    main()
