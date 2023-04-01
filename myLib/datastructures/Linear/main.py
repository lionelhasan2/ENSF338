from SLL import SLL
from CSLL import CSLL
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

    #testCSLL.SortedInsert(DNode(5))
    testCSLL.InsertHead(DNode(9))
    testCSLL.InsertHead(DNode(12))
    testCSLL.Sort()
    #testCSLL.Print()

   #testCSLL.SortedInsert(DNode(18))

    testCSLL.Print()

    testCSLL.DeleteHead()

    testCSLL.Print()

    testCSLL.DeleteTail()

    testCSLL.Print()



testSLL()

print("Testing CSLL \n")
testCSLL()


