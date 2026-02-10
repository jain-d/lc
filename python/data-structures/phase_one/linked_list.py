# 206. Reverse Linked List
from __future__ import annotations
from dataclasses import dataclass

"""
So the solution I see here is that we have to travel through the entire linked list. And as we do that, we keep on changing the order of the pointer of each node such that the past becomes next, we preserve the current and move the what was the next and we repeat, make the past as next for this node.

Here, we will have to maintain 2 states, on which holds the past (which will become next), and another which will hold the previously stored next (for us to progress forward).
We keep going until our next pointer is Not None.
Single Pass. O(n) complexity.
"""

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
