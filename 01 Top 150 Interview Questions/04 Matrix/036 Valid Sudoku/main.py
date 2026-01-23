'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.'''

'''intuition: To validate a Sudoku board, we can use three sets of data structures to keep track of the numbers we have seen so far in each row, column, and 3x3 sub-box. As we iterate through each cell in the board, we check if the number has already been seen in the corresponding row, column, or sub-box. If it has, we return false. If we finish checking all cells without finding any duplicates, we return true.'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        sqr_set = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                sqr = (i//3)*3 + j//3
                if val == ".":
                    continue
                if val in row_set[i] or val in col_set[j] or val in sqr_set[sqr]:
                    return False
                row_set[i].add(val)
                col_set[j].add(val)
                sqr_set[sqr].add(val)
        return True