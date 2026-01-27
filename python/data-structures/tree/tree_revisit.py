from __future__ import annotations
from dataclasses import dataclass

# forgot binary tree, trying it out again


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


tree = Tree()

for entry in [5, 3, 9, 2, 4, 1, 9, 7, 12, 6, 8, 10, 11]:
    tree.insert(entry)


