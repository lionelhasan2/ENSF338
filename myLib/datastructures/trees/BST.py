import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))


from nodes.TNode import TNode

class BST:
    def __init__(self, root=None):
        if isinstance(root, TNode): #isinstance determines what type of argument it is
            self.root = root #IDK HOW TF I WOULD MAKE IT REFERENCE A SUBTREE LIKE WHATTT????????????. Its good as is -Lionel
        elif isinstance(root, int):
            self.root = TNode(data=root)
        else:
            self.root = None
    
    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def Insert(self, param):
        if isinstance(param, TNode):
            if self.root is None:
                self.root = param
            else:
                self.Insert(param.data)
        elif isinstance(param, int):
            if self.root is None:
                self.root = TNode(param)
            else:
                current_node = self.root
                parent_node = None
                while current_node is not None:
                    parent_node = current_node
                    if param < current_node.data:
                        current_node = current_node.left
                    elif param > current_node.data:
                        current_node = current_node.right
                    else:
                        return
                if param < parent_node.data:
                    parent_node.left = TNode(param)
                    parent_node.left.parent = parent_node
                else:
                    parent_node.right = TNode(param)
                    parent_node.right.parent = parent_node



    def delete(self, val):
        if self.root is None:
            return

        node = self.search(val)
        if node is None:
            return

        parent = node.parent

        # case 1: node is a leaf node
        if node.left is None and node.right is None:
            if parent is None:
                self.root = None
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None

        # case 2: node has only one child
        elif node.left is None:
            if parent is None:
                self.root = node.right
            elif parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
            node.right.parent = parent

        elif node.right is None:
            if parent is None:
                self.root = node.left
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
            node.left.parent = parent

        # case 3: node has both left and right children
        else:
            # find the node with the smallest value in the right subtree
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            # replace node's value with temp's value
            node.data = temp.data
            # delete the node with temp's value in the right subtree
            if temp.parent.left == temp:
                temp.parent.left = temp.right
            else:
                temp.parent.right = temp.right
            if temp.right is not None:
                temp.right.parent = temp.parent

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

    def printInOrder(self, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            self.printInOrder(node.left)

        node.print()

        if node.right is not None:
            self.printInOrder(node.right)


    def printBF(self):
        if self.root is None:
            return
        
        queue = [self.root]
        
        while queue:
            current_node = queue.pop(0)
            current_node.print()
            
            if current_node.get_left():
                queue.append(current_node.get_left())
                
            if current_node.get_right():
                queue.append(current_node.get_right())