'''
Problem: Merge Two Sorted List
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

#Create the blueprint of our node,
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def twoSortedList(List1, List2):
        # I will need two pointers, one at the head of each list
        dummy = Node(0)
        curr = dummy
        pointer1 = List1
        pointer2 = List2


        while pointer1 and pointer2:
            # I need to create a new list, creating nodes
            if pointer1.val < pointer2.val:
                curr.next = pointer1
                pointer1 = pointer1.next

            else:
                curr.next = pointer2
                pointer2 = pointer2.next
            curr = curr.next

        if pointer1:
            curr.next = pointer1  # If List1 has remaining nodes, append them
        elif pointer2:
            curr.next = pointer2


        return dummy.next

    def printLinkedList(Node):
        while Node:
            print(Node.val, end="-->")
            Node = Node.next




        # I would like to compare each of the nodes at the inital position and so on

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3

node4 = Node(4)
node5 = Node(5)
node4.next = node5
node6 = Node(6)
node5.next = node6

solution = Solution.twoSortedList(node1, node4)
Solution.printLinkedList(solution)



