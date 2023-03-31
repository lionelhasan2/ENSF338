
from nodes.Dnode import Dnode

class DoublyLinkedList:

    def __init__(self): #if list is empty no 
        self.head = None
        self.size = 0
        self.tail = None 

    def __init__(self, node):
        self.head = node 
        self.size = 1
        self.tail = node #tail pointing to same node as head

    def insert_head(self, new_node):
        if self.head is None: #if it is empty DLL
            self.head = new_node
            self.tail = new_node
        else: #if there it is not empty
            new_node.next = self.head #new_node points at head
            new_node.prev = None #new_node is first so nothing to point backwards at
            self.head = new_node
        self.size += 1

    def insertTail(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
    
    def insert(self, new_node, position):
        if position < 1 or position > self.size + 1:
            raise ValueError("Invalid position")
        if position == 1: #this will be the only node in the DLL
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
        else: 
            curr_node = self.head
            for i in range(1, position - 1): #loop till find pos want add
                curr_node = curr_node.next
            new_node.next = curr_node.next
            new_node.prev = curr_node
            curr_node.next = new_node
        self.size += 1

    #CHECK OVER SORT
    def sort(self):
        if self.head is None:
            return
        # Traverse the list from the second node
        current = self.head.next
        while current is not None:
            # Save the current node and its data
            node = current
            data = current.data
            
            # Find the proper position to insert the current node
            prev_node = current.prev
            while prev_node is not None and prev_node.data > data:
                # Move the previous node to the next position
                prev_node.next.data = prev_node.data
                prev_node = prev_node.prev
                
            # Insert the current node in the proper position
            if prev_node is None:
                # The current node should be inserted at the beginning
                current.data = self.head.data
                self.head.data = data
            else:
                # The current node should be inserted after the previous node
                prev_node.next.data = data
                current.data = node.data

            # Move to the next node
            current = node.next
    

    def isSorted(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def SortedInsert(self, node):
        if not self.isSorted():
            self.sort()
        
        if self.head is None: # The list is empty, so insert the node at the beginning
            self.head = node
            self.tail = node

        elif self.head.data >= node.data: # The new node should be inserted at the beginning
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        elif self.tail.data <= node.data: # The new node should be inserted at the end
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
        else:  # Find the proper position to insert the new node
            current = self.head
            while current.next is not None and current.next.data < node.data:
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node

    def Search(self, node):
        current = self.head
        while current is not None:
            if current.val == node.val:
                return current
            current = current.next
        return None

    
    def DeleteHead(self):
        if self.head is None:
            return 
        else:
            # deleted_node = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else: #if the DLL is empty now
                self.tail = None 
            self.size -= 1

    def DeleteTail(self):
        if self.head is None:
            return 
        elif self.head.next is None:
            self.head = None
        else:
            # deleted_node = self.tail
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            else: #if DLL if empty now
                self.head = None
            self.size -= 1
    
    #NGL CHECK OVER
    def Delete(self, node):
        if self.head is None:
            return
        elif self.head.val == node.val: 
            return self.delete_head()
        elif self.tail.val == node.val:
            return self.delete_tail()
        else:
            current = self.head
            while current.next is not None and current.next.val != node.val:
                current = current.next
            if current.next is None:
                return # Dont do anything bc list was empty
            else:
                current.prev = current.next #THE PREVIOUS NODE NOW POINTS TO NEXT NODE
                
    def Clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def Print(self):
        current_node = self.head
        print("The size of the doubly linked list is:" + self.size)
        print("The doubly linked list is sorted:" + self.is_sorted())
        while current_node is not None:
            print("The value of the node is:" + current_node.data)
            current_node = current_node.next



