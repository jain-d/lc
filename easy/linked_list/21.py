from typing import Optional


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        newNode = ListNode(value)
        self.head = newNode
        self.length = 1

    def append(self, value):
        newNode = ListNode(value)
        if self.length == 0:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
            newNode.next = None
        self.length += 1

    def print_list(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    merged_list = ListNode(0)
    pointer = merged_list
    print(pointer.value)
    temp1 = list1
    temp2 = list2

    while temp1.value or temp2.value:
        if temp1.value == temp2.value:
            pointer.next = temp1
            pointer = pointer.next
            pointer.next = temp2
        else:
            if temp1.value < temp2.value:
                pointer.next = temp1
                temp1 = temp1.next
            elif temp1.value > temp2.value:
                pointer.next = temp2
                temp2 = temp2.next
            else:
                if temp1.value:
                    pointer.next = temp1
                    temp1 = temp1.next
                elif temp2.value:
                    pointer.next = temp2
                    temp2 = temp2.next
                pointer = pointer.next

    return merged_list.next


def print_list(node: ListNode):
    if not node:
        return None
    else:
        temp = node
        while temp:
            print(temp.value)
            temp = temp.next


list1 = [1, 2, 4]
list2 = [1, 3, 4]

linked_list_one = LinkedList(list1[0])
linked_list_two = LinkedList(list2[0])

for i in range(1, len(list1)):
    linked_list_one.append(list1[i])

for i in range(1, len(list2)):
    linked_list_two.append(list2[i])

merged_list = mergeTwoLists(linked_list_one.head, linked_list_two.head)

print_list(merged_list)
