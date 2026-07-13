from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("Welcome to the Telegram Session Generator!")


API_ID = input("Enter your API ID (integer): ")
API_HASH = input("Enter your API Hash (string): ")

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("Session string generated successfully!")
    print(client.session.save())
