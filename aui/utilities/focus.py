#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Alternative to Individual Views using QFrame
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

from PyQt4.QtGui import (QFrame)
from PyQt4.QtCore import (pyqtSignal, QObject)


class FocusView(QFrame, QObject):
    inside = pyqtSignal(str, str, name='inside')

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.default_style = self.styleSheet()

    def enterEvent(self, QEvent):
        self.setStyleSheet('border: 2px solid rgb(0, 128, 255); color: rgb(0, 128, 255);')
        self.inside.emit('Focus', self.objectName())

    def leaveEvent(self, QEvent):
        self.setStyleSheet(self.default_style)
