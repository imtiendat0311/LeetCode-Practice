# Faster than 93.09% online python3 submission
# Less mem than 13.90% online python3 submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        a,_,_= self.something(root)
        return a 
    def something(self,root: Optional[TreeNode]):
        if root is None:
            return True,float("inf"),-float("inf")
        if root.left is None and root.right is None:
            return True,root.val,root.val
        isleftBST,leftSubMin,leftSubMax = self.something(root.left)
        isrightBST,rightSubMin,rightSubMax = self.something(root.right)
        if isleftBST and isrightBST and leftSubMax<root.val<rightSubMin:
            return True,min(leftSubMin,root.val),max(rightSubMax,root.val)
        return False,None,None  