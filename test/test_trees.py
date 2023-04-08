from myLib.datastructures.Trees.AVL import AVL
from myLib.datastructures.Trees.BST import BST
from myLib.datastructures.nodes.TNode import TNode
import sys
from pathlib import Path
from io import StringIO
import pytest


parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

def test_TNodeSettersandGetters():
    test = TNode()
    test.set_data(10)
    test.set_balance(1)
    left = TNode(6)
    right = TNode(15)
    parent = TNode(20)
    test.set_left(left)
    test.set_right(right)
    test.set_parent(parent)
    assert test.get_data() == 10 and test.get_balance() == 1 and test.get_left() == left and test.get_right() == right and test.get_parent() == parent


def test_TNodeConstructor():
    test = TNode(10, 1, TNode(20), TNode(6), TNode(15))
    assert test.get_data() == 10 and test.get_balance() == 1 and test.get_left().get_data() == 6 and test.get_right().get_data() == 15 and test.get_parent().get_data() == 20

def test_TnodeToString():
    test = TNode(10, 1, TNode(6), TNode(15), TNode(20))
    assert test.toString() == "10"

def test_TNodePrint():
    test = TNode(10, 1, TNode(6), TNode(15), TNode(20))
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    test.print()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == "Data: 10, Balance: 1\n"


def test_BSTSetRootTnodeChildren():
    testTree = BST()
    testNode = TNode(2)
    testNode.set_left(TNode(1))
    testNode.set_right(TNode(3))
    testNode.get_right().set_right(TNode(4))
    testTree.set_root(testNode)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '2\n1\n3\n4\n'


def test_BSTInsertParamsandBreadthFirst():
    testTree = BST()
    testNode = TNode(6)
    testTree.Insert(testNode)
    testTree.Insert(4)
    testTree.Insert(9)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '6\n4\n9\n'



def test_BSTprintinOrder():
    # Testing print in order function
    testTree = BST()
    testNode = TNode(6)
    testTree.Insert(testNode)
    testTree.Insert(4)
    testTree.Insert(9)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printInOrder()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '4\n6\n9\n'

# Testing delete function for a value that is in the tree

def test_BSTDelete():
    testTree = BST()
    testTree.Insert(2)
    testTree.Insert(5)
    testTree.Insert(7)
    testTree.Insert(11)
    testTree.Insert(1)
    testTree.Insert(3)
    testTree.Delete(5)
    result = testTree.Search(5)
    assert (result == None)


#TODO test delete function for val not in tree

def test_BSTDeleteNone():
    testTree = BST()
    testTree.Insert(2)
    testTree.Insert(5)
    testTree.Insert(7)
    testTree.Insert(11)
    testTree.Insert(1)
    testTree.Insert(3)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.Delete(6)
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == 'The node with value 6 does not exist in the tree.\n'


def test_BSTDeleteMultipleOccurences():
    testTree = BST()
    testTree.Insert(2)
    testTree.Insert(5)
    testTree.Insert(7)
    testTree.Insert(11)
    testTree.Insert(1)
    testTree.Insert(3)
    testTree.Insert(5)
    testTree.Delete(5)
    result = testTree.Search(5)
    assert (result == None)

def test_BSTSearch():
    testTree = BST(TNode(2))
    testNode = TNode(5)
    testTree.Insert(testNode)
    testTree.Insert(0)
    testTree.Insert(7)
    testTree.Insert(6)
    resultNode = testTree.Search(5)
    assert resultNode.get_data() == testNode.get_data()

# Testing AVL search function. This assumes that the search function returns None if the value is not found.
def test_BSTSearchNone():
    testTree = BST(TNode(2))
    testNode = TNode(5)
    testTree.Insert(testNode)
    testTree.Insert(0)
    testTree.Insert(7)
    testTree.Insert(6)
    resultNode = testTree.Search(3)
    assert resultNode == None


def test_BSTInsertTNodeWithChildren():
    testTree = BST()
    testNode = TNode(2)
    testNode.set_left(TNode(1))
    testNode.set_right(TNode(3))
    testNode.get_right().set_right(TNode(4))
    testTree.set_root(4)
    testTree.Insert(testNode)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '4\n2\n1\n3\n4\n'





