__author__ = 'Argen'

import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget

from aui.gui.status import ui_statusbar


class StatusBar(QWidget, ui_statusbar.Ui_statusBarWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)
    main = StatusBar(None)
    # main.example()
    main.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()