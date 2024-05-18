import requests
import json
import time
import uuid
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from pyrogram import Client, filters
from pyrogram.types import Message
import logging
from logging.handlers import RotatingFileHandler

# ========== Logging ==========#
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger()
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# =========== Configuration ===========#
api_id = 20299588  # Replace with your actual API ID
api_hash = 'f550d6179131c293d658f15f8c24f594'  # Replace with your actual API Hash
bot_token = '6877077737:AAE79BKV7PR_EF4BaiyN0-xKPzT-J7Erx-Q'  # Replace with your actual Bot Token

# =========== Client ===========#
bot = Client(
    "bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
)

RWA_URL = "https://rozgarapinew.teachx.in/post/login"
HDR = {
    "Client-Service": "Appx",
    "Auth-Key": "appxapi",
    "User-ID": "-2",
    "Authorization": "",
    "User_app_category": "",
    "Language": "en",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "okhttp/4.9.1"
}

@bot.on_message(filters.command(["lakshay"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    
    try:
        input1 = await bot.listen(editable.chat.id)
        raw_text = input1.text.strip()
        await input1.delete()

        email, password = raw_text.split("*")
        info = {"email": email, "password": password}

        res = requests.post(RWA_URL, data=info, headers=HDR)
        res.raise_for_status()
        output = res.json()

        userid = output["data"]["userid"]
        token = output["data"]["token"]

        hdr1 = HDR.copy()
        hdr1.update({
            "User-ID": userid,
            "Authorization": token,
            "Host": "rozgarapinew.teachx.in"
        })

        await editable.edit("**Login Successful**")

        res1 = requests.get(f"https://rozgarapinew.teachx.in/get/mycourse?userid={userid}", headers=hdr1)
        res1.raise_for_status()
        b_data = res1.json()['data']

        cool = "\n".join([f"`{data['id']}` - **{data['course_name']}**" for data in b_data])
        await editable.edit(f'**You have these batches :-**\n\n**BATCH-ID -      BATCH NAME**\n\n{cool}')

        editable1 = await m.reply_text("**Now send the Batch ID to Download**")
        input2 = await bot.listen(editable.chat.id)
        batch_id = input2.text.strip()
        await editable1.delete()
        await input2.delete()

        editable2 = await m.reply_text("📥**Please wait keep patience.** 🧲 `Scraping URL.`")
        time.sleep(2)

        # Fetch subjects and topics
        res2 = requests.get(f"https://rozgarapinew.teachx.in/get/allsubjectfrmlivecourseclass?courseid={batch_id}", headers=hdr1)
        res2.raise_for_status()
        subject_data = res2.json()["data"]
        subject_ids = [subject["subjectid"] for subject in subject_data]

        await editable2.edit("📥**Please wait keep patience.** 🧲 `Scraping URL..`")
        time.sleep(2)

        all_topic_ids = []
        for subject_id in subject_ids:
            res3 = requests.get(f"https://rozgarapinew.teachx.in/get/alltopicfrmlivecourseclass?courseid={batch_id}&subjectid={subject_id}", headers=hdr1)
            res3.raise_for_status()
            topic_data = res3.json()['data']
            all_topic_ids.extend([topic["topicid"] for topic in topic_data])

        hdr11 = {
            "Host": "rozgarapinew.teachx.in",
            "Client-Service": "Appx",
            "Auth-Key": "appxapi",
            "User-Id": userid,
            "Authorization": token
        }

        cool2 = ""
        await editable2.edit("📥**Please wait keep patience.** 🧲 `Scraping URL...`")
        for t in all_topic_ids:
            res4 = requests.get(f"https://rozgarapinew.teachx.in/get/livecourseclassbycoursesubtopconceptapiv3?topicid={t}&start=-1&conceptid=1&courseid={batch_id}&subjectid={subject_id}", headers=hdr11)
            res4.raise_for_status()
            topicid = res4.json()["data"]
            for data in topicid:
                b64 = data["download_link"] if data["download_link"] else data["pdf_link"]
                tid = data["Title"].replace(" : ", " ").replace(" :- ", " ").replace(" :-", " ").replace(":-", " ").replace("_", " ").replace("(", "").replace(")", "").replace("&", "").strip()
                key = "638udh3829162018".encode("utf8")
                iv = "fedcba9876543210".encode("utf8")
                ciphertext = bytearray.fromhex(b64decode(b64.encode()).hex())
                cipher = AES.new(key, AES.MODE_CBC, iv)
                plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
                b = plaintext.decode('utf-8')
                cool2 += f"{tid}:{b}\n"

        await editable2.edit("Scraping completed successfully!")
        await editable2.delete()

        file_name = next((x['course_name'] for x in b_data if str(x['id']) == batch_id), str(uuid.uuid4()))
        with open(f'{file_name}.txt', 'w') as f:
            f.write(cool2)

        await m.reply_document(f"{file_name}.txt")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        await editable.edit(f"An error occurred: {str(e)}")

bot.run()
