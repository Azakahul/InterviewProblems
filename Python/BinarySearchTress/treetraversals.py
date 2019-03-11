# A function to do inorder tree traversal. This will return the values in the order of creation.
def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.val),
        printinorder(root.right)

# A function to do preorder tree traversal. This is normally used when making a copy of a binary search tree
def printpreorder(root):
    if root:
        print(root.val),
        printpreorder(root.left)
        printpreorder(root.right)

# A function to do postorder tree traversal .  This is normally used to delete a binary search tree.
def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.val),