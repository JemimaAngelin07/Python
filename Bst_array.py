class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def sorted_array_to_bst(n):
    if not n:
        return None
    mid_val = len(n)//2
    node = TreeNode(n[mid_val])
    node.left = sorted_array_to_bst(n[:mid_val])
    node.right  = sorted_array_to_bst(n[mid_val+1:])
    return node
def preorder(node):
    if not node:
        return 
    print(node.val)
    preorder(node.left)
    preorder(node.right)

result=sorted_array_to_bst([1,2,3,4,5,6,7])
preorder(result)