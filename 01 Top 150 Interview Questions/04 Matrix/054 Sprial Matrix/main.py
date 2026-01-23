'''Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100'''

'''intuition: To traverse a matrix in spiral order, we can maintain four boundaries (top, bottom, left, right) that define the current layer of the matrix we are traversing. We start from the top-left corner and move right until we hit the right boundary, then move down, left, and up, adjusting the boundaries inward after completing each direction. We continue this process until we have visited all elements in the matrix.'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_limit = -1
        bottom_limit = len(matrix)
        left_limit = -1
        right_limit = len(matrix[0])
        cell_count = bottom_limit * right_limit
        i,j = 0,0

        result = []

        direction = {"right": [0,1],  "left": [0,-1], "up" : [-1,0], "down" : [1,0]}
        next_direction = {"right": "down", "down" : "left", "left": "up", "up": "right"}
        current_direction = "right"
        
        while(len(result)<cell_count):
            result.append(matrix[i][j])

            next_i,next_j = i+direction[current_direction][0], j+direction[current_direction][1]

            if next_i>top_limit and next_i < bottom_limit and next_j>left_limit and next_j < right_limit:
                i,j = next_i, next_j
            else:
                current_direction = next_direction[current_direction]
                if (next_j>=right_limit):
                    top_limit+=1
                elif(next_j <= left_limit):
                    bottom_limit -=1
                elif(next_i <= top_limit):
                    left_limit +=1
                elif(next_i>=bottom_limit):
                    right_limit-=1
                next_i,next_j = i+direction[current_direction][0], j+direction[current_direction][1]
                i,j = next_i, next_j
        
        return result
