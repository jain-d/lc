from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    left: Node | None = None
    right: Node | None = None

def bfs(tree: Node) -> list[int]:
    address_list: list[Node] = [tree]
    val_list: list[int] = [tree.val]
    index = 0

    while True:
        if index == len(address_list):
            break
        current_node = address_list[index]
        if current_node.left:
            address_list.append(current_node.left)
            val_list.append(current_node.left.val)
        if current_node.right:
            address_list.append(current_node.right)
            val_list.append(current_node.right.val)
        index += 1
    
    return val_list


tree_one = Node(5, Node(3, Node(2), Node(4)), Node(8, Node(7, Node(6)), Node(9)))

print(bfs(tree_one))
