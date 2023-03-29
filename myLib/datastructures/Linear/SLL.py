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

    def is_sorted(self):
        if not self.head:
            return True  # an empty list is sorted
        curr = self.head
        while curr.next:
            if curr.next.val < curr.val:
                return False
            curr = curr.next
        return True


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

    def insert(self, node, position):
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

    def getNextNode(self, node):
        return node.next

    def getLastNode(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node
    

    def DeleteHead(self):

        if self.head is None:
            return 
        else:
            node = self.head.next
            self.head = node
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
        if self.head is None:
            return
        else:
            self.head = None
            self.tail = None

    def Print(self):
        current_node = self.head
        print("The size of the singly linked list is:" +self.size)
        print("The singly linked list is sorted:" + self.is_sorted())
        while current_node is not None:
            print("The value of the node is:" + current_node.data)
            current_node = current_node.next

    