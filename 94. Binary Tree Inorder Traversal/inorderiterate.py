class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a,b = [],[(root,False)]
        while b:
            c,d = b.pop()
            if d:
                a.append(c.val)
            else:
                if c is not None:
                    b.append((c.right,False))
                    b.append((c,True))
                    b.append((c.left,False))
        return a