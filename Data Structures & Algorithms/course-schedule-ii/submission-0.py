class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        in_degree = [0]*numCourses 

        for dest,src in prerequisites:
            graph[src].append(dest)
            in_degree[dest]+=1
        
        queue = deque([i for i in range(numCourses) if in_degree[i]==0])

        while queue:
            node = queue.popleft() 
            res.append(node)
            print(node)
            for neighbor in graph[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []
        