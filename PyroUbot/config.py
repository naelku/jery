import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "5912811985").split()))

API_ID = int(os.getenv("API_ID", "22555106"))

API_HASH = os.getenv("API_HASH", "6c4b6b1c95ea0fc34474d3cf92e17953")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7746258374:AAEP3_gnok0PAXSRMxS5xah43UFodBpWe9U")

OWNER_ID = int(os.getenv("OWNER_ID", "5912811985"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-4869300682").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aortulsk:KxCX5EQdssavL4dm@cluster0.qsywpr2.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4871574834"))
