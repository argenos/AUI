# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Prob.ui'
#
# Created: Fri Apr 24 22:39:22 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_ProbabilityWidget(object):
    def setupUi(self, ProbabilityWidget):
        ProbabilityWidget.setObjectName(_fromUtf8("ProbabilityWidget"))
        ProbabilityWidget.resize(250, 667)
        ProbabilityWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(ProbabilityWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.probabilityPlots = QtGui.QStackedWidget(ProbabilityWidget)
        self.probabilityPlots.setObjectName(_fromUtf8("probabilityPlots"))
        self.selectPlot = QtGui.QWidget()
        self.selectPlot.setObjectName(_fromUtf8("selectPlot"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.selectPlot)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.probPlot = QtGui.QLabel(self.selectPlot)
        self.probPlot.setMinimumSize(QtCore.QSize(150, 150))
        self.probPlot.setMaximumSize(QtCore.QSize(250, 250))
        self.probPlot.setText(_fromUtf8(""))
        self.probPlot.setScaledContents(True)
        self.probPlot.setObjectName(_fromUtf8("probPlot"))
        self.verticalLayout_2.addWidget(self.probPlot)
        self.probabilityPlots.addWidget(self.selectPlot)
        self.detectPlot = QtGui.QWidget()
        self.detectPlot.setObjectName(_fromUtf8("detectPlot"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.detectPlot)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.probPlot_2 = QtGui.QLabel(self.detectPlot)
        self.probPlot_2.setMinimumSize(QtCore.QSize(150, 150))
        self.probPlot_2.setMaximumSize(QtCore.QSize(250, 250))
        self.probPlot_2.setText(_fromUtf8(""))
        self.probPlot_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/probability/database_data/plots/prob/detect.png")))
        self.probPlot_2.setScaledContents(True)
        self.probPlot_2.setObjectName(_fromUtf8("probPlot_2"))
        self.verticalLayout_5.addWidget(self.probPlot_2)
        self.probabilityPlots.addWidget(self.detectPlot)
        self.mapPlot = QtGui.QWidget()
        self.mapPlot.setObjectName(_fromUtf8("mapPlot"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.mapPlot)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.probPlot_3 = QtGui.QLabel(self.mapPlot)
        self.probPlot_3.setMinimumSize(QtCore.QSize(150, 150))
        self.probPlot_3.setMaximumSize(QtCore.QSize(250, 250))
        self.probPlot_3.setText(_fromUtf8(""))
        self.probPlot_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/probability/database_data/plots/prob/mapping.png")))
        self.probPlot_3.setScaledContents(True)
        self.probPlot_3.setObjectName(_fromUtf8("probPlot_3"))
        self.verticalLayout_6.addWidget(self.probPlot_3)
        self.probabilityPlots.addWidget(self.mapPlot)
        self.navigatePlot = QtGui.QWidget()
        self.navigatePlot.setObjectName(_fromUtf8("navigatePlot"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.navigatePlot)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.probPlot_4 = QtGui.QLabel(self.navigatePlot)
        self.probPlot_4.setMinimumSize(QtCore.QSize(150, 150))
        self.probPlot_4.setMaximumSize(QtCore.QSize(250, 250))
        self.probPlot_4.setText(_fromUtf8(""))
        self.probPlot_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/probability/database_data/plots/prob/navigate.png")))
        self.probPlot_4.setScaledContents(True)
        self.probPlot_4.setObjectName(_fromUtf8("probPlot_4"))
        self.verticalLayout_4.addWidget(self.probPlot_4)
        self.probabilityPlots.addWidget(self.navigatePlot)
        self.reviewPlot = QtGui.QWidget()
        self.reviewPlot.setObjectName(_fromUtf8("reviewPlot"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.reviewPlot)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.probPlot_5 = QtGui.QLabel(self.reviewPlot)
        self.probPlot_5.setMinimumSize(QtCore.QSize(150, 150))
        self.probPlot_5.setMaximumSize(QtCore.QSize(250, 250))
        self.probPlot_5.setText(_fromUtf8(""))
        self.probPlot_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/probability/database_data/plots/prob/review.png")))
        self.probPlot_5.setScaledContents(True)
        self.probPlot_5.setObjectName(_fromUtf8("probPlot_5"))
        self.verticalLayout_7.addWidget(self.probPlot_5)
        self.probabilityPlots.addWidget(self.reviewPlot)
        self.inspectPlot = QtGui.QWidget()
        self.inspectPlot.setObjectName(_fromUtf8("inspectPlot"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.inspectPlot)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.probPlot_6 = QtGui.QLabel(self.inspectPlot)
        self.probPlot_6.setMinimumSize(QtCore.QSize(150, 150))
        self.probPlot_6.setMaximumSize(QtCore.QSize(250, 250))
        self.probPlot_6.setText(_fromUtf8(""))
        self.probPlot_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/probability/database_data/plots/prob/inspect.png")))
        self.probPlot_6.setScaledContents(True)
        self.probPlot_6.setObjectName(_fromUtf8("probPlot_6"))
        self.verticalLayout_8.addWidget(self.probPlot_6)
        self.probabilityPlots.addWidget(self.inspectPlot)
        self.explorePlot = QtGui.QWidget()
        self.explorePlot.setObjectName(_fromUtf8("explorePlot"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.explorePlot)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.probPlot_7 = QtGui.QLabel(self.explorePlot)
        self.probPlot_7.setMinimumSize(QtCore.QSize(150, 150))
        self.probPlot_7.setMaximumSize(QtCore.QSize(250, 250))
        self.probPlot_7.setText(_fromUtf8(""))
        self.probPlot_7.setPixmap(QtGui.QPixmap(_fromUtf8(":/probability/database_data/plots/prob/explore.png")))
        self.probPlot_7.setScaledContents(True)
        self.probPlot_7.setObjectName(_fromUtf8("probPlot_7"))
        self.verticalLayout_9.addWidget(self.probPlot_7)
        self.probabilityPlots.addWidget(self.explorePlot)
        self.verticalLayout.addWidget(self.probabilityPlots)
        self.goalLabel = QtGui.QLabel(ProbabilityWidget)
        self.goalLabel.setObjectName(_fromUtf8("goalLabel"))
        self.verticalLayout.addWidget(self.goalLabel)
        self.goalList = QtGui.QComboBox(ProbabilityWidget)
        self.goalList.setObjectName(_fromUtf8("goalList"))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.goalList)
        self.groupBox_2 = QtGui.QGroupBox(ProbabilityWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setMargin(4)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 7, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 5, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 6, 0, 1, 1)
        self.horizontalSlider_12 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_12.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_12.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_12.setTickInterval(10)
        self.horizontalSlider_12.setObjectName(_fromUtf8("horizontalSlider_12"))
        self.gridLayout_2.addWidget(self.horizontalSlider_12, 2, 1, 1, 1)
        self.horizontalSlider_14 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_14.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_14.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_14.setTickInterval(10)
        self.horizontalSlider_14.setObjectName(_fromUtf8("horizontalSlider_14"))
        self.gridLayout_2.addWidget(self.horizontalSlider_14, 4, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.horizontalSlider_18 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_18.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_18.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_18.setTickInterval(10)
        self.horizontalSlider_18.setObjectName(_fromUtf8("horizontalSlider_18"))
        self.gridLayout_2.addWidget(self.horizontalSlider_18, 8, 1, 1, 1)
        self.horizontalSlider_17 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_17.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_17.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_17.setTickInterval(10)
        self.horizontalSlider_17.setObjectName(_fromUtf8("horizontalSlider_17"))
        self.gridLayout_2.addWidget(self.horizontalSlider_17, 7, 1, 1, 1)
        self.horizontalSlider_16 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_16.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_16.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_16.setTickInterval(10)
        self.horizontalSlider_16.setObjectName(_fromUtf8("horizontalSlider_16"))
        self.gridLayout_2.addWidget(self.horizontalSlider_16, 6, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 8, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)
        self.horizontalSlider_15 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_15.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_15.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_15.setTickInterval(10)
        self.horizontalSlider_15.setObjectName(_fromUtf8("horizontalSlider_15"))
        self.gridLayout_2.addWidget(self.horizontalSlider_15, 5, 1, 1, 1)
        self.horizontalSlider_10 = QtGui.QSlider(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalSlider_10.setFont(font)
        self.horizontalSlider_10.setMaximum(100)
        self.horizontalSlider_10.setSingleStep(1)
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_10.setTickInterval(10)
        self.horizontalSlider_10.setObjectName(_fromUtf8("horizontalSlider_10"))
        self.gridLayout_2.addWidget(self.horizontalSlider_10, 0, 1, 1, 1)
        self.horizontalSlider_11 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_11.setTickInterval(10)
        self.horizontalSlider_11.setObjectName(_fromUtf8("horizontalSlider_11"))
        self.gridLayout_2.addWidget(self.horizontalSlider_11, 1, 1, 1, 1)
        self.horizontalSlider_13 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_13.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_13.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_13.setTickInterval(10)
        self.horizontalSlider_13.setObjectName(_fromUtf8("horizontalSlider_13"))
        self.gridLayout_2.addWidget(self.horizontalSlider_13, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.updateLayout = QtGui.QHBoxLayout()
        self.updateLayout.setSpacing(0)
        self.updateLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.updateLayout.setObjectName(_fromUtf8("updateLayout"))
        spacerItem = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.updateLayout.addItem(spacerItem)
        self.updateButton = QtGui.QPushButton(ProbabilityWidget)
        self.updateButton.setMinimumSize(QtCore.QSize(0, 32))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.updateLayout.addWidget(self.updateButton)
        self.verticalLayout.addLayout(self.updateLayout)
        self.probPlot.setBuddy(self.updateButton)
        self.probPlot_2.setBuddy(self.updateButton)
        self.probPlot_3.setBuddy(self.updateButton)
        self.probPlot_4.setBuddy(self.updateButton)
        self.probPlot_5.setBuddy(self.updateButton)
        self.probPlot_6.setBuddy(self.updateButton)
        self.probPlot_7.setBuddy(self.updateButton)
        self.goalLabel.setBuddy(self.goalList)

        self.retranslateUi(ProbabilityWidget)
        self.probabilityPlots.setCurrentIndex(1)
        QtCore.QObject.connect(self.goalList, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.probabilityPlots.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(ProbabilityWidget)

    def retranslateUi(self, ProbabilityWidget):
        ProbabilityWidget.setWindowTitle(_translate("ProbabilityWidget", "Form", None))
        self.goalLabel.setText(_translate("ProbabilityWidget", "Goal:", None))
        self.goalList.setItemText(0, _translate("ProbabilityWidget", "<Select>", None))
        self.goalList.setItemText(1, _translate("ProbabilityWidget", "Detect", None))
        self.goalList.setItemText(2, _translate("ProbabilityWidget", "Map", None))
        self.goalList.setItemText(3, _translate("ProbabilityWidget", "Navigate", None))
        self.goalList.setItemText(4, _translate("ProbabilityWidget", "Review status", None))
        self.goalList.setItemText(5, _translate("ProbabilityWidget", "Inspect current site", None))
        self.goalList.setItemText(6, _translate("ProbabilityWidget", "Explore", None))
        self.groupBox_2.setTitle(_translate("ProbabilityWidget", "Probabilities", None))
        self.label_17.setText(_translate("ProbabilityWidget", "On Main View", None))
        self.label_12.setText(_translate("ProbabilityWidget", "On Main Screenshot", None))
        self.label_15.setText(_translate("ProbabilityWidget", "C2 Clicked", None))
        self.label_16.setText(_translate("ProbabilityWidget", "Extra Clicked", None))
        self.label_11.setText(_translate("ProbabilityWidget", "On C2", None))
        self.label_14.setText(_translate("ProbabilityWidget", "C1 Clicked", None))
        self.label_10.setText(_translate("ProbabilityWidget", "On C1", None))
        self.label_18.setText(_translate("ProbabilityWidget", "On Add View", None))
        self.label_13.setText(_translate("ProbabilityWidget", "On Extra Screenshot", None))
        self.updateButton.setText(_translate("ProbabilityWidget", "Update", None))

