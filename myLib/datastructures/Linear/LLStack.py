
class StackList:

    def __init__(self, node=None):
        self.head = node 
        self.size = 1 if node else 0
        self.tail = node #tail pointing to same node as head

    def InsertTail(self, new_node):
        print("ERROR! InsertTail does not follow a stack-based structure")
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

    def Insert(self, node, position):
        # if(position-1 != 0): #IF POSITION IS NOT THE FIRST ONE THEN IT DONT FOLLOW THE FIFO STRUCTURE
        #     print("ERROR! Can only push to the head of a stack-based structure")
        #     return
        # else:
        #     self.Push( node)
        print("Insert function does not follow a stack-based structure")
        return

    def isSorted(self): #IDK IF THIS SHOULD JUST RETURN EMPTY OR NOT TBH
        if not self.head:
            return True  # an empty list is sorted
        curr = self.head
        while curr.next:
            if curr.next.val < curr.val:
                return False
            curr = curr.next
        return True

    def Sort(self):
        print("ERROR! Sort does not follow a stack-based structure")
        return

    def SortedInsert(self,new_node):
        print("ERROR! Sorted Insert does not follow a stack-based structure")
        return

    def Search(self, node):
        curr = self.head
        while curr:
            if curr.val == node.val:
                return curr
            curr = curr.next
        return None
    
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
    
    def Delete(self, node):
        print("ERROR! Deleting at a specific node does not follow a stack-based structure")
        print("Must pop from the head to follow a First In First Out Structure, use the function pop to do so")
        return

    def Clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        current_node = self.head
        print("The size of list:", self.size)
        print("The doubly linked list is sorted:", self.isSorted())
        print(f"The value of the node is:", end=" ")
        while current_node is not None:
            print(current_node.val, end=" ")
            current_node = current_node.next
        print()
    

    