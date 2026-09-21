class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         # Your code goes here
        graph = defaultdict(list)
        in_degree = [0]*numCourses

        for dest,src in prerequisites:
            graph[src].append(dest)
            in_degree[dest]+=1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        count = 0 
        while queue:
            node = queue.popleft()
            count+=1

            for neighbor in graph[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses
        