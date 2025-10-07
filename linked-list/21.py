# Merge Two Sorted Lists
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None

def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode:
    new_list = ListNode()
    current = new_list
    while list1 or list2:
        if not list1:
            current.next = list2
            break
        elif not list2:
            current.next = list1
            break

        if list1.val <= list2.val:
            current.next = ListNode(list1.val)
            list1 = list1.next
            current = current.next
            continue
        if list2.val <= list1.val:
            current.next = ListNode(list2.val)
            list2 = list2.next
            current = current.next

    new_list = new_list.next
    return new_list

list_one = ListNode(1, ListNode(2, ListNode(4)))

list_two = ListNode(1, ListNode(3, ListNode(4)))

list_three = merge_two_lists(list_one, list_two)
print(list_three)
answer = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

flag = True
while list_three and answer:
    print("second loop")
    if list_three.val == answer.val:
        list_three = list_three.next
        answer = answer.next
        continue
    flag = False

print("\033[32mPASS" if flag else "\033[31FAIL")
