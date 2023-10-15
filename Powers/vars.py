from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default="6663040181:AAEdRPMg1h8CaImyX5Wf8ERWNdUg8y97S-k")
    API_ID = int(config("API_ID", default="29722120"))
    API_HASH = config("API_HASH", default="91f3bf8651edfa748856cfcad07f55bb")
    OWNER_ID = int(config("OWNER_ID", default=1983471689))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default="-1001829052958"))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="1983471689",
        ).split(" ")
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="1983471689",
        ).split(" ")
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="1983471689",
        ).split(" ")
    ]
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
    AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="mongodb+srv://helloyeager8:dSaini9485@cluster0.bhqp2fq.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
    DB_NAME = config("DB_NAME", default="esdeath")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/ ! .").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="chatdiscussion17")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="esdeath_xb")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""
    owner_username = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6663040181:AAEdRPMg1h8CaImyX5Wf8ERWNdUg8y97S-k"
    API_ID = 29722120  # Your APP_ID from Telegram
    API_HASH = "91f3bf8651edfa748856cfcad07f55bb" #Your api hash from Telegram
    OWNER_ID = 1983471689  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001829052958 # Your Private Group ID for logs
    DEV_USERS = [1983471689]
    SUDO_USERS = [1983471689]
    WHITELIST_USERS = [1983471689]
    DB_URI = "mongodb+srv://helloyeager8:dSaini9485@cluster0.bhqp2fq.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"  # Your mongo DB URI
    DB_NAME = "esdeath"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    RMBG_API = ""
    PREFIX_HANDLER = ["!", "/", "$", "."]
    SUPPORT_GROUP = "chatdiscussion17"
    SUPPORT_CHANNEL = "esdeath_xb"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = ""
    WORKERS = 8
