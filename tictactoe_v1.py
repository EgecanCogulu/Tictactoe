# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:08:53 2021

@author: Egecan
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
import os


fig, ax = plt.subplots()

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print ('x = %d, y = %d'%( ix, iy))

    global coords
    coords = [ix, iy]
    grid_plotter(["X","X","X","X","X","X","X","X","X"])
    return None


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

    for i in range(9):
        
        margin=0.3666666
        if grid[i]=="-":
            plt.text(i%3+margin,2-i//3+margin, "", fontsize=35)
        if grid[i]=="X":
            plt.text(i%3+margin,2-i//3+margin, "X", fontsize=35)
        if grid[i]=="O":
            plt.text(i%3+margin,2-i//3+margin, "O", fontsize=35)        
    return (fig,ax)


def update_grid():
    plt.close()
    grid_plotter(["X","O","-","X","O","-","X","O","-"])
    

grid_plotter(["X","O","-","X","O","-","X","O","-"])
