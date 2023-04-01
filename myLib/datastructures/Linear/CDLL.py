
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
            new_node.next = self.head 
            new_node.prev = self.tail 
            self.head.prev = new_node 
            self.tail.next = new_node
            self.head = new_node
        self.size += 1

    def insertTail(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    #CHECK OVER NGL
    def insert(self, new_node, position):
        if position == 1:
            self.insert_head(new_node)
        elif position == self.size + 1:
            self.insert_tail(new_node)
        elif 1 < position <= self.size:
            curr_node = self.head
            for i in range(1, position - 1): #loop till find pos want add
                curr_node = curr_node.next #CURR_NODE IS AT SPOT WANT NEW_NODE TO BE
            
            new_node.next = curr_node.next 
            new_node.prev = curr_node
            curr_node.next = new_node
            # curr_node.next.prev = new_node #I THINK CURR NODE WILL PROLLY BE POINTING TO CORRECT PREV NODE ALREADY SO NO NEED CHANGE
            self.size += 1
        else:
            raise ValueError("Invalid position")


    #CHECK OVER SORT
    def sort(self):
        if self.head is None:
            return
        
        sorted_head = self.head
        unsorted_head = self.head.next
        sorted_tail = self.head

        while unsorted_head != self.head:
            current = unsorted_head
            unsorted_head = unsorted_head.next
            if current.data < sorted_head.data:
                current.prev = sorted_tail
                current.next = sorted_head
                sorted_head.prev = current
                sorted_tail.next = current
                sorted_head = current
            else:
                sorted_iter = sorted_head
                while sorted_iter != sorted_tail and current.data > sorted_iter.next.data:
                    sorted_iter = sorted_iter.next
                current.prev = sorted_iter
                current.next = sorted_iter.next
                sorted_iter.next.prev = current
                sorted_iter.next = current
                if sorted_iter == sorted_tail:
                    sorted_tail = current

        self.head = sorted_head

    def isSorted(self): #NO CHANGE BC IM JUST TRAVERSING LIST FOWARDS FAM
        current = self.head
        while current is not None and current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def SortedInsert(self, node):
        if not self.isSorted():
            self.Sort()
        
        if self.head is None or node.data <= self.head.data:
            self.insert_head(node)
        elif node.data >= self.tail.data:
            self.insert_tail(node)
        else:
            current = self.head
            while current.next != self.head and current.next.data < node.data:
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1

        
    def Search(self, node):
        current = self.head
        while current is not None:
            if current == node:
                return current
            current = current.next
        return None

    
    def DeleteHead(self):
        if self.head is None:
            return 
        if self.size == 1: #if just 1 element in CDLL
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head.next.prev = self.tail
            self.tail.next = self.head.next
            self.head = self.head.next
            self.size -= 1



    def DeleteTail(self):
        if self.head is None:
            return 
        if self.size == 1: #if just 1 element in CDLL
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = self.tail.prev
            self.size -= 1
    
    #NGL CHECK OVER
    def Delete(self, node):
        if self.head is None:
            return
        elif self.head == node: 
            return self.delete_head()
        elif self.tail == node:
            return self.delete_tail()
        else:
            current = self.head.next
            while current != self.head:
                if current == node:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    return
                current = current.next
                
    def Clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def Print(self):
        print("List Length:" + self.size)
        print("Sorted Status:" + self.is_sorted())
        if self.head is not None:
            current = self.head
            while True:
                print(current.data, end=" <-> ")
                current = current.next
                if current == self.head:
                    break
            print()
        else:
            print("List is empty")

# def main():
#     # Create a circular doubly linked list and insert nodes
#     cdll = DoublyLinkedList()
#     cdll.SortedInsert(Dnode(5))
#     cdll.SortedInsert(Dnode(2))
#     cdll.SortedInsert(Dnode(9))
#     cdll.SortedInsert(Dnode(1))

#     # Print the unsorted list
#     print("Unsorted list:")
#     cdll.printList()

#     # Sort the list and print it again
#     cdll.Sort()
#     print("Sorted list:")
#     cdll.printList()

# if __name__ == "__main__":
#     main()
