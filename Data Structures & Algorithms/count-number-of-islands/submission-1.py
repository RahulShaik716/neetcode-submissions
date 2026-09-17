class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows,cols = len(grid),len(grid[0])
        count = 0 

        def dfs(r,c):
            if ((r,c) in visited or r not in range(rows) or c not in range(cols)):
                return 
            visited.add((r,c))
            if r+1 in range(rows) and c in range(cols) and grid[r+1][c] == "1":
                dfs(r+1,c)
            if r-1 in range(rows) and c in range(cols) and grid[r-1][c] == "1":
                dfs(r-1,c)
            if r in range(rows) and c+1 in range(cols) and grid[r][c+1] == "1":
                dfs(r,c+1)
            if r in range(rows) and c-1 in range(cols) and grid[r][c-1] == "1":
                dfs(r,c-1)

                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count+=1
                    dfs(r,c)
        return count