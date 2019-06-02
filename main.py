import os

from dotenv import load_dotenv

from sms import send

if __name__ == "__main__":
	to_number = account_sid = os.environ.get('PERSONAL_PHONE_NUMBER')
	load_dotenv()
	send(to_number=to_number)
