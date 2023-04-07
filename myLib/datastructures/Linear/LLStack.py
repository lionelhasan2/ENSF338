import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from SLL import SLL

class LLStack(SLL):

    def __init__(self, node=None):
        self.head = node 
        self.size = 1 if node else 0
        self.tail = node #tail pointing to same node as head

    def InsertTail(self, new_node):
        return

    # def insertHead(self, new_node): #CHANGED NAME TO MATCH STACK
    def Push(self, new_node):
        # if self.head is None:
        #     self.head = new_node
        # else:
        #     head_node = self.head
        #     new_node.next = head_node
        #     self.head = new_node
        # self.size += 1
        super().InsertHead(new_node)

    def Insert(self, node, position):
        return

    def isSorted(self):
        super().is_Sorted()

    def Sort(self):
        return

    def SortedInsert(self,new_node):
        return

    def Search(self, node):
        # super().Search(node)

        curr = self.head
        while curr:
            if curr.val == node.val:
                return curr
            curr = curr.next
        return None
    
    # def DeleteHead(self): #CHANGED NAME TO FOLLOW STACK
    def Pop(self):
        # if self.size == 0:
        #     raise ValueError("Stack is empty")
        # popped_node = self.head
        # self.head = self.head.next
        # popped_node.next = None
        # self.size -= 1
        super().DeleteHead()
    
    def DeleteTail(self):
        return
    
    def Delete(self, node):
        return

    def Clear(self):
        super().Clear()

    def Print(self):
        super().Print()
    

    