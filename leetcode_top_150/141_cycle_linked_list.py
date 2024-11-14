from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Example usage:
# Create nodes for a linked list with a cycle
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Link nodes to form a cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle

# Check for cycle
solution = Solution()
print(solution.hasCycle(node1))  # Expected output: True

# Create nodes for a linked list without a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

# Check for cycle in a non-cyclic list
print(solution.hasCycle(node1))  # Expected output: False
