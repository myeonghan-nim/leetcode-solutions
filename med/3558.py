from collections import deque
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        max_depth = 0
        visited = [False] * (n + 1)
        visited[1] = True
        queue = deque([(1, 0)])

        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, depth + 1))

        if max_depth == 0:
            return 0

        return pow(2, max_depth - 1, MOD)
