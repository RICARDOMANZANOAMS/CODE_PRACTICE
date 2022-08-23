#Inheritance
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#the class solution inherits all the values and properties from TreeNode.
#Since we do not include __init__ in solution class,
#the class solution inherits the init from treenode. For this reason, 
#we initialize solution class as the treenode class a=Solution(3)

#In the class solution, we extend the class treenode adding an extra function.
#Since we pass self, we can use all the values that we create before for the treenode class
class Solution(TreeNode):
    def checkTree(self, root):
        print(self.val)
        print(self.right)
        print(self.left)
        print("he")
        print(root)

a=Solution(3)
a.checkTree(4)
