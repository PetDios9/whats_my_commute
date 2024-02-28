import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_commute(api_key, start, end):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": start,
        "destinations": end,
        "key": api_key
    }
    res = requests.get(base_url, params=params)
    if res.status_code == 200:
        data = res.json()
        print(data)
        if data["status"] == "OK":

            distance = data["rows"][0]["elements"][0]["distance"]["text"]
            duration = data["rows"][0]["elements"][0]["duration"]["text"]
            return distance, duration
        else:
            print("Request failed.")
            return None, None
    else:
        print("Failed to make the request.")
        return None, None
    
api_key = os.getenv("APIKEY")
start = os.getenv("START")
end = os.getenv("END")

if __name__ == '__main__':
    distance, duration = get_commute(api_key, start, end)
    print(distance, duration)