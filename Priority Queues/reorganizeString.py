# Problem: 767. Reorganize String
# Link: https://leetcode.com/problems/reorganize-string/description/

# My Solution 1 - Using priority queue (Beats 5.6%)
class Solution:
    def reorganizeString(self, s: str) -> str:
        m = {}
        a = []
        for x in s:
            if x not in m:
                m[x] = 0
            m[x] += 1
            a.append((-m[x], x))
        heapify(a)
        ans = f"{heappop(a)[1]}"
        while len(a) > 0:
            t_q = []
            while len(a) > 0 and a[0][1] == ans[-1]:
                t_q.append(heappop(a))
            if len(a) > 0:
                ans = ans + heappop(a)[1]
            else:
                return ""
            for tup in t_q:
                heappush(a, tup)
        return ans

# Analysis:
# Runtime: O(n) - 
# Memory: O(n) - 
# Takeaway - In heapq, the first item in array is the highest priority.
#            You can use this knowledge to perform a peek.
