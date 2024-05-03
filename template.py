# Problem: 116. Populating Next Right Pointers in Each Node
# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

# My Solution:
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        a = []
        def trav(n: 'Optional[Node]', h:int):
            nonlocal a
            if n:
                if h == len(a):
                    a.append([])
                trav(n.left, h + 1)
                a[h].append(n)
                trav(n.right, h + 1)

        trav(root, 0)

        for nodes in a:
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i+1]
        return root

# Analysis: <Runtime complexity analysis & more...>
