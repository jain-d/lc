# Reverse Linked List
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    next: Node | None = None

def reverse_list(head: Node | None) -> Node | None:
    if not head:
        return head

    past_node: Node | None = None
    while head:
        current = head
        head = head.next
        current.next = past_node
        past_node = current

    return past_node
