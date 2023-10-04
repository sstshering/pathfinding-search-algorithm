
# the class node stores the row,col of the grid and the cost
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
            self.down = Node(Map[self.row+1][self.col], self.row+1, self.col)
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
            cost += dest.cost #cost of the nodes we trace back 
            path.append([dest.row,dest.col]) #save the coordinates of the current node
            dest = dest.predecesor  #move to the current node's predecesor
            
        path = path[::-1]  #reverse the path
        return path,cost