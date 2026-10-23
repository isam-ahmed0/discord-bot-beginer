import sys
import time
import asyncio
import os
from core_api import api_call
from api import mod
from api.message import *
from api.stat import *
from client import bot
from client import bot, shut
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from gui import dialog

class BotGUI:
    def __init__(self):
        
        loader = QUiLoader()
        self.window = loader.load("main.ui")
        self.window.btn_home.clicked.connect(lambda: self.set_page(0))
        self.window.btn_mod.clicked.connect(lambda: self.set_page(1))
        self.window.quit_btn.clicked.connect(self.close_app)
        self.window.test.clicked.connect(lambda: send_hi(1474758092569841707, "hi"))
        print(f"Total pages in StackedWidget: {self.window.stackedWidget.count()}")
        try:
            self.window.btn_set.clicked.connect(lambda: self.set_page(2))
        except Exception as e:
            print(e)
        self.window.online_type.currentTextChanged.connect(self.set_stat)
        self.window.up_activity.clicked.connect(self.set_activity)

        # The nmod things:
        self.window.ban_btn.clicked.connect(self.ban_window)

        self.window.show()

    def set_page(self, i):
        self.window.stackedWidget.setCurrentIndex(i)

    def set_activity(self):
        n = self.window.activity_entry.text()
        activity(n)
    
    def set_stat(self):
        status = self.window.online_type.currentText()
        stat_change(status)
        
    def ban_window0(self):
        self.kick_dialog = dialog.show("kick_dialog.ui")

        guild = self.kick_dialog.guid.text().strip()
        user = self.kick_dialog.uid.text().strip()
        
        self.kick_dialog.ok.clicked.connect(lambda: mod.ban(guild, user))
        # self.kick_dialog.cancel.clicked.connect(self.)

    def ban_window(self):
        self.kick_dialog = dialog.show("kick_dialog.ui")

        def submit(_checked=False):
            guild = self.kick_dialog.guid.text().strip()
            user = self.kick_dialog.uid.text().strip()
            mod.ban(guild, user)

        self.kick_dialog.ok.clicked.connect(submit)
        
    def close_app(self):
        self.window.close()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  client = BotGUI()
  sys.exit(app.exec())

def run_gui():
    app = QApplication(sys.argv)
    client = BotGUI()
    sys.exit(app.exec())
