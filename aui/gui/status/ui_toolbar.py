# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/toolbar.ui'
#
# Created: Mon Aug 31 02:35:04 2015
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

class Ui_toolbarWidget(object):
    def setupUi(self, toolbarWidget):
        toolbarWidget.setObjectName(_fromUtf8("toolbarWidget"))
        toolbarWidget.resize(717, 63)

        self.retranslateUi(toolbarWidget)
        QtCore.QMetaObject.connectSlotsByName(toolbarWidget)

    def retranslateUi(self, toolbarWidget):
        toolbarWidget.setWindowTitle(_translate("toolbarWidget", "Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    toolbarWidget = QtGui.QWidget()
    ui = Ui_toolbarWidget()
    ui.setupUi(toolbarWidget)
    toolbarWidget.show()
    sys.exit(app.exec_())

