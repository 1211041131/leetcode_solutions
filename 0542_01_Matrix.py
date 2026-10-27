from collections import deque

class Solution(object):

    def updateMatrix(self, mat):
        row=len(mat)
        col=len(mat[0])
        queue=deque()
        vis=[[0]*col for _ in range(row)]
        dis=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    queue.append([i,j,0])
                    vis[i][j]=1
        while len(queue):
            i,j,d=queue.popleft()
            dis[i][j]=d
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i=x+i
                new_j=y+j
                if new_i>=row or new_j>=col or new_i<0 or new_j<0:
                    continue
                if vis[new_i][new_j]==1:
                    continue 
                queue.append([new_i,new_j,d+1])
                vis[new_i][new_j]=1
        return dis
