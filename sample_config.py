import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5545728732:AAGi3z4YazR_CxoqpbsjSdz3Q7yZoiW5vug")
    API_ID = int(os.environ.get("API_ID", 7856100))
    API_HASH = os.environ.get("API_HASH","dba409d7e8d44ab5bb689378deea1792")
    DOWNLOAD_LOCATION = "./DOWNLOADS"

