class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set() 
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res+=1
        return res