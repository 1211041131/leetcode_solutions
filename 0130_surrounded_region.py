from collections import deque
from copy import deepcopy
class Solution(object):
    def solve(self, board):
        row=len(board)
        col=len(board[0])
        copy=deepcopy(board)
        queue=deque()
        vis=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if (i == 0 or i == row-1 or j == 0 or j == col-1) and board[i][j] == "O":
                    queue.append([i,j])
                    vis[i][j]=1
        while len(queue):
            i,j=queue.popleft()
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_x,new_y=i+x,j+y
                if new_x>=row or new_y>=col or new_x<0 or new_y<0:
                    continue 
                if vis[new_x][new_y]==1:
                    continue
                if board[new_x][new_y]=="X":
                    continue
                queue.append([new_x,new_y])
                vis[new_x][new_y]=1
        for i in range(row):
            for j in range(col):
                if vis[i][j]==0 and board[i][j]=="O":
                    board[i][j]="X"
        
 