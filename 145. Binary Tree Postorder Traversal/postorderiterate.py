# Runtime: 33 ms, faster than 91.92% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.8 MB, less than 60.40% of Python3 online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        a,b = [],[(root,False)]
        while b:
            c,d = b.pop()
            if d:
                a.append(c.val)
            else:
                if c is not None:
                    b.append((c,True))
                    b.append((c.right,False))
                    b.append((c.left,False))
        return a