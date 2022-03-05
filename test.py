import math
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import Polygon
import numpy as np
from utils import  check_obstacle, gen_neighbours, dijkstra
from dimensions import *

def init():
    scat.set_offsets([])
    return scat,
def animate(i, l_vis):
    if(i<=l_vis):
        line.set_data(path_x[0], path_y[0])
        data = np.hstack((visited_x[:i,np.newaxis], visited_y[:i, np.newaxis]))
        scat.set_offsets(data)
    else:
        line.set_data(path_x[:(i-l_vis)*30], path_y[:(i-l_vis)*30])
    return scat, line,

if __name__ == "__main__":
    src_x, src_y, dst_x, dst_y = 0, 0, 0, 0
    while(True):
        src_x = random.randint(0,int((x_max-1)/2))
        src_y = random.randint(0, y_max)
        dst_x = random.randint(int((x_max-1)/2), x_max)
        dst_y = random.randint(0, y_max)

        if(check_obstacle([src_x, src_y]) and check_obstacle([dst_x, dst_y])):
            break

    src = (src_x, src_y)
    dst = (dst_x, dst_y)
    src = (0, 0)
    dst = (114, 100)
    print("Source Point is : ", src)
    print("Destination Point is : ", dst)


    fig = plt.figure()
    ax = plt.axes(xlim=(0, x_max), ylim=(0, y_max))
    ax.set_facecolor('k')
    print("Exploring using Dijkstra's algorithm")
    print("Press Enter key to continue...")
    input()
    path, visited = dijkstra(src, dst)
    path.append(src)
    path.insert(0,dst)
    visited_x = np.array(visited)[:,0]
    visited_y = np.array(visited)[:,1]
    path_x = np.array(path)[:,0]
    path_y = np.array(path)[:,1]

    line, = ax.plot(path_x, path_y, color = 'g')
    scat = ax.scatter([], [], s=2, color='w')



    h_i = Polygon([h1_i, h2_i, h3_i, h4_i, h5_i, h6_i], facecolor = 'r')
    h = Polygon([h1, h2, h3, h4, h5, h6],facecolor = 'b')
    ax.add_patch(h_i)
    ax.add_patch(h)


    p_i = Polygon([p1_i, p2_i, p3_i, p4_i], facecolor = 'r')
    p = Polygon([p1, p2, p3, p4], facecolor = 'b')
    ax.add_patch(p_i)
    ax.add_patch(p)


    circle_i = plt.Circle(centre, radius_i, color='r', fill=True)
    circle = plt.Circle(centre, radius, color='b', fill=True)
    ax.add_patch(circle_i)
    ax.add_patch(circle)
    # plt.show()
    animator = FuncAnimation(fig, animate, frames = (len(visited)+len(path)) ,fargs=[len(visited)], interval = 1, repeat=False, blit=True)
    print("Save simulation to disk? (rendering takes a while)")
    print("Press y or n : ")
    save = input()
    if save == 'y' or save =='Y':
        print("Rendering frames to disk...This may take a while...")
        animator.save('animation.mp4')
    plt.show()
    
    
