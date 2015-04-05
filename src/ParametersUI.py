# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/Parameters.ui'
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

class Ui_AUIParameters(object):
    def setupUi(self, AUIParameters):
        AUIParameters.setObjectName(_fromUtf8("AUIParameters"))
        AUIParameters.resize(250, 599)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AUIParameters.sizePolicy().hasHeightForWidth())
        AUIParameters.setSizePolicy(sizePolicy)
        AUIParameters.setMinimumSize(QtCore.QSize(250, 599))
        AUIParameters.setMaximumSize(QtCore.QSize(300, 524287))
        self.AUIParams = QtGui.QWidget()
        self.AUIParams.setObjectName(_fromUtf8("AUIParams"))
        self.verticalLayout = QtGui.QVBoxLayout(self.AUIParams)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.contents = QtGui.QTabWidget(self.AUIParams)
        self.contents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.contents.setTabPosition(QtGui.QTabWidget.South)
        self.contents.setObjectName(_fromUtf8("contents"))
        self.Tab1 = QtGui.QWidget()
        self.Tab1.setObjectName(_fromUtf8("Tab1"))
        self.tab1Layout = QtGui.QVBoxLayout(self.Tab1)
        self.tab1Layout.setSpacing(0)
        self.tab1Layout.setMargin(0)
        self.tab1Layout.setObjectName(_fromUtf8("tab1Layout"))
        self.episodes = QtGui.QGroupBox(self.Tab1)
        self.episodes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.episodes.setObjectName(_fromUtf8("episodes"))
        self.episodesLayout = QtGui.QGridLayout(self.episodes)
        self.episodesLayout.setMargin(1)
        self.episodesLayout.setObjectName(_fromUtf8("episodesLayout"))
        self.startEpisodeButton = QtGui.QPushButton(self.episodes)
        self.startEpisodeButton.setMinimumSize(QtCore.QSize(44, 44))
        self.startEpisodeButton.setCheckable(False)
        self.startEpisodeButton.setFlat(False)
        self.startEpisodeButton.setObjectName(_fromUtf8("startEpisodeButton"))
        self.episodesLayout.addWidget(self.startEpisodeButton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.resetEpisodeButton = QtGui.QPushButton(self.episodes)
        self.resetEpisodeButton.setMinimumSize(QtCore.QSize(44, 44))
        self.resetEpisodeButton.setAutoFillBackground(True)
        self.resetEpisodeButton.setAutoDefault(True)
        self.resetEpisodeButton.setFlat(False)
        self.resetEpisodeButton.setObjectName(_fromUtf8("resetEpisodeButton"))
        self.episodesLayout.addWidget(self.resetEpisodeButton, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stopEpisodeButton = QtGui.QPushButton(self.episodes)
        self.stopEpisodeButton.setMinimumSize(QtCore.QSize(44, 44))
        self.stopEpisodeButton.setCheckable(False)
        self.stopEpisodeButton.setObjectName(_fromUtf8("stopEpisodeButton"))
        self.episodesLayout.addWidget(self.stopEpisodeButton, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.episodeTimer = QtGui.QLCDNumber(self.episodes)
        self.episodeTimer.setMinimumSize(QtCore.QSize(60, 30))
        self.episodeTimer.setMaximumSize(QtCore.QSize(16777215, 44))
        self.episodeTimer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.episodeTimer.setFrameShadow(QtGui.QFrame.Plain)
        self.episodeTimer.setObjectName(_fromUtf8("episodeTimer"))
        self.episodesLayout.addWidget(self.episodeTimer, 2, 0, 1, 3)
        self.tab1Layout.addWidget(self.episodes)
        self.userStatus = QtGui.QGroupBox(self.Tab1)
        self.userStatus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.userStatus.setObjectName(_fromUtf8("userStatus"))
        self.userStatusLayout = QtGui.QVBoxLayout(self.userStatus)
        self.userStatusLayout.setSpacing(0)
        self.userStatusLayout.setMargin(0)
        self.userStatusLayout.setObjectName(_fromUtf8("userStatusLayout"))
        self.stress = QtGui.QGroupBox(self.userStatus)
        self.stress.setFlat(True)
        self.stress.setObjectName(_fromUtf8("stress"))
        self.stressLayout = QtGui.QVBoxLayout(self.stress)
        self.stressLayout.setSpacing(0)
        self.stressLayout.setMargin(1)
        self.stressLayout.setObjectName(_fromUtf8("stressLayout"))
        self.stressLevel = QtGui.QProgressBar(self.stress)
        self.stressLevel.setMouseTracking(True)
        self.stressLevel.setMaximum(10)
        self.stressLevel.setProperty("value", 0)
        self.stressLevel.setObjectName(_fromUtf8("stressLevel"))
        self.stressLayout.addWidget(self.stressLevel)
        self.stressSlider = QtGui.QSlider(self.stress)
        self.stressSlider.setMaximum(10)
        self.stressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.stressSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.stressSlider.setTickInterval(1)
        self.stressSlider.setObjectName(_fromUtf8("stressSlider"))
        self.stressLayout.addWidget(self.stressSlider)
        self.userStatusLayout.addWidget(self.stress)
        self.cognitiveLoad = QtGui.QGroupBox(self.userStatus)
        self.cognitiveLoad.setFlat(True)
        self.cognitiveLoad.setObjectName(_fromUtf8("cognitiveLoad"))
        self.cognitiveLoadLayout = QtGui.QVBoxLayout(self.cognitiveLoad)
        self.cognitiveLoadLayout.setSpacing(0)
        self.cognitiveLoadLayout.setMargin(1)
        self.cognitiveLoadLayout.setObjectName(_fromUtf8("cognitiveLoadLayout"))
        self.cognitiveLoadLevel = QtGui.QProgressBar(self.cognitiveLoad)
        self.cognitiveLoadLevel.setMaximum(10)
        self.cognitiveLoadLevel.setProperty("value", 0)
        self.cognitiveLoadLevel.setObjectName(_fromUtf8("cognitiveLoadLevel"))
        self.cognitiveLoadLayout.addWidget(self.cognitiveLoadLevel)
        self.cognitiveLoadSlider = QtGui.QSlider(self.cognitiveLoad)
        self.cognitiveLoadSlider.setMaximum(10)
        self.cognitiveLoadSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cognitiveLoadSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.cognitiveLoadSlider.setTickInterval(1)
        self.cognitiveLoadSlider.setObjectName(_fromUtf8("cognitiveLoadSlider"))
        self.cognitiveLoadLayout.addWidget(self.cognitiveLoadSlider)
        self.userStatusLayout.addWidget(self.cognitiveLoad)
        self.tab1Layout.addWidget(self.userStatus)
        self.taskContext = QtGui.QGroupBox(self.Tab1)
        self.taskContext.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.taskContext.setObjectName(_fromUtf8("taskContext"))
        self.taskLayout = QtGui.QVBoxLayout(self.taskContext)
        self.taskLayout.setMargin(0)
        self.taskLayout.setObjectName(_fromUtf8("taskLayout"))
        self.currentContext = QtGui.QComboBox(self.taskContext)
        self.currentContext.setMinimumSize(QtCore.QSize(0, 44))
        self.currentContext.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.currentContext.setFrame(True)
        self.currentContext.setObjectName(_fromUtf8("currentContext"))
        self.currentContext.addItem(_fromUtf8(""))
        self.currentContext.addItem(_fromUtf8(""))
        self.currentContext.addItem(_fromUtf8(""))
        self.currentContext.addItem(_fromUtf8(""))
        self.currentContext.addItem(_fromUtf8(""))
        self.currentContext.addItem(_fromUtf8(""))
        self.taskLayout.addWidget(self.currentContext)
        self.currentWidget = QtGui.QLabel(self.taskContext)
        self.currentWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.currentWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.currentWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.currentWidget.setObjectName(_fromUtf8("currentWidget"))
        self.taskLayout.addWidget(self.currentWidget)
        self.tab1Layout.addWidget(self.taskContext)
        self.robotStatus = QtGui.QGroupBox(self.Tab1)
        self.robotStatus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.robotStatus.setObjectName(_fromUtf8("robotStatus"))
        self.AUIStatusLayout = QtGui.QVBoxLayout(self.robotStatus)
        self.AUIStatusLayout.setSpacing(0)
        self.AUIStatusLayout.setMargin(1)
        self.AUIStatusLayout.setObjectName(_fromUtf8("AUIStatusLayout"))
        self.AUIbatteryLevel = QtGui.QGroupBox(self.robotStatus)
        self.AUIbatteryLevel.setFlat(True)
        self.AUIbatteryLevel.setObjectName(_fromUtf8("AUIbatteryLevel"))
        self.AUIbatteryLayout = QtGui.QVBoxLayout(self.AUIbatteryLevel)
        self.AUIbatteryLayout.setSpacing(0)
        self.AUIbatteryLayout.setMargin(1)
        self.AUIbatteryLayout.setObjectName(_fromUtf8("AUIbatteryLayout"))
        self.AUIbattery = QtGui.QProgressBar(self.AUIbatteryLevel)
        self.AUIbattery.setMouseTracking(True)
        self.AUIbattery.setProperty("value", 100)
        self.AUIbattery.setObjectName(_fromUtf8("AUIbattery"))
        self.AUIbatteryLayout.addWidget(self.AUIbattery)
        self.batterySlider = QtGui.QSlider(self.AUIbatteryLevel)
        self.batterySlider.setMaximum(100)
        self.batterySlider.setProperty("value", 100)
        self.batterySlider.setOrientation(QtCore.Qt.Horizontal)
        self.batterySlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.batterySlider.setTickInterval(10)
        self.batterySlider.setObjectName(_fromUtf8("batterySlider"))
        self.AUIbatteryLayout.addWidget(self.batterySlider)
        self.AUIStatusLayout.addWidget(self.AUIbatteryLevel)
        self.AUIwifiLevel = QtGui.QGroupBox(self.robotStatus)
        self.AUIwifiLevel.setFlat(True)
        self.AUIwifiLevel.setObjectName(_fromUtf8("AUIwifiLevel"))
        self.AUIwifiLayout = QtGui.QVBoxLayout(self.AUIwifiLevel)
        self.AUIwifiLayout.setSpacing(0)
        self.AUIwifiLayout.setMargin(1)
        self.AUIwifiLayout.setObjectName(_fromUtf8("AUIwifiLayout"))
        self.AUIwifi = QtGui.QProgressBar(self.AUIwifiLevel)
        self.AUIwifi.setMouseTracking(True)
        self.AUIwifi.setProperty("value", 100)
        self.AUIwifi.setAlignment(QtCore.Qt.AlignCenter)
        self.AUIwifi.setTextVisible(True)
        self.AUIwifi.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.AUIwifi.setObjectName(_fromUtf8("AUIwifi"))
        self.AUIwifiLayout.addWidget(self.AUIwifi)
        self.wifiSlider = QtGui.QSlider(self.AUIwifiLevel)
        self.wifiSlider.setMaximum(100)
        self.wifiSlider.setProperty("value", 100)
        self.wifiSlider.setOrientation(QtCore.Qt.Horizontal)
        self.wifiSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.wifiSlider.setTickInterval(10)
        self.wifiSlider.setObjectName(_fromUtf8("wifiSlider"))
        self.AUIwifiLayout.addWidget(self.wifiSlider)
        self.AUIStatusLayout.addWidget(self.AUIwifiLevel)
        self.tab1Layout.addWidget(self.robotStatus)
        self.contents.addTab(self.Tab1, _fromUtf8(""))
        self.verticalLayout.addWidget(self.contents)
        AUIParameters.setWidget(self.AUIParams)

        self.retranslateUi(AUIParameters)
        self.contents.setCurrentIndex(0)
        QtCore.QObject.connect(self.stressSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.stressLevel.setValue)
        QtCore.QObject.connect(self.wifiSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.AUIwifi.setValue)
        QtCore.QObject.connect(self.batterySlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.AUIbattery.setValue)
        QtCore.QObject.connect(self.cognitiveLoadSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.cognitiveLoadLevel.setValue)
        QtCore.QMetaObject.connectSlotsByName(AUIParameters)

    def retranslateUi(self, AUIParameters):
        AUIParameters.setWindowTitle(_translate("AUIParameters", "AUI Parameters", None))
        self.episodes.setTitle(_translate("AUIParameters", "Episodes", None))
        self.startEpisodeButton.setText(_translate("AUIParameters", "Start", None))
        self.resetEpisodeButton.setText(_translate("AUIParameters", "New", None))
        self.stopEpisodeButton.setText(_translate("AUIParameters", "Stop", None))
        self.userStatus.setTitle(_translate("AUIParameters", "User Status", None))
        self.stress.setTitle(_translate("AUIParameters", "Stress Level", None))
        self.cognitiveLoad.setTitle(_translate("AUIParameters", "Cognitive Load", None))
        self.taskContext.setTitle(_translate("AUIParameters", "Task Context", None))
        self.currentContext.setItemText(0, _translate("AUIParameters", "<Select Task>", None))
        self.currentContext.setItemText(1, _translate("AUIParameters", "Forward navigation", None))
        self.currentContext.setItemText(2, _translate("AUIParameters", "Backward navigation", None))
        self.currentContext.setItemText(3, _translate("AUIParameters", "Camera inspection", None))
        self.currentContext.setItemText(4, _translate("AUIParameters", "Map review", None))
        self.currentContext.setItemText(5, _translate("AUIParameters", "New screenshot", None))
        self.currentWidget.setText(_translate("AUIParameters", "<No Widget>", None))
        self.robotStatus.setTitle(_translate("AUIParameters", "Robot status", None))
        self.AUIbatteryLevel.setTitle(_translate("AUIParameters", "Battery", None))
        self.AUIwifiLevel.setTitle(_translate("AUIParameters", "WiFi", None))
        self.contents.setTabText(self.contents.indexOf(self.Tab1), _translate("AUIParameters", "Control", None))

