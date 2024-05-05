# Problem: 3111. Minimum Rectangles to Cover Points
# Link: https://leetcode.com/problems/minimum-rectangles-to-cover-points/description/

# My Solution 1 - Using binary search (Beats 94.33% | 91.20%)
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        l = sorted([x for x, _ in points])
        n = len(l)
        start = 0
        count = 0
        while start < n:
            n_start = bisect_right(l, l[start] + w, start)
            count += 1
            if n_start == n:
                break
            start = n_start
        return count

# Analysis:
# Runtime: O(nlog(n)) - Using binary search, including creation and search
# Memory: O(n) - Where n is the number of x coordinates
# Takeaway - Use binsect_right to find the rightmost item that is 