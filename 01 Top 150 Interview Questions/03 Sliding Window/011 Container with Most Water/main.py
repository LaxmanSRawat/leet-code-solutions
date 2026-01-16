'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104'''

'''intuition: We can use the two-pointer technique to solve this problem efficiently. We start with two pointers, one at the beginning and one at the end of the array. We calculate the area formed by the lines at these two pointers and update the maximum area if the current area is larger. Then, we move the pointer pointing to the shorter line inward, as moving the longer line inward cannot increase the area. We repeat this process until the two pointers meet.'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        capacity = 0

        while(l<r):
            capacity = max(capacity, min(height[l],height[r])*(r-l))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return capacity