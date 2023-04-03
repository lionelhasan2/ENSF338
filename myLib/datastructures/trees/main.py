from nodes.TNode import TNode
import BST

def testBST():
    test = BST()
    root = test.insert(10)
    [x for x in test.breadth_first(root)] #tests printBF



if __name__ == "__main__":

    print("Testing BST \n")
    testBST()
