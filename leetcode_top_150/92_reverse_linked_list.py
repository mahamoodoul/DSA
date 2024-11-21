class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    # Create a dummy node to make handling edge cases easier
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move `prev` pointer to one node before the `left` position
    for _ in range(left - 1):
        prev = prev.next

    # `start` is the first node to be reversed, `then` is the node that will be moved
    start = prev.next
    then = start.next

    # Reverse the sublist between `left` and `right`
    for _ in range(right - left):
        start.next = then.next
        then.next = prev.next
        prev.next = then
        then = start.next

    return dummy.next

# Example usage
# Input: 1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4
# Output: 1 -> 4 -> 3 -> 2 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

left, right = 2, 4
reversed_head = reverseBetween(head, left, right)

# Print the reversed list
curr = reversed_head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
