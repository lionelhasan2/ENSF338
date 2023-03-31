from SLL import SLL
from nodes.Dnode import Dnode

class CSLL(SLL):
    def __init__(self):
        self.head = None
        self.size = 0
        self.sorted = False

    def InsertTail(self, node):
        if self.head == None:
            self.head = node
            self.head.next = self.head
        else:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = node
            node.next.next = self.head
        self.size += 1

    def InsertHead(self, node_arg):
        """Insert a new node at the head of the circular linked list."""

        if not self.head:
            # If the list is empty, make the new node the head
            self.head = node_arg
            node_arg.next = self.head
        else:
            # Traverse the list to find the last node and update its next pointer
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = node_arg
            node_arg.next = self.head
            self.head = node_arg

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
    


    def Delete(self, node):
        """Delete the given node from the circular linked list."""
        if not self.head:
            # If the list is empty, there's nothing to delete
            return

        if self.head == node:
            # If the node to delete is the head, update the head to point to the next node
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next != self.head:
            if current_node.next == node:
                # If the next node is the one to delete, update the current node's next pointer to skip over it
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # Check if the node to be deleted is the last node
        if current_node.next == self.head and current_node.next == node:
            current_node.next = self.head.next
            self.head = self.head.next
            return

        # If we reach the head again without finding the node, it's not in the list
        return
    
    def Sort(self):
        """Sort the circular linked list using insertion sort."""
        if not self.head or not self.head.next:
            # If the list is empty or has only one element, it's already sorted
            return

        current_node = self.head.next
        while current_node != self.head:
            value_to_insert = current_node.data
            insert_position = None
            insert_after = self.head
            while insert_after != current_node:
                if insert_after.data <= value_to_insert:
                    insert_position = insert_after
                insert_after = insert_after.next

            if insert_position is None:
                # If the node should be inserted at the beginning of the list
                insert_position = self.head
                while insert_position.next != self.head:
                    insert_position = insert_position.next
            else:
                insert_position = insert_position.next

            new_node = Dnode(value_to_insert)
            new_node.next = insert_position.next
            insert_position.next = new_node
            current_node = current_node.next

        # Update the head to point to the smallest element in the sorted list
        new_head = self.head
        while new_head.next != self.head and new_head.next.data >= self.head.data:
            new_head = new_head.next
        self.head = new_head

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
            while True:
                print(current_node.data, end=" ")
                current_node = current_node.next
                if current_node == self.head:
                    break
            print()