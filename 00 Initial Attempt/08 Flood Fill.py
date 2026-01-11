class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        
        if n == 0:
            return image
        
        array = [0] *m*n
        original_color = image[sr][sc]
        
        image,array= floodFill(image,sr,sc,color,original_color,m,n,array)
        return image

def floodFill(image,x,y,color,original_color,m,n,array):
    print(image,x,y,color,original_color,m,n,array)
    if (array[n*x + y]):
        return image,array
    
    if(image[x][y]==original_color):
        print("change color")
        image[x][y] = color
        array[n*x + y] = 1
        print(image,x,y,color,original_color,m,n,array)
        
        # left
        if(y!= 0 and (not array[n*x + (y-1)]) ):
            print("left")
            image,array = floodFill(image,x,y-1,color,original_color,m,n,array)
            print(array)
        # right
        if(y!=n-1 and (not array[n*x + (y+1)])):
            print("right")
            image,array = floodFill(image,x,y+1,color,original_color,m,n,array)
        #top
        if(x!= 0 and (not array[n*(x-1) + y])):
            print("top")
            image,array = floodFill(image,x-1,y,color,original_color,m,n,array)
        #bottom
        if(x!= m-1 and (not array[n*(x+1) + y])):
            print("bottom")
            image,array = floodFill(image,x+1,y,color,original_color,m,n,array)
    return image,array

solObj = Solution()
print(solObj.floodFill([[0,0,0],[0,0,0]],0,0,2))