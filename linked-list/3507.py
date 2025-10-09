# Minimum Pair Removal to Sort Array I
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None
    prev: ListNode | None = None

class Solution:
    def minimum_pair_removal(self, nums: list[int]) -> int:
        array_list: ListNode = ListNode()
        array_pointer = array_list
        sum_list: ListNode = ListNode()
        sum_pointer = sum_list
        needs_work = False
        steps = 0
        for index, value in enumerate(nums):
            if not index:
                array_list.val = value
                array_list.prev = None
            else:
                array_pointer.next = ListNode(value)
                if not array_pointer.val <= value:
                    needs_work = True
                sum_pointer.next = ListNode(array_pointer.val + array_pointer.next.val)
                sum_pointer.next.prev = sum_pointer
                sum_pointer = sum_pointer.next
                array_pointer.next.prev = array_pointer
                array_pointer = array_pointer.next
        sum_list = sum_list.next
        if sum_list:
            sum_list.prev = None
        
        if not needs_work:
            return steps

        while sum_list:
            steps += 1
            array_pointer = array_list
            sum_pointer = sum_list
            location = self.smallest_sum(sum_list)
            while location:
                array_pointer = array_pointer.next
                sum_pointer = sum_pointer.next
                location -= 1

            if sum_pointer.prev:
                sum_pointer.prev.val += array_pointer.next.val

            if sum_pointer.next:
                sum_pointer.next.val += array_pointer.val

            array_pointer.val = sum_pointer.val
            array_pointer.next = array_pointer.next.next
            if array_pointer.next:
                array_pointer.next.prev = array_pointer

            if sum_pointer.next and sum_pointer.prev:
                sum_pointer.prev.next = sum_pointer.next
                sum_pointer.next.prev = sum_pointer.prev
            elif not sum_pointer.prev and sum_pointer.next:
                sum_list = sum_pointer.next
                sum_list.prev = None
            elif not sum_pointer.next and sum_pointer.prev:
                sum_pointer.prev.next = None
            else:
                sum_pointer = None

            if self.is_non_decreasing(array_list):
                print(array_list)
                return steps

        return steps


    def is_non_decreasing(self, l_list: ListNode | None) -> bool:
        is_it: bool = True
        while l_list:
            if l_list.prev:
                if l_list.prev.val > l_list.val:
                    is_it = False
            l_list = l_list.next

        return is_it


    def smallest_sum(self, sum_list: ListNode | None) -> int:
        smallest_sum: list[tuple[int, int]] = []
        steps = 0

        while sum_list:
            while smallest_sum and sum_list.val < smallest_sum[-1][0]:
                smallest_sum.pop()

            if not smallest_sum:
                smallest_sum.append((sum_list.val, steps))

            sum_list = sum_list.next
            steps += 1

        return smallest_sum[-1][-1]


solution = Solution()
print(solution.minimum_pair_removal([1,2,2,3, 3]))
