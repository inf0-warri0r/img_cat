# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sat May 18 23:17:06 2013
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

"""
Author : tharindra galahena (inf0_warri0r)
Project: image categorizetion using SOM
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


class Ui_testing_window(object):
    def setupUi(self, testing_window):
        testing_window.setObjectName("testing_window")
        testing_window.resize(800, 528)
        self.centralwidget = QtGui.QWidget(testing_window)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 430, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 470, 361, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 430, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 470, 101, 31))
        self.label_2.setObjectName("label_2")
        self.open_b = QtGui.QPushButton(self.centralwidget)
        self.open_b.setGeometry(QtCore.QRect(500, 430, 105, 31))
        self.open_b.setObjectName("open_b")
        self.open_f = QtGui.QPushButton(self.centralwidget)
        self.open_f.setGeometry(QtCore.QRect(500, 470, 105, 31))
        self.open_f.setObjectName("open_f")
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(610, 430, 171, 71))
        self.start.setObjectName("start")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(13, 13, 771, 401))
        self.textEdit.setObjectName("textEdit")
        testing_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(testing_window)
        self.statusbar.setObjectName("statusbar")
        testing_window.setStatusBar(self.statusbar)

        self.retranslateUi(testing_window)
        QtCore.QMetaObject.connectSlotsByName(testing_window)

    def retranslateUi(self, testing_window):
        testing_window.setWindowTitle(QtGui.QApplication.translate("testing_window", "Tester", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("testing_window", "beach data set", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("testing_window", "forest data set", None, QtGui.QApplication.UnicodeUTF8))
        self.open_b.setText(QtGui.QApplication.translate("testing_window", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.open_f.setText(QtGui.QApplication.translate("testing_window", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.start.setText(QtGui.QApplication.translate("testing_window", "start", None, QtGui.QApplication.UnicodeUTF8))

