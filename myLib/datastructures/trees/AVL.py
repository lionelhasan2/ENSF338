import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))


from nodes.TNode import TNode
from BST import BST

class AVL(BST):
        
    def __init__(self, root = None):
        if isinstance(root, TNode):
            if root.left or root.right is None:
                self.root = root
            else:
                self.avlCreator(root)
        elif isinstance(root, int):
            self.root = TNode(data=root)
        else:
            self.root = None
    

    def balance_avl(self):
        # Update the heights of all nodes in the tree
        self.update_heights(self.root)

        # Balance the tree by performing rotations
        self.root = self.balance_tree(self.root)
        self.updateBalance(self.root)
        

    def update_heights(self, node):
        # Recursively update the height of a node and its children
        if node is None:
            return -1
        node.height = 1 + max(self.update_heights(node.left), self.update_heights(node.right))
        return node.height

    def balance_tree(self, node):
        # Balance a tree rooted at the given node
        if node is None:
            return None

        # Balance the left and right subtrees
        node.left = self.balance_tree(node.left)
        node.right = self.balance_tree(node.right)

        # Check the balance factor and perform rotations if necessary
        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1:
            if self.get_balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)
        elif balance_factor < -1:
            if self.get_balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)

        return node

    def get_balance_factor(self, node):
        # Get the balance factor of a node
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1
        return left_height - right_height

    def rotate_left(self, node):
        # Perform a left rotation on a node
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_heights(node)
        self.update_heights(new_root)
        return new_root

    def rotate_right(self, node):
        # Perform a right rotation on a node
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_heights(node)
        self.update_heights(new_root)
        return new_root





    


