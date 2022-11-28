# Runtime: 25 ms, faster than 99.10% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.7 MB, less than 96.79% of Python3 online submissions for Binary Tree Postorder Traversal.

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
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]