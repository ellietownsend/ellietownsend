'''
Problem:
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''


# Going to need to make a node blueprint for our linked List
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def removeElem(head, num):
        #Edge case: List is empty
        if not head:
            return None
        #Making a dummy node to simplify head removal:
        dummy = Node(0)
        #Connecting out new node to the list given
        dummy.next = head

        current = dummy
        # Need to traverse to look for this number, start at our created node
        while current.next:
            if current.next.val == num: #Checking the node after the one were at
                #remove that node
                current.next = current.next.next
            else: #The first handles the pointer if we need to move it
                current = current.next


        pointer2 = dummy.next
        while pointer2:
            print(pointer2.val, end="-->")
            pointer2 = pointer2.next

    #Need a way to iterate through the linked list




node = Node(4)
node1 = Node(5)
node.next = node1
node2 = Node(6)
node1.next = node2
node3 = Node(1)
node2.next = node3
node4 = Node(5)
node3.next = node4
solution = Solution.removeElem(node,5)


