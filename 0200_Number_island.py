class Solution(object):
    def dfs(self,grid,copy,i,j,row,col,vis):
        if i<0 or j<0 or j>=col or i>=row:
            return
        if copy[i][j]=="0":
            return 
        if vis[i][j] == 1:
            return

        vis[i][j]=1
        self.dfs(grid,copy,i+1,j,row,col,vis)
        self.dfs(grid,copy,i,j+1,row,col,vis)
        self.dfs(grid,copy,i,j-1,row,col,vis)
        self.dfs(grid,copy,i-1,j,row,col,vis)

    def numIslands(self, grid):
        row=len(grid)
        col=len(grid[0])
        copy=deepcopy(grid)
        vis=[[0]*col for _ in range(row)]
        count=0
        for i in range(row):
            for j in range(col):
                if copy[i][j]=="1" and vis[i][j]==0:
                    count+=1

                    self.dfs(grid,copy,i,j,row,col,vis)
        return count 

            