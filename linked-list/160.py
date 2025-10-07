# Intersection of Two Linked List
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next: ListNode | None = None

# Solution One
def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode | None:
    address_store = set()

    copy_a = head_a
    while copy_a:
        address_store.add(id(copy_a))
        copy_a = copy_a.next

    copy_b = head_b
    while copy_b:
        if id(copy_b) in address_store:
            return copy_b
        copy_b = copy_b.next
