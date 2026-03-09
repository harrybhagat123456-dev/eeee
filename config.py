import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # Telegram API ki ID
    API_ID = int(os.environ.get("API_ID", "0"))
    # Telegram API ki Hash
    API_HASH = os.environ.get("API_HASH", "")
    # Admin user IDs (comma-separated)
    ADMIN_ID = [int(x.strip()) for x in os.environ.get("ADMIN_ID", "0").split(",") if x.strip()]
    # MongoDB database ka URL
    DB_URL = os.environ.get("DB_URL", "")
    # Database ka naam
    DB_NAME = os.environ.get("DB_NAME", "MY_BOT_DB")
    # Text log channel ki ID
    TXT_LOG = int(os.environ.get("TXT_LOG", "0"))
    # Authentication log channel ki ID
    AUTH_LOG = int(os.environ.get("AUTH_LOG", "0"))
    # Hit log channel ki ID
    HIT_LOG = int(os.environ.get("HIT_LOG", "0"))
    # DRM dump channel ki ID
    DRM_DUMP = int(os.environ.get("DRM_DUMP", "0"))
    # Main channel ki ID
    CHANNEL = int(os.environ.get("CHANNEL", "0"))
    # Channel ka link
    CH_URL = os.environ.get("CH_URL", "")
    # Bot ke owner ka Telegram link
    OWNER = os.environ.get("OWNER", "")
    # Thumbnail image ka URL
    THUMB_URL = os.environ.get("THUMB_URL", "")
