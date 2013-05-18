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

from PIL import Image
import os


class image:

    def __init__(self, w, h):
        self.img_list = list()
        self.name_list = list()
        self.ow = w
        self.oh = h

    def get_all_images(self, path):
        #self.img_list = list()
        for dirname, dirnames, filenames in os.walk(path):
            for filename in filenames:
                name = os.path.join(dirname, filename)
                self.name_list.append((filename, name))
                t = Image.open(name)
                t = t.resize((self.ow, self.oh))
                self.img_list.append(t)
        return len(self.img_list)

    def get_name(self, n):
        return self.name_list[n]

    def get_data_set(self, n):
        ls = list()

        p = self.img_list[n].load()
        for y in range(0, self.oh):
            for x in range(0, self.ow):
                sm = float(p[x, y][0]) + float(p[x, y][1]) + float(p[x, y][2])
                if sm == 0.0:
                    sm = 1
                ls.append(float(p[x, y][0]) / sm)
                ls.append(float(p[x, y][1]) / sm)
                ls.append(float(p[x, y][2]) / sm)
        return ls

    def save_all(self):
        for i in range(0, len(self.img_list)):
            self.img_list[i].save(str(i) + ".jpg")
