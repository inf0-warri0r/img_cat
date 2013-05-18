# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train.ui'
#
# Created: Sat May 18 23:17:17 2013
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


class Ui_trainer_window(object):
    def setupUi(self, trainer_window):
        trainer_window.setObjectName("trainer_window")
        trainer_window.resize(495, 634)
        self.centralwidget = QtGui.QWidget(trainer_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.fb = QtGui.QLineEdit(self.centralwidget)
        self.fb.setGeometry(QtCore.QRect(120, 22, 271, 31))
        self.fb.setObjectName("fb")
        self.ff = QtGui.QLineEdit(self.centralwidget)
        self.ff.setGeometry(QtCore.QRect(120, 70, 271, 31))
        self.ff.setObjectName("ff")
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(10, 120, 471, 27))
        self.start.setObjectName("start")
        self.b_open = QtGui.QPushButton(self.centralwidget)
        self.b_open.setGeometry(QtCore.QRect(400, 20, 81, 31))
        self.b_open.setObjectName("b_open")
        self.f_open = QtGui.QPushButton(self.centralwidget)
        self.f_open.setGeometry(QtCore.QRect(400, 70, 81, 31))
        self.f_open.setObjectName("f_open")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 160, 471, 421))
        self.textEdit.setObjectName("textEdit")
        trainer_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(trainer_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 29))
        self.menubar.setObjectName("menubar")
        trainer_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(trainer_window)
        self.statusbar.setObjectName("statusbar")
        trainer_window.setStatusBar(self.statusbar)

        self.retranslateUi(trainer_window)
        QtCore.QMetaObject.connectSlotsByName(trainer_window)

    def retranslateUi(self, trainer_window):
        trainer_window.setWindowTitle(QtGui.QApplication.translate("trainer_window", "Trainer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("trainer_window", "beach folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("trainer_window", "forest folder", None, QtGui.QApplication.UnicodeUTF8))
        self.start.setText(QtGui.QApplication.translate("trainer_window", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.b_open.setText(QtGui.QApplication.translate("trainer_window", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.f_open.setText(QtGui.QApplication.translate("trainer_window", "open", None, QtGui.QApplication.UnicodeUTF8))

