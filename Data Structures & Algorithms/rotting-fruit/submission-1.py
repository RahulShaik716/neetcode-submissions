class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #you need no of fresh oranges . 
        #whenever you encounter them in bfs , reduce fresh orange count -1 
        #when fresh oranges = 0 then return time 

        visited = set() 
        rows,cols = len(grid),len(grid[0])
        queue = deque()
        count = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count+=1
                #add rotten ones to the queue
                if grid[r][c] == 2:
                    queue.append([r,c])
                    visited.add((r,c))
        
        if count == 0:
            return 0
        def makeRotten(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visited:
                return 
            #add fresh ones to the queue.
            visited.add((r,c))
            queue.append([r,c])
                
        time = 0 
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    count -=1 
                makeRotten(r+1,c)
                makeRotten(r-1,c)
                makeRotten(r,c+1)
                makeRotten(r,c-1)
            time+=1
        
        return time-1 if count == 0 else -1
            
