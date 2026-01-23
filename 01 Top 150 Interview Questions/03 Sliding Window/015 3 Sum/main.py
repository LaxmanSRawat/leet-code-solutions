'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105'''

'''
intuition: To solve the 3Sum problem, we can sort the input array and then use a two-pointer technique to find pairs that sum up to the negative of the current element. We iterate through the sorted array, and for each element, we set two pointers: one starting just after the current element and the other at the end of the array. We then check the sum of the three elements. If the sum is zero, we add the triplet to our result list and move both pointers inward while skipping duplicates. If the sum is less than zero, we move the left pointer to the right to increase the sum. If the sum is greater than zero, we move the right pointer to the left to decrease the sum. This process continues until all unique triplets are found.'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        i=0
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            while(j < k):
                total = nums[i]+nums[j]+nums[k]
                if total  == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<=k and nums[j] == nums[j-1]):
                        j+=1
                    while(j<=k and nums[k] == nums[k+1]):
                        k-=1
                elif total <0:
                    j+=1
                else:
                    k-=1
                    
        return result
