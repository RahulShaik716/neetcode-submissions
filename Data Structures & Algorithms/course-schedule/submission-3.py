class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degrees = [0]*numCourses 

        for src,dest in prerequisites:
            graph[src].append(dest)
            in_degrees[dest] += 1
        
        queue = deque([i for i in range(numCourses) if in_degrees[i]==0])

        count = 0 
        while queue:
            node = queue.popleft() 
            count+=1 

            for neighbor in graph[node]:
                in_degrees[neighbor]-=1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses
        