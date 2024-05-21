# Problem: 695. Max Area of Island
# Link: https://leetcode.com/problems/max-area-of-island/description/

# My Solution 1 - Recursive DFS solution
class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        n = len(g)
        m = len(g[0])
        c = 0
        mx = 0
        def trav(i: int, j: int) -> int:
            nonlocal c
            if g[i][j] == 1:
                c += 1
                g[i][j] = 0
                if i > 0: trav(i-1, j)
                if j < m-1: trav(i, j+1)
                if i < n-1: trav(i+1, j)
                if j > 0: trav(i, j-1)
            
        for i in range(n):
            for j in range(m):
                trav(i, j)
                mx = max(mx, c)
                c = 0
        return mx
            

# Analysis:
# Runtime: O(n * m) - We visit every square once
#                     The DFS is only initiated from cells that are part of an unvisited island
# Memory: O(n * m) - The recursive nature of this solution requires n*m stack calls
#                    in the worst case scenario, where the island itself is n*m sized.