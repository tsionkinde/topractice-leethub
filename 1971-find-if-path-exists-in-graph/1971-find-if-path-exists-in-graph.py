from collections import deque, defaultdict
class Solution:
    def validPath(self, n, edges, source, destination):
        visited=set()
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            #base case
            if node==destination:
                return True
            visited.add(node)
            #path
            for neigh in graph[node]:
                if neigh not in visited:
                    if dfs(neigh):
                        return True
            return False  
        return dfs( source)          

    