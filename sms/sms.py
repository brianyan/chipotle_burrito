import os

from twilio.rest import Client

def send(to_number):
	account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
	auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
	from_number = os.environ.get('TWILIO_PHONE_NUMBER')
	client = Client(account_sid, auth_token)

	message = client.messages \
	                .create(
	                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
	                     from_=from_number,
	                     to=to_number
	                 )

	print(message.sid)