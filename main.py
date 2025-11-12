import asyncio
import sys
import traceback
import os
import logging
from pyrogram import idle
from bot import Bot
from helper_func import *
from config import *

# Setup logging - prints with timestamps, flushes automatically
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)


async def main():
    logging.info("Starting bot...")
    bot = Bot()
    await bot.start()

    logging.info("Bot started. Running idle...")
    await idle()

    logging.info("Shutdown signal received, stopping bot...")
    await bot.stop()
    logging.info("Bot stopped.")

async def restart_bot():
    logging.info("Restarting bot in 5 seconds...")
    await asyncio.sleep(5)
    logging.info("Restarting now...")
    # Flush stdout/stderr before exec
    sys.stdout.flush()
    sys.stderr.flush()
    # Replace current process with new one (proper restart)
    os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Gracefully shutting down bot (Ctrl+C detected)...")
        sys.exit(0)
    except Exception:
        logging.error("Unexpected crash:\n%s", traceback.format_exc())
        # Restart bot properly
        asyncio.run(restart_bot())
