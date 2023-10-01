# pathfinding-search-algorithm
Use of basic search algorithm (BFS, IDS, and A*-heuristic) to solve common AI pathfinding problems.
Pathfinding
Pathfinding is a common problem that artificial agents must solve, including mapping services, artificial vehicles, AIs in real-time strategy games, and robots that must navigate in the physical world. For this assignment, we will focus on a simplified pathfinding problem. Your program will search for the shortest path from a starting location to a goal location on a square grid. However, this grid will have some impassable locations and varying terrain costs that must be accounted for. The agent is allowed to move in any of the four primary directions (up, down, left, right) but not diagonally or outside the bounds of the map. 

Your program should read in a map file that specifies the map in the following format.  The file name should be able to be specified on the command line. The first line has the dimensions of the map, the second line has the coordinates of the starting location (row-column), and the third line has the coordinates of the goal location. After that is the specification of the map, which consists of digits between 0 and 5, separated by spaces. These numbers represent the movement cost for moving to a given space on the grid. The number 0 is a special case and is considered impassable terrain.  The numbers 1-5 are the number of turns required to move to the given square, with 1 being the lowest cost and 5 being the highest.  There is no cost for moving to the starting location. The following is an example of the map format. 

5 7
1 2
4 3
2 4 2 1 4 5 2
0 1 2 3 5 3 1
2 0 4 4 1 2 4
2 5 5 3 2 0 1
4 3 3 2 1 0 1

Search Algorithms

You will implement and compare three of the search algorithms discussed in class and in the book:

1)	Breadth-first search
2)	Iterative deepening search
3)	A* search

For all three algorithms, you should implement repeat-state checking, so that you do not revisit states you have already expanded. 

For A* search you should use the Manhattan distance as your heuristic, but implement the algorithm in a general way so that a new heuristic could be used. 

Your program should run each search algorithm with a 3-minute time cutoff (i.e., you should stop the search with no result after a maximum of 3 minutes of runtime).  For each of the three algorithms, print out the following information to the console:

1)	The cost of the path found
2)	The number of nodes expanded 
3)	The maximum number of nodes held in memory
4)	The runtime of the algorithm in milliseconds
5)	The path as a sequence of coordinates (row, col), (row col), …, (row, col)

If the algorithm terminates without finding a result, print -1 for the path cost and NULL for the path sequence. You should still print the number of nodes and the runtime. 
