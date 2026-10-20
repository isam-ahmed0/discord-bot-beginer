from core_api import api_call
from client import bot
import discord

@api_call
async def stat_change(st: str):
    if st == "online":
        await bot.change_presence(status=discord.Status.online)
    elif st == "offline":
        await bot.change_presence(status=discord.Status.offline)
    elif st == "idle":
        await bot.change_presence(status=discord.Status.idle)
    elif st == "dnd":
        await bot.change_presence(status=discord.Status.dnd)