class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        visited = set() 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rows,cols = len(grid),len(grid[0])
        count = 0 
        

        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row,col = queue.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc 
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count+=1
                    bfs(i,j)
        return count