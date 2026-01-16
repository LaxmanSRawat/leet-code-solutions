'''You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

 

Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1
 

Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 are not the starting points of any snake or ladder.'''

'''intuition: We can use Breadth-First Search (BFS) to explore the board level by level. Each level in the BFS represents a dice roll. From each cell, we can move to the next 6 cells (representing the possible outcomes of a dice roll). If we encounter a snake or ladder, we move to its destination. We keep track of visited cells to avoid cycles. The first time we reach the last cell, we return the number of dice rolls taken to get there. If we exhaust all possibilities without reaching the last cell, we return -1.'''

from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        print(n)
        target = n*n
        q = deque()
        q.append(1)
        count = 0
        visited = set()

        def getcell(cell, n):
            i = n - 1 -(cell-1)//n
            
            if (n-1-i)%2 == 0:
                j = (cell-1)%n 
            else:
                j = n-1-(cell-1)%n

            return i, j

        while q:
            for _ in range(len(q)):
                cell = q.popleft()
                
                if cell == target:
                    return count
                
                for dice in range(1, 7):
                    next_cell = cell + dice
                    
                    if next_cell > target:
                        break
                    
                    i, j = getcell(next_cell, n)
                    if board[i][j] != -1:
                        next_cell = board[i][j]
                    
                    if next_cell not in visited:
                        visited.add(next_cell)
                        q.append(next_cell)
            
            count += 1

        return -1 