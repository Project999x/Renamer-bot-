
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from mega import Mega
import asyncio
import time
import logging
import json
from datetime import datetime
from database import db
from config import *
from plugins.scrapper import *

# ═══════════════════════════════════════════════════════════════════════════════════
# 👨‍💼 ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs
# ═══════════════════════════════════════════════════════════════════════════════════

@Client.on_message(filters.private & filters.command("addpremium") & filters.user(ADMINS))
async def add_premium_user(client, message):
    """Add premium user - Admin only"""
    try:
        parts = message.text.split()
        if len(parts) != 3:
            await message.reply(
                "**ᴜsᴀɢᴇ:** `/addpremium user_id plan_type`\n\n"
                "**ᴘʟᴀɴ ᴛʏᴘᴇs:**\n"
                "• `7_days` - 7 ᴅᴀʏs ᴘʀᴇᴍɪᴜᴍ\n"
                "• `3_months` - 3 ᴍᴏɴᴛʜs ᴘʀᴇᴍɪᴜᴍ\n"
                "• `6_months` - 6 ᴍᴏɴᴛʜs ᴘʀᴇᴍɪᴜᴍ\n\n"
                "**ᴇxᴀᴍᴘʟᴇ:** `/addpremium 123456789 3_months`"
            )
            return
        
        user_id = int(parts[1])
        plan_type = parts[2]
        
        if plan_type not in PREMIUM_PLANS:
            await message.reply("❌ ɪɴᴠᴀʟɪᴅ ᴘʟᴀɴ ᴛʏᴘᴇ!")
            return
        
        plan_data = PREMIUM_PLANS[plan_type]
        success = await db.add_premium_user(user_id, plan_data['name'], plan_data['days'])
        
        if success:
            await message.reply(
                f"✅ **ᴘʀᴇᴍɪᴜᴍ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**\n\n"
                f"👤 **ᴜsᴇʀ ɪᴅ:** `{user_id}`\n"
                f"💎 **ᴘʟᴀɴ:** {plan_data['name']}\n"
                f"⏰ **ᴅᴜʀᴀᴛɪᴏɴ:** {plan_data['days']} ᴅᴀʏs"
            )
            
            # Notify user
            try:
                await client.send_message(
                    user_id,
                    f"🎉 **ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!**\n\n"
                    f"ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ɢʀᴀɴᴛᴇᴅ **{plan_data['name']}**!\n\n"
                    f"💎 **ʙᴇɴᴇғɪᴛs:**\n"
                    f"✅ ᴜɴʟɪᴍɪᴛᴇᴅ ғɪʟᴇ ʀᴇɴᴀᴍɪɴɢ\n"
                    f"✅ ᴘʀɪᴏʀɪᴛʏ sᴜᴘᴘᴏʀᴛ\n"
                    f"✅ ғᴀsᴛᴇʀ ᴘʀᴏᴄᴇssɪɴɢ\n\n"
                    f"ᴇɴᴊᴏʏ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴇxᴘᴇʀɪᴇɴᴄᴇ! 🚀"
                )
            except:
                pass
        else:
            await message.reply("❌ ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴅᴅ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ!")
            
    except ValueError:
        await message.reply("❌ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ ɪᴅ!")
    except Exception as e:
        await message.reply(f"❌ ᴇʀʀᴏʀ: {str(e)}")

