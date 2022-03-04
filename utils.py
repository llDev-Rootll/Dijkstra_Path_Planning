from queue import PriorityQueue
import math
from dimensions import *

def to_pygame(coords, height=250):
    """Convert coordinates into pygame coordinates (lower-left => top left)."""
   
    return (coords[0], height - coords[1])

def eq_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2==x1:
        return [x1]
    slope =(y2 - y1)/(x2 - x1)
    intercept = y1-(slope*x1)

    return [slope, intercept]

def check_polygon(p):
    
    x, y = p
    eq1 = eq_line(p4_i, p1_i)
    l1_flag = y - eq1[0]*x - eq1[1]>=0
    eq2 = eq_line(p1_i, p2_i)
    l2_flag = y - eq2[0]*x - eq2[1]<=0
    # print(l2_flag)
    eq3 = eq_line(p2_i, p3_i)
    l3_flag = y - eq3[0]*x - eq3[1]>=0
    eq4 = eq_line(p3_i, p4_i)
    l4_flag = y - eq4[0]*x - eq4[1]<=0

    eq_m = eq_line(p1_i, p3_i)
    m_flag = y - eq_m[0]*x - eq_m[1]<=0

    
    tri_1 = l2_flag and l3_flag and not(m_flag)
    tri_2 = l1_flag and l4_flag and m_flag

    flag = tri_1 or tri_2

    return flag


def check_hexagon(p):
    sixty = math.pi/3
    
    x, y = p
    eq1 = eq_line(h1_i, h2_i)
    l1_flag = y - eq1[0]*x - eq1[1]<=0
    l2_flag = x<=h2_i[0]
    eq3 = eq_line(h3_i, h4_i)
    l3_flag = y - eq3[0]*x - eq3[1]>=0
    eq4 = eq_line(h4_i, h5_i)
    l4_flag = y - eq4[0]*x - eq4[1]>=0
    eq5 = eq_line(h5_i, h6_i)
    l5_flag = x>=h5_i[0]
    eq6 = eq_line(h6_i, h1_i)
    l6_flag = y - eq6[0]*x - eq6[1]<=0

    flag = l1_flag and l2_flag and l3_flag and l4_flag and l5_flag and l6_flag

    return flag


def check_circle(p):
    x, y = p
    return (x-300)*(x-300) + (y-185)*(y-185) - 45*45<=0

def check_obstacle(current):
    x, y = current
    
    if (x > x_max) or (y > y_max) or (x < 0) or (y < 0):
        return False

    if(check_circle(current) or check_hexagon(current) or check_polygon(current)):
        return False
    
    return True
def gen_neighbours(current):
    neighbour = []
    x, y = current
    actions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]
    for action in actions:
        if check_obstacle((x+action[0], y+action[1])):
            if action[0]!=0 and action[1]!=0:
                neighbour.append([(x+action[0], y+action[1]), 1.4])
            else:
                neighbour.append([(x+action[0], y+action[1]), 1])
    
    return neighbour

def dijkstra(src, dst):
    node_cost={}
    node_prev={}

    node_cost[src] = 0
    visited=[]

    queue = PriorityQueue()
    queue.put((node_cost[src], src))
    path = []
    while queue:
        current = queue.get()[1]
        print("Exploring node : ", current)
        if current == dst:
            print("Found...")
            temp = dst
            while(node_prev[temp]!=src):
                path.append(node_prev[temp])
                temp = node_prev[temp]
            break;
                
        if current not in visited:
            if(check_obstacle(current)):
                visited.append(current)
            neighbours = gen_neighbours(current)

            for nr, cost in neighbours:
                n_cost = node_cost[current] + cost
                if (not node_cost.get(nr)):
                    node_cost[nr] = n_cost
                    node_prev[nr] = current
                else:
                    if(n_cost<node_cost[current]):
                        node_cost[nr] = n_cost
                        node_prev[nr] = current
                queue.put((node_cost[nr], nr))
    
    return path, visited