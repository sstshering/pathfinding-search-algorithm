import time
# pathfinding algorithm using BFS, IDS and A^*(heuristic)

# read map file that stores the dimension of the grid, start and goal location in the grid and the grid
# read map file into 2d array
def read_mapFile(filePath):
    # read the file
    with open(filePath, 'r') as mapFile:
        # first line has the dimensions
        # reads the line, spilts, maps into int list
        dimension =list(map(int, mapFile.readline().split()))
        # second line has the start location
        start=list(map(int, mapFile.readline().split()))
        # third line has the goal location
        goal=list(map(int, mapFile.readline().split()))
        # read the grid coordinates
        mapGrid =[]
        for i in range(dimension):
            # gets each row of the map grid from the file
            rows= list(map(int, mapFile.readline().split()))
            mapGrid.append(rows)
    return dimension, start, goal, mapGrid

# the class node stores the row,col of the grid
class Node:
    def __init__(self, row, col,parent = None):
        self.row= row
        self.col =col
        self.parent=parent

# breadth-first search
def bfs(dimension, start, goal, mapGrid):
    # contains all the visited nodes
    visited =set()
    # begin the queue with the start coordinates
    queue = [Node(start[0], start[1])]
    while queue:
        # the first node
        node = queue.pop(0)
        # check if it reached the goal node
        if node.row == goal[0] and node.col==goal[1]:
            path=[]
            # if its at the goal, then add it to the path list
            path.append((node.row, node.col))
            node = node.parent
            
        # add the node in visited so there
        if node not in visited:
            visited.add(node)
        
    
# generate successor nodes (up, down, left, right)
def successorNodes():
    return 

#
def main():
    # get the map's info
    filePath = "map1.txt"
    dimension, start, goal, grid =read_mapFile(filePath)
    # start the timer
    startTime= time.time()
    # call bfs search, also keep track of the expandded nodes
    path = bfs(dimension, start, goal, grid)
    # end the timer
    endTime=time.time()

    if path:
        print("Path found:", path)
        # print cost?
    else:
        print("Path not found")

    print("Runtime:", (endTime - startTime))


