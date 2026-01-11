class Solution:
    def productExceptSelf(self, nums):
        product = 1

        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] *= product
            product *= nums[i]
        
        product =1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= product
            product *= nums[i]
        

        # forward_products = [1]* (len(nums) + 1)
        # backward_products = [1]* (len(nums) + 1)
        # for i in range(len(nums)):
        #     product *= nums[i]
        #     forward_products[i+1] = product
        
        # print(product,forward_products)
        # for i in range(len(nums)-1, -1,-1):
        #     backward_products[i] = backward_products[i+1]*nums[i]  
        #     if nums[i] >= 0:          
        #         result[i] = product - forward_products[i]*backward_products[i+1]*(nums[i]-1)
        #     else:
        #         result[i] = product + forward_products[i]*backward_products[i+1]*(abs(nums[i])+1)

        #     print(i,nums[i]-1)
        
        return result

print(Solution().productExceptSelf([-1,1,0,-3,3]))


        
        