import asyncio
import random
import sys
import logging
from datetime import datetime

import pytz
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode

from bot import Bot
from config import OWNER_ID, START_PIC
from helper_func import get_start_msg
from database import db

# Constants
IST = pytz.timezone("Asia/Kolkata")

# Inline keyboard layout
def get_start_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about"),
            InlineKeyboardButton("🔒 ᴄʟᴏsᴇ", callback_data="close")
        ],
        [InlineKeyboardButton("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/shizukawachan")]
    ])

# /start command handler
@Bot.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    user_id = message.from_user.id

    # Add user to database if not already present
    if not await db.present_user(user_id):
        await db.add_user(user_id)

    # Prepare message
    start_pic = random.choice(START_PIC)
    mention = message.from_user.mention
    caption = get_start_msg(mention)
    keyboard = get_start_keyboard()

    await message.delete()
    
    await message.reply_photo(
        photo=start_pic,
        caption=caption,
        reply_markup=keyboard,
        quote=True
    )
