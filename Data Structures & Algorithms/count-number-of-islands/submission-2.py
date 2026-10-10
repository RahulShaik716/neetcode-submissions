class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])

        visited = set() 
        count = 0 
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c]!="1":
                return 
            
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
        return count



        