# Red Black Tree
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class RBNode:
    val: int
    red: bool = True
    parent: RBNode | None = None
    left: RBNode | None = None
    right: RBNode | None = None

    def __str__(self):
        return f"[{self.left}\t{self.val}|{'R' if self.red else 'B'}\t{self.right}]"


class RBTree:
    def __init__(self, val):
        self.root = RBNode(val=val, red=False)

    def insert(self, val):
        current = self.root
        while current:
            if val > current.val:
                if current.right:
                    current = current.right
                else:
                    new_node = RBNode(val=val, parent=current)
                    current.right = new_node
                    if current.red:
                        self.fix_insert(new_node)
            elif val < current.val:
                if current.left:
                    current = current.left
                else:
                    new_node = RBNode(val=val, parent=current)
                    current.left = new_node
                    if current.red:
                        self.fix_insert(new_node)
            else:
                return

    def fix_insert(self, new_node):
        # recoloring
        parent_node = new_node.parent
        grandfather_node = parent_node.parent
        uncle_node = grandfather_node.left if grandfather_node.right == parent_node else grandfather_node.right
        # recoloring conditional check
        if uncle_node and uncle_node.red:
            # recolor code here
            uncle_node.red = False
            parent_node.red = False
            current = grandfather_node
            while current:
                current.red ^= True
                current = current.parent

            self.root.red = False
        else:
            # rotation code here
            print("THIS WILL REQUIRE \033[32mROTATION\033[0m")

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def __str__(self):
        return f"{self.root}"



rb_tree = RBTree(20)
rb_tree.insert(10)
rb_tree.insert(25)
rb_tree.insert(23)
rb_tree.insert(22)
print(rb_tree)
