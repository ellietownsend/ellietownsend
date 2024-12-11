'''
Given the head of a sorted linked list, delete all duplicates such that each element
appears only once. Return the linked list sorted as well.
'''



class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution(object):
    def removeDups(L1):
        #Edge case:
        if not L1:
            return None
        # Use two pointers for comparison
        p1 = L1.next
        # Want the first one to be one step ahead of second
        p2 = L1
        while p1:
            #p1 because I want to make it to the very end of the list
            if p1.val == p2.val:
                #Process of node deletion: set the current.next pointer to the node after deletion
                #Have to be careful about: .next.next exists
                #Going to delete the second duplicate, do not have to worry about deleting head
                p2.next = p1.next
            else:
                p2 = p2.next

            p1 = p1.next


        #To print a linkedlist we have to iterate all the way though

        current = L1
        while current:
            print(current.val, end=" -> ")
            current = current.next



node1 = Node(1)
node2 = Node(1)
node1.next = node2
node3 = Node(2)
node2.next = node3
node4 = Node(3)
node3.next = node4
node5 = Node(3)
node4.next = node5

solution = print(Solution.removeDups(node1))