# Copy List with Random Pointer
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    next: Node | None = None
    random: Node | None = None


def copy_random_list(head: Node) -> Node:
    new_list = Node(0) if head else None
    new_pointer = new_list
    mapping_record: dict[int, Node] = {}
    unfound_nodes_record: dict[int, [Node]] = {}
    while head:
        new_pointer.val = head.val
        mapping_record.update({id(head): new_pointer})
        new_pointer.next = Node(0) if head.next else None

        if head.random:
            if id(head.random) in mapping_record:
                new_pointer.random = mapping_record.get(id(head.random))
            elif id(head.random) in unfound_nodes_record:
                (unfound_nodes_record.get(id(head.random))).append(new_pointer)
            else:
                unfound_nodes_record.update({id(head.random): [new_pointer, ]})
        else:
            new_pointer.random = None

        if id(head) in unfound_nodes_record:
            for node in unfound_nodes_record.get(id(head)):
                node.random = new_pointer
            unfound_nodes_record.pop(id(head))

        head = head.next
        new_pointer = new_pointer.next

    return new_list



list_one = Node(7)
list_two = Node(13)
list_three = Node(11)
list_four = Node(10)
list_five = Node(1)
list_one.next = list_two
list_one.random = None
list_two.next = list_three
list_two.random = list_one
list_three.next = list_four
list_three.random = list_five
list_four.next = list_five
list_four.random = list_three
list_five.random = list_one

head_node = list_one

retrived_list = copy_random_list(head_node)
flag = True
while retrived_list:
    if head_node and (retrived_list.val == head_node.val and retrived_list is not head_node):
        if (retrived_list.random and head_node.random) and (retrived_list.random.val == head_node.random.val and retrived_list.random is not head_node.random):
            pass
        elif retrived_list.random == head_node.random == None:
            pass
        else:
            flag = False
    retrived_list = retrived_list.next
    head_node = head_node.next
if flag:
    print("\033[32mPASS\033[0m")
else:
    print("\033[31mFAIL\033[0m")

# Testing linked lists deepcopies 
"""
@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None


def copy_list(head: ListNode) -> ListNode:
    new_list: ListNode | None = ListNode() if head else None
    new_pointer = new_list
    while head:
        new_pointer.val = head.val
        new_pointer.next = head.next if not head.next else ListNode()
        new_pointer = new_pointer.next
        head = head.next

    return new_list



head_node = ListNode(5, ListNode(4, ListNode(3, ListNode(2, None))))
new_list = copy_list(None)
flag = True
while new_list:
    if new_list.val == head_node.val and new_list is not head_node:
        pass
    else:
        print("\033[31mFAIL\033[0m")
        flag = False
        break
    new_list = new_list.next
    head_node = head_node.next

if flag:
    print("\033[32mPASS\033[0m")
"""
