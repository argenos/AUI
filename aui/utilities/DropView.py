from PyQt4.QtCore import pyqtSignal

__author__ = 'Argen'

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import (QFrame, QLabel)

from aui.gui.views.sources import camera


class DView(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")

    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin informacion
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Establecer el widget en una nueva posicion
        pos = event.pos()
        self.wid = event.source()
        self.wid.setParent(self)
        self.layout().addWidget(self.wid)
        event.acceptProposedAction()

        if self.parent().objectName() == 'currentViews':
            print 'Current views'
            minSize = QtCore.QSize(100, 100)
            maxSize = QtCore.QSize(16777215, 16777215)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(16777215, 16777215)
        elif self.parent().objectName() == 'viewsGroup':
            print 'Available views'
            minSize = QtCore.QSize(50, 50)
            maxSize = QtCore.QSize(70, 70)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(70, 70)

        self.wid.show()

        print self.objectName()
        print self.children()


class DCurrentView(QFrame):
    viewnames = ['trightLabel', 'tleftLabel', 'bleftLabel', 'brightLabel']
    widgetnames = ['']
    content = pyqtSignal(str, str, name='MV')

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.pos()
        self.wid = event.source()
        avViews = self.wid.parent()
        self.wid.setParent(self)
        self.layout().addWidget(self.wid)
        event.acceptProposedAction()

        # children = self.findChildren(camera.Camera)
        # if children != 0:
        #    print 'DCurrentView!'
        #    for child in children:
        #        avViews.layout().addWidget(child)

        children = self.findChildren(Marker)
        for child in children:
            #if child.objectName() in self.viewnames:
            child.setVisible(False)

        # if self.parent().objectName() == 'currentViews':
        minSize = QtCore.QSize(100, 100)
        maxSize = QtCore.QSize(16777215, 16777215)
        self.wid.setMaximumSize(maxSize)
        self.wid.setMinimumSize(minSize)
        self.wid.resize(16777215, 16777215)

        self.wid.show()

        #print 'Drop Current View', self.wid.objectName()
        self.content.emit(self.wid.objectName(), 'MV')

    def dragLeaveEvent(self, event):
        marker = self.findChildren(Marker)
        children = self.children()
        if len(children) == 3:
            for mark in marker:
                mark.setVisible(True)
        #for child in children:
        #    #if child.objectName() in self.viewnames:
        #    child.setVisible(True)


        # for child in children:
        #    if child.objectName() in self.viewnames:
        #        child.setVisible(True)
        #        event.source.setVisible(False)


class Marker(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)


class DAvailableView(QFrame):
    viewnames = ['trightLabel', 'tleftLabel', 'bleftLabel', 'brightLabel']
    av_wid = pyqtSignal(str, str, name='AV')

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.pos()
        self.wid = event.source()
        prevView = self.wid.parent()
        # self.layout().addWidget(self.wid)
        # event.acceptProposedAction()


        # children = prevView.findChildren(QtGui.QLabel)
        # for child in children:
        #    if child.objectName() in self.viewnames:
        #        child.setVisible(True)

        self.wid.setParent(self)
        self.layout().addWidget(self.wid)
        event.acceptProposedAction()
        # print event.source()

        # if self.parent().objectName() == 'viewsGroup':
        minSize = QtCore.QSize(50, 50)
        maxSize = QtCore.QSize(70, 70)
        self.wid.setMaximumSize(maxSize)
        self.wid.setMinimumSize(minSize)
        self.wid.resize(70, 70)

        self.wid.show()
        #print 'Drop Available View', self.wid.objectName()
        self.av_wid.emit(self.wid.objectName(), 'AV')

    def dragLeaveEvent(self, event):
        pass
        #children = self.findChildren(Marker)
        #children = self.children()
        #print 'Leaving AV views', children
        # for child in children:
        #    if child.objectName() in self.viewnames:
        #        child.setVisible(True)
        #        event.source.setVisible(False)