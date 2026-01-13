'''Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).'''

'''Intuition: We can use the sliding window technique to solve this problem efficiently. We maintain a window defined by two pointers (left and right) and expand the right pointer to increase the sum until it meets or exceeds the target. Once the sum is sufficient, we try to shrink the window from the left side to find the minimum length that still satisfies the condition. We keep track of the minimum length found during this process.'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l = 0 
        r = 0
        sum = 0

        while(r<len(nums)):
            sum += nums[r]
            if sum >= target:
                min_len = min(min_len, r-l+1)
                
                while(l<r and sum >= target):
                    sum-=nums[l]
                    l+=1
                    if sum >= target:
                        min_len = min(min_len, r-l+1)
            r+=1
        if min_len == float('inf'):
            return 0
        else:
            return min_len