
import cv2
import matplotlib.pyplot as plt
import sys
import numpy as np
sys.path.append('algorithms')
import hmap as k
import json

def getter(filename='data/raw/xy_data.json'):
    with open(filename, 'r') as f:
        pos_dict = json.load(f)
    x = [pos[0] for pos in pos_dict.values()]
    y = [pos[1] for pos in pos_dict.values()]

    return np.array(x), np.array(y)

def start ():
    X,Y = getter(filename='data/raw/xy_data.json')
    x_mesh, y_mesh ,xc , yc,h= k.mesh(X, Y)
    intensity_l = k.distance(xc,yc,X,Y,h)
    inten = np.array(intensity_l)
    plt.pcolormesh(x_mesh,y_mesh,inten)
    plt.plot(X,Y,'ro')
    plt.colorbar()
    plt.show()

    
