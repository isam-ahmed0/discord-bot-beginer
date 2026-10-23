import asyncio
import threading
import time
import logging
from client import bot
from gui.main import BotGUI, run_gui
# from cli import cli
from bot_token import *

handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")


bott = threading.Thread(
      target=lambda: bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG), daemon=True
  )
bott.start()

time.sleep(3)
run_gui()