

class DoublyLinkedList:

    def __init__(self, node=None):
        self.head = node 
        self.size = 1 if node else 0
        self.tail = node #tail pointing to same node as head

    def insertHead(self, new_node):
        if self.head is None: #if it is empty DLL
            self.head = new_node
            self.tail = new_node
        else: #if there it is not empty
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insertTail(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert(self, new_node, position):
        if position < 1 or position > self.size + 1:
            raise ValueError("Invalid position")
        if position == 1:
            self.insertHead(new_node)
        elif position == self.size + 1:
            self.insertTail(new_node)
        else: 
            current = self.head
            for _ in range(position - 2):
                current = current.next
            new_node.prev = current
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            self.size += 1

    # #CHECK OVER SORT, DOES NOT WORK
    def sort(self):
        if (self.isSorted() == True):
            return
        if self.head is None or self.head.next is None:
            return
        
        neighbourNode = self.head.next
        while neighbourNode != None:
            keyData = neighbourNode.val
            sorted_node = neighbourNode.prev
            while sorted_node != None and sorted_node.val > keyData:
                sorted_node.next.val = sorted_node.val
                sorted_node = sorted_node.prev
            if sorted_node:
                sorted_node.next.val = keyData
            else:
                self.head.val = keyData
            neighbourNode = neighbourNode.next

        # sorted_tail = self.head
        # while sorted_tail.next:
        #     to_insert = sorted_tail.next
        #     to_insert_prev = to_insert.prev
        #     to_insert_next = to_insert.next

        #     if to_insert.val >= sorted_tail.val:
        #         sorted_tail = sorted_tail.next
        #     else:
        #         # Remove to_insert from the list
        #         to_insert_prev.next = to_insert_next
        #         if to_insert_next:
        #             to_insert_next.prev = to_insert_prev

        #         # Find the insertion point
        #         insertion_point = self.head
        #         while insertion_point and insertion_point.val < to_insert.val:
        #             insertion_point = insertion_point.next

        #         # Insert the node
        #         if insertion_point == self.head:
        #             to_insert.next = self.head
        #             self.head.prev = to_insert
        #             self.head = to_insert
        #         else:
        #             to_insert.prev = insertion_point.prev
        #             to_insert.next = insertion_point
        #             insertion_point.prev.next = to_insert
        #             insertion_point.prev = to_insert

        #         if to_insert_next:
        #             to_insert_next.prev = to_insert_prev
    
    def isSorted(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.val > current.next.val:
                return False
            current = current.next
        return True
    
    #THIS DOES NOT WORK
    def SortedInsert(self, node):
        if (self.isSorted() != True):
            self.sort()
        if self.head is None: # The list is empty, so insert the node at the beginning
            self.head = node
            self.tail = node
            self.size += 1
            return
        elif self.head.val >= node.val: # The new node should be inserted at the beginning
            self.insertHead(node)
            return
        elif self.tail.val <= node.val: # The new node should be inserted at the end
            self.insertTail(node)
            return
        else:  # Find the proper position to insert the new node
            current = self.head
            while current.next is not None and current.next.val < node.val:
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1

    #ngl i dont think it works properly bc what if 2 objects same val and, the next and previous nodes will never be the same
    def Search(self, node): #WORKS BUT RETURNS AN OBJECT??????
        current = self.head
        while current is not None:
            if current.val == node.val:
                return current
            current = current.next
        return None

    def DeleteHead(self):
        if self.head is None: #list is empty
            return 
        elif self.head == self.tail: # the list has only one node
            self.head = None
            self.tail = None
            self.size = 0
            return
        else:
            next_node = self.head.next
            next_node.prev = None
            self.head.next = None
            self.head = next_node
            self.size -= 1
        
    def DeleteTail(self):
        if self.head is None: #list is empty
            return 
        elif self.head == self.tail: # the list has only one node
            self.head = None
            self.tail = None
            self.size = 0
            return
        else:
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail.prev = None
            self.tail = prev_node
            self.size -= 1
    
    #NGL CHECK OVER, only deletes the first instance of this node, idk
    def Delete(self, node):
        if self.head is None: # empty
            return
        elif node.val == self.head.val: # node to delete is the head node
            self.DeleteHead()
            return
        elif node.val == self.tail.val: # node to delete is the tail node
            self.DeleteTail()
            return
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.val == node.val:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    self.size -= 1
                    return
                current_node = current_node.next
            print("node is not found in existing")         
                
    def Clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def Print(self):
        current_node = self.head
        print("The size of the doubly linked list is:", self.size)
        print("The doubly linked list is sorted:", self.isSorted())
        while current_node is not None:
            print(f"The value of the node is: {current_node.val}")
            current_node = current_node.next