import asyncio
import json
import logging
import os
import re
import subprocess
import sys
import time
from logging.handlers import RotatingFileHandler
from subprocess import getstatusoutput
import requests
import json
import time
import uuid
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyromod import listen
from base64 import b64decode
import online.helpers.vid as helper
from online.Config import *
from online.helpers.button import keyboard
from online.helpers.sudoers import *
from online.helpers.text import *
import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from subprocess import getstatusoutput
import logging
import os
import sys
import re
import cloudscraper
from bs4 import BeautifulSoup

# ==========Logging==========#
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging = logging.getLogger()

# =========== Client ===========#
bot = Client(
    "bot",
    bot_token= "6877077737:AAE79BKV7PR_EF4BaiyN0-xKPzT-J7Erx-Q",
    api_id=api_id,
    api_hash=api_hash,
)

print(listen.__file__)

@bot.on_message(filters.command(["lakshay"]))
async def account_login(bot: Client, m: Message):

    url = "https://elearn.crwilladmin.com/api/v5/login-other"
    data = {
        "deviceType": "android",
        "password": "Rohit@123",
        "deviceIMEI": "",
        "deviceModel": "",
        "deviceVersion": "R(Android 11.0)",
        "email": "rohitrkr7652607@gmail.com",
        "deviceToken": ""
       }
    headers = {
        "Host": "elearn.crwilladmin.com",
        "Token": "",
        "Usertype": "",
        "Appver": "84",
        "Apptype": "android",
        "Content-Type": "application/json; charset=utf-8",
        "Content-Length": "352",
        "Accept-Encoding": "gzip, deflate",
        "user-agent": "okhttp/5.0.0-alpha",
        'Connection': 'Keep-Alive'
    }
    
    proxy_host = ['104.26.3.116']
    
    proxies = {
       'https': proxy_host,
       'http': proxy_host,
    }
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password** \n or \nSend **TOKEN** like This this:-  **TOKEN**" )
    input1:message=await bot.listen(editable.chat.id)
    raw_text = input1.text
    s = requests.Session()
    data={}
    if "*" in raw_text:
      data["email"] = raw_text.split("*")[0]
      data["password"] = raw_text.split("*")[1]
      await input1.delete(True)
      #s = requests.Session()
      response = s.post(url = url, headers=headers, json=data, timeout=10)
      if response.status_code == 200:
          data = response.json()
          token = data["data"]["token"]
          await m.reply_text(token)
      else:
          await m.reply_text("go back to response")
      await m.reply_text(f"Here is your ```{token}```")
    else:
      token = raw_text
    html1 = s.get("https://elearn.crwilladmin.com/api/v5/comp/my-batch?&token=" + token).json()
    topicid = html1["data"]["batchData"]
    cool=""
    for data in topicid:
        instructorName=(data["instructorName"])
        FFF="**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa =f" ```{data['id']}```      - **{data['batchName']}**\n{data['instructorName']}\n\n"
        #aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}')>4096:
            await m.reply_text(aa)
            cool =""
        cool+=aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    html2 = s.get("https://elearn.crwilladmin.com/api/v5/comp/batch-topic/"+raw_text2+"?type=class&token="+token).json()
    topicid = html2["data"]["batch_topic"]
    bn = html2["data"]["batch_detail"]["name"]
    vj=""
    for data in topicid:
        tids = (data["id"])
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            await m.reply_text(idid)
            vj = ""
        vj+=idid
    vp = ""
    for data in topicid:
        tn = (data["topicName"])
        tns=f"{tn}&"
        if len(f"{vp}{tn}")>4096:
            await m.reply_text(tns)
            vp=""
        vp+=tns
    cool1 = ""
    for data in topicid:
        t_name=(data["topicName"].replace(" ",""))
        tid = (data["id"])
        scraper = cloudscraper.create_scraper()
        ffx = s.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+tid+"&token="+token).json()
            #ffx = json.loads(html3)
        vcx =ffx["data"]["class_list"]["batchDescription"]
        vvx =ffx["data"]["class_list"]["classes"]
        vvx.reverse()
        zz= len(vvx)
        BBB = f"{'**TOPIC-ID - TOPIC - VIDEOS**'}"
        hh = f"```{tid}```     - **{t_name} - ({zz})**\n"

