# Remove Linked List Element
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None

def remove_element(head: ListNode, val: int) -> ListNode:
    current = head
    prev: ListNode | None = None
    while current:
        if current.val == val:
            if prev:
                prev.next = current.next
            else:
                head = current.next
        else:
            prev = current
        current = current.next

    return head
