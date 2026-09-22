from collections import deque

class Solution:
    def shortestPath(self, V, edges, src, dest):
        queue = deque()
        distance = [-1] * V

        adj_list = [[] for _ in range(V)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        queue.append([src, 0])
        distance[src] = 0

        while len(queue) != 0:
            node, dis_t = queue.popleft()

            for adjnode in adj_list[node]:
                if distance[adjnode] == -1:
                    distance[adjnode] = dis_t + 1
                    queue.append([adjnode, dis_t + 1])

        return distance[dest]
        