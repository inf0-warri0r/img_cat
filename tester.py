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

from PySide import QtGui, QtCore
from test import Ui_testing_window
import sys
import som4
import weights
import image
import time
import thread


class MyWidget(QtGui.QMainWindow, Ui_testing_window):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)
        self.beach_dir = ""
        self.forest_dir = ""
        self.d = weights.data("weights")
        self.ow, self.oh, self.inpm, self.inpn, self.w, self.m = self.d.load()
        if self.ow == -1:
            QtGui.QMessageBox.about(self, "ERROR", "error in weights file")
            exit(0)
        self.s = som4.som(self.ow * self.oh * 3, self.inpm + self.inpn, 0.01)
        self.s.init()
        print self.ow * self.oh * 3 * (self.inpm + self.inpn), " ", len(self.m)
        self.s.put_weights(self.w, self.m)
        self.img1 = image.image(self.ow, self.oh)
        self.img2 = image.image(self.ow, self.oh)
        self.text = ""
        self.f_dir = ""
        self.b_dir = ""
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.re_write)
        self.timer.start()
        self.start.clicked.connect(self.start_func)
        self.open_b.clicked.connect(self.open_b_dir)
        self.open_f.clicked.connect(self.open_f_dir)
        self.run = False

    def start_func(self):
        self.b_dir = self.lineEdit.text()
        self.f_dir = self.lineEdit_2.text()
        if self.b_dir == "" or self.f_dir == "":
            QtGui.QMessageBox.about(self, "ERROR",
                    "choose test data folders for beach and forest")
            return 0
        thread.start_new_thread(self.thread_func, ())

    def open_b_dir(self):
        text = QtGui.QFileDialog.getExistingDirectory(self, "beach")
        self.lineEdit.setText(text)

    def open_f_dir(self):
        text = QtGui.QFileDialog.getExistingDirectory(self, "forest")
        self.lineEdit_2.setText(text)

    def re_write(self):
        if self.run:
            self.textEdit.setText(self.text)
            v = self.textEdit.verticalScrollBar().maximum()
            self.textEdit.verticalScrollBar().setValue(v)

    def thread_func(self):
        self.run = True
        self.text = ""
        self.text = "Loading Images ..."
        self.nb = self.img1.get_all_images(self.b_dir)
        self.nf = self.img2.get_all_images(self.f_dir)
        self.text = self.text + "   done !!!\n"
        self.text = self.text + "\ncategory - beach"
        self.text = self.text + "\n------------------\n"
        miss1 = 0
        for i in range(0, self.nb):

            dataset = self.img1.get_data_set(i)
            name = self.img1.get_name(i)
            ct = int(self.s.find(dataset))

            if ct < 9:
                cat = "forest"
                miss1 = miss1 + 1
            else:
                cat = "beach"

            self.text = self.text + "image " + name[0] + " = "
            self.text = self.text + str(cat) + "\n"

        self.text = self.text + "\nnumber of errors = " + str(miss1)
        self.text = self.text + " total = " + str(self.nb) + "\n"

        self.text = self.text + "\ncategory - forest"
        self.text = self.text + "\n------------------\n"
        miss2 = 0
        for i in range(0, self.nf):

            dataset = self.img2.get_data_set(i)
            name = self.img2.get_name(i)
            ct = int(self.s.find(dataset))

            if ct < 9:
                cat = "forest"
            else:
                cat = "beach"
                miss2 = miss2 + 1

            self.text = self.text + "image " + name[0] + " = "
            self.text = self.text + str(cat) + "\n"

        self.text = self.text + "\nnumber of errors = " + str(miss2)
        self.text = self.text + " total = " + str(self.nf) + "\n"

        miss = miss1 + miss2
        total = self.nb + self.nf

        self.text = self.text + "\ntotal error = "
        self.text = self.text + str(float(miss) / float(total))
        self.text = self.text + "\n\n -----TESTING COMPLEATED----\n\n"

        time.sleep(1)
        self.run = False

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
