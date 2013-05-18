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
from train import Ui_trainer_window
import som4
import weights
import image
import time
import thread
import sys


class MyWidget(QtGui.QMainWindow, Ui_trainer_window):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)
        self.ow = 80
        self.oh = 60
        self.d = weights.data("weights")
        self.img = image.image(self.ow, self.oh)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.re_write)
        self.timer.start()
        self.start.clicked.connect(self.start_func)
        self.b_open.clicked.connect(self.open_b)
        self.f_open.clicked.connect(self.open_f)
        self.run = False

    def open_b(self):
        text = QtGui.QFileDialog.getExistingDirectory(self, "beach")
        self.fb.setText(text)

    def open_f(self):
        text = QtGui.QFileDialog.getExistingDirectory(self, "forest")
        self.ff.setText(text)

    def start_func(self):
        self.b_dir = self.fb.text()
        self.f_dir = self.ff.text()
        if self.b_dir == "" or self.f_dir == "":
            QtGui.QMessageBox.about(self, "ERROR",
                    "choose test data folders for beach and forest")
            return 0
        thread.start_new_thread(self.thread_func, ())

    def open_b_dir(self):
        print "aa"
        text = QtGui.QFileDialog.getExistingDirectory(self, "beach")
        self.cb.setText(text)

    def open_f_dir(self):
        text = QtGui.QFileDialog.getExistingDirectory(self, "forest")
        self.cf.setText(text)

    def re_write(self):
        if self.run:
            self.textEdit.setText(self.text)
            v = self.textEdit.verticalScrollBar().maximum()
            self.textEdit.verticalScrollBar().setValue(v)

    def thread_func(self):
        self.run = True
        self.text = ""
        self.text = "Loading Images ..."
        self.num_cls_f = self.img.get_all_images(self.f_dir)
        self.num_cls_b = self.img.get_all_images(self.b_dir) - self.num_cls_f
        self.text = "Loading Images ...Done !!!\n\n"
        if self.num_cls_f + self.num_cls_b <= 1:
            self.text = "Error - no enough images\n"
            return 0
        self.s = som4.som(self.ow * self.oh * 3,
                        self.num_cls_f + self.num_cls_b, 0.01)
        self.s.init()

        self.text = self.text + "total number of class : "
        self.text = self.text + str(self.num_cls_f + self.num_cls_b) + "\n"

        for i in range(0, self.num_cls_f + self.num_cls_b):
            dataset = self.img.get_data_set(i)
            indx = self.s.learn(dataset, str(i))
            self.text = self.text + "\nclass : " + str(i) + "\n\n"
            error = 0
            txt = self.text
            pb = ""

            for j in range(0, 400):
                error = self.s.train(indx)
                if j % 10 == 0:
                    self.text = txt + str(float(j) / 4) + "% : " + pb + "=>"
                    pb = pb + "="

            self.text = txt + "100% : " + pb + "=>"
            self.text = self.text + "\n\nerror : " + str(error) + "\n"

        w, m = self.s.get_weights()
        self.d.save(self.ow, self.oh, self.num_cls_f, self.num_cls_b, w, m)
        self.text = self.text + "\n\n---TRAINING COMPLEATED---\n"
        time.sleep(1)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
