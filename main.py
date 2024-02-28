from get_commute import get_commute
from send_message import send_message
from dotenv import load_dotenv
import sys
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
API_KEY = os.getenv("APIKEY")
START = os.getenv("START")
END = os.getenv("END")
CARRIER = os.getenv("CARRIER")

distance, duration = get_commute(API_KEY, START, END)

MESSAGE = f"Hello Peter. The time it will take you to work is {duration}"

if distance is None: 
    MESSAGE = "There was an error! Fix it Peter!"

send_message(PHONE_NUMBER, CARRIER, MESSAGE)