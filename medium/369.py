"""
Given a non-negative number represented as a singly linked list of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
Example:
Input:
1->2->3
Output:
1->2->4
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def plusOne(node):
    if not node:
        return ListNode(1)
    node = reverse(node)
    carrier = 1
    head = node
    while head:
        carrier += head.val
        head.val = carrier % 10
        carrier /= 10
        tail = head
        head = head.next
    if carrier == 1:
        tail.next = ListNode(1)
    return reverse(node)

def reverse(node):
    dummy = ListNode(0)
    while node:
        next_node = dummy.next
        dummy.next = node
        node = node.next
        dummy.next.next = next_node
    return dummy.next
