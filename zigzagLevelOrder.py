
# My solution
# Problem: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a = []
        def trav(h: int, n: Optional[TreeNode]):
            nonlocal a
            if n:
                if h == len(a): 
                    a.append(deque())
                trav(h+1, n.left)
                if (h % 2) == 1:
                    a[h].appendleft(n.val)
                else:
                    a[h].append(n.val)
                trav(h+1, n.right)
        trav(0, root)
        return a

# Analysis
# 