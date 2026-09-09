import os

# --- Fill these in (or set as env vars of the same name on your host) ---

# Get these from https://my.telegram.org (log in, "API development tools")
API_ID = int(os.environ.get("API_ID", "30585211"))
API_HASH = os.environ.get("API_HASH", "2d1546542a11fe2dc961cf8cdab362d2")

# Leave blank locally (first run will log in interactively and save a
# file-based session named SESSION_NAME). On a server with no interactive
# stdin (Render, Docker, etc.), you MUST set SESSION_STRING instead --
# generate it once by running login_local.py on your own machine.
SESSION_STRING = os.environ.get("SESSION_STRING", "1BVtsOLABu7B_daqTZlQFj4apLaz0jpjzkAgCVh7ocpvKTfCw23eHATi9QWNJzn0kKgeDMVHHQR6MUVgjZad0xuU_HXaksTH19lolEgmgiYOL1kXL2Lpvf1cBYcvu7c2kuitjsXPEhyhjwhrPBRXQXme5OXCPMq5vYy-uTRniwhXoYu1Bj7swf71Dalcsob9X1iKQA8QD9p7F2qp91M0K7tzsr6ao89kpb5LpxjtWqjTv3evw_nJEpoUmWZCjGY1VwI-vznPULYO18b4oS0XRuZrX8jEL-KMGCMpcrIi6xFWDc96MNtPlMoFirwgAZWf_z7UL8Z4thLCIiiDqEWhFSZgt82aFeOg=")

# Only used for the local file-based session fallback (ignored if
# SESSION_STRING is set).
SESSION_NAME = "stardust_userbot"

# The chat where Skycoach Boosters Notifier posts. Can be:
#   - the bot's @username (e.g. "SkycoachBoostersBot")
#   - a chat id (int)
#   - "me" if it DMs you directly
SOURCE_CHAT = os.environ.get("SOURCE_CHAT", "skycoach_boosters_notifyer_bot")

# Extra safety filter: only auto-click if the message sender's username
# matches this. Set to empty string to disable this check (not
# recommended if the chat has other members).
BOT_USERNAME = os.environ.get("BOT_USERNAME", "skycoach_boosters_notifyer_bot")
