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

img = image.image(ow, oh)

num_classes = img.get_all_images("./forest")
num_classes = img.get_all_images("./beach")

s = som4.som(ow * oh * 3, num_classes, 0.01)
s.init()

img.save_all()
print num_classes

for i in range(0, num_classes):
    dataset = img.get_data_set(i)
    indx = s.learn(dataset, str(i))
    print "-------------------- ", i
    for j in range(0, 400):
        print s.train(indx)

w, m = s.get_weights()
d.save(ow, oh, num_classes, w, m)
