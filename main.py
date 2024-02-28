from get_commute import get_commute
from send_message import send_message
from dotenv import load_dotenv
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
API_KEY = os.getenv("APIKEY")
START = os.getenv("START")
END = os.getenv("END")

distance, duration = get_commute(API_KEY, START, END)

MESSAGE = f"Hello Peter. The time it will take you to work is {duration}"

send_message(PHONE_NUMBER, 'verizon', MESSAGE)