# Testing AVL constructor & insertion with root value. Tests whether tree is balanced after insertion and whether balance factors are correct. 
# Breadth first search is used to return the state of the tree.

def test_AVLConstructorRootVal():

    testTree = AVL(2)
    testTree.Insert(5)
    testTree.Insert(0)
    testTree.Insert(7)
    testTree.Insert(6)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '2\n0\n6\n5\n7\n'


# Testing AVL constructor & insertion with root node. Tests whether tree is balanced after insertion and whether balance factors are correct.
# PrintInOrder is used to return the state of the tree.

def test_AVLConstructorRootNodeandPrintInOrder():
    testTree = AVL(TNode(2))
    testTree.Insert(5)
    testTree.Insert(0)
    testTree.Insert(7)
    testTree.Insert(6)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printInOrder()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '0\n2\n5\n6\n7\n'





# Testing AVL search function. This assumes that the search function returns the node with the correct data value.
def test_AVLSearch():
    testTree = AVL(TNode(2))
    testNode = TNode(5)
    testTree.Insert(testNode)
    testTree.Insert(0)
    testTree.Insert(7)
    testTree.Insert(6)
    resultNode = testTree.Search(5)
    assert resultNode.get_data() == testNode.get_data()

# Testing AVL search function. This assumes that the search function returns None if the value is not found.
def test_AVLSearchNone():
    testTree = AVL(TNode(2))
    testNode = TNode(5)
    testTree.Insert(testNode)
    testTree.Insert(0)
    testTree.Insert(7)
    testTree.Insert(6)
    resultNode = testTree.Search(3)
    assert resultNode == None


# Testing get root function


def test_AVLGetRoot():
    test_Tnode = TNode(2)
    testTree = AVL(test_Tnode)
    returnedNode = testTree.get_root()
    assert returnedNode == test_Tnode


def test_AVLSetRoot():
    testTree = AVL()
    testTree.set_root(2)
    testTree.Insert(5)
    testTree.Insert(0)
    testTree.Insert(7)
    testTree.Insert(6)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printInOrder()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '0\n2\n5\n6\n7\n'


# Testing if setting root node to a tnode with children works. This assumes that the left and right children of the tnode are correctly placed as well.
def test_AVLSetRootTnodeChildren():
    testTree = AVL()
    testNode = TNode(2)
    testNode.set_left(TNode(1))
    testNode.set_right(TNode(3))
    testNode.get_right().set_right(TNode(4))
    testTree.set_root(testNode)
    print("Testing Breadth First Search after setting root node to a TNode with children 1 and 3:")
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '2\n1\n3\n4\n'


def test_AVLConstructorRootTnodeChildrenandBreadthFirst():

    testNode = TNode(2)
    testNode.set_left(TNode(1))
    testNode.set_right(TNode(3))
    testNode.get_right().set_right(TNode(4))
    testTree = AVL(testNode)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '2\n1\n3\n4\n'

def test_AVLInsertTNodeWithChildren():
    testTree = AVL()
    testNode = TNode(2)
    testNode.set_left(TNode(1))
    testNode.set_right(TNode(3))
    testNode.get_right().set_right(TNode(4))
    testTree.set_root(4)
    testTree.Insert(testNode)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == '2\n1\n4\n3\n4\n'


def test_AVLDeleteNode():
    testTree = AVL()
    testTree.Insert(2)
    testTree.Insert(1)
    testTree.Insert(3)
    testTree.Insert(4)
    testTree.Delete(3)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.printBF()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    result = testTree.Search(3)
    assert (result == None)
    assert output == '2\n1\n4\n'


def test_AVLDeleteNodeNone():
    testTree = AVL()
    testTree.Insert(2)
    testTree.Insert(1)
    testTree.Insert(3)
    testTree.Insert(4)
    testTree.Delete(5)
    captured_output = StringIO()
    sys.stdout = captured_output
    captured_output = StringIO()
    sys.stdout = captured_output
    testTree.Delete(0)
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == 'The node with value 0 does not exist in the tree.\n'