from __future__ import annotations
from collections import deque
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    right: Node | None = None
    left: Node | None = None

    def __str__(self):
        return f"[{self.left}  {self.val}  {self.right}]"

class Tree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, new_node: int):
        if not self.root:
            self.root = Node(new_node)
        else:
            self._insert(new_node, self.root)

    def _insert(self, new_node: int, current_node: Node):
        if new_node > current_node.val:
            if current_node.right:
                self._insert(new_node, current_node.right)
            else:
                current_node.right = Node(new_node)
        else:
            if current_node.left:
                self._insert(new_node, current_node.left)
            else:
                current_node.left = Node(new_node)

    def __str__(self):
        if self.root:
            return f"{self.root}"
        else:
            return "NONE"

    def bfs(self):
        current_node = self.root
        order: deque = deque([current_node,])
        fast_mem_check: set = {id(current_node)}

        while order:
            print()
            for node in order:
                print(node.val, end="   ")
            visiting_node = order.popleft()
            if visiting_node.left and (lnode_address := id(visiting_node.left)) not in fast_mem_check:
                order.append(visiting_node.left)
                fast_mem_check.add(lnode_address)
            if visiting_node.right and (rnode_address := id(visiting_node.right)) not in fast_mem_check:
                order.append(visiting_node.right)
                fast_mem_check.add(rnode_address)
        

tree = Tree()

for entry in [5, 3, 9, 2, 4, 1, 7, 12, 6, 8, 10, 11]:
    tree.insert(entry)

tree.bfs()
