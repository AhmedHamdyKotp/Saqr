
import numpy as np
import math

X = []
Y = []
def getter (x,y) :
    for i in x :
        X.append(i)
    for i in y :
        Y.append(i)

def kde_quartic(d,h):
    dn = d / h
    P = (15/16)*(1-dn**2)**2
    return P

def mesh (X,Y):
    grid_size = 1
    h=.1
    min_x = min(X)
    max_x = max(X)
    min_y = min(Y)
    max_y = max(Y)

    x_grid = np.arange(min_x - h , max_x + h , grid_size)
    y_grid = np.arange(min_y - h , max_y +h , grid_size)

    x_mesh , y_mesh = np.meshgrid(x_grid,y_grid)
    xc = x_mesh + (grid_size/2)
    yc = y_mesh + (grid_size/2)
    return x_mesh , y_mesh , xc ,yc

def distance (xc,yc,x,y):
    intensity_list=[]
    for j in range(len(xc)):
        intensity_row=[]
        for k in range(len(xc[j])):
            kde_value_list=[]
            for i in range(len(x)):
                # CALCULATE DISTANCE
                d=math.sqrt((xc[j][k]-x[i])**2+(yc[j][k]-y[i])**2)
                if d<=.1:
                    p=kde_quartic(d,.1)
                else:
                    p=0
                kde_value_list.append(p)
            # SUM ALL INTENSITY VALUE
            p_total=sum(kde_value_list)
            intensity_row.append(p_total)
        intensity_list.append(intensity_row)
    return intensity_list

