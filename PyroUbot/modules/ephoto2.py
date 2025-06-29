import os
from PyroUbot import *
import requests

__MODULE__ = "ᴇᴘʜᴏᴛᴏ 2"
__HELP__ = """**「 BANTUAN UNTUK MODULE EPHOTO 2 」**

<blockquote><b>✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .cloth (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ᴄʟᴏᴛʜ**

✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .galaxy (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ɢᴀʟᴀxʏ**

✮➛ **ᴘᴇʀɪɴᴛᴀʜ: .magma (ᴛᴇxᴛ)**
✮➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ᴍᴀɢᴍᴀ**</b></blockquote>"""

def tweet(text):
    url = "https://api.botcahx.eu.org/api/ephoto/cloth"
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
    url = "https://api.botcahx.eu.org/api/ephoto/galaxy"
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
    url = "https://api.botcahx.eu.org/api/textpro/magma"
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

          
@PY.UBOT("magma")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .magma Boysz")
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
                                  
@PY.UBOT("galaxy")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .galaxy Boysz")
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
                                  
@PY.UBOT("cloth")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .cloth Boysz")
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
