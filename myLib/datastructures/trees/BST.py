import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
print(sys.path)


from nodes.TNode import TNode

class BST:
    def __init__(self, root=None):
        if isinstance(root, TNode): #isinstance determines what type of argument it is
            self.root = root #IDK HOW TF I WOULD MAKE IT REFERENCE A SUBTREE LIKE WHATTT????????????
        elif isinstance(root, int):
            self.root = TNode(data=root)
        else:
            self.root = None
    
    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, param):
        if isinstance(param, TNode):
            if self.root is None:
                self.root = param
            else:
                self.insert(param.val)
        elif isinstance(param, int):
            if self.root is None:
                self.root = TNode(param)
            elif param < self.root.val:
                self.root.left = self.insert(self.root.left, param)
            elif param > self.root.val:
                self.root.right = self.insert(self.root.right, param)

    #NGL JUST GOT IT FROM CHATGPT IDK IF THIS WORKS
    def delete(self, val):
        if root is None:
            return

        # If the node to be deleted is less than the root node,
        # then it lies in left subtree
        if val < root.val:
            root.left = TNode(root.left, val)

        # If the node to be deleted is greater than the root node,
        # then it lies in right subtree
        elif val > root.val:
            root.right = TNode(root.right, val)

        # If the node to be deleted is the same as the root node,
        # then this is the node to be deleted
        else:
            # Case 1: Node with no children
            if root.left is None and root.right is None:
                root = None

            # Case 2: Node with only one child
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left

            # Case 3: Node with two children
            else:
                # Find the inorder successor
                temp = root.right
                while temp.left is not None:
                    temp = temp.left

                # Copy the inorder successor's value to the node to be deleted
                root.val = temp.val

                # Delete the inorder successor
                root.right = TNode(root.right, temp.val)

    def search(self, val):
        current = self.root
        while current is not None:
            if val == current.data:
                return current
            elif val <= current.data:
                current = current.left
            else:
                current = current.right
        return None

    def printInOrder(self):
        current = self.root
        if current is not None:
            self.printInOrder(current.left)
            print(current.data, end=" ")
            self.printInOrder(current.right)

    def printBF(self):
        root = self.root
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0) # Remove from front
            yield current.data
            #print(current.data)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
