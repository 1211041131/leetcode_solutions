from collections import deque

class Solution(object):
    def eventualSafeNodes(self, graph):
        V = len(graph)
        queue = deque()
        result = []
        adj_list = [[] for _ in range(V)]
        degree = [0] * V

        for node in range(V):
            for adj in graph[node]:
                adj_list[adj].append(node)
                degree[node] += 1

        for i in range(V):
            if degree[i] == 0:
                queue.append(i)

        while len(queue) != 0:
            cur = queue.popleft()
            result.append(cur)

            for adj in adj_list[cur]:
                degree[adj] -= 1

                if degree[adj] == 0:
                    queue.append(adj)

        result.sort()
        return result