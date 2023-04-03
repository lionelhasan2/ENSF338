import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))


from nodes.TNode import TNode
from BST import BST

def testBST():
    test = BST()
    root = test.insert(10)
    [x for x in test.breadth_first(root)] #tests printBF



if __name__ == "__main__":

   # print("Testing BST \n")
   # testBST()
    print("Testing AVL \n")

