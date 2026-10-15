from collections import deque 
from copy import deepcopy
class Solution(object):
    def orangesRotting(self, grid):
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        fresh=0
        grid_copy=deepcopy(grid)
        for i in range(0,row):
            for j in range (0,col):
                if grid[i][j]==2:
                    queue.append([i,j])
                if grid[i][j]==1:
                    fresh+=1
        time=0
        while queue and fresh>0:
            
         
            level_size = len(queue)
            for _ in range(level_size):
                i,j=queue.popleft()
                for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i=r+i
                    new_j=c+j
                    if new_i<0 or new_j<0 or new_j>=col or new_i>=row:
                        continue
                    if grid_copy[new_i][new_j]==0 or grid_copy[new_i][new_j]==2:
                        continue  
                    if grid_copy[new_i][new_j]==1:
                        queue.append([new_i,new_j])
                        grid_copy[new_i][new_j]=2
                        fresh-=1
            time+=1
        if fresh>0:
            return -1
        else:
            return time


                

        