class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return binary_search(nums,0,len(nums)-1,target)
    
def binary_search(array, left, right,target):
    
    mid = (left+right)//2
    # print(array, left, right,target,mid,array[left],array[right],array[mid])
    if array[mid] == target:
        # print("here",mid)
        return mid
    if left == mid:
        if array[right] == target:
            return right
        return -1
    if array[mid]> target:
        index = binary_search(array,left,mid,target)
    else:
        index = binary_search(array,mid,right,target)
    return index

solution_obj = Solution()
print(solution_obj.search([2,5],5))
print(solution_obj.search([-1,0,3,5,9,12],2))
print(solution_obj.search([-1,0,3,5,9,12],9))
print(solution_obj.search([2],5))
print(solution_obj.search([2],2))