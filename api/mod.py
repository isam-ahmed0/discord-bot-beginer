import discord
from core_api import api_call
from client import bot

@api_call
async def ban(g_id: int, m_id: int, reason: str = "Not provided"):
    guild_id = int(g_id)
    guild = bot.get_guild(guild_id)
    member_id = int(m_id)
    member = guild.get_member(member_id) or await guild.fetch_member(member_id)
    
    return await member.ban(reason=reason)