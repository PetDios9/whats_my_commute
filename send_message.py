import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
 
def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
    print('message sent!')
 
 
if __name__ == "__main__":
    message = "Hi lol"
    send_message(PHONE_NUMBER, 'verizon', message)
