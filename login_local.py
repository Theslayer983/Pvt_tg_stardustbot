"""
Run this ONCE on your own machine (not on the server) to log in
interactively and generate a portable session string.

Usage:
    pip install telethon
    python login_local.py

It will ask for your phone number, the login code Telegram sends you,
and your 2FA password if you have one. At the end it prints a long
string — copy that whole string and set it as the SESSION_STRING
environment variable on your host (Render, etc). Do NOT share it or
commit it anywhere; it grants full access to your Telegram account.
"""

from telethon import TelegramClient
from telethon.sessions import StringSession

import config

with TelegramClient(StringSession(), config.API_ID, config.API_HASH) as client:
    session_string = client.session.save()
    print("\n" + "=" * 60)
    print("Copy everything between the lines below into your")
    print("SESSION_STRING environment variable on the server:")
    print("=" * 60)
    print(session_string)
    print("=" * 60)
