class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        visited = [0]*(m*n)
        island_count = 0 

        def traverseIsland(grid,i,j,m,n,visited):
            #traverse to right
            
            if j+1<n and grid[i][j+1] == '1' and not visited[i*(n)+(j+1)]:
                visited[i*(n)+(j+1)] = 1
                traverseIsland(grid,i,j+1,m,n,visited)
            #traverse to bottom
            if i+1<m and grid[i+1][j] == '1' and not visited[(i+1)*(n)+(j)]:
                visited[(i+1)*(n)+(j)] = 1
                traverseIsland(grid,i+1,j,m,n,visited)

        for i in range(0, m):
            for j in range(0,n):
                current_cell = i*(n) + j
                if not visited[current_cell] and grid[i][j] == '1':
                      print(i,j)
                      visited[current_cell] = 1
                      island_count +=1
                      traverseIsland(grid,i,j,m,n,visited)


        return island_count

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# grid = [["1","1","1"],
#         ["1","0","1"],
#         ["1","1","1"]]

grid = [["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]

print(Solution().numIslands(grid))