# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/Map.ui'
#
# Created: Sun Apr  5 22:41:15 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MapWidget(object):
    def setupUi(self, MapWidget):
        MapWidget.setObjectName(_fromUtf8("MapWidget"))
        MapWidget.setWindowModality(QtCore.Qt.NonModal)
        MapWidget.resize(70, 70)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MapWidget.sizePolicy().hasHeightForWidth())
        MapWidget.setSizePolicy(sizePolicy)
        MapWidget.setMinimumSize(QtCore.QSize(50, 50))
        MapWidget.setMaximumSize(QtCore.QSize(70, 70))
        MapWidget.setSizeIncrement(QtCore.QSize(1, 1))
        MapWidget.setBaseSize(QtCore.QSize(50, 50))
        MapWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MapWidget.setMouseTracking(True)
        self.layout = QtGui.QVBoxLayout(MapWidget)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.map = QtGui.QLabel(MapWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map.sizePolicy().hasHeightForWidth())
        self.map.setSizePolicy(sizePolicy)
        self.map.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.map.setFont(font)
        self.map.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.map.setMouseTracking(True)
        self.map.setFrameShape(QtGui.QFrame.StyledPanel)
        self.map.setFrameShadow(QtGui.QFrame.Sunken)
        self.map.setText(_fromUtf8(""))
        self.map.setPixmap(QtGui.QPixmap(_fromUtf8(":/maps/resources/maps/03.jpg")))
        self.map.setScaledContents(True)
        self.map.setAlignment(QtCore.Qt.AlignCenter)
        self.map.setWordWrap(True)
        self.map.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.map.setObjectName(_fromUtf8("map"))
        self.layout.addWidget(self.map)

        self.retranslateUi(MapWidget)
        QtCore.QMetaObject.connectSlotsByName(MapWidget)

    def retranslateUi(self, MapWidget):
        MapWidget.setWindowTitle(_translate("MapWidget", "Map", None))

import resources_rc
