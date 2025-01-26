from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next# Helper function to create a linked list from a list

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        for i in range (n+1):
            first = first.next
        while first:
            first = first.next
            second  = second.next
        second.next = second.next.next
        return dummy.next
    


# Example usage
solution = Solution()
input_list = [1, 2, 3, 4, 5]  # Linked list: 1 -> 2 -> 3 -> 4 -> 5
n = 2  # Remove the 2nd node from the end
head = create_linked_list(input_list)
updated_head = solution.removeNthFromEnd(head, n)
result = linked_list_to_list(updated_head)
print(result)  # Should output: [1, 2, 3, 5]