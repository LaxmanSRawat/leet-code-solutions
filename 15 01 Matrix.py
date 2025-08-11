class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n = len(mat[0])
        
        loop_count = 1
        result = [[0]*n for _ in range(m)]
        complete = False
        while(not complete):
            complete = True
            for i in range (0,m):
                for j in range(0,n):
                    if mat[i][j]:
                        complete = False
                        #left
                        if j>0 and mat[i][j-1] == 0:
                            result[i][j] = loop_count
                            
                        #right
                        elif j<n-1 and mat[i][j+1] == 0:
                            result[i][j] = loop_count

                        #top
                        elif i>0 and mat[i-1][j] == 0:
                            result[i][j] = loop_count

                        #bottom
                        elif i<m-1 and mat[i+1][j] == 0:
                            result[i][j] = loop_count


            for i in range (0,m):
                for j in range(0,n):
                    if result[i][j] == loop_count:
                        mat[i][j] = 0
            
            loop_count+=1
        return result

print(Solution().updateMatrix([[1,1,1,1],[1,1,0,1],[1,1,1,1],[1,1,1,1]]))