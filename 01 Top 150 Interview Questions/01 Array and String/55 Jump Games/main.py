'''You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105'''

'''Intuition: We can use a greedy approach to solve this problem. We maintain a variable 'fuel' that represents the maximum number of steps we can still take from our current position. We start at the first index with an initial fuel equal to the value at that index. As we move through the array, we decrease our fuel by 1 for each step we take. If at any point our fuel becomes zero before reaching the last index, we cannot proceed further and return false. However, if we reach the last index or if our fuel allows us to reach it, we return true. This approach runs in O(n) time and uses O(1) space.'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = nums[0]
        i=0
        destination = len(nums)-1
        while(fuel >0 and i < destination):
            fuel -=1
            i+=1
            
            if i == destination:
                return True
            
            fuel = max(fuel,nums[i])
        
        return i == destination
        