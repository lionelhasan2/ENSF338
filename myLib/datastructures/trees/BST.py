from nodes.TNode import TNode

class BST:
    def __init__(self, root=None):
        if isinstance(root, TNode):
            self.root = root
        elif isinstance(root, int):
            self.root = TNode(data=root)
        else:
            self.root = None

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, node):
        if isinstance(node, TNode):
            if self.root is None:
                self.root = node
            else:
                self._insert_node(self.root, node)
        elif isinstance(node, int):
            new_node = TNode(data=node)
            if self.root is None:
                self.root = new_node
            else:
                self._insert_node(self.root, new_node)

    def _insert_node(self, current, node):
        if node.data < current.data:
            if current.left is None:
                current.left = node
                node.parent = current
            else:
                self._insert_node(current.left, node)
        else:
            if current.right is None:
                current.right = node
                node.parent = current
            else:
                self._insert_node(current.right, node)

    def delete(self, val):
        node = self.search(val)
        if node is None:
            print(f"{val} not found in the tree.")
            return
        if node.left and node.right:
            successor = self._find_min(node.right)
            node.data = successor.data
            self.delete(successor)
        elif node.parent is None:
            if node.left:
                self.root = node.left
            else:
                self.root = node.right
            self.root.parent = None
        elif node.left or node.right:
            if node == node.parent.left:
                if node.left:
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.left = node.right
                    node.right.parent = node.parent
            else:
                if node.left:
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent
        else:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

    def search(self, val):
        return self._search_node(self.root, val)

    def _search_node(self, current, val):
        if current is None or current.data == val:
            return current
        # elif val < current.data:
