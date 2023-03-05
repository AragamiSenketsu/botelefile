import os

API_ID = int(29835490)
API_HASH = "d98453e3790f608f70b38426f915866c"
BOT_TOKEN = "5742581146:AAHz38p1ktPS2NEaPCBgYeNQZOLYXL-4Vnw"
DB_CHANNEL_ID = "-1001794831285"
IS_PRIVATE = false # any input is ok But True preferable
OWNER_ID = int(5516570253)
UPDATE_CHANNEL = 
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
