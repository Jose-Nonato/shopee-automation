import requests, os
from dotenv import load_dotenv
load_dotenv()


TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.text
