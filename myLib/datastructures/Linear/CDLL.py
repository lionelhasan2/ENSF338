
class CircularDoublyLinkedList:

    def __init__(self, node=None):
        self.head = node 
        self.size = 1 if node else 0
        self.tail = node

    def InsertHead(self, new_node):
        if self.head is None: #if it is empty DLL
            self.head = new_node
            self.tail = new_node
            self.next = new_node
            self.prev = new_node
        else: #if there it is not empty
            new_node.next = self.head 
            new_node.prev = self.tail
            self.head.prev = new_node 
            self.tail.next = new_node
            self.head = new_node
        self.size += 1

    def InsertTail(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.next = new_node
            self.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    #CHECK OVER NGL
    def Insert(self, new_node, position):
        if position == 1:
            self.InsertHead(new_node)
        elif position == self.size + 1:
            self.InsertTail(new_node)
        elif 1 < position <= self.size:
            curr_node = self.head
            for i in range(1, position - 1): #loop till find pos want add
                curr_node = curr_node.next #CURR_NODE IS AT SPOT WANT NEW_NODE TO BE
            new_node.next = curr_node.next 
            new_node.prev = curr_node
            curr_node.next = new_node
            curr_node.next.prev = new_node 
            self.size += 1
        else:
            raise ValueError("Invalid position")

    # CHECK OVER SORT
    # def sort(self):
    #     if self.head is None:
    #         return
        
    #     sorted_head = self.head
    #     unsorted_head = self.head.next
    #     sorted_tail = self.head

    #     while unsorted_head != self.head:
    #         current = unsorted_head
    #         unsorted_head = unsorted_head.next
    #         if current.val < sorted_head.val:
    #             current.prev = sorted_tail
    #             current.next = sorted_head
    #             sorted_head.prev = current
    #             sorted_tail.next = current
    #             sorted_head = current
    #         else:
    #             sorted_iter = sorted_head
    #             while sorted_iter != sorted_tail and current.val > sorted_iter.next.val:
    #                 sorted_iter = sorted_iter.next
    #             current.prev = sorted_iter
    #             current.next = sorted_iter.next
    #             sorted_iter.next.prev = current
    #             sorted_iter.next = current
    #             if sorted_iter == sorted_tail:
    #                 sorted_tail = current

    #     self.head = sorted_head

    def isSorted(self): #NO CHANGE BC IM JUST TRAVERSING LIST FOWARDS FAM
        current = self.head
        while current != self.tail:
            if current.val > current.next.val:
                return False
            current = current.next
        return True

    # def SortedInsert(self, node):
    #     if (self.isSorted() != True):
    #         self.sort()
    #     if self.head is None: # The list is empty, so insert the node at the beginning
    #         self.head = node
    #         self.tail = node
    #         self.prev = node
    #         self.next = node
    #         self.size += 1
    #         return
    #     elif self.head.val >= node.val: # The new node should be inserted at the beginning
    #         self.insertHead(node)
    #         return
    #     elif self.tail.val <= node.val: # The new node should be inserted at the end
    #         self.insertTail(node)
    #         return
    #     else:  # Find the proper position to insert the new node
    #         current = self.head
    #         while current.next is not None and current.next.val < node.val:
    #             current = current.next
    #         node.next = current.next
    #         node.prev = current
    #         current.next.prev = node
    #         current.next = node
    #         self.size += 1


    def Search(self, node):
        current = self.head
        while current.next != self.head:
            if current.val == node.val:
                return current
            current = current.next
        return None
    
    def DeleteHead(self):
        if self.head is None:
            return 
        if self.size == 1: #if just 1 element in CDLL
            self.head = None
            self.tail = None
            self.prev = None
            self.next = None
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
            self.prev = None
            self.next = None
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
        elif self.head.val == node.val: 
            return self.DeleteHead()
        elif self.tail.val == node.val:
            return self.DeleteTail()
        else:
            current = self.head
            while current != self.tail:
                if current.val == node.val:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    return
                current = current.next
            print("Node is not found in exisitng list")   
                
    def Clear(self):
        self.head = None
        self.tail = None
        self.prev = None
        self.next = None
        self.size = 0
    
    def Print(self):
        print("List Length:", self.size)
        print("Sorted Status:", self.isSorted())
        if self.head is not None:
            current = self.head
            print("List Content:", end=" ")
            while True:
                print(current.val, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()
        else:
            print("List is empty")