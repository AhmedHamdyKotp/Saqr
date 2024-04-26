
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def build (G):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')    
    for node in G.nodes:
        node_size = G.degree(node) * 100  # Calculate node size here
        node_color = 'skyblue' if G.nodes[node]['type'] == 'individual' else 'lightgreen'
    X =[] ; Y =[] ; Z =[]
    File = open('data/processed/odes.txt','r')
    lines = File.readlines()
    for i in range (len(lines)):
        ss = lines[i].split(',')
        X.append(float(ss[0]))
        Y.append(float(ss[1]))
        Z.append(float(ss[2]))
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.scatter(X, Y, Z, s=node_size, c=node_color)
    ax.set_label('X')
    ax.set_label('Y')
    ax.set_label('Z')
    plt.draw()
    