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


# Solution 2: Using BFS traversal
class Solution:
    def connect(self, r: 'Optional[Node]') -> 'Optional[Node]':
        if r == None:
            return
        q = deque([(r, 0)])
        while len(q) > 0:
            n, lvl = q.pop()
            if len(q) > 0 and q[-1][1] == lvl:
                n.next = q[-1][0]
            if n.left: q.appendleft((n.left, lvl + 1))
            if n.right: q.appendleft((n.right, lvl + 1))
        return r


# Analysis:
# Time complexity: O(n + m) -> O(n), where we process n number of nodes
# Space complexity: O(n), where queue stores maximum of n/2 nodes (at the last
# level), so O(n)
