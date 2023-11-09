class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
def is_bst(root):
    stack=[]
    prev=None

    while stack or root:
        while root:
            stack.append(root)
            root=root.left
        root=stack.pop()
        if prev and root.val <= prev.val:
            return False
        prev=root
        root=root.right
    return True

root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)

result=is_bst(root)
print(result)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)

result=is_bst(root)
print(result)