#         hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"

        if len(f'{cool1}{hh}')>4096:
            await m.reply_text(hh)
            cool1=""
        cool1+=hh
    await m.reply_text(f'Batch details of **{bn}** are:\n\n{BBB}\n\n{cool1}\n\n**{vcx}**')
    editable2= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")    
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
        
#              xvv = raw_text9.split('&')
#              for z in range(0,len(xvv)):
#                  p =xvv[z]

            #gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57
            #scraper = cloudscraper.create_scraper()
            html4 = s.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+t+"&token="+token).content
            ff = json.loads(html4)
            #vc =ff.json()["data"]["class_list"]["batchDescription"]
            mm = ff["data"]["class_list"]["batchName"].replace("/ "," ")
            vv =ff["data"]["class_list"]["classes"]
            vv.reverse()
            #clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
            #await m.reply_text(clan)
            count = 1
            try:
                for data in vv:
                    vidid = (data["id"])
                    lessonName = (data["lessonName"]).replace("/", "_")
                    
                    bcvid = (data["lessonUrl"][0]["link"])
                     #lessonName = re.sub('\|', '_', cf)

                    if bcvid.startswith("62"):
                        try:
                            #scraper = cloudscraper.create_scraper()
                            html6 = s.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video = json.loads(html6)
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            #print(video_url)
                            #scraper = cloudscraper.create_scraper()
                            html5 = s.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl = json.loads(html5)
                            stoken = surl["data"]["token"]
                            #print(stoken)
                            
                            link = (video_url+"&bcov_auth="+stoken)
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    #cc = (f"{lessonName}:{link}")
                    #await m.reply_text(cc)
                    elif bcvid.startswith("63"):
                        try:
                            #scraper = cloudscraper.create_scraper()
                            html7 = s.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video1 = json.loads(html7)
                            video_source1 = video1["sources"][5]
                            video_url1 = video_source1["src"]
                            #print(video_url)
                            #scraper = cloudscraper.create_scraper()
                            html8 = s.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl1 = json.loads(html8)
                            stoken1 = surl1["data"]["token"]
                            #print(stoken)
                            
                            link = (video_url1+"&bcov_auth="+stoken1)
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    #cc = (f"{lessonName}:{link}")
                    #await m.reply_text(cc)
                    else:
                        link=("https://www.youtube.com/embed/"+bcvid)
                    cc = (f"{lessonName}::{link}")
                    with open(f"{mm }{t_name}.txt", 'a') as f:
                        f.write(f"{lessonName}:{link}\n")
                    #await m.reply_document(f"{mm }{t_name}.txt")
            except Exception as e:
                await m.reply_text(str(e))
        await m.reply_document(f"{mm }{t_name}.txt")
        #os.remove(f"{mm }{t_name}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    try:
        notex = await m.reply_text("Do you want download notes ?\n\nSend **y** or **n**")
        input5:message = await bot.listen (editable.chat.id)
        raw_text5 = input5.text
        if raw_text5 == 'y':
            scraper = cloudscraper.create_scraper()
            html7 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/batch-notes/"+raw_text2+"?topicid="+raw_text2+"&token="+token).content
            pdfD=json.loads(html7)
            k=pdfD["data"]["notesDetails"]
            bb = len(pdfD["data"]["notesDetails"])
            ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
            await m.reply_text(ss)
            k.reverse()
            count1 = 1
            try:
                
                for data in k:
                    name=(data["docTitle"])
                    s=(data["docUrl"]) 
                    xi =(data["publishedAt"])
                    with open(f"{mm }{t_name}.txt", 'a') as f:
                        f.write(f"{name}:{s}\n")
                    continue
                await m.reply_document(f"{mm }{t_name}.txt")
                    
            except Exception as e:
                await m.reply_text(str(e))
            #await m.reply_text("Done")
    except Exception as e:
        print(str(e))
    await m.reply_text("Done")


@bot.on_message(filters.command(["muskan"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    rwa_url = "https://rozgarapinew.teachx.in/post/login"
    hdr = {"Client-Service": "Appx",
           "Auth-Key": "appxapi",
           "User-ID": "-2",
           "Authorization": "",
           "User_app_category": "",
           "Language": "en",
           "Content-Type": "application/x-www-form-urlencoded",
           "Content-Length": "236",
           "Accept-Encoding": "gzip, deflate",
           "User-Agent": "okhttp/4.9.1"
           }
    info = {"email": "", "password": ""}
    input1 = await bot.listen(editable.chat.id)
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    res = requests.post(rwa_url, data=info, headers=hdr).content
    output = json.loads(res)
    userid = output["data"]["userid"]
    token = output["data"]["token"]
    hdr1 = {
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-ID": userid,
        "Authorization": token,
        "User_app_category": "",
        "Language": "en",
        "Host": "rozgarapinew.teachx.in",
        "User-Agent": "okhttp/4.9.1"
    }
    
    await editable.edit("**login Successful**")
    res1 = requests.get("https://rozgarapinew.teachx.in/get/mycourse?userid="+userid, headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    
    for data in b_data:
        t_name = data['course_name']
        FFF = "**BATCH-ID -      BATCH NAME **"
        aa = f" `{data['id']}`      - **{data['course_name']}**\n\n"
        if len(f'{cool}{aa}') > 4096:
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await editable.delete(True)
    await input2.delete(True)
    editable2 = await m.reply_text("📥**Please wait keep patientce.** 🧲    `Scraping Url.`")
    time.sleep(2)
    # Before the loop where you process topic data
    b_name = None  # Define b_name with a default value



# Inside the loop where you reply with the document

    # Fetch subject IDs corresponding to the batch ID
    res2 = requests.get("https://rozgarapinew.teachx.in/get/allsubjectfrmlivecourseclass?courseid="+raw_text2, headers=hdr1).json()
    subject_data = res2["data"]
    # Extract subject IDs from the response
    subject_ids = [subject["subjectid"] for subject in subject_data]
    await editable2.edit("📥**Please wait keep patientce.** 🧲    `Scraping Url..`")
    time.sleep(2)
    # Fetch topic IDs corresponding to each subject ID
    all_topic_ids = []
    for subject_id in subject_ids:
        res3 = requests.get("https://rozgarapinew.teachx.in/get/alltopicfrmlivecourseclass?courseid="+raw_text2+"&subjectid="+subject_id, headers=hdr1)
        topic_data = res3.json()['data']
        topic_ids = [topic["topicid"] for topic in topic_data]
        all_topic_ids.extend(topic_ids)
    # Inside the loop where you check for batch name
    b_name = next((x['id'] for x in b_data if str(x['course_name']) == raw_text2), None)
    # Now all_topic_ids contains all the topic IDs for the given batch ID

    xv = all_topic_ids  # Use all_topic_ids as the list of topic IDs

    hdr11 = {
        "Host": "rozgarapinew.teachx.in",
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-Id": userid,
        "Authorization": token
    }    
    
    cool2 = ""  # Define cool2 outside the loop to accumulate all URLs
    await editable2.edit("📥**Please wait keep patientce.** 🧲    `Scraping Url...`")
    for t in xv:  # Loop through all topic IDs
        res4 = requests.get("https://rozgarapinew.teachx.in/get/livecourseclassbycoursesubtopconceptapiv3?topicid=" + t + "&start=-1&conceptid=1&courseid=" + raw_text2 + "&subjectid=" + subject_id, headers=hdr11).json()
        topicid = res4["data"]
        for data in topicid:
            if data["download_link"]:
                b64 = (data["download_link"])
            else:
                b64 = (data["pdf_link"])
            tid = data["Title"].replace(" : ", " ").replace(" :- ", " ").replace(" :-", " ").replace(":-", " ").replace("_", " ").replace("(", "").replace(")", "").replace("&", "").strip()
            zz = len(tid)
            key = "638udh3829162018".encode("utf8")
            iv = "fedcba9876543210".encode("utf8")
            ciphertext = bytearray.fromhex(b64decode(b64.encode()).hex())
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            b = plaintext.decode('utf-8')
            cc0 = f"{tid}:{b}"
            if len(f'{cool2}{cc0}') > 9999:
                cool2 = ""
            cool2 += cc0
    await editable2.edit("Scraping completed successfully!")
    await editable2.delete(True)
    # Outside the loop, write all URLs to a single file and reply with the document
    file_name = b_name if b_name else str(uuid.uuid4())  # Use batch name if available, else generate a random file name
    with open(f'{file_name}.txt', 'w') as f:
        f.write(cool2)
    await m.reply_document(f"{file_name}.txt")

bot.run()
