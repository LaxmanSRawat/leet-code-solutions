# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        end = head
        current_length = 1
        while(True):
            count = 0
            prev_end = end
            while(end.next and count < current_length):
                end = end.next
                count +=1
            if(end.next == None and count < current_length):
                if current_length>1:
                    for _ in range((count)//2+1):
                        mid = mid.next
                    return mid.val
                else:
                    return end.val
            mid = prev_end
            
            current_length *= 2

# print(Solution().middleNode(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, ListNode(6,ListNode(7,ListNode(8,ListNode(9,ListNode(10,ListNode(11)))))))))))))
print(Solution().middleNode(ListNode(1)))
            
            
        
