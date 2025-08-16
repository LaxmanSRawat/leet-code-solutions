from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        for i in range(0, m):
            for j in range(0,n):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    grid[i][j] = float("inf")
        
        while(queue):
            cell = queue.popleft()
            i,j = cell[0], cell[1]

            #top
            if i-1 >= 0 and grid[i-1][j]>grid[i][j]+1:
                grid[i-1][j] = grid[i][j]+1
                queue.append([i-1,j])

            #bottom
            if i+1 < m and grid[i+1][j]>grid[i][j]+1:
                grid[i+1][j] = grid[i][j]+1
                queue.append([i+1,j])

            #left
            if j-1 >= 0 and grid[i][j-1]>grid[i][j]+1:
                grid[i][j-1] = grid[i][j]+1
                queue.append([i,j-1])

            #right
            if j+1 < n and grid[i][j+1]>grid[i][j]+1:
                grid[i][j+1] = grid[i][j]+1
                queue.append([i,j+1])


        max_minute = grid[i][j]
        for i in range(0, m):
            for j in range(0,n):
                max_minute = max(max_minute, grid[i][j])
        if max_minute == float('inf'):
            return -1
        return max_minute

# grid = [[2,1,1],
#         [1,1,0],
#         [0,1,1]] #expected output = 4
# # grid = [[2,1,1],
# #         [0,1,1],
# #         [1,0,1]] #expected output = -1
# grid = [[0,2]] #expected output = 0
grid = [[2,1,1],
        [1,1,1],
        [0,1,2]] #expected output = 2
print(Solution().orangesRotting(grid))