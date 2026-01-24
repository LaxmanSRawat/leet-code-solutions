'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.'''

'''intuition: To add two numbers represented by linked lists, we can traverse both lists simultaneously, adding corresponding digits along with any carry from the previous addition. We create a new linked list to store the result. If one list is shorter, we continue adding the remaining digits of the longer list along with the carry. If there's a carry left after processing both lists, we add a new node for it at the end of the result list.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode()
        start = node
        carry = 0

        while(l1 and l2):
            sum = l1.val + l2.val + carry
            node.next = ListNode(sum%10)
            carry = sum//10
            node = node.next
            l1 = l1.next
            l2 = l2.next

        
        while(l1):
            sum = l1.val+ carry
            node.next = ListNode(sum%10)
            carry = sum//10
            node = node.next
            l1 = l1.next
        
        while(l2):
            sum = l2.val+ carry
            node.next = ListNode(sum%10)
            carry = sum//10
            node = node.next
            l2 = l2.next
        
        if carry:
            node.next = ListNode(1)

        return start.next