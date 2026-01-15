'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.'''

'''intuition: We can use Depth-First Search (DFS) to traverse the grid. Whenever we encounter a '1', we increment our island count and use DFS to mark all connected '1's as '0's (visited). This way, we ensure that we only count each island once.'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverseIsland(grid,rows,cols,i,j):
            grid[i][j] = "0"

            #top
            if i>0 and grid[i-1][j] == "1":
                traverseIsland(grid,rows,cols,i-1,j)
            #bottom
            if i<rows-1 and grid[i+1][j] == "1":
                traverseIsland(grid,rows,cols,i+1,j)
            #left
            if j>0 and grid[i][j-1] == "1":
                traverseIsland(grid,rows,cols,i,j-1)
            #right
            if j<cols-1 and grid[i][j+1] == "1":
                traverseIsland(grid,rows,cols,i,j+1)

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count+=1
                    traverseIsland(grid,rows,cols, i,j)

        return count
