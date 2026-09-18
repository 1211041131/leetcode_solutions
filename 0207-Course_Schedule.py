from collections import deque 
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        result=[]
        queue=deque()
        adj_list=[[]for _ in range(numCourses)]
        degree=[0]*numCourses
        for u,v in prerequisites :
            adj_list[u].append(v)
            degree[v]+=1

        for i in range (0,numCourses):
            if degree[i]==0:
                queue.append(i)

        while len (queue)!=0:
            cnode=queue.popleft()
            result.append(cnode)
            for adj in adj_list[cnode]:
                degree[adj]-=1
                if degree[adj]==0:
                    queue.append(adj)


        if len(result)==numCourses:
            return True
        else:
            return False






        