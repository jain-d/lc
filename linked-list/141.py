# Linked List Cycle
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next: ListNode | None = None

def has_cycle(head: ListNode) -> bool:
    address_set: set[int] = set()
    copy_head = head
    while copy_head:
        address = id(copy_head)
        if address in address_set:
            return True
        address_set.add(address)
        copy_head = copy_head.next
    return False
