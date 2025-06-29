from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʙᴀsᴇ64"
__HELP__ = """
<blockquote><b>Bantuan Untuk base64

perintah : <code>{0}base64</code>
untuk encode base64 contoh <code>{0}base64</code> [code]

perintah : <code>{0}decbase64</code>
untuk decode base64 contoh <code>{0}decbase64</code> [code base64]</b></blockquote>
"""

@PY.UBOT("base64")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .base64 [code]"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6298414727487818323>😉</emoji>proccesing encode base64....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://vapis.my.id/api/tobase64?q={a}')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>**HASIL ENCODE BY KINGZUSERBOT:** `{x}`</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")

@PY.UBOT("decbase64")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .decbase64 [code base64]"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6298414727487818323>😉</emoji>proccesing decode base64....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://vapis.my.id/api/toutf8?q={a}')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>**HASIL DECODE BY KINGZUSERBOT:** `{x}`</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
