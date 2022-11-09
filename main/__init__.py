#Github.com/desibanda05

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 19109759
API_HASH = b027557e1eb9fab0c2a3bbf42cfc4e92
BOT_TOKEN = 5546885039:AAGqPuikM22ZnDdDK0-VQn8fK8E5VtOYHGc
SESSION = BQARgGSvqkHtznvJVnGEH5KpX4PPYrSTda8SunKRartqTIjZhZf5VNIP4Jmpw_eya_0hLyJ0KBk-wDA0t_EadhDmMJIjdFP75ffVVA1KAl2SKaRlA-za37w5bkiXyB9p3k0ZbJiAYBqbbejr2RFzw5vpqFDR5_vr4JIIvWovo7nvYo_xODjnTLvXpHfcLGOiOvL3LpXVWiydhvX8Z2UXRArop0nyR6pDJ0bA9_fDNND3HNLfWUHTy1wKsHKyAYutgwRKbjjB7k0YseEDAHZuJiCQiHZWYQweYchHBWG6sIYx64D0b8ayJuyWJ2uLAXomAp9H9uYMRilOECs9QtvRCLZNVh0S8QA
FORCESUB = config("FORCESUB", default=None)
AUTH = 1444745969

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
