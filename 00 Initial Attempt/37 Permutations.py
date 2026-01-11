from collections import deque
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        set_nums = set()
        result = []
        def DFS(nums, set_nums, result, current_combination):
            for num in nums:
                print(num,set_nums,current_combination,result)
                if num not in set_nums:
                    current_combination.append(num)
                    set_nums.add(num)
                    if len(current_combination) == len(nums):
                        result.append(list(current_combination))
                        print(num,set_nums,current_combination,result)
                    else:
                        DFS(nums,set_nums,result,current_combination)
                    set_nums.remove(num)
                    current_combination.pop()
        
        DFS(nums,set_nums,result,[])
        return result

print(Solution().permute([1]))