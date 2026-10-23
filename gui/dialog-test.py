import sys
import time
import asyncio
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import dialog

app = QApplication(sys.argv)

window = dialog.show("kick_dialog.ui")
sys.exit(app.exec())