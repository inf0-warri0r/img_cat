"""
Author : tharindra galahena (inf0_warri0r)
Project: image catagarizetion using SOM
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

import som4
import weights
import image


ow = 640 / 8
oh = 480 / 8

d = weights.data("weights")
ow, oh, inp, w, m = d.load()

print "w = ", ow, " h = ", oh, " classes = ", inp

img1 = image.image(ow, oh)
img2 = image.image(ow, oh)

s = som4.som(ow * oh * 3, inp, 0.01)
s.init()
print len(s.get_weights()[0]), " ", len(w)
s.put_weights(w, m)

nb = img1.get_all_images("./test/b")
nf = img2.get_all_images("./test/f")

print "beach test\n"

for i in range(0, nb):

    dataset = img1.get_data_set(i)
    name = img1.get_name(i)
    ct = int(s.find(dataset))

    if ct < 7:
        cat = "forest"
    else:
        cat = "beach"

    print "image ", name[0], " = ", cat, " ", ct

print "forest test\n"

for i in range(0, nf):

    dataset = img2.get_data_set(i)
    name = img2.get_name(i)
    ct = int(s.find(dataset))

    if ct < 7:
        cat = "forest"
    else:
        cat = "beach"

    print "image ", name[0], " = ", cat, " ", ct
