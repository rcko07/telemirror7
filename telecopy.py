"""
Make full copy of telegram channel
"""
import time
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon.tl.types import MessageService

# put your values
# Telegram API
API_HASH = ""
API_ID = ""
# Session string by login.py
SESSION_STRING = ""
SOURCE_CHAT = '@'
TARGET_CHAT = '@'
# Timeout after 50 messages
LIMIT_TO_WAIT = 50


def do_full_copy():
    with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        amount_sended = 0
        for message in client.iter_messages(SOURCE_CHAT):
            # skip if service messages
            if isinstance(message, MessageService):
                continue
            try:
                client.send_message(TARGET_CHAT, message)
                amount_sended += 1
                if amount_sended >= LIMIT_TO_WAIT:
                    amount_sended = 0
                    time.sleep(1)
            except Exception as e:
                print(e)

        print("Done")


if __name__ == "__main__":
    do_full_copy()
