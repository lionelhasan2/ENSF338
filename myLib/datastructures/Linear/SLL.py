from nodes.Dnode import Dnode


class CSLL:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
        self.sorted = False

    def __init__(self, node):
        self.head = node
        self.size = 1
        self.tail = node
        self.sorted = False

    def is_Sort(self):
        if not self.head:
            self.sorted = True  # an empty list is sorted
        curr = self.head
        while curr.next:
            if curr.next.val < curr.val:
                self.sorted = False
            curr = curr.next
        self.sorted = True


    def insertTail(self, new_node):
        if self.head is None:
            self.head = node
        else:
            node = self.tail
            node.next = new_node
        self.size += 1

    def insertHead(self, new_node):
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
        if not self.head or not self.head.next:
            return self.head
        
        new_head = Dnode(-1)
        new_head.next = self.head
        
        last_sorted = self.head
        curr = last_sorted.next
        
        while curr:
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                prev = new_head
                while prev.next.val < curr.val:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = last_sorted.next
        self.head = new_head.next
        self.sorted = True


    def SortedInsert(self,node):

        new_node = node

        if not self.head:
            self.head = new_node
            return

        if (self.is_sorted()!= True):
            self.Sort()

        if new_node.val <= self.head.val:
            new_node.next = self.head
            self.head = new_node
            return
        
        curr = self.head
        
        while curr.next and curr.next.val < new_node.val:
            curr = curr.next
            
        new_node.next = curr.next
        curr.next = new_node
        

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

    def Print(self):
        current_node = self.head
        print("The size of the singly linked list is:" +self.size)
        print("The singly linked list is sorted:" + self.is_sorted())
        while current_node is not None:
            print("The value of the node is:" + current_node.data)
            current_node = current_node.next

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
        print("List length:", self.length)

        # Print the sorted status
        print("Sorted: " + ("Yes" if self.sorted else "No"))

        # Print the list content
        if not self.head:
            print("List is empty")
        else:
            current_node = self.head
            print("List content:", end=" ")
            while current_node:
                print(current_node.data, end=" ")
                current_node = current_node.next
            print()

    def SortedInsert(self,node_arg):

        if not self.head or node_arg.data <= self.head.data:
            node_arg.next = self.head
            self.head = node_arg

        if (self.sorted == False):
            self.insertTail(node_arg)
            self.sort()
            self.size +=1
        else:
            current_node = self.head
            # Traverse the list until we find the correct position for the new node
            while current_node.next and node_arg.data > current_node.next.data:
                current_node = current_node.next
            node_arg.next = current_node.next
            current_node.next = node_arg

        self.length += 1
        self.sorted = True
            

