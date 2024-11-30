# Create a node class, a node comes with the data and the next pointer
from itertools import filterfalse
from operator import truediv, index

from TwoPointer import solution


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None # Initally connecting the node to nothing, something we have to set later

class Solution(object):
    def cycle(self, headA, headB):
        length1 = 0
        currentA = headA
        while currentA:
            length1 +=1
            currentA = currentA.next

        length2 = 0
        currentB = headB
        while currentB:
            length2 += 1
            currentB = currentB.next


        if length1 > length2:
            for _ in range(length1 - length2):
                headA = headA.next

        elif length2 > length1:
            # Move headA to the point where both lists have equal length remaining
            for _ in range(length2 - length1):
                headB = headB.next

        while headA and headB:
            if headA.val == headB.val:
                return headA.val
            headA = headA.next
            headB = headB.next
        return None







node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node8




solution = Solution()
print("Test Case 3: ", solution.cycle(node1, node4))







