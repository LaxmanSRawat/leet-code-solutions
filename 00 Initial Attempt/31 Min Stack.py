class ListNode(object):
    def __init__(self, val,next, curr_min = None):
        self.val = val
        if curr_min != None:
            self.min = min(val,curr_min)
        else:
            print('here',self.val)
            self.min = val
        self.next = next

class MinStack(object):

    def __init__(self):
        self.root_node = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.root_node:
            print("here 1")
            new_node = ListNode(val,self.root_node,self.root_node.min)
            
        else:
            print("here 2")
            new_node = ListNode(val,self.root_node)
        self.root_node = new_node

        
    def pop(self):
        """
        :rtype: None
        """
        if self.root_node:
            self.root_node = self.root_node.next
        

    def top(self):
        """
        :rtype: int
        """
        return self.root_node.val

        

    def getMin(self):
        """
        :rtype: int
        """
        return self.root_node.min


# Your MinStack object will be instantiated and called as such:
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())
# minStack.pop()
# print(print(minStack.top())())
# print(minStack.getMin())


minStack = MinStack()
minStack.push(0)
print(minStack.getMin())
minStack.push(1)
print(minStack.getMin())
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
minStack.push(-2)
minStack.push(-1)
minStack.push(-2)
print(minStack.getMin())
minStack.pop()
print(minStack.top()) 
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()