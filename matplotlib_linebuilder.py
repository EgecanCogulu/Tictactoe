# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:31:40 2021

@author: Egecan
"""

from matplotlib import pyplot as plt

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


fig,ax =plt.subplots()
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

plt.show()