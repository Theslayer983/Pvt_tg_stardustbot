import os

# --- Fill these in (or set as env vars of the same name on your host) ---

# Get these from https://my.telegram.org (log in, "API development tools")
API_ID = int(os.environ.get("API_ID", "30585211"))
API_HASH = os.environ.get("API_HASH", "2d1546542a11fe2dc961cf8cdab362d2")

# Leave blank locally (first run will log in interactively and save a
# file-based session named SESSION_NAME). On a server with no interactive
# stdin (Render, Docker, etc.), you MUST set SESSION_STRING instead --
# generate it once by running login_local.py on your own machine.
SESSION_STRING = os.environ.get("SESSION_STRING", "1BVtsOLEBu8Pj-iX12T33jwQYJqD-0llt9ktwxC-ihaCvaLJUsD6CmLBinEfYDIvAmRLDsMrF__2w9XZxz3SUkW8M_fGS1njajJmlraKVZ0lUx_kkPwFJfLT3yG1FgJGlA0rurilzn9Xg-f68F7SmcZONlaEQYUCBZkJuOy2qiVpf9v_PXtXUzf0RaykA-ZSO7kfUZNvxkZ4QJQmCAlrpMHTQTlQ3I3FBgRYv_TICMOSbLS5RgjxHxww-IStRBsQizIhwDpyGHx1MSNnGyQErKPov3DUp-ppevrP-EbB2DenmvDT-o9L31F4HLGTUyMfcbEAfof93uD4Gd09B17oumSzKH-SSqjc=")

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
