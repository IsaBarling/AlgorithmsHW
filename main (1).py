class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev
