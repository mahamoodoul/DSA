# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        current = dummy_node
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current_digit = total % 10

            current.next = ListNode(current_digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next node after the dummy node, as it holds the actual result
        return dummy_node.next







node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
l2 = [5,6,4]