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

import random


class som:
    def __init__(self, inp, out, lrate):
        self.num_inputs = inp
        self.num_outputs = out
        self.num_weights = inp * out
        self.leaning_rate = lrate
        self.inputs = list()
        self.outputs = list()
        self.weights = list()
        self.mp = list()

        for i in range(0, self.num_outputs):
            self.weights.append(list())
            self.outputs.append(0.0)
        for i in range(0, self.num_inputs):
            self.inputs.append(0.0)

        for i in range(0, self.num_outputs):
            self.mp.append('_')

    def init(self):
        for i in range(0, self.num_outputs):
            for j in range(0, self.num_inputs):
                self.weights[i].append(random.uniform(0.0, 1.0))

    def get_weights(self):
        lst = list()
        for i in range(0, self.num_outputs):
            for j in range(0, self.num_inputs):
                lst.append(self.weights[i][j])
        return lst, self.mp

    def put_weights(self, lst, mp):
        n = 0
        for i in range(0, self.num_outputs):
            for j in range(0, self.num_inputs):
                self.weights[i][j] = lst[n]
                n = n + 1
        for i in range(0, self.num_outputs):
            self.mp[i] = mp[i]

    def normalize(self, inp):
        sm = 0.0
        for i in range(0, self.num_inputs):
            sm = sm + inp[i] ** 2.0
        sm = sm ** 0.5
        for i in range(0, self.num_inputs):
            inp[i] = inp[i] / sm
        return inp

    def learn(self, inp, ch):

        self.inputs = self.normalize(inp)
        index = 0
        mx = -1
        for i in range(0, self.num_outputs):
            self.outputs[i] = 0.0
            for j in range(0, self.num_inputs):
                o = self.outputs[i]
                self.outputs[i] = o + self.weights[i][j] * self.inputs[j]

            if self.outputs[i] > mx:
                index = i
                mx = self.outputs[i]

        while self.mp[index] != '_':
            index = (index + 1) % self.num_outputs
        self.mp[index] = ch
        return index

    def find(self, inp):
        self.inputs = self.normalize(inp)
        mx = -10000.0
        index = 0
        for i in range(0, self.num_outputs):
            self.outputs[i] = 0.0
            for j in range(0, self.num_inputs):
                o = self.outputs[i]
                self.outputs[i] = o + self.weights[i][j] * self.inputs[j]
            if self.outputs[i] > mx:
                index = i
                mx = self.outputs[i]

        return self.mp[index]

    def train(self, index):
        be = 0.0
        for i in range(0, self.num_inputs):
            e = self.inputs[i] - self.weights[index][i]
            if e > be:
                be = e
            w = self.weights[index][i]
            self.weights[index][i] = w + self.leaning_rate * e

        return be
