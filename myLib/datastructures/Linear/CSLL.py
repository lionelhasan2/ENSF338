import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))


from nodes.Dnode import DNode

class CSLL():


    def __init__(self,node =None):

        self.head = node

        if(node == None):
            self.size = 0 
        
        else:
            self.size = 1
        self.sorted = False
        self.tail = None

    def is_Sorted(self):
        """Check if the circular linked list is sorted in non-descending order."""
        if self.size <= 1:
            self.sorted = True
            return
        
        curr = self.head
        while curr.next != self.head:
            if curr.val > curr.next.val:
                self.sorted = False
                return
            curr = curr.next
            
        # Check the last element with the first element


        self.sorted = True

    def InsertTail(self, node):
        self.InsertHead(node)
        self.head = self.head.next

    def InsertHead(self, node):
        if not self.head:
     # circular reference
            self.head = node
            self.head.next = self.head     # circular reference
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            node.next = self.head
            self.head = node
            curr.next = self.head
        self.size += 1

    def Insert(self, node, position):
        if position < 1 or position > self.size + 1:
            raise ValueError("Invalid position")
        if position == 1:
            if not self.head:
                # If the list is empty, make the new node the head and set its next pointer to itself
                node.next = node
                self.head = node
            else:
                # If the list is not empty, insert the new node at the head and update the last node's next pointer
                last_node = self.head
                while last_node.next != self.head:
                    last_node = last_node.next
                node.next = self.head
                self.head = node
                last_node.next = node
        else:
            curr_node = self.head
            for i in range(1, position - 1):
                curr_node = curr_node.next
            node.next = curr_node.next
            curr_node.next = node
        self.size += 1

    def Search(self, node):
        curr = self.head
        while curr.next != self.head:
            if curr == node:
                return True
            curr = curr.next
        return False
    
    def DeleteTail(self):
        """Delete the tail node of the circular linked list."""
        if not self.head:
            # If the list is empty, there's nothing to delete
            return

        # Find the last node and the second-to-last node in the list
        last_node = self.head
        second_to_last_node = None
        while last_node.next != self.head:
            second_to_last_node = last_node
            last_node = last_node.next

        # If there is only one node in the list, delete it
        if last_node == self.head:
            self.head = None

        # Otherwise, delete the last node and update the second-to-last node's `next` pointer
        else:
            second_to_last_node.next = self.head
            last_node.next = None
        self.size -=1

    def DeleteHead(self):
        """Delete the head node of the circular linked list."""
        if not self.head:
            # If the list is empty, there's nothing to delete
            return

        # Find the last node in the list
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next

        # If there is only one node in the list, delete it
        if last_node == self.head:
            self.head = None

        # Otherwise, delete the head node and update the last node's `next` pointer
        else:
            second_node = self.head.next
            self.head.next = None
            self.head = second_node
            last_node.next = second_node
        self.size -=1
    
    # def Delete(self, node):
    #     """Delete the given node from the circular linked list."""
    #     if not self.head:
    #         # If the list is empty, there's nothing to delete
    #         return

    #     if self.head == node:
    #         # If the node to delete is the head, update the head to point to the next node
    #         self.head = self.head.next
    #         return

    #     current_node = self.head
    #     while current_node.next != self.head:
    #         if current_node.next == node:
    #             # If the next node is the one to delete, update the current node's next pointer to skip over it
    #             current_node.next = current_node.next.next
    #             return
    #         current_node = current_node.next

    #     # Check if the node to be deleted is the last node
    #     if current_node.next == self.head and current_node.next == node:
    #         current_node.next = self.head.next
    #         self.head = self.head.next
    #         return

    #     # If we reach the head again without finding the node, it's not in the list
    #     return

    def Delete(self, node):
        i = 0
        node_occurrences = self.count_node_occurrences(node)
        while i < node_occurrences:
            if self.head is None: # empty
                return
            elif self.head.val == node.val: # node to delete is the head node
                self.DeleteHead()
            # elif self.tail.val == node.val: # node to delete is the tail node
            #     self.DeleteTail()
            else:
                current_node = self.head
                while current_node.next != self.head:
                    if current_node.next.val == node.val:
                        current_node.next = current_node.next.next
                        self.size -= 1
                        break
                    current_node = current_node.next 
            i += 1

    def Sort(self):

        self.is_Sorted()
        if not self.head or not self.head.next or self.sorted == True:
            return
        
        # Create a new head node to mark the beginning of the sorted list
        new_head = DNode(-1)
        new_head.next = self.head
        
        # Initialize the pointers for the sorted and unsorted portions of the list
        last_sorted = self.head
        curr = last_sorted.next
        
        while curr != self.head:
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

        curr2 = self.head
        while curr2 != curr2.next:
            curr2 = curr2.next
        curr2.next = self.head


    def Clear(self):
        """Delete the entire circular linked list."""
        if not self.head:
            # If the list is empty, there's nothing to delete
            return

        # Find the last node in the list
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next

        # Delete all nodes in the list
        current_node = self.head
        while current_node != last_node:
            next_node = current_node.next
            current_node.next = None
            current_node = next_node
        last_node.next = None

        # Update head pointer to indicate the list is empty
        self.head = None

    def Print(self):
        """Print the circular linked list information on the screen."""
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
            while True:
                print(current_node.val, end=" ")
                current_node = current_node.next
                if current_node == self.head:
                    break
            print()
        print()

    def SortedInsert(self, new_node):
        """Insert a new node into the circular linked list in non-descending order."""
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            self.head.next = self.head # make the head point to itself for circularity
            self.size += 1
            return

        if not self.sorted:
            self.Sort()

        # If the new node's value is less than or equal to the head's value,
        # insert the new node at the beginning of the list
        if new_node.val <= self.head.val:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        # Find the correct position to insert the new node
        curr = self.head
        while (curr.next != self.head) and curr.next.val < new_node.val:
            curr = curr.next
        
        # Insert the new node into the list
        new_node.next = curr.next
        curr.next = new_node
        self.size +=1
    
    def count_node_occurrences(self,node):
        """
        Counts the number of occurrences of a given node in a circular doubly linked list.

        Args:
        - node: the node to search for in the list.

        Returns:
        - The number of occurrences of the node in the list.
        """

        count = 0
        current_node = self.head

        if current_node is None:
            # The list is empty, so there can be no occurrences of the node.
            return 0

        # Traverse the list from the head node until we reach it again.
        while True:
            if current_node.val == node.val:
                count += 1

            current_node = current_node.next

            if current_node == self.head:
                # We've reached the end of the list and circled back to the head.
                break

        return count
