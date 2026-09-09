"""
Stardust order auto-approver for Skycoach Boosters Notifier.

Watches a Telegram chat for messages from a specific bot, and when a
message text mentions "stardust", automatically presses the "Get Order"
inline button on that message (which sends callback_data like
"get_order EQ16680" back to the bot on your behalf).

This uses Telethon in USERBOT mode (logs in as your own Telegram
account), because only the account that actually "sees" the inline
keyboard can press it. A regular Bot API bot cannot click buttons
attached to another bot's messages in an arbitrary chat.

Setup:
  1. pip install telethon python-dotenv
  2. Get api_id / api_hash from https://my.telegram.org
  3. Fill in config.py (or .env) with your values
  4. Run: python bot.py
     First run will ask for your phone number + login code (one time).
     After that it reuses the saved session file.
"""

import asyncio
import logging
import re
import sqlite3
from pathlib import Path

from telethon import TelegramClient, events
from telethon.sessions import StringSession

import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("stardust-autoapprove")

DB_PATH = Path(__file__).parent / "processed_orders.db"

# Matches "stardust" anywhere, case-insensitive (covers "10 mil stardust",
# "Stardust", "STARDUST", etc.)
STARDUST_RE = re.compile(r"stardust", re.IGNORECASE)

# Matches the order id in "New order #EQ16680: ..."
ORDER_ID_RE = re.compile(r"#([A-Z0-9]+)")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS processed (order_id TEXT PRIMARY KEY, ts DATETIME DEFAULT CURRENT_TIMESTAMP)"
    )
    conn.commit()
    return conn


def already_processed(conn, order_id: str) -> bool:
    cur = conn.execute("SELECT 1 FROM processed WHERE order_id = ?", (order_id,))
    return cur.fetchone() is not None


def mark_processed(conn, order_id: str):
    conn.execute("INSERT OR IGNORE INTO processed (order_id) VALUES (?)", (order_id,))
    conn.commit()


async def main():
    conn = init_db()

    if config.SESSION_STRING:
        session = StringSession(config.SESSION_STRING)
    else:
        # File-based session only works when you can answer the login
        # prompt interactively (local machine). On a server with no
        # stdin, this WILL crash with EOFError -- run login_local.py
        # locally first and set SESSION_STRING on the server instead.
        session = config.SESSION_NAME

    client = TelegramClient(session, config.API_ID, config.API_HASH)

    @client.on(events.NewMessage(chats=config.SOURCE_CHAT))
    async def handler(event):
        text = event.raw_text or ""

        # Only react to messages actually coming from the notifier bot,
        # in case the chat has other participants/messages too.
        sender = await event.get_sender()
        sender_username = getattr(sender, "username", None)
        if config.BOT_USERNAME and sender_username != config.BOT_USERNAME:
            return

        if not STARDUST_RE.search(text):
            return  # not a stardust order, ignore (e.g. Raids Boost, etc.)

        match = ORDER_ID_RE.search(text)
        order_id = match.group(1) if match else None

        if order_id and already_processed(conn, order_id):
            log.info("Order %s already processed, skipping", order_id)
            return

        if not event.buttons:
            log.warning("Stardust order matched but message has no buttons: %s", text)
            return

        # Find the "Get Order" button specifically (don't just click [0][0]
        # blindly in case layout ever changes) and press it.
        clicked = False
        for row in event.buttons:
            for button in row:
                if button.text.strip().lower() == "get order":
                    log.info("Auto-approving stardust order %s -> clicking '%s' (data=%r)",
                             order_id, button.text, button.data)
                    await button.click()
                    clicked = True
                    break
            if clicked:
                break

        if not clicked:
            log.warning("No 'Get Order' button found on stardust message: %s", text)
            return

        if order_id:
            mark_processed(conn, order_id)

        log.info("Done: order %s auto-approved", order_id)

    log.info("Starting client, listening for stardust orders...")
    try:
        await client.start()
    except EOFError:
        raise SystemExit(
            "No SESSION_STRING set and this environment has no interactive "
            "stdin to log in with. Run login_local.py on your own machine "
            "once, then set the SESSION_STRING env var on this server."
        )
    log.info("Logged in. Watching chat: %s", config.SOURCE_CHAT)
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
