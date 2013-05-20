#!/usr/bin/env python

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

from PySide import QtGui
from categorize import Ui_categorizer_window
import sys
import weights
from PIL import Image
import som


class MyWidget(QtGui.QMainWindow, Ui_categorizer_window):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)
        self.d = weights.data("weights")
        self.ow, self.oh, self.inpm, self.inpn, self.w, self.m = self.d.load()
        if self.ow == -1:
            QtGui.QMessageBox.about(self, "ERROR", "error in weights file")
            exit(0)

        self.s = som.som(self.ow * self.oh * 3, self.inpm + self.inpn, 0.01)
        self.s.init()
        self.s.put_weights(self.w, self.m)
        self.file = ""
        self.pushButton_2.clicked.connect(self.open)
        self.pushButton.clicked.connect(self.open_file)
        self.label.setScaledContents(True)

    def open_file(self):
        self.file = QtGui.QFileDialog.getOpenFileName(self, 'Open File')[0]
        self.lineEdit.setText(self.file)
        qimage = QtGui.QImage(self.file)
        pix = QtGui.QPixmap.fromImage(qimage)
        self.label.setPixmap(pix)

    def open(self):
        if self.file == "":
            return 0
        img1 = Image.open(self.file)
        ls = list()

        p = img1.load()
        for y in range(0, self.oh):
            for x in range(0, self.ow):
                sm = float(p[x, y][0]) + float(p[x, y][1]) + float(p[x, y][2])
                if sm == 0.0:
                    sm = 1
                ls.append(float(p[x, y][0]) / sm)
                ls.append(float(p[x, y][1]) / sm)
                ls.append(float(p[x, y][2]) / sm)
        ct = int(self.s.find(ls))
        if ct < self.inpm:
            cat = "forest"
        else:
            cat = "beach"
        QtGui.QMessageBox.about(self, "Category", "Category = " + cat)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
