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


class data:

    def __init__(self, name):
        self.file_name = name

    def load(self):
        try:
            f = open(self.file_name, 'r')
            cat = f.read()
            f.close()
            weights = list()
            mp = list()
            lst = cat.splitlines()
            ow, oh, m, n = lst[0].split(',')
            num_w = int(ow) * int(oh) * 3 * (int(m) + int(n))
            for i in range(1, num_w + 1):
                weights.append(float(lst[i]))
            for i in range(num_w + 1, num_w + int(m) + int(n) + 1):
                mp.append(lst[i])
            return int(ow), int(oh), int(m), int(n), weights, mp
        except Exception:
            return -1, -1, -1, -1, -1

    def save(self, ow, oh, inpm, inpn, lst, mp):
        f = open(self.file_name, 'w')
        st = str(ow) + "," + str(oh) + "," + str(inpm) + "," + str(inpn)
        f.write(st + "\n")
        for l in lst:
            f.write(str(l) + "\n")
        for l in mp:
            f.write(l + "\n")
        f.close()
