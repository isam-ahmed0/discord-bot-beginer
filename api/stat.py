from core_api import api_call
from client import bot
import discord

current_st = discord.Status.online
current_pr = None

@api_call
async def stat_change(st: str):
    global current_st
    if st == "online":
        current_st = discord.Status.online
    elif st == "offline":
        current_st = discord.Status.offline
    elif st == "idle":
        current_st = discord.Status.idle
    elif st == "dnd":
        current_st = discord.Status.dnd
    
    await bot.change_presence(status=current_st, activity=current_pr)

@api_call
async def activity(n):
    global current_pr
    if n:
        current_pr = discord.Game(name=n)
    else:
        current_pr = None
        
    # Send both status and activity together
    await bot.change_presence(status=current_st, activity=current_pr)