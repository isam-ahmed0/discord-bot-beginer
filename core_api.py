import asyncio
import sys
from client import *

def api_call(func):
    def wrapper(*args, **kwargs):
        if not bot.loop or not bot.is_ready():
            raise RuntimeError("Bot is not runnning.")
        
        future = asyncio.run_coroutine_threadsafe(func(*args, **kwargs), bot.loop)
        return future.result(timeout=5)
    return wrapper