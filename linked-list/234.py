# Palindrome Linked List
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None


# Solution One
def is_palindrome(head: ListNode) -> bool:
    list_for_linked_list: list[int] = []
    copy_head = head
    while copy_head:
        list_for_linked_list.append(copy_head.val)
        copy_head = copy_head.next

    i, j = 0, len(list_for_linked_list) - 1
    while i <= j:
        if list_for_linked_list[i] != list_for_linked_list[j]:
            return False

    return True
