# Binary Search Tree
from __future__ import annotations

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def add(self, val):
        if val > self.val:
            if self.right:
                self.right.add(val)
            else:
                self.right = BST(val)
        elif val < self.val:
            if self.left:
                self.left.add(val)
            else:
                self.left = BST(val)
        else:
            print("\033[1mDUPLICATE\033[0m values not \033[1;31mALLOWED\033[0m")
            return

    def delete(self, val: int) -> BST:
        if val == self.val:
            if not self.left and not self.right:
                return None
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                self.val = self.right.get_min()
                self.right = self.right.delete(self.val)

        elif val > self.val and self.right:
            self.right = self.right.delete(val)
        elif val < self.val and self.left:
            self.left = self.left.delete(val)

        return self

    def preorder(self, visited):
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)

        return visited

    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)

        return visited

    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            self.right.inorder(visited)

        return visited

    def get_min(self):
        return self.val if not self.left else self.left.get_min()

    def get_max(self):
        return self.val if not self.right else self.right.get_max()


    def __str__(self):
        return f"[{self.left}\t{self.val}\t{self.right}]"


bst = BST(10)


bst.add(12)
bst.add(6)
bst.add(7)
bst.add(11)
bst.add(8)
bst.add(5)

bst.add(9)
bst.add(25)
print(bst)
"""
delete_node = input("which node to delete? ")
bst = bst.delete(int(delete_node))
"""

print("Preorder\t", bst.preorder([]))
print("Postorder\t", bst.postorder([]))
print("Inorder\t\t", bst.inorder([]))
