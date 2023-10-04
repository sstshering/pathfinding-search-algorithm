import random 
import numpy as np

def gen_map(dim1,dim2):
    filename = 'TestCase_'+str(dim1)+'_'+str(dim2)
    with  open(filename, 'w') as f:
        f.write(f'{dim1} {dim2}\n')
        start_point = (random.randint(1,dim1/2), random.randint(1,dim2/2))
        goal_point = (random.randint(start_point[0],dim1), random.randint(start_point[0],dim2))
        f.write(f'{start_point[0]} {start_point[1]}\n')
        f.write(f'{goal_point[0]} {goal_point[1]}\n')
        cost = np.random.randint(0,5, size=(dim1,dim1))
        if cost[start_point]==0:
            cost[start_point]==np.random.randint(1,5)
        if cost[goal_point]==0:
            cost[goal_point]==np.random.randint(1,5)
        for i in range(cost.shape[0]):
            f.write(str(cost[i]).replace('[','').replace(']','')+'\n')