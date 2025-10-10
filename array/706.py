# Design HashMap
from __future__ import annotations
from dataclasses import dataclass

# Original, sMoL bRaIn solution
class MyHashMap:
    def __init__(self):
        self.hash_map: list[list[int]] = [[], []]

    def put(self, key: int, value: int) -> None:
        if self.hash_map[0].count(key):
            self.hash_map[1][self.hash_map[0].index(key)] = value
            return
        self.hash_map[0].append(key)
        self.hash_map[1].append(value)

    def get(self, key: int) -> int:
        if self.hash_map[0].count(key):
            return self.hash_map[1][self.hash_map[0].index(key)]
        return -1

    def remove(self, key: int) -> None:
        if self.hash_map[0].count(key):
            self.hash_map[0].pop(index := self.hash_map[0].index(key))
            self.hash_map[1].pop(index)
        return


# The real shit
@dataclass
class ListNode:
    key: int
    val: int
    next: ListNode | None = None

class HashMap:
    def __init__(self):
        self.hash_map: list[ListNode | None] = [None] * 1000

    def _hash(self, key: int) -> int:
        return key % len(self.hash_map)

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.hash_map[index]:
            self.hash_map[index] = ListNode(key, value)
            return
        pointer = self.hash_map[index]
        while pointer:
            if pointer.key == key:
                pointer.val = value
                return
            if not pointer.next:
                pointer.next = ListNode(key, value)
                return
            pointer = pointer.next

    def get(self, key: int) -> int:
        index = self._hash(key)
        pointer = self.hash_map[index]
        while pointer:
            if pointer.key == key:
                return pointer.val
            pointer = pointer.next
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        pointer = self.hash_map[index]
        if pointer:
            if pointer.key == key:
                self.hash_map[index] = pointer.next
                return

            prev = pointer
            pointer = pointer.next
            while pointer:
                if pointer.key == key:
                    prev.next = pointer.next
                    return
                prev = pointer
                pointer = pointer.next
        
        return
