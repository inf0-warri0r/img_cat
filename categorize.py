# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat May 18 23:05:57 2013
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

"""
Author : tharindra galahena (inf0_warri0r)
Project: image categarizetion using SOM
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 14/05/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""

from PySide import QtCore, QtGui


class Ui_categorizer_window(object):
    def setupUi(self, catagorizer_window):
        catagorizer_window.setObjectName("catagorizer_window")
        catagorizer_window.resize(801, 610)
        self.centralwidget = QtGui.QWidget(catagorizer_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 10, 105, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 10, 105, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 421, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 761, 501))
        self.label.setText("")
        self.label.setObjectName("label")
        catagorizer_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(catagorizer_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 29))
        self.menubar.setObjectName("menubar")
        catagorizer_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(catagorizer_window)
        self.statusbar.setObjectName("statusbar")
        catagorizer_window.setStatusBar(self.statusbar)

        self.retranslateUi(catagorizer_window)
        QtCore.QMetaObject.connectSlotsByName(catagorizer_window)

    def retranslateUi(self, catagorizer_window):
        catagorizer_window.setWindowTitle(QtGui.QApplication.translate("catagorizer_window", "Catagorizer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("catagorizer_window", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("catagorizer_window", "find", None, QtGui.QApplication.UnicodeUTF8))

