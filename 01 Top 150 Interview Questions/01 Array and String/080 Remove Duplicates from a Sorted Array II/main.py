'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
'''

'''
Intuition: Similar to the previous problem of removing duplicates from a sorted array, but here we allow each unique element to appear at most twice. We can use a pointer to track the position of the last allowed element and a flag to indicate whether we have already included a duplicate.
An alternative apporach is to allow first two elements by default and then start checking from the third element onwards. If the current element is not equal to the element at position k-2, we can include it.
'''

class Solution:
    def removeDuplicates(self, nums) -> int:
        k=1
        is_allowed = True
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                k+=1
                is_allowed = True
                nums[k-1] = nums[i]
                print(nums[k], nums[i],i,k)
            else:
                if is_allowed:
                    k+=1
                    is_allowed = False
                    nums[k-1] = nums[i]
                    print(nums[k], nums[i],i,k)
        return nums[:k]

print(Solution().removeDuplicates([1,1,1,2,2,3])) 