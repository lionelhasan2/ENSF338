from nodes.Dnode import DNode

class SLL:


    def __init__(self, node = None):
        self.head = node
        self.size = 1
        self.tail = node
        self.sorted = False

    def is_Sorted(self):
        if self.size <= 1:
            self.sorted = True
        
        curr = self.head
        
        while curr.next:
            if curr.val > curr.next.val:
                self.sorted = False
                return
            curr = curr.next

        self.sorted = True


    def InsertTail(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            node = self.tail
            node.next = new_node
        self.size += 1

    def InsertHead(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            head_node = self.head
            new_node.next = head_node
            self.head = new_node
        self.size += 1

    def Insert(self, node, position):
        if position < 1 or position > self.size + 1:
            raise ValueError("Invalid position")
        if position == 1:
            node.next = self.head
            self.head = node
        else:
            curr_node = self.head
            for i in range(1, position - 1):
                curr_node = curr_node.next
            node.next = curr_node.next
            curr_node.next = node
        self.size += 1
    ##check over sometime 



    def Sort(self):
        if not self.head or not self.head.next or self.sorted == True:
            return
        
        # Create a new head node to mark the beginning of the sorted list
        new_head = DNode(-1)
        new_head.next = self.head
        
        # Initialize the pointers for the sorted and unsorted portions of the list
        last_sorted = self.head
        curr = last_sorted.next
        
        while curr:
            # If the current node is greater than or equal to the last sorted node,
            # simply move the last sorted pointer forward
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # If the current node is less than the last sorted node,
                # find the correct position to insert it in the sorted portion of the list
                prev = new_head
                while prev.next.val < curr.val:
                    prev = prev.next
                
                # Remove the current node from the unsorted portion of the list
                last_sorted.next = curr.next
                
                # Insert the current node into the sorted portion of the list
                curr.next = prev.next
                prev.next = curr
            
            # Move the current pointer forward
            curr = last_sorted.next
        
        # Set the head of the list to the next node after the new head node
        self.head = new_head.next
        self.sorted = True

        

    def Search(self, node):
        curr = self.head
        while curr:
            if curr == node:
                return True
            curr = curr.next
        return False


    def getListHead(self):
        return self.head


    def DeleteHead(self):
        """Delete the head node of the singly linked list."""
        if not self.head:
            # If the list is empty, there's nothing to delete
            return

        # If there is only one node in the list, delete it
        if not self.head.next:
            self.head = None

        # Otherwise, delete the head node and update the `head` pointer
        else:
            self.head = self.head.next
        self.size -= 1
    

    def DeleteTail(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            self.size -=1

    def Clear(self):
        """Delete the entire linked list."""
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = None
            current_node = next_node
        self.head = None



    def Delete(self, node):
        """Delete the given node from the list."""
        if not self.head:
            # If the list is empty, there's nothing to delete
            return

        if self.head == node:
            # If the node to delete is the head, update the head to point to the next node
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next == node:
                # If the next node is the one to delete, update the current node's next pointer to skip over it
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If we reach the end of the list without finding the node, it's not in the list
        return

    def Print(self):
        """Print the list information on the screen."""
        # Print the list length
        print("List size:", self.size)
        self.is_Sorted()

        # Print the sorted status
        print("Sorted: " + ("Yes" if self.sorted else "No"))

        # Print the list content
        if not self.head:
            print("List is empty")
        else:
            current_node = self.head
            print("List content:", end=" ")
            while current_node:
                print(current_node.val, end=" ")
                current_node = current_node.next
            print()
        print()

    def SortedInsert(self, new_node):
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            return
        
        if (self.sorted == False):
            self.Sort()
        
        # If the new node's value is less than the head's value,
        # set the new node as the new head
        if new_node.val <= self.head.val:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Find the correct position to insert the new node
        curr = self.head
        while curr.next and curr.next.val < new_node.val:
            curr = curr.next
        
        # Insert the new node into the list
        new_node.next = curr.next
        curr.next = new_node
        self.size +=1



            

