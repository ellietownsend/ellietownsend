'''
We have a fast pointer that traverses two at a time, and one that is always halfway behind it.
How do we find if it has a cycle: The fast pointer will eventually catch up to the slow pointer
We can alter speed
'''

# Must initialize two pointers

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        # Traverse the list using two pointers
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

            # If the two pointers meet, there's a cycle
            if slow == fast:
                entry = head
                while entry!=slow:
                    entry = entry.next
                    slow = slow.next
                return True

        # If the fast pointer reaches the end, there's no cycle
        return None

# Test case 1: Linked List without a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

# Test case 2: Linked List with a cycle
node5 = ListNode(1)
node6 = ListNode(2)
node7 = ListNode(3)
node8 = ListNode(4)

node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node6  # Creates a cycle


solution = Solution()

print("Test Case 1: ", solution.hasCycle(node1))


print("Test Case 2: ", solution.hasCycle(node5))