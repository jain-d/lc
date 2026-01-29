from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    left: Node | None = None
    right: Node | None = None

    def __str__(self):
        return f"[{self.left}  {self.val}  {self.right}]"

def tree_entry(element: int, tree: Node):
    if element < tree.val:
        if tree.left:
            tree_entry(element, tree.left)
        else:
            tree.left = Node(element)
    else:
        if tree.right:
            tree_entry(element, tree.right)
        else:
            tree.right = Node(element)

def bfs(tree: Node):
    nodes: list = [tree]
    i = 0
    while i < len(nodes):
        current_node = nodes[i]
        if current_node.left:
            nodes.append(current_node.left)
        if current_node.right:
            nodes.append(current_node.right)

        i += 1
    print([node.val for node in nodes])

def dfs(tree: Node):
    if not tree.left and not tree.right:
        return [tree.val,]

    root = []
    if tree.left:
        root.extend(dfs(tree.left))

    root.append(tree.val)

    if tree.right:
        root.extend(dfs(tree.right))

    return root
    
elements = [25, 10, 40, 5, 15, 30, 50, 2, 7, 13, 18, 35]
tree: Node

for index, element in enumerate(elements):
    if not index:
        tree = Node(element)
    else:
        tree_entry(element, tree)

print(dfs(tree))
