"""
Make full copy of telegram channel
"""
import time
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon.tl.types import MessageService

# put your values
# Telegram API
API_HASH = "b2298b31d8ac442a25c3c6d23d8f9b72"
API_ID = "18885110"
# Session string by login.py
SESSION_STRING = "BABTkvYx6ccM5TtIP4Apmopk_H-kz1jwSgBYmIhI4cdMQPYQ2tI0kJz8SOPiBPPbxtR7Kg5nqFs7rDFwr7Tgh79HjT_bpShMvGwM5tScarBKMclrpr0A2CKzEr53PYweu0GMkc4vh05lo6EgfXQ_oOy3KKUy5OKI6x5aJ-8NRVFZlluje2A7S6rssIMEiz2cD_D17e2_cOcVvEYLjX02vj1Gzbb6Jx06Gl_vSJ_h1HB51tJaPb4IIzuK5zaX0CV_mOOhnlWi55ZzWSIathFkF1KdaD1J1uzbB4skwWgdIeK-398R7x-KT01bWzlPKucrFxBSSJZjk0vcEOs70e6cqyAAAAAEzgK4EA"
SOURCE_CHAT = '@sicakindirimn'
TARGET_CHAT = '@twitterbotss'
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
