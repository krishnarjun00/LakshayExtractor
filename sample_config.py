import os

api_id = 20299588
api_hash = os.environ.get("API_HASH", "f550d6179131c293d658f15f8c24f594")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "5374602611")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "5374602611")
owner_users = [int(num) for num in osowner_users.split(",")]
