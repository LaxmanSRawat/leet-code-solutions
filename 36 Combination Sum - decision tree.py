from collections import deque
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def recursiveTraverse(candidates,start_index,target,sum, stack,result):
            for index in range(start_index, len(candidates)):
                print(start_index,stack,index,candidates[index])
                if (sum + candidates[index]) == target:
                    stack.append(candidates[index])
                    result.append(list(stack))
                    stack.pop()
                    return 
                elif (sum + candidates[index]) > target:
                    return
                else:
                    stack.append(candidates[index])
                    sum = sum + candidates[index]
                    recursiveTraverse(candidates,index,target,sum,stack,result)
                    sum = sum - candidates[index]
                    stack.pop()

        result = []

        candidates.sort()

        sum = 0
        stack = deque()
        recursiveTraverse(candidates,0,target,sum,stack,result)
        
        return result
            




print(Solution().combinationSum([2,3,5],8))
# print(Solution().combinationSum([18,34,2,16,25,6,35],20))