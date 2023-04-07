import sys
from pathlib import Path
from io import StringIO
import pytest


parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from myLib.datastructures.nodes.Dnode import DNode
from myLib.datastructures.Linear.SLL import SLL
from myLib.datastructures.Linear.DLL import doublyLL
from myLib.datastructures.Linear.CSLL import CSLL
from myLib.datastructures.Linear.CDLL import doublyCLL
from myLib.datastructures.Linear.LLStack import LLStack
from myLib.datastructures.Linear.LLQueue import LLQueue

from io import StringIO
import sys

def test_SLL():

    # print("Testing no node constructor, InsertTail, InsertHead, Insert, Print")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    testsll = SLL()
    testsll.InsertTail(DNode(3))
    testsll.InsertHead( DNode(6))
    testsll.Insert(DNode(2), 2)
    testsll.InsertHead(DNode(2))
    testsll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List size: 4\nSorted: No\nList content: 1 6 2 3 \n"

    # print("Testing sort and sortInsert")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    # testsll.Sort()
    # testsll.SortedInsert(DNode(5))
    # testsll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List size: 5\nSorted: Yes\nList content: 1 2 3 5 6 \n"

    # print("Testing deleteHead, deleteTail, delete")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    # testsll.DeleteHead()
    # testsll.DeleteTail()
    testsll.Delete(DNode(2)) #DOESNT WORK RN
    testsll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List size: 5\nSorted: Yes\nList content: 2 5 \n"

    # print("Testing search")
    # if(testsll.Search(DNode(2))): #THIS DOES NOT WORK
    #     print("Search function for the node with value 2  was successful")
    # else:
    #     print("Search function for the node with value 2  was unsuccessful")

    # testsll.Clear()

def test_DLL():

    print("Testing given node constructor, InsertTail, InsertHead, Insert, Print")
    captured_output = StringIO()
    sys.stdout = captured_output
    dll = doublyLL(DNode(0)) 
    dll.InsertHead(DNode(-5))
    dll.Insert(DNode(6), 2)
    dll.InsertTail(DNode(3))
    dll.Insert(DNode(6), 1)
    dll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 5\nSorted: False\nList content: 6 -5 6 0 3 \n"

    print("Testing sort and sortInsert")
    captured_output = StringIO()
    sys.stdout = captured_output
    dll.Sort()
    dll.SortedInsert(DNode(5))
    dll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 6\nSorted: True\nList content: -5 0 3 5 6 6 \n"

    print("Testing deleteHead, deleteTail, delete")
    captured_output = StringIO()
    sys.stdout = captured_output
    dll.DeleteHead()
    dll.DeleteTail()
    dll.Delete(DNode(6)) 
    dll.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 3\nSorted: True\nList content: 0 3 5 \n"

    print("Testing search")
    if(dll.Search(DNode(0))): #NGL IDK IF ITS SUPPOSED TO RETURN OBJECT OR SUCCESSFUL
        print("Search function for the node with value 0  was successful")
        print(dll.Search(DNode(0)))
    else:
        print("Search function for the node with value 0  was unsuccessful")

    dll.Clear()

def test_CSLL():
    # print("Testing given node constructor, InsertTail, InsertHead, Insert, Print")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    csll = doublyLL(DNode(2)) 
    csll.InsertHead(DNode(-5))
    csll.InsertTail(DNode(10))
    csll.Insert(DNode(10), 1)
    csll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List size: 4\nSorted: False\nList content: 10 -5 2 3 \n"

    # print("Testing sort and sortInsert")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    # csll.Sort()
    # csll.SortedInsert(DNode(20))
    # csll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List size: 5\nSorted: True\nList content: -5 2 3 10 20 \n"

    # print("Testing deleteHead, deleteTail, delete")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    # csll.DeleteHead()
    # csll.DeleteTail()
    csll.Delete(DNode(10))
    csll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List size: 2\nSorted: True\nList content: 2 10 \n"

    # print("Testing search")
    # if(csll.Search(DNode(2))): #NGL IDK IF ITS SUPPOSED TO RETURN OBJECT OR SUCCESSFUL
    #     print("Search function for the node with value 0  was successful")
    #     print(csll.Search(DNode(2)))
    # else:
    #     print("Search function for the node with value 0  was unsuccessful")

    # csll.Clear()

def test_CDLL():
    # print("Testing given node constructor, InsertTail, InsertHead, Insert, Print")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    cdll = doublyCLL(DNode(0))
    cdll.InsertHead(DNode(-5))
    cdll.Insert(DNode(5), 2)
    cdll.InsertTail(DNode(3))
    cdll.Insert(DNode(6), 2)
    cdll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List Length: 5\nSorted Status: False\nList Content: -5 6 5 0 3 \n"

    # print("Testing sort and sortInsert")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    # cdll.Sort()
    # cdll.SortedInsert(DNode(-100))
    # cdll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List Length: 6\nSorted Status: True\nList Content: -100 -5 0 3 5 6 \n"

    # print("Testing deleteHead, deleteTail, delete")
    # captured_output = StringIO()
    # sys.stdout = captured_output
    # cdll.DeleteHead()
    # cdll.DeleteTail()
    cdll.Delete(DNode(5))
    cdll.Print()
    # output = captured_output.getvalue()
    # sys.stdout = sys.__stdout__
    # print(output)
    # assert output == "List Length: 3\nSorted Status: True\nList Content: -5 0 5 \n"

    # print("Testing search")
    # if(cdll.Search(DNode(2))): #NGL IDK IF ITS SUPPOSED TO RETURN OBJECT OR SUCCESSFUL
    #     print("Search function for the node with value 0  was successful")
    #     print(cdll.Search(DNode(2)))
    # else:
    #     print("Search function for the node with value 0  was unsuccessful")

    # cdll.Clear()

def test_LLStack():
    print("Testing given node constructor, InsertTail, InsertHead, Insert, Print")
    captured_output = StringIO()
    sys.stdout = captured_output
    stack = LLStack(DNode(0)) 
    stack.Push(DNode(-5))
    stack.Push(DNode(3))
    stack.Insert(DNode(6), 2) #Should not work
    stack.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 3\nSorted: No\nList content: 3 -5 0 \n"

    stack.Sort() #Should not work
    stack.SortedInsert(DNode(-1)) #should not work
    stack.DeleteTail() #should not work
    stack.Delete(DNode(-5)) #Should not work

    print("Testing Pop")
    captured_output = StringIO()
    sys.stdout = captured_output
    stack.Pop() 
    stack.Print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    print(output)
    assert output == "List size: 2\nSorted: Yes\nList content: -5 0 \n"

    print("Testing search")
    if(stack.Search(DNode(-5))): #NGL IDK IF ITS SUPPOSED TO RETURN OBJECT OR SUCCESSFUL
        print("Search function for the node with value 0  was successful")
        print(stack.Search(DNode(-5)))
    else:
        print("Search function for the node with value 0  was unsuccessful")

    stack.Clear()


def test_LLQueue():
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

if __name__ == "__main__":
    # print("TESTING SLL \n")
    # test_SLL()
    # print()

    # print("TESTING DLL \n")
    # test_DLL()
    # print()

    print("TESTING CSLL \n")
    test_CSLL()
    print()

    # print("TESTING CDLL \n")
    # test_CDLL()
    # print()

    # print("TESTING StackLL \n")
    # test_LLStack()
    # print()

    # print("TESTING LLQueue \n")
    # test_LLQueue()
