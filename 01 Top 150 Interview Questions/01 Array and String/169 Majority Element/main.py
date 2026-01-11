'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

'''Intuition: We can use the Boyer-Moore Voting Algorithm to find the majority element in linear time and constant space. The idea is to maintain a count of the current candidate for the majority element. When we encounter the same element, we increment the count; when we encounter a different element, we decrement the count. If the count reaches zero, we select a new candidate. Since the majority element appears more than n/2 times, it will remain as the candidate at the end.'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element=nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count > 0:
                if nums[i] == majority_element:
                    count +=1
                else:
                    count -=1
            else:
                majority_element = nums[i]
                count =1
        return majority_element