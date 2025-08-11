class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n = len(mat[0])
        queue = []
        for i in range(0,m):
            for j in range(0,n):
                if mat[i][j] == 0:
                    queue.append([i,j])
                if mat[i][j]:
                    mat[i][j] = 10**4 +1
        
        while(len(queue)):
            i = queue[0][0]
            j = queue[0][1]
            #left
            if j > 0 and mat[i][j-1] > mat[i][j] + 1:
                mat[i][j-1]  = mat[i][j] + 1
                queue.append([i,j-1])
            #Right
            if j < n-1 and mat[i][j+1] > mat[i][j] + 1:
                mat[i][j+1]  = mat[i][j] + 1
                queue.append([i,j+1])
            #top
            if i > 0 and mat[i-1][j] > mat[i][j] + 1:
                mat[i-1][j]  = mat[i][j] + 1
                queue.append([i-1,j])
            #bottom
            if i < m-1 and mat[i+1][j] > mat[i][j] + 1:
                mat[i+1][j]  = mat[i][j] + 1
                queue.append([i+1,j])
            queue.pop(0)
        
        return mat
                
print(Solution().updateMatrix([[1,1,1,1],[1,1,0,1],[1,1,1,1],[1,1,1,1]]))