class Solution(object):
    def dfs(self,row,col,inital,color,vis,i,j):
        if row<0 or col<0 or row>=i or col>=j:
            return 
        if vis[row][col]!=inital:
            return
        if vis[row][col]==color:
            return 
        vis[row][col]=color
        self.dfs(row+1,col,inital,color,vis,i,j)
        self.dfs(row,col+1,inital,color,vis,i,j)
        self.dfs(row,col-1,inital,color,vis,i,j)
        self.dfs(row-1,col,inital,color,vis,i,j)
    def floodFill(self, image, sr, sc, color):
        i=len(image)
        j=len(image[0])
        if image[sr][sc]==color:
            return image
        vis=deepcopy(image)
        inital=vis[sr][sc]
        self.dfs(sr,sc,inital,color,vis,i,j)
        
        return vis 
        