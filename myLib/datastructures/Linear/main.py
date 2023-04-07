import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))



from SLL import SLL
from CSLL import CSLL
from LLQueue import LLQueue

from LLStack import LLStack
from CDLL import doublyCLL
from DLL import doublyLL

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
    dll = doublyLL(DNode(0)) #uses the 2nd constructor
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    dll.Insert(DNode(6), 1)
    dll.Print() #SHOULD PRINT 6,-5,6,0,3
    print()

    dll.sort()
    dll.Print() #SHOULD PRINT -5,0,3,6,6
    print()

    dll.SortedInsert(DNode(-1))
    dll.Print() #SHOULD PRINT -5,-1,0,3,6,6
    print()

    print("Search node with value 7:", dll.Search(DNode(7))) #should return None
    print("Search node with value 6:", dll.Search(DNode(6))) #should return object
    print()

    dll.DeleteHead() 
    dll.Print() #SHOULD PRINT -1,0,3,6,6
    print()

    dll.DeleteTail() 
    dll.Print() #SHOULD PRINT -1,0,3,6
    print()

    dll.Delete(DNode(0))
    dll.Print() #SHOULD PRINT -1,3,6
    print()

    dll.Clear()
    dll.Print() #NOTHING IN LIST

def testCDLL():
    cdll = doublyCLL(DNode(0))
    cdll.InsertHead(DNode(-5))
    cdll.Insert(DNode(5), 2)
    cdll.InsertTail(DNode(3))
    cdll.Insert(DNode(6), 2)
    cdll.Print()
    print()

    cdll.Sort()
    cdll.Print() #SHOULD PRINT 
    print()

    cdll.SortedInsert(DNode(5))
    cdll.Print() #SHOULD PRINT 
    print()

    print("Search node with value 7:", cdll.Search(DNode(7))) #should return None
    print("Search node with value 3:", cdll.Search(DNode(3))) #should return object
    print()

    cdll.DeleteHead() 
    cdll.Print() #prints  -1, 0, 3, 6, 6
    print()

    cdll.DeleteTail()  #prints  -1, 0, 3, 6
    cdll.Print()
    print()

    cdll.Delete(DNode(5)) #prints -1, 3, 6
    cdll.Print()
    print()

    cdll.Clear()

def testLLStack():
    stack = LLStack(DNode(0)) #uses the 2nd constructor
    stack.Push(DNode(-5))
    stack.Push(DNode(3))
    stack.Insert(DNode(6), 2) #SHOULD NOT WORK
    stack.Print() #3,-5,0
    print()

    stack.Sort() #Should not work
    stack.SortedInsert(DNode(-1)) #should not work
    stack.Print()
    print()

    print("Search node with value 7:", stack.Search(DNode(7))) #should return None
    print("Search node with value 0:", stack.Search(DNode(0))) #should return the object
    print()

    stack.Pop() 
    stack.Print() #should print -5, 0
    print()

    stack.DeleteTail() #should not work
    stack.Delete(DNode(-5)) #Should not work

    stack.Clear()

if __name__ == "__main__":

    print("Testing DLL \n")
    testDLL()
    print()

    print("Testing CDLL \n")
    testCDLL()

    # print("Testing StackLL \n")
    # testLLStack()

    # print("Testing SLL \n")
    # testSLL()

    # print("Testing LLQueue \n")
    # testLLQueue()




