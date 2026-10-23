import sys
import time
import asyncio
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def show(ui):
    loader = QUiLoader()
    diabox = loader.load(ui)
    diabox.show()
    return diabox