import sys
sys.path.append("./")
import time
import numpy as np
import random


class Node:
    def __init__(self, cost, row, col):
        self.cost = cost
        self.row = row
        self.col = col
        self.predecesor = None
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        
    #expand up, down, left, and right of the current node  
    def Expand(self, Map):
        #If node has room to expand Up
        if self.row > 0 and Map[self.row-1][self.col] > 0:
            self.up = Node(Map[self.row-1][self.col], self.row-1, self.col)
            self.up.predecesor = self
        
        #If node has room to expand Down
        if self.row < len(Map)-1 and Map[self.row+1][self.col] > 0:
            self.down = Node(Map[self.row + 1 ][self.col], self.row + 1, self.col)
            self.down.predecesor = self
            
        #If node has room to expand Right
        if self.col < len(Map[0])-1 and Map[self.row][self.col+1] > 0:
            self.right = Node(Map[self.row][self.col+1], self.row, self.col+1)
            self.right.predecesor = self
            
        #If node has room to expand Left
        if self.col > 0 and Map[self.row][self.col-1] > 0:
            self.left = Node(Map[self.row][self.col-1], self.row, self.col-1)
            self.left.predecesor = self
            
        return
            
    def TraceBack(self):
        path = []
        cost = 0
        dest = self
        while(dest.predecesor != None):
            cost += dest.cost 
            path.append([dest.row,dest.col]) 
            dest = dest.predecesor 
            
        path = path[::-1] 
        return path,cost
        

def BFS(Map, sp, gp,timeout):
    st_time = time.time()
    visited_Nodes = [] #List of the visited nodes
    queue = [] 
    start_node = Node(sp[0],sp[1],sp[2])
    queue.append(start_node)
    maxNodes = len(queue)
    nodesExpanded = 0
    while(len(queue) != 0): 
        if time.time() - st_time > timeout:
            
            print("Timeout! No path found.")  #Timeout
            break
            
        currNode = queue.pop(0)
        if tuple([currNode.row,currNode.col]) in visited_Nodes: #Ignoring already visited nodes.
            continue
        visited_Nodes.append((currNode.row,currNode.col)) 
        #xpand the current node
        currNode.Expand(Map) 
        nodesExpanded += 1
        nodesToAppend = []
        print("Expanding: " + str((currNode.row+1,currNode.col+1)) + " Cost: " + str(currNode.cost))
        if currNode.up != None:
            if tuple([currNode.up.row,currNode.up.col])==tuple(gp): 
                print("Expanding= " + str(nodesExpanded))
                print("Max nodes held in memory = " + str(maxNodes))
                return visited_Nodes,currNode.up
            nodesToAppend.append(currNode.up) 

        if currNode.down != None:
            if tuple([currNode.down.row,currNode.down.col])==tuple(gp):
                print("Expanding= " + str(nodesExpanded))
                print("Max nodes held in memory = " + str(maxNodes))
                return visited_Nodes,currNode.down 
            nodesToAppend.append(currNode.down)
            
        if currNode.right != None:
            if tuple([currNode.right.row,currNode.right.col])==tuple(gp): 
                print("Expanding= " + str(nodesExpanded))
                print("Max nodes held in memory = " + str(maxNodes))
                return visited_Nodes,currNode.right 
            nodesToAppend.append(currNode.right) 
            
        if currNode.left != None:
            if tuple([currNode.left.row,currNode.left.col])==tuple(gp): 
                print("Expanding= " + str(nodesExpanded))
                print("Max nodes held in memory = " + str(maxNodes))
                return visited_Nodes,currNode.left
            nodesToAppend.append(currNode.left) 
            
        nodesToAppend.sort(key=lambda x: x.cost, reverse = False) 
        while(len(nodesToAppend) != 0): 
            queue.append(nodesToAppend.pop(0))
            
        if len(queue) > maxNodes:
            maxNodes = len(queue)
            
    print("Nodes expanded = " + str(nodesExpanded))
    print("Max nodes held in memory = " + str(maxNodes))
    return visited_Nodes ,None 

