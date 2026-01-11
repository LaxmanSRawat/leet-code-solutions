class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]
        
        sumNums = []
        smallest_negative_value = None

        for i in nums:
            if len(sumNums):
                if i < 0 and sumNums[-1] < 0:
                    sumNums[-1]+=i
                elif i < 0 and sumNums[-1] >= 0:
                    sumNums.append(i)
                elif i>=0 and sumNums[-1] >= 0:
                    sumNums[-1]+=i
                else:
                    sumNums.append(i)
            else:
                sumNums.append(i)
            
            if i < 0:
                if not smallest_negative_value or i>smallest_negative_value:
                    smallest_negative_value = i



        if len(sumNums) == 1:
            if sumNums[0] >= 0:
                return sumNums[0]
            else:
                return smallest_negative_value
        
        reset_flag = False
        last_largest_sum = 0
        current_largest_sum = 0
        print(sumNums)
        for i in range(0, len(sumNums)):
            print(i,sumNums[i],current_largest_sum,last_largest_sum,reset_flag)
            if sumNums[i]<0:
                if current_largest_sum > abs(sumNums[i]) and i != len(sumNums)-1 and sumNums[i+1]>abs(sumNums[i]):
                    current_largest_sum+=sumNums[i]
                else:
                    reset_flag = True
            else:
                current_largest_sum+=sumNums[i]
                reset_flag = False

            if current_largest_sum>last_largest_sum:
                    last_largest_sum = current_largest_sum

            if reset_flag:
                current_largest_sum = 0
            
        return last_largest_sum
            
print(Solution().maxSubArray([-9,-2,1,8,7,-6,4,9,-9,-5,0,5,-2,5,9,7]))