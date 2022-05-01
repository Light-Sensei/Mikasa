import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from MikasaRobot.events import register
from MikasaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/8e67fc63f44c03a91dd76.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Yo!! [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Micchon Shikimori.** \n\n"
  TEXT += "♡ **I'm Working Properly Baka!!** \n\n"
  TEXT += f"♡ **Eren : [Light Yagami♡ (夜神月♡)](https://t.me/itz_light_yagami)** \n\n"
  TEXT += f"♡ **Library Version :** `{telever}` \n\n"
  TEXT += f"♡ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"♡ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ♡**"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/MikasaXupdates"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/MikasaXsupport"), 
                       Button.url("ᴇʀᴇɴ", "https://t.me/Itz_Light_Yagami")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
