class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]

        indegree = [0] * numCourses 

        for src,dest in prerequisites:
            adj[src].append(dest)
            indegree[dest]+=1 
        
        queue = deque([x for x in range(numCourses) if indegree[x] == 0])
        output = []
        while queue:
            vertex = queue.popleft()
            output.append(vertex)

            for nei in adj[vertex]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return len(output) == numCourses

        