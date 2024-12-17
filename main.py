from AVL import AVLTree
from RB import RedBlackTree
from BT import BinaryTree
import graphics
import random
import sys
sys.setrecursionlimit(100000)
size = [ i*1000 for i in list(range(1, 20))]
#size = [20]
keys = list(range(1, max(size)*2))
#random.shuffle(keys)

avl_h = []
rb_h = []
bt_h = []

for i in size:
    selection = keys[0:i]
    avl_tree = AVLTree()
    bt_tree = BinaryTree()
    rb_tree = RedBlackTree()
    for j in selection:
        avl_tree.insert(j)
        rb_tree.insert(j)
        bt_tree.insert(j)
    avl_h.append(graphics.find_height(avl_tree.root))
    rb_h.append(graphics.find_height(rb_tree.root))
    bt_h.append(graphics.find_height(bt_tree.root))
"""graphics.visualize(avl_tree.root, "avl") 
avl_tree.delete(9) 
graphics.visualize(avl_tree.root, " New tree")"""

graphics.plots(size, avl_h, "AVL") 
graphics.plots(size, rb_h, "Red Black") 
graphics.plots(size, bt_h, "Binary") 

"""graphics.visualize(rb_tree.root, "rb_tree")

print("Postorder traversal")
graphics.postorder_traversal(rb_tree.root)
print("\nInorder traversal")
graphics.inorder_traversal(rb_tree.root)
print("\nPreorder traversal")
graphics.preorder_traversal(rb_tree.root)
print("\nWide traversal")
graphics.wide_traversal(rb_tree.root)"""
"""
graphics.visualize(avl_tree.root, "avl_tree")
graphics.visualize(rb_tree.root, "rb_tree")"""
