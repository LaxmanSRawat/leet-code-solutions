class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        print(nums)
        for i in range(0,len(nums)-2):
            
            j = i +1
            k = len(nums)-1
            
            if i>0 and nums[i] == nums[i-1]:
                continue

            while(j < k):
                print(i,j,k,nums[i],nums[j],nums[k])
                sum = nums[i]+nums[j]+nums[k]
                # if j>i+1 and nums[j] == nums[j-1]:
                #     j+=1
                #     continue
                # if k<len(nums) - 1 and nums[k] == nums[k+1]:
                #     k-=1
                #     continue
                if sum == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while(nums[j] == nums[j-1] and j<k):
                        j+=1
                elif sum > 0:
                    k -=1
                else:
                    j+=1
                
        return result
    

print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))