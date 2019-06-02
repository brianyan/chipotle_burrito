import os

from twilio.rest import Client

def send(from_number, to_number):
	account_sid = 
	auth_token = 'your_auth_token'
	client = Client(account_sid, auth_token)

	message = client.messages \
	                .create(
	                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
	                     from_=from_number,
	                     to=to_number
	                 )

	print(message.sid)