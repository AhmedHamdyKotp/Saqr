import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
sys.path.append('src\modules')
from modules import visualizer as vi

X , Y = vi.heatmap_algorithms()
print(X,Y)
