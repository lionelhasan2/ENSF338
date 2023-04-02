from Linear.CDLL import CircularDoublyLinkedList;
from nodes.Dnode import DNode;

def main():
    dll = CircularDoublyLinkedList(DNode(0)) #uses the 2nd constructor
    dll.insertHead(DNode(-5))
    dll.insert(DNode(6), 2)
    dll.insertTail(DNode(3))
    dll.insert(DNode(6), 1)
    dll.Print() #SHOULD PRINT 6,-5,6,0,3
    print()

    # dll.sort()
    # dll.Print() #SHOULD PRINT 
    # print()

    # dll.SortedInsert(DNode(-1))
    # dll.Print() #SHOULD PRINT 
    # print()

    print("Search node with value 7:", dll.Search(DNode(7))) #should return None
    print("Search node with value 0:", dll.Search(DNode(0))) #should return object
    print()

    dll.DeleteHead() 
    dll.Print() #SHOULD PRINT -5,6,0,3
    print()

    dll.DeleteTail() 
    dll.Print() #SHOULD PRINT -5,6,0
    print()

    dll.Delete(DNode(0))
    dll.Print() #SHOULD PRINT  -5, 6
    print()

    dll.Clear()
    dll.Print() #NOTHING IN LIST


if __name__ == "__main__":
    main()