# Cheching the map setting
def gen_map(dim1,dim2):
    filename = 'TestCase_'+str(dim1)+'_'+str(dim2)+'.txt'
    with  open(filename, 'w') as f:
        f.write(f"{dim1} {dim2}\n")
        start_point = (random.randint(1,dim1-1), random.randint(1,dim2-1))
        goal_point = (random.randint(1,dim1 -1), random.randint(1,dim2-1))
        f.write(f'{start_point[0]} {start_point[1]}\n')
        f.write(f'{goal_point[0]} {goal_point[1]}\n')
        cost = np.random.randint(0,5, size=(dim1,dim1))
        if cost[start_point[0]-1][start_point[1]-1]==0:
            cost[start_point[0]-1][start_point[1]-1]=np.random.randint(1,5)
        if cost[goal_point[0]-1][goal_point[1]-1]==0:
            cost[goal_point[0]-1][goal_point[1]-1]=np.random.randint(1,5)
        for i in range(cost.shape[0]):
            f.writelines(str(cost[i]).replace('[','').replace(']',''))
            f.write('\n')
        return filename

def read_env(inp_file_name):
    map_setting = [] 
    inp_file = open(inp_file_name, "r")
    for line in inp_file:
        map_setting.append([int(i) for i in line.strip().split(' ')])
    return map_setting

def env_check(env):
    if env[1][0]<1 or env[1][1] > env[0][1]:
        print("Start point is not in the map!")
        return False
    elif env[2][0]<1 or env[2][1] > env[0][1]:
        print("Goal point is not in the map!")
        return False
    elif np.array(env[3:]).shape != tuple(env[0]):
        print("Incostitency in the map size and cost matrix")
        return False
    elif env[3:][env[1][0]-1][env[1][1]-1]  == 0:
        print("Starting point is an impassable terrain!")
        return False
    elif env[3:][env[2][0]-1][env[2][1]-1]  == 0:
        print("Goal point is an impassable terrain!")
        return False
    elif env[1] == env[2]:
        print("Starting point is and goal points are the same!")
        return False
    else:
        print("The envirument is ok!")
        return True

def draw_map(MapSetting, route_list):
    st_p = tuple([i - 1 for i in MapSetting[1]])
    g_p = tuple([i - 1 for i in MapSetting[2]])
    grid = np.array(MapSetting[3:],dtype=object)
    impassable_ind = np.where(grid==0)
    passable_ind = np.where(grid!=0)
    for i in zip(impassable_ind[0],impassable_ind[1]):
        grid.itemset(i, 'X')
    for i in zip(passable_ind[0],passable_ind[1]):
        grid.itemset(i, '.')  
    
    for i in route_list[:-1]:
        grid.itemset(tuple(i), '-')
    grid.itemset(st_p, 'S')
    grid.itemset(g_p, 'G') 
    return grid
file_namne = gen_map(10,10)

start_time = time.time()    
#file_namne = './TestCase_10_10_1.txt'
algorithm = 'BFS' 
timeout = 180

map_setting = read_env(file_namne)
map_status = env_check(map_setting)
map_size, start_point, goal_point, costs = map_setting[0], map_setting[1], map_setting[2], map_setting[3:]


start_point = [i - 1 for i in start_point]
goal_point = [i - 1 for i in goal_point]
if map_status:
    start_point.insert(0, costs[start_point[0]][start_point[1]])  # insert the initial coordinate cost
    if algorithm == "BFS":  # BFS Arlgorithm
        visited_Nodes,results = BFS(costs, start_point, goal_point, timeout)
        if results != None:
            route_list = [[i + 1 for i in j]for j in results.TraceBack()[0]]
            print("The path route from {} to {} is: {}".format(tuple(list([start_point[1] + 1, start_point[2] + 1])),
                                                               tuple(list([goal_point[0] + 1, goal_point[1] + 1])),
                                                               route_list[:-1]))
            print("The cost of the path found: " ,  str(results.TraceBack()[1]))
            print(draw_map(map_setting, results.TraceBack()[0]))
        else:
            print("No Path was found to the goal! ")
            print('Expanded nodes:')
            print(draw_map(map_setting, visited_Nodes))

    print("The runtime of the {} algorithm: {time:.3f} seconds".format(algorithm,time=time.time() - start_time))
