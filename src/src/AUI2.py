# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 02:57:21 2014

@author: Argentina Ortega Sáinz
@version: 0.0.2
"""
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QFrame, 
                         QHBoxLayout, QVBoxLayout, 
                         QSizePolicy, QLabel)
                         
import Camera
import MixedInitiative
import NewView
import Map
import Pointcloud
import Screenshot
import Wifi
import Battery
import Joystick
import Parameters

'''
Adaptive User Interface for TRADR project
'''
class AUI(QWidget):    
    def __init__(self,parent=None):
        super(AUI, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0, 0 , 1280, 800)
        self.setWindowTitle("Adaptive TRADR OCU")
        
        '''        
        Layout Definitions for the complete AUI
        '''
        
        #Global Layout for AUI Parameters + TRADR GUI
        self.globalLayout = QHBoxLayout()
        self.setLayout(self.globalLayout)

        self.MainLayout = QVBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.globalLayout.addLayout(self.MainLayout)
        
        self.GUILayout = QHBoxLayout()
        self.GUILayout.setObjectName("GUILayout")
        
        self.ViewsLayout = QVBoxLayout()
        self.ViewsLayout.setObjectName("ViewsLayout")        
                
        
        self.ScreenshotLayout = QVBoxLayout()
        self.ScreenshotLayout.setObjectName("ScreenshotLayout")
        
        self.StatusLayout = QVBoxLayout()
        self.StatusLayout.setObjectName("StatusLayout")
        
        '''
        Widgets
        '''
        #self.horizontalLayout_4 = QtGui.QHBoxLayout(self)
        #self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.mixedInitiative = MixedInitiative.MixedInitiative(self)
        self.MainLayout.addWidget(self.mixedInitiative)
        
        self.MainLayout.addLayout(self.GUILayout)
        self.views = QtGui.QGroupBox("Available Views",self)
        self.views.setMinimumSize(QtCore.QSize(550, 70))
        self.views.setMaximumSize(QtCore.QSize(5000, 150))
        self.views.setObjectName("views")
        self.viewsGroupLayout = QtGui.QHBoxLayout(self.views)
        self.viewsGroupLayout.setObjectName("viewsGroupLayout")
        
        minSize = QtCore.QSize(50, 50)
        maxSize = QtCore.QSize(70, 70)
        stretch = 0
        self.pointcloud = Pointcloud.Pointcloud(self,minSize,maxSize,stretch)
        self.viewsGroupLayout.addWidget(self.pointcloud)

        minSize = QtCore.QSize(50, 50)
        maxSize = QtCore.QSize(70, 70)
        stretch = 0
        self.map = Map.Map(self,minSize,maxSize,stretch)
        self.viewsGroupLayout.addWidget(self.map)

        minSize = QtCore.QSize(50, 50)
        maxSize = QtCore.QSize(70, 70)
        stretch = 0         
        self.extra = NewView.NewView(self,minSize,maxSize,stretch)        
        self.viewsGroupLayout.addWidget(self.extra)
        self.ViewsLayout.addWidget(self.views)
        
        
        self.MainViews = QtGui.QGridLayout()
        self.MainViews.setObjectName("MainViews")

        
        minSize = QtCore.QSize(100, 100)
        maxSize = QtCore.QSize(300, 300)
        stretch = 3        
        self.Camera1 = Camera.Camera(self,1,minSize,maxSize,stretch)        
        self.MainViews.addWidget(self.Camera1,1,2)
        
        
        minSize = QtCore.QSize(100, 100)
        maxSize = QtCore.QSize(200, 200)
        stretch = 1 
        self.Camera2 = Camera.Camera(self,2,minSize,maxSize,stretch)
        self.MainViews.addWidget(self.Camera2, 0, 0)
        
        self.ViewsLayout.addLayout(self.MainViews)
        self.GUILayout.addLayout(self.ViewsLayout)
        
        minSize = QtCore.QSize(150, 150)
        maxSize = QtCore.QSize(200, 200)
        stretch = 1
        self.CurrentScreenshot = Screenshot.Screenshots(self,250,300,stretch)
        
        
        self.GUILayout.addWidget(self.CurrentScreenshot)
        
        minSize = QtCore.QSize(80, 80)
        maxSize = QtCore.QSize(120, 120)
        
        self.battery = Battery.Battery(self, minSize, maxSize)
        self.wifi = Wifi.Wifi(self, minSize, maxSize)
        
        minSize = QtCore.QSize(80, 80)
        maxSize = QtCore.QSize(120, 120)
        self.joystick = Joystick.Joystick(self, minSize, maxSize)
        
        self.StatusLayout.addWidget(self.battery)
        self.StatusLayout.addWidget(self.wifi)
        self.StatusLayout.addStretch()        
        self.StatusLayout.addWidget(self.joystick)
        
        self.GUILayout.addLayout(self.StatusLayout)
        
        self.parameters = Parameters.AUIParameters(self)
        self.globalLayout.addWidget(self.parameters)
        
        '''
        QtCore.QObject.connect(self.battery_slider, QtCore.SIGNAL("valueChanged(int)"), self.battery.setValue)
        QtCore.QObject.connect(self.wifi_slider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.setValue)
        QtCore.QObject.connect(self.battery_slider, QtCore.SIGNAL("valueChanged(int)"), self.battery_level.setValue)
        QtCore.QObject.connect(self.wifi_slider, QtCore.SIGNAL("valueChanged(int)"), self.wifi_level.setValue)
        QtCore.QObject.connect(self.stress_slider, QtCore.SIGNAL("valueChanged(int)"), self.stress_level.setValue)
        QtCore.QMetaObject.connectSlotsByName(self)            
        '''
        self.show()
        
   
        
def main():
    app = QtGui.QApplication(sys.argv)
    main = AUI()
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
