# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/battery.ui'
#
# Created: Thu Jul  2 13:42:17 2015
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_batteryStatus(object):
    def setupUi(self, batteryStatus):
        batteryStatus.setObjectName(_fromUtf8("batteryStatus"))
        batteryStatus.resize(159, 107)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(batteryStatus.sizePolicy().hasHeightForWidth())
        batteryStatus.setSizePolicy(sizePolicy)
        self.BatteryLayout = QtGui.QVBoxLayout(batteryStatus)
        self.BatteryLayout.setSpacing(1)
        self.BatteryLayout.setMargin(0)
        self.BatteryLayout.setObjectName(_fromUtf8("BatteryLayout"))
        self.batteryLevel = QtGui.QGroupBox(batteryStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryLevel.sizePolicy().hasHeightForWidth())
        self.batteryLevel.setSizePolicy(sizePolicy)
        self.batteryLevel.setMouseTracking(True)
        self.batteryLevel.setInputMethodHints(QtCore.Qt.ImhNone)
        self.batteryLevel.setFlat(False)
        self.batteryLevel.setCheckable(False)
        self.batteryLevel.setObjectName(_fromUtf8("batteryLevel"))
        self.batteryBoxLayout = QtGui.QVBoxLayout(self.batteryLevel)
        self.batteryBoxLayout.setMargin(3)
        self.batteryBoxLayout.setObjectName(_fromUtf8("batteryBoxLayout"))
        self.batteryBoxLevel = QtGui.QHBoxLayout()
        self.batteryBoxLevel.setSpacing(1)
        self.batteryBoxLevel.setObjectName(_fromUtf8("batteryBoxLevel"))
        self.battery = CProgressBar(self.batteryLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery.sizePolicy().hasHeightForWidth())
        self.battery.setSizePolicy(sizePolicy)
        self.battery.setProperty("value", 100)
        self.battery.setAlignment(QtCore.Qt.AlignCenter)
        self.battery.setTextVisible(False)
        self.battery.setInvertedAppearance(False)
        self.battery.setObjectName(_fromUtf8("battery"))
        self.batteryBoxLevel.addWidget(self.battery)
        self.value = QtGui.QLabel(self.batteryLevel)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.value.setFont(font)
        self.value.setObjectName(_fromUtf8("value"))
        self.batteryBoxLevel.addWidget(self.value)
        self.p = QtGui.QLabel(self.batteryLevel)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p.setFont(font)
        self.p.setObjectName(_fromUtf8("p"))
        self.batteryBoxLevel.addWidget(self.p)
        self.batteryBoxLayout.addLayout(self.batteryBoxLevel)
        self.charge = HButton(self.batteryLevel)
        self.charge.setMinimumSize(QtCore.QSize(0, 44))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(175, 175, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 175, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 175, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.charge.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.charge.setFont(font)
        self.charge.setAutoFillBackground(True)
        self.charge.setStyleSheet(_fromUtf8(""))
        self.charge.setFlat(True)
        self.charge.setObjectName(_fromUtf8("charge"))
        self.batteryBoxLayout.addWidget(self.charge)
        self.BatteryLayout.addWidget(self.batteryLevel)

        self.retranslateUi(batteryStatus)
        QtCore.QObject.connect(self.charge, QtCore.SIGNAL(_fromUtf8("clicked()")), self.battery.reset)
        QtCore.QObject.connect(self.battery, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.value.setNum)
        QtCore.QMetaObject.connectSlotsByName(batteryStatus)

    def retranslateUi(self, batteryStatus):
        batteryStatus.setWindowTitle(_translate("batteryStatus", "Form", None))
        self.batteryLevel.setTitle(_translate("batteryStatus", "Battery", None))
        self.value.setText(_translate("batteryStatus", "100", None))
        self.p.setText(_translate("batteryStatus", "%", None))
        self.charge.setText(_translate("batteryStatus", "Charge", None))

from aui.utilities.ColorProgressBar import CProgressBar
from aui.utilities.HoverButtons import HButton

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    batteryStatus = QtGui.QWidget()
    ui = Ui_batteryStatus()
    ui.setupUi(batteryStatus)
    batteryStatus.show()
    sys.exit(app.exec_())