@Client.on_message(filters.private & filters.command("removepremium") & filters.user(ADMINS))
async def remove_premium_user(client, message):
    """Remove premium user - Admin only"""
    try:
        parts = message.text.split()
        if len(parts) != 2:
            await message.reply(
                "**ᴜsᴀɢᴇ:** `/removepremium user_id`\n\n"
                "**ᴇxᴀᴍᴘʟᴇ:** `/removepremium 123456789`"
            )
            return
        
        user_id = int(parts[1])
        success = await db.remove_premium_user(user_id)
        
        if success:
            await message.reply(
                f"✅ **ᴘʀᴇᴍɪᴜᴍ ʀᴇᴍᴏᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**\n\n"
                f"👤 **ᴜsᴇʀ ɪᴅ:** `{user_id}`"
            )
            
            # Notify user
            try:
                await client.send_message(
                    user_id,
                    f"⚠️ **ᴘʀᴇᴍɪᴜᴍ ᴇxᴘɪʀᴇᴅ/ʀᴇᴍᴏᴠᴇᴅ**\n\n"
                    f"ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ʜᴀs ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ.\n\n"
                    f"ʏᴏᴜ ᴄᴀɴ ɴᴏᴡ ʀᴇɴᴀᴍᴇ ᴜᴘ ᴛᴏ {FREE_LIMIT} ғɪʟᴇs ғᴏʀ ғʀᴇᴇ.\n\n"
                    f"ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ʀᴇɴᴇᴡ ᴘʀᴇᴍɪᴜᴍ!"
                )
            except:
                pass
        else:
            await message.reply("❌ ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ!")
            
    except ValueError:
        await message.reply("❌ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ ɪᴅ!")
    except Exception as e:
        await message.reply(f"❌ ᴇʀʀᴏʀ: {str(e)}")

@Client.on_message(filters.private & filters.command("premiumlist") & filters.user(ADMINS))
async def list_premium_users(client, message):
    """List all premium users - Admin only"""
    try:
        premium_users = await db.get_premium_users()
        
        if not premium_users:
            await message.reply("📝 **ɴᴏ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs ғᴏᴜɴᴅ**")
            return
        
        text = f"💎 **ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs ʟɪsᴛ** ({len(premium_users)})\n\n"
        
        for i, user in enumerate(premium_users, 1):
            end_date = user['end_date'].strftime('%d-%m-%Y')
            text += (
                f"**{i}.** `{user['user_id']}`\n"
                f"   💎 {user['plan_type']}\n"
                f"   📅 ᴇxᴘɪʀᴇs: {end_date}\n\n"
            )
            
            # Split message if too long
            if len(text) > 3500:
                await message.reply(text)
                text = ""
        
        if text:
            await message.reply(text)
            
    except Exception as e:
        await message.reply(f"❌ ᴇʀʀᴏʀ: {str(e)}")

@Client.on_message(filters.private & filters.command("stats") & filters.user(ADMINS))
async def bot_stats(client, message):
    """Show bot statistics - Admin only"""
    try:
        total_users = await db.get_total_users()
        premium_users = await db.get_premium_users()
        premium_count = len(premium_users)
        
        # Calculate uptime (you can implement this based on bot start time)
        uptime = "N/A"  # Implement uptime calculation if needed
        
        stats_text = (
            f"📊 **ʙᴏᴛ sᴛᴀᴛɪsᴛɪᴄs**\n\n"
            f"👥 **ᴛᴏᴛᴀʟ ᴜsᴇʀs:** {total_users}\n"
            f"💎 **ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs:** {premium_count}\n"
            f"🆓 **ғʀᴇᴇ ᴜsᴇʀs:** {total_users - premium_count}\n"
            f"⏰ **ᴜᴘᴛɪᴍᴇ:** {uptime}\n"
            f"🔄 **ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs:** {len(mega_sessions)}\n"
            f"🏷️ **ᴀᴄᴛɪᴠᴇ ᴘʀᴇғɪxᴇs:** {len(user_prefixes)}\n\n"
            f"💡 **sᴜᴘᴇʀ ᴏᴘᴛɪᴍɪᴢᴇᴅ ᴍᴇɢᴀ ʀᴇɴᴀᴍᴇʀ**"
        )
        
        await message.reply(stats_text)
        
    except Exception as e:
        await message.reply(f"❌ ᴇʀʀᴏʀ: {str(e)}")

# ═══════════════════════════════════════════════════════════════════════════════════
# 💎 ᴘʀᴇᴍɪᴜᴍ ᴄᴀʟʟʙᴀᴄᴋ ʜᴀɴᴅʟᴇʀs
# ═══════════════════════════════════════════════════════════════════════════════════

@Client.on_callback_query(filters.regex(r"^buy_"))
async def premium_callback(client, callback_query):
    """Handle premium plan selection"""
    try:
        plan_key = callback_query.data.split("_", 1)[1]
        
        if plan_key not in PREMIUM_PLANS:
            await callback_query.answer("❌ ɪɴᴠᴀʟɪᴅ ᴘʟᴀɴ!", show_alert=True)
            return
        
        plan_data = PREMIUM_PLANS[plan_key]
        user_id = callback_query.from_user.id
        
        # Create contact admin button
        contact_text = (
            f"💎 **{plan_data['name']} sᴇʟᴇᴄᴛᴇᴅ**\n\n"
            f"💰 **ᴘʀɪᴄᴇ:** {plan_data['price']}\n"
            f"⏰ **ᴅᴜʀᴀᴛɪᴏɴ:** {plan_data['days']} ᴅᴀʏs\n"
            f"🎯 **ʙᴇɴᴇғɪᴛs:** ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴇɴᴀᴍɪɴɢ\n\n"
            f"👤 **ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ:** `{user_id}`\n\n"
            f"📞 **ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴄᴏᴍᴘʟᴇᴛᴇ ᴘᴀʏᴍᴇɴᴛ**\n"
            f"sᴇɴᴅ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ ᴀɴᴅ sᴇʟᴇᴄᴛᴇᴅ ᴘʟᴀɴ ᴛᴏ ᴀᴅᴍɪɴ."
        )
        
        contact_button = InlineKeyboardMarkup([
            [InlineKeyboardButton("👨‍💼 ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ", url=f"https://t.me/{OWNER_TAG}")]
        ])
        
        await callback_query.message.edit_text(
            contact_text,
            reply_markup=contact_button
        )
        
        await callback_query.answer("✅ ᴘʟᴀɴ sᴇʟᴇᴄᴛᴇᴅ! ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ɴᴏᴡ.", show_alert=True)
        
    except Exception as e:
        await callback_query.answer(f"❌ ᴇʀʀᴏʀ: {str(e)}", show_alert=True)

# ═══════════════════════════════════════════════════════════════════════════════════
# 🔄 ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴘʀᴇᴍɪᴜᴍ ᴇxᴘɪʀʏ ᴄʜᴇᴄᴋ
# ═══════════════════════════════════════════════════════════════════════════════════

async def check_premium_expiry():
    """Check and remove expired premium users"""
    try:
        expired_users = await db.get_expired_premium_users()
        
        for user_id in expired_users:
            await db.remove_premium_user(user_id)
            logger.info(f"Removed expired premium user: {user_id}")
            
            # Optionally notify user about expiry
            try:
                await client.send_message(
                    user_id,
                    f"⚠️ **ᴘʀᴇᴍɪᴜᴍ ᴇxᴘɪʀᴇᴅ**\n\n"
                    f"ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ʜᴀs ᴇxᴘɪʀᴇᴅ.\n\n"
                    f"ʏᴏᴜ ᴄᴀɴ ɴᴏᴡ ʀᴇɴᴀᴍᴇ ᴜᴘ ᴛᴏ {FREE_LIMIT} ғɪʟᴇs ғᴏʀ ғʀᴇᴇ.\n\n"
                    f"ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ʀᴇɴᴇᴡ ᴘʀᴇᴍɪᴜᴍ!"
                )
            except:
                pass
                
    except Exception as e:
        logger.error(f"Error checking premium expiry: {e}")

# # Run premium expiry check every hour
# import asyncio
# from apscheduler.schedulers.asyncio import AsyncIOScheduler

# scheduler = AsyncIOScheduler()
# scheduler.add_job(check_premium_expiry, 'interval', hours=1)
# scheduler.start()

# ═══════════════════════════════════════════════════════════════════════════════════
# 🏁 ᴇɴᴅ ᴏғ sᴄʀᴀᴘᴘᴇʀ ᴍᴏᴅᴜʟᴇ
# ═══════════════════════════════════════════════════════════════════════════════════
