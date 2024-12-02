class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def NthNodeDeletionEnd(head, n):
        pointer1 = head
        pointer2 = head
        count = 0
        # First priority, find the nth node from the end, with a singly linked list we traverse from the end
        for _ in range(n):
            pointer1 = pointer1.next

        while pointer1:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            count +=1

        entry = head
        for _ in range(count -1):
            entry = entry.next

        if entry.next and entry.next.next: # Always want to avoid a null pointer error
            entry.next = entry.next.next

        while head:
            print(head.val)
            head = head.next

#Second Attempt:
class Solution2:
  def removeNthFromEnd(self, head, n):
    slow = head
    fast = head

    for _ in range(n):
      fast = fast.next
    if not fast:
      return head.next

    while fast.next:
      slow = slow.next
      fast = fast.next
    slow.next = slow.next.next

    return head



node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5
n = 2
soultion = print(Solution.NthNodeDeletionEnd(node1, n))








        # 2 pointers, because were looking at two parts at once


