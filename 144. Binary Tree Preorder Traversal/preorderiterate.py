# Runtime: 33 ms, faster than 91.56% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.9 MB, less than 60.31% of Python3 online submissions for Binary Tree Preorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        a,b = [],[(root,False)]
        while b:
            c,d = b.pop()
            if d:
                a.append(c.val)
            else:
                if c is not None:
                    b.append((c.right,False))
                    b.append((c.left,False))
                    b.append((c,True))
        return a