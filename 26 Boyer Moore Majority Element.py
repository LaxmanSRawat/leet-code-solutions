class Solution:
    def majorityElement(self, nums) -> int:
        candidate = 0
        frequency = 0
        
        for num in nums:
            if num == candidate:
                frequency+=1
            elif frequency > 1:
                frequency-=1
            else:
                candidate = num
                frequency = 1

        return candidate
    
print(Solution().majorityElement([1,3,4,5,6,4,3,21,2,4,5,6,3,3,22,4,66,7,43,3,3,5,3,3]))
        