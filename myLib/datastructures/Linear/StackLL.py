
from nodes.Dnode import Dnode


class List:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def __init__(self, node):
        self.head = node
        self.size = 1
        self.tail = node

    def insertTail(self, new_node):
        print("ERROR! This function does not follow a stack-based structure")
        return

    # def insertHead(self, new_node): #CHANGED NAME TO MATCH STACK
    def Push(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            head_node = self.head
            new_node.next = head_node
            self.head = new_node
        self.size += 1

    def insert(self, node, position):
        if(position-1 != 0): #IF POSITION IS NOT THE FIRST ONE THEN IT DONT FOLLOW THE FIFO STRUCTURE
            print("ERROR! This function does not follow a stack-based structure")
            return
        else:
            self.Push(self, node)

    def is_sorted(self): #IDK IF THIS SHOULD JUST RETURN EMPTY OR NOT TBH
        if not self.head:
            return True  # an empty list is sorted
        curr = self.head
        while curr.next:
            if curr.next.val < curr.val:
                return False
            curr = curr.next
        return True

    def Sort(self):
        print("ERROR! This function does not follow a stack-based structure")
        return

    def SortedInsert(self,new_node):
        print("ERROR! This function does not follow a stack-based structure")
        return

    def Search(self, node):
        curr = self.head
        while curr:
            if curr == node:
                return True
            curr = curr.next
        return False
    
    # def DeleteHead(self): #CHANGED NAME TO FOLLOW STACK
    def Pop(self):
        if self.size == 0:
            raise ValueError("Stack is empty")
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.size -= 1
        # return popped_node #DO I EVEN NEED TO RETURN THIS OR AM I JUST DELETING?????
    
    def DeleteTail(self):
        print("ERROR! This function does not follow a stack-based structure")
        return

    def Clear(self):
        if self.head is None:
            return
        else:
            self.head = None
            self.tail = None

    def Print(self):
        current_node = self.head
        print("The size of the singly linked list is:" + self.size)
        print("The singly linked list is sorted:" + self.is_sorted())
        while current_node is not None:
            print("The value of the node is:" + current_node.data)
            current_node = current_node.next

    