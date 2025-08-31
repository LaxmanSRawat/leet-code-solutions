class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def searchTarget(nums,target,start,end):
            if start == end:
                if nums[start] == target:
                    return start
                else:
                    return -1


            mid = (start+end)//2

            if nums[mid] == target:
                return mid

            if (nums[start] <= nums[mid] and nums[start] <=target <nums[mid]) or (nums[start] > nums[mid] and (nums[start] <= target or nums[mid] > target)):
                return searchTarget(nums,target,start,mid)
            if (nums[mid] <= nums[end] and nums[mid] <target <=nums[end]) or (nums[mid] > nums[end] and (nums[mid] < target or nums[mid] >= target)):
                return searchTarget(nums,target,mid+1,end)

            return -1
                
        start = 0
        end = len(nums) - 1
        
        return searchTarget(nums,target,start,end)
    
# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1
 

print(Solution().search([4,5,6,7,0,1,2],0))
print(Solution().search([4,5,6,7,0,1,2],3))
print(Solution().search([1],0))
print(Solution().search([1,3],3))