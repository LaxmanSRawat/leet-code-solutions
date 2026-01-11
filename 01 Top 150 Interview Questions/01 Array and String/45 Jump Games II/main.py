'''You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].'''

'''Intuition: To solve the problem of finding the minimum number of jumps to reach the last index, we can use a greedy approach. We maintain three variables: 'jumps' to count the number of jumps made, 'farthest' to track the farthest index we can reach with the current number of jumps, and 'boundary' to mark the end of the current jump range. As we iterate through the array, we update 'farthest' with the maximum reachable index from the current position. When we reach the 'boundary', it means we need to make another jump, so we increment 'jumps' and update 'boundary' to 'farthest'. This way, we ensure that we are always making the optimal jumps to reach the end of the array in the minimum number of steps. This approach runs in O(n) time and uses O(1) space.
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps= 0
        farthest = 0
        boundary = 0


        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])

            if(i==boundary):
                jumps+=1
                boundary = farthest
        
        return jumps
            


        