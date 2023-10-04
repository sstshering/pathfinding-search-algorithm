import time
import sys 
import mapfileGenerator
import Treesearch
# pathfinding algorithm using BFS, IDS and A^*(heuristic)

# read map file that stores the dimension of the grid, start and goal location in the grid and the grid
# read map file into 2d array
def read_mapFile(fileName):
    # read the file
    with open(fileName, 'r') as mapFile:
        # first line has the dimensions
        # reads the line, spilts, maps into int list
        # dimension= list(mapFile.readline().split())
        dimension =list(map(int, mapFile.readline().split()))
        print(dimension)
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


# breadth-first search
def bfs(dimension, start, goal, mapGrid):
    # contains all the visited nodes
    visited =set()
    # begin the queue with the start coordinates
    queue = [Treesearch.Node(0,start[0], start[1])]
    while queue:
        path=[]
        # if queue is empty
        if len(queue)==0:
            return path
        # the first node
        node = queue.pop(0)
        visited.add(node)
        # check if it reached the goal node
        if node.row == goal[0] and node.col==goal[1]:
            # if its at the goal, then add it to the path list
            path.append((node.row, node.col))
            node = node.predecesor
            return path
        # add the node in visited so there
        if node not in visited:
            visited.add(node)
        # successor neighbor.node
        # neighbor = successorNodes(node, dimension)
        
            
# # generate successor nodes (up, down, left, right)
# def successorNodes(node, dimension):
#     for i in range(dimension[0]):
#         upNode = (Treesearch.Node.row-1, Treesearch.Node.col)
#         return
#     pass

#
def main():
    #get sys command from user
    userCommand =sys.argv()
    fileName = sys[0]
    searchType = sys[1]
    # get the map's info
    #filePath = "map1.txt"
    dimension, start, goal, grid = read_mapFile(fileName)
    # print(start)
    # searchType = input()
    if searchType=="bfs":
        # start the timer
        startTime= time.time()
        # call bfs search, also keep track of the expandded nodes
        path = bfs(dimension, start, goal, grid)
        # end the timer
        endTime=time.time()

        if path:
            print("Path found:", path)
            # print cost
            print("Total cost:" )
        else:
            print("Path not found")

        print("Runtime:", (endTime - startTime))


