# Reorder List
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next: ListNode | None = None


def reorder_list(head: ListNode) -> None:
    if not head.next:
        return

    node_stack: list[int] = []
    copy = head
    while copy:
        node_stack.append(copy)
        copy = copy.next

    reformat = head

    while True:
        if reformat == node_stack[-1]:
            reformat.next = None
            return
        elif reformat.next == node_stack[-1]:
            reformat.next.next = None
            return

        node_stack[-1].next = reformat.next
        reformat.next = node_stack.pop()
        reformat = reformat.next.next


input_one = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
input_two = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
inputs = (input_one, input_two)

for input_list in inputs:
    print(input_list)
    reorder_list(input_list)
    print(input_list,  end="\n\n")
