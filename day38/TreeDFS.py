class TreeNode:
    def __init__(self,val=0,left=None,Right=None):
        self.val=val
        self.left=left
        self.right=Right
def PreorderTraversal(root):
    if root ==None:
        return
    print(root.val,end=" ")
    PreorderTraversal(root.left)
    PreorderTraversal(root.right)    

##    Inorder Traversal
def InorderTraversal(root):
    if root ==None:
        return
    
    InorderTraversal(root.left)
    print(root.val,end=" ")
    InorderTraversal(root.right)
## postorder Travesal
    def PostorderTraversal(root):
        if root ==None:
            return
        
        PostorderTraversal(root.left)
        
        PostorderTraversal(root.right)
        print(root.val,end=" ")

root =TreeNode(1)
root.left=  TreeNode(2)
root.left.left=  TreeNode(4)
root.left.right=  TreeNode(5)
root.left.right.right=  TreeNode(11)
root.left.left.left=  TreeNode(9)
root.left.left.left.right=  TreeNode(10)

root.right=TreeNode(3)
root.right.right=TreeNode(6)
root.right.right.left=TreeNode(7)
root.right.right.right=TreeNode(8)
PreorderTraversal(root)
InorderTraversal(root)
(root)



       
       
            