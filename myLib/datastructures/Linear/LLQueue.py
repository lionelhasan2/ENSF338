import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from nodes.Dnode import DNode
from Linear.SLL import SLL


class LLQueue(SLL):


    def __init__(self, node = None):
        self.head = node
        self.size = 1
        self.tail = None
        self.sorted = False

    def is_empty(self):
        return self.head is None

    def enqueue(self, node):
        new_node = node
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        return temp.val