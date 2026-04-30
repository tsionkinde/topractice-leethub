class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE = 0
        BLACK = 1
        GREY = 2
        
        Color = {k: WHITE for k in range(numCourses)}
        cycle = False

        adj_list = defaultdict(list)

        # create adjacency list
        for a, b in prerequisites: 
            adj_list[b].append(a)
        
        def dfs(node): 
            nonlocal cycle 

            if cycle: 
                return 

            Color[node] = GREY

            for nei in adj_list[node]:
                if Color[nei] == WHITE: 
                    dfs(nei)
                elif Color[nei] == GREY: 
                    cycle = True 
                    return 

            Color[node] = BLACK
        
        
        for node in range(numCourses): 
            if Color[node] == WHITE: 
                dfs(node)
        
        return not cycle
        
        