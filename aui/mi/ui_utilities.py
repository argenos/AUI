# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/utilities.ui'
#
# Created: Mon Jun 29 20:31:27 2015
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

class Ui_utilities(object):
    def setupUi(self, utilities):
        utilities.setObjectName(_fromUtf8("utilities"))
        utilities.resize(287, 484)
        self.utilitiesLayout = QtGui.QVBoxLayout(utilities)
        self.utilitiesLayout.setObjectName(_fromUtf8("utilitiesLayout"))
        self.utilityPlot = QtGui.QLabel(utilities)
        self.utilityPlot.setMinimumSize(QtCore.QSize(0, 70))
        self.utilityPlot.setMaximumSize(QtCore.QSize(300, 16777215))
        self.utilityPlot.setText(_fromUtf8(""))
        self.utilityPlot.setScaledContents(True)
        self.utilityPlot.setObjectName(_fromUtf8("utilityPlot"))
        self.utilitiesLayout.addWidget(self.utilityPlot)
        self.goalLabel = QtGui.QLabel(utilities)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.goalLabel.setFont(font)
        self.goalLabel.setObjectName(_fromUtf8("goalLabel"))
        self.utilitiesLayout.addWidget(self.goalLabel)
        self.goalList = QtGui.QComboBox(utilities)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.goalList.setFont(font)
        self.goalList.setObjectName(_fromUtf8("goalList"))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.utilitiesLayout.addWidget(self.goalList)
        self.tables = QtGui.QStackedWidget(utilities)
        self.tables.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tables.setObjectName(_fromUtf8("tables"))
        self.select = QtGui.QWidget()
        self.select.setObjectName(_fromUtf8("select"))
        self.verticalLayout = QtGui.QVBoxLayout(self.select)
        self.verticalLayout.setMargin(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tables.addWidget(self.select)
        self.detect = QtGui.QWidget()
        self.detect.setObjectName(_fromUtf8("detect"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.detect)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.detectTable = QtGui.QTableView(self.detect)
        self.detectTable.setObjectName(_fromUtf8("detectTable"))
        self.verticalLayout_2.addWidget(self.detectTable)
        self.tables.addWidget(self.detect)
        self.mapping = QtGui.QWidget()
        self.mapping.setObjectName(_fromUtf8("mapping"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.mapping)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.mappingTable = QtGui.QTableView(self.mapping)
        self.mappingTable.setObjectName(_fromUtf8("mappingTable"))
        self.verticalLayout_3.addWidget(self.mappingTable)
        self.tables.addWidget(self.mapping)
        self.navigate = QtGui.QWidget()
        self.navigate.setObjectName(_fromUtf8("navigate"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.navigate)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.navigateTable = QtGui.QTableView(self.navigate)
        self.navigateTable.setObjectName(_fromUtf8("navigateTable"))
        self.verticalLayout_4.addWidget(self.navigateTable)
        self.tables.addWidget(self.navigate)
        self.review = QtGui.QWidget()
        self.review.setObjectName(_fromUtf8("review"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.review)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.reviewTable = QtGui.QTableView(self.review)
        self.reviewTable.setObjectName(_fromUtf8("reviewTable"))
        self.verticalLayout_5.addWidget(self.reviewTable)
        self.tables.addWidget(self.review)
        self.inspect = QtGui.QWidget()
        self.inspect.setObjectName(_fromUtf8("inspect"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.inspect)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.inspectTable = QtGui.QTableView(self.inspect)
        self.inspectTable.setObjectName(_fromUtf8("inspectTable"))
        self.verticalLayout_6.addWidget(self.inspectTable)
        self.tables.addWidget(self.inspect)
        self.explore = QtGui.QWidget()
        self.explore.setObjectName(_fromUtf8("explore"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.explore)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.exploreTable = QtGui.QTableView(self.explore)
        self.exploreTable.setObjectName(_fromUtf8("exploreTable"))
        self.verticalLayout_7.addWidget(self.exploreTable)
        self.tables.addWidget(self.explore)
        self.utilitiesLayout.addWidget(self.tables)
        self.updateLayout = QtGui.QHBoxLayout()
        self.updateLayout.setSpacing(0)
        self.updateLayout.setMargin(1)
        self.updateLayout.setObjectName(_fromUtf8("updateLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.updateLayout.addItem(spacerItem)
        self.saveButton = QtGui.QPushButton(utilities)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 32))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.updateLayout.addWidget(self.saveButton)
        spacerItem1 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.updateLayout.addItem(spacerItem1)
        self.updateButton = QtGui.QPushButton(utilities)
        self.updateButton.setMinimumSize(QtCore.QSize(0, 32))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.updateLayout.addWidget(self.updateButton)
        self.utilitiesLayout.addLayout(self.updateLayout)
        self.utilityPlot.setBuddy(self.updateButton)
        self.goalLabel.setBuddy(self.goalList)

        self.retranslateUi(utilities)
        self.tables.setCurrentIndex(6)
        QtCore.QObject.connect(self.updateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.utilityPlot.update)
        QtCore.QObject.connect(self.goalList, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.tables.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(utilities)
        utilities.setTabOrder(self.goalList, self.updateButton)

    def retranslateUi(self, utilities):
        utilities.setWindowTitle(_translate("utilities", "Form", None))
        self.goalLabel.setText(_translate("utilities", "Goal:", None))
        self.goalList.setItemText(0, _translate("utilities", "<Select>", None))
        self.goalList.setItemText(1, _translate("utilities", "Detect", None))
        self.goalList.setItemText(2, _translate("utilities", "Map", None))
        self.goalList.setItemText(3, _translate("utilities", "Navigate", None))
        self.goalList.setItemText(4, _translate("utilities", "Review status", None))
        self.goalList.setItemText(5, _translate("utilities", "Inspect current site", None))
        self.goalList.setItemText(6, _translate("utilities", "Explore", None))
        self.saveButton.setText(_translate("utilities", "Save", None))
        self.updateButton.setText(_translate("utilities", "Update", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    utilities = QtGui.QWidget()
    ui = Ui_utilities()
    ui.setupUi(utilities)
    utilities.show()
    sys.exit(app.exec_())

