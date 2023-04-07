import sys
from pathlib import Path
from io import StringIO
import pytest


parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))


from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.trees.BST import BST
from myLib.datastructures.trees.AVL import AVL




def test_BST():
    testTree = BST()
    testNode = TNode(6)
    testTree.Insert(testNode)
    testTree.Insert(4)
    testTree.Insert(9)
    #Testing Breadth First Search after inserting the values 6, 4, and 9:")
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == "Data: 6, Balance: 0\nData: 4, Balance: 0\nData: 9, Balance: 0\n"


    print("Testing  printInOrder:")
    testTree.printInOrder()

    #Testing print in order function 
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printInOrder()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == "Data: 4, Balance: 0\nData: 6, Balance: 0\nData: 9, Balance: 0\n"

    #Testing delete function
    testTree.Insert(2)
    testTree.Insert(5)
    testTree.Insert(7)
    testTree.Insert(11)
    testTree.Insert(1)
    testTree.Insert(3)
    print("Testing delete for the value 5")
    testTree.delete(5)
    print("Testing printBF after inserting 2,5,7,11,1,3 and deleting 5")
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    #assert output == "Data: 6, Balance: 1\nData: 4, Balance: 1\nData: 9, Balance: 0\nData: 2, Balance: 0\nData: 7, Balance: 0\nData: 11, Balance: 0\nData: 1, Balance: 0\nData: 3, Balance: 0"

    print("Testing search on the value 9")
    assert(testTree.search(9))


    print()


    #[x for x in test.breadth_first(root)] #tests printBF

def test_Tnode():
    test = TNode()
    print("Setting data to 10 and balance to 1")
    test.set_data(10)
    test.set_balance(1)
    left = TNode(6)
    right = TNode(15)
    parent = TNode(20)
    test.set_left(left)
    print("Setting left node to " + str(left.get_data()))
    test.set_right(right)
    print("Setting right node to " + str(right.get_data()))
    test.set_parent(parent)
    print("Setting parent node to " + str(parent.get_data()))
    print("Data of testNode: " + str(test.get_data()))
    print("Balance of testNode: " + str(test.get_balance()))
    print("Left Node data: ")
    test.get_left().print()
    print("Right Node data: ")
    test.get_right().print()
    print("Parent Node data: ")
    test.get_parent().print()


def test_BST2():
        testTree = BST()
        testNode = TNode(2)
        testTree.Insert(testNode)
        testTree.Insert(5)
        testTree.Insert(0)
        testTree.Insert(7)
        testTree.Insert(6)


        print("Testing Breadth First Search after inserting the values 6, 4, and 9:")
        testTree.printBF()


def test_AVL():
        testTree = AVL(TNode(2))
        testTree.Insert(5)
        testTree.Insert(0)
        testTree.Insert(7)
        testTree.Insert(6)
        print("Testing Breadth First Search after inserting the values 2, 5, 0, 7, and 6:")
        captured_output = StringIO()
        sys.stdout = captured_output
        captured_output = StringIO()
        sys.stdout = captured_output
        testTree.printBF()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        assert output == "Data: 2, Balance: -1\nData: 0, Balance: 0\nData: 6, Balance: 0\nData: 5, Balance: 0\nData: 7, Balance: 0\n"











if __name__ == "__main__":

    print("Testing BST \n")
    test_BST()
    print("Testing TNode \n")
    test_Tnode()

