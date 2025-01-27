#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rprename/app.py

import sys
from PySide6.QtWidgets import QApplication
from .views import Window

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
    sys.exit(app.exec())
    # return app.exec()