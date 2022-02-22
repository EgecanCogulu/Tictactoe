# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:16:24 2021

@author: Egecan
"""

import numpy as np
import pylab as plt
from matplotlib.widgets import Slider



turn=1
def onclick(val):
    global turn
    x, y = val.xdata, val.ydata
    ix=int(x)
    iy=int(y)
    texts[ix+3*iy].set_position(positions[ix+3*iy])

    if turn==1:
        texts[ix+3*iy].set_text("X")
        turn=2
    else:
        texts[ix+3*iy].set_text("O")
        turn=1
    plt.draw()

def grid_plotter(grid):

    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onclick)
    ax.set_aspect(1)
    ax.tick_params(axis='both',which='both', bottom=False,left=False, labelbottom=False,labelleft=False)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    for i in range(4):
        plt.vlines(x=i, ymin=0, ymax=3,lw=1,color="k")
        plt.hlines(y=i, xmin=0, xmax=3,lw=1,color="k")
        
    
    margin=0.5
    c=0.160
    global positions
    positions=[[1*margin-c,1*margin-c],[3*margin-c,1*margin-c],[5*margin-c,1*margin-c],
               [1*margin-c,3*margin-c],[3*margin-c,3*margin-c],[5*margin-c,3*margin-c],
               [1*margin-c,5*margin-c],[3*margin-c,5*margin-c],[5*margin-c,5*margin-c]]
    
    global texts
    texts=[""]*9
    for (index,mytext) in enumerate(texts):
        texts[index] = ax.text(*positions[index],mytext,fontsize=45)
        
    plt.show()
    return None


grid_plotter(1)

    
    