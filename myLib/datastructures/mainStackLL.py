from Linear.StackLL import StackList;
from nodes.Dnode import DNode;

def main():
    dll = StackList(DNode(0)) #uses the 2nd constructor
    dll.Push(DNode(-5))
    dll.Push(DNode(3))
    dll.insert(DNode(6), 1) #SHOULD WORK
    dll.insert(DNode(6), 2) #SHOULD NOT WORK
    dll.Print()
    print()

    # dll.sort() #SORT DOES NOT WORK
    # dll.Print()
    # dll.SortedInsert(DNode(-1)) #does not work sometimes
    # dll.Print()
    # print()

    # print("Search node with value 7:", dll.Search(DNode(7))) #should return None
    # print("Search node with value 0:", dll.Search(DNode(0))) #should return object
    # print()

    # dll.Pop() 
    # dll.Print() 
    # print()

    # dll.DeleteTail() 
    # dll.Print() #SHOULD PRINT 6,-5,0
    # print()

    # dll.Delete(DNode(-5)) #DOES NOT WORK IF I USE 0 BUT WORKS IF I USE 6
    dll.Print() #SHOULD PRINT 6,0,3
    print()

    # dll.Clear()
    # dll.Print() #NOTHING IN LIST


if __name__ == "__main__":
    main()