# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        result =[]
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result) + " -> None"

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        print("list1",list1)
        print("list2",list2)
        current_list1_node = list1
        current_list2_node = list2

        result_list = ListNode()
        result_list_head = result_list
        
        while(True):
            print("current_list1_node",current_list1_node)
            print("current_list2_node",current_list2_node)
            print("result_list_head",result_list_head)
            if current_list1_node == None and current_list2_node == None:
                return result_list_head.next
             
            if current_list1_node == None:
                result_list.next = current_list2_node

                return result_list_head.next
                 
            elif current_list2_node == None:
                result_list.next = current_list1_node
                return result_list_head.next
            
            else:
                print(current_list2_node.val, current_list1_node.val, )
                if current_list2_node.val < current_list1_node.val:
                    result_list.next = ListNode(current_list2_node.val)
                    result_list = result_list.next
                    current_list2_node = current_list2_node.next
                    
                else:
                    result_list.next = ListNode(current_list1_node.val)
                    result_list = result_list.next
                    current_list1_node = current_list1_node.next
              

Node_1_1 = ListNode(4)
Node_1_2 = ListNode(2,Node_1_1)
Node_1_3 = ListNode(1,Node_1_2)

Node_2_1 = ListNode(4)
Node_2_2 = ListNode(3,Node_2_1)
Node_2_3 = ListNode(1,Node_2_2)

solution_object = Solution()
print(solution_object.mergeTwoLists(Node_1_3,Node_2_3))