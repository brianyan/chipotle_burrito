import os

from dotenv import load_dotenv

from sms import send

if __name__ == "__main__":
	load_dotenv()
	print(os.environ.get('TWILIO_ACCOUNT_SID'))
	# send()