from SLL import SLL
from CSLL import CSLL
from LLQueue import LLQueue

from LLStack import StackList
from CDLL import CircularDoublyLinkedList
from DLL import DoublyLinkedList

from nodes.Dnode import DNode




def testSLL():
    testSLL = SLL()
    testSLL.InsertTail(DNode(3))
    testSLL.InsertHead( DNode(6))
    testSLL.SortedInsert(DNode(2))
    testSLL.Print()
    testSLL.InsertHead(DNode(1))
    testSLL.Sort()
    testSLL.Print()

    testSLL.SortedInsert(DNode(5))
    testSLL.InsertHead(DNode(9))
    testSLL.InsertHead(DNode(12))
    testSLL.Print()

    testSLL.SortedInsert(DNode(18))

    testSLL.Print()

    testSLL.DeleteHead()

    testSLL.Print()

    testSLL.DeleteTail()

    testSLL.Print()

def testCSLL():
    testCSLL = CSLL()
    
    testCSLL.InsertHead(DNode(6))
    
    testCSLL.Print()
    testCSLL.InsertHead(DNode(1))
    testCSLL.Print()

    testCSLL.SortedInsert(DNode(5))
    testCSLL.InsertHead(DNode(9))
    testCSLL.InsertHead(DNode(12))
    testCSLL.Sort()
    testCSLL.Print()

    testCSLL.SortedInsert(DNode(18))

    testCSLL.Print()

    testCSLL.DeleteHead()

    testCSLL.Print()

    testCSLL.DeleteTail()

    testCSLL.Print()

def testLLQueue():
    testLLQueue = LLQueue()
    testLLQueue.enqueue(DNode(3))
    testLLQueue.enqueue(DNode(6))
    testLLQueue.enqueue(DNode(2))
    testLLQueue.Print()
    testLLQueue.enqueue(DNode(1))
    testLLQueue.enqueue(DNode(5))
    testLLQueue.enqueue(DNode(9))
    testLLQueue.enqueue(DNode(12))
    testLLQueue.Print()
    print("Dequeueing: " + str(testLLQueue.dequeue())+"\n")
    print("Dequeueing: " + str(testLLQueue.dequeue())+"\n")
    testLLQueue.Print()

def testDLL():
    dll = DoublyLinkedList(DNode(0)) #uses the 2nd constructor
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    dll.Insert(DNode(6), 1)
    dll.Print() #SHOULD PRINT 6,-5,6,0,3
    print()

    dll.sort()
    dll.Print() #SHOULD PRINT -5,0,3,6,6
    print()

    # dll.SortedInsert(DNode(-1))
    # dll.Print() #SHOULD PRINT -5,-1,0,3,6,6
    # print()

    # print("Search node with value 7:", dll.Search(DNode(7))) #should return None
    # print("Search node with value 6:", dll.Search(DNode(6))) #should return object
    # print()

    # dll.DeleteHead() 
    # dll.Print() #SHOULD PRINT -1,0,3,6,6
    # print()

    # dll.DeleteTail() 
    # dll.Print() #SHOULD PRINT -1,0,3,6
    # print()

    # dll.Delete(DNode(0))
    # dll.Print() #SHOULD PRINT -1,3,6
    # print()

    # dll.Clear()
    # dll.Print() #NOTHING IN LIST

def testCDLL():
    dll = CircularDoublyLinkedList(DNode(0))
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    dll.Insert(DNode(6), 1)
    dll.Print() #prints 6, -5, 6, 0, 3
    print()

    # dll.sort()
    # dll.Print() #SHOULD PRINT 
    # print()

    # dll.SortedInsert(DNode(-1))
    # dll.Print() #SHOULD PRINT 
    # print()

    # print("Search node with value 7:", dll.Search(DNode(7))) #should return None
    # print("Search node with value 0:", dll.Search(DNode(0))) #should return object
    # print()

    # dll.DeleteHead() 
    # dll.Print() #prints  -5, 6, 0, 3
    # print()

    # dll.DeleteTail()  #prints  -5, 6, 0
    # dll.Print()
    # print()

    # dll.Delete(DNode(0)) #NEEDS FIXING
    # dll.Print()
    # print()

    # dll.Clear()
    # dll.Print()

def testLLStack():
    dll = StackList(DNode(0)) #uses the 2nd constructor
    dll.Push(DNode(-5))
    dll.Push(DNode(3))
    dll.Insert(DNode(6), 1) #SHOULD NOT WORK
    dll.Insert(DNode(6), 2) #SHOULD NOT WORK
    dll.Print() #3,-5,0
    print()

    dll.Sort() #Should not wokr
    dll.SortedInsert(DNode(-1)) #should not work

    print("Search node with value 7:", dll.Search(DNode(7))) #should return None
    print("Search node with value 0:", dll.Search(DNode(0))) #should return the object
    print()

    dll.Pop() 
    dll.Print() #should print -5, 0
    print()

    dll.DeleteTail() 
    dll.Delete(DNode(-5)) #Should not work
    print()

    dll.Clear()
    dll.Print() #NOTHING IN LIST



if __name__ == "__main__":




    print("Testing LLQueue \n")
    testLLQueue()




