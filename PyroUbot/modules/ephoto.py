import os
from PyroUbot import *
import requests

__MODULE__ = "ᴇᴘʜᴏᴛᴏ"
__HELP__ = """**「 BANTUAN UNTUK MODULE EPHOTO 」**

<blockquote><b>✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .television (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ᴛᴇʟᴇᴠɪsɪᴏɴ**

✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .glasse (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ɢʟᴀssᴇ**

✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .blackpink (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ʙʟᴀᴄᴋᴘɪɴᴋ**

✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .blackpink2 (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ʙʟᴀᴄᴋᴘɪɴᴋ2**

✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .coverpubg (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ʙʟᴀᴄᴋᴘɪɴᴋ2**

✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .hororr (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ʜᴏʀᴏʀʀʀ**</b></blockquote>"""

def tweet(text):
    url = "https://api.botcahx.eu.org/api/ephoto/televisi"
    params = {
        "text": text,
        "apikey": "Biyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def rob(text):
    url = "https://api.botcahx.eu.org/api/ephoto/coverpubg"
    params = {
        "text": text,
        "apikey": "Biyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def robottt(text):
    url = "https://api.botcahx.eu.org/api/ephoto/horor"
    params = {
        "text": text,
        "apikey": "Biyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

          
@PY.UBOT("hororr")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .hororrr Boysz")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = robottt(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")
                                  
@PY.UBOT("coverpubg")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .coverpubg Boysz")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = rob(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")
                                  
@PY.UBOT("blackpink")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .blackpink Boysz")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = fb(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")
@PY.UBOT("blackpink2")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .blackpink Boysz")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = fbs(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")
@PY.UBOT("television")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .television Boysz")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = tweet(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")

@PY.UBOT("glasse")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .gllaases Boysz")
        return

    request_text = args[1]
    processing_msg = await message.edit("ʟᴏᴀᴅɪɪɪɴɢ..........")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▱▱▱▱▱ 𝟸𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▱▱▱▱ 𝟺𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▱▱▱ 𝟼𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▱▱ 𝟾𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("▰▰▰▰▰▰▰ 𝟷𝟶𝟶%")
    await asyncio.sleep(0.1)
    processing_msg = await message.edit("✦ sᴜᴄᴄᴇssғᴜʟʟʏ ✦")
    await asyncio.sleep(0.1)
    image_content = tweets(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")
                                                                                                                              
