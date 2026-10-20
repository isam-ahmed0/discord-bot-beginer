from core_api import api_call
from client import bot

@api_call
async def send_hi(chid: int, message: str):
    channel = bot.get_channel(chid) or await bot.fetch_channel(chid)
    return await channel.send(message)