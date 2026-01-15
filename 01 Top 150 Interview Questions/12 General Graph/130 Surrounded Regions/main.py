'''You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.'''

'''intuition: We can use Depth-First Search (DFS) to mark all 'O's connected to the border as safe (not to be flipped). We can temporarily change these 'O's to a different character (like 'S') during the DFS. After marking, we can iterate through the board again to flip all remaining 'O's to 'X's (as they are surrounded) and convert 'S's back to 'O's.'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

        def dfs(i,j,rows,cols,board):
            if (i<0 or i>=rows or j<0 or j>=cols or board[i][j] != "O"):
                return
            
            board[i][j] = "S"

            dfs(i+1,j,rows,cols,board)
            dfs(i-1,j,rows,cols,board)
            dfs(i,j+1,rows,cols,board)
            dfs(i,j-1,rows,cols,board)
        
        for i in range(rows):
            for j in range(cols):
                if ((i in [0,rows-1]) or (j in [0,cols-1])) and board[i][j] == "O":
                    dfs(i,j,rows,cols,board)
        
        for i in range(rows):
            for j in range(cols):
                if(board[i][j]=="S"):
                    board[i][j] = "O"
                elif(board[i][j]=="O"):
                    board[i][j] = "X"