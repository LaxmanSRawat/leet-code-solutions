'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)'''

'''Intuition: To solve the problem without using division and in O(n) time, we can use two passes through the array. In the first pass, we calculate the prefix product for each element and store it in the output array. In the second pass, we calculate the suffix product and multiply it with the corresponding prefix product in the output array. This way, each element in the output array will be the product of all elements except itself. We can achieve O(1) extra space complexity by using the output array to store the results.'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1 for _ in range(n)]
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer          