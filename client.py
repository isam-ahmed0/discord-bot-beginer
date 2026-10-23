import discord
# import queue
from discord.ext import commands, tasks
from discord import app_commands
import asyncio
# import threading
import discord_webhook
from bot_token import *
import logging
# import yt_dlp
import os

handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.typing = True
bot = commands.Bot(command_prefix=".", intents=intents)

def shut():
    if bot.loop and bot.loop.is_running:
        asyncio.run_coroutine_threadsafe(bot.change_presence(status=discord.Status.offline), bot.loop)
        asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
        print("Bot offline")

def ban_core():
    asyncio.run_coroutine_threadsafe(ban_them)

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print("Synced")
    except Exception as e:
        print(e)
    await bot.change_presence(
        status=discord.Status.idle, 
        activity=discord.Game(name="Hi"))
    print(f"We are ready! {bot.user}")


if __name__ == "__main__":
    from extra.on import *
    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)