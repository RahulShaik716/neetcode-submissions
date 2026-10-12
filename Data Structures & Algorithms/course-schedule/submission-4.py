class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[]  for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for dest,src in prerequisites:
            adj[src].append(dest)
            in_degree[dest]+=1
        
        queue = deque([x for x in range(numCourses) if in_degree[x] == 0])

        result = []

        while queue:
            node = queue.popleft() 
            result.append(node)

            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return True if len(result) == numCourses else False
