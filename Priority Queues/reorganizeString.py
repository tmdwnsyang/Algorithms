# Problem: 767. Reorganize String
# Link: https://leetcode.com/problems/reorganize-string/description/

# My Solution 1 - Using priority queue with duplicates (Beats 5.6%) 
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
# Runtime: O(nlog(n)) - Where n is the total number of characters
# Memory: O(n) - Where n is the total number of characters
# Takeaway - In heapq, the first item in array is the highest priority.
#            You can use this knowledge to perform a peek.

# Solution 2 - Priority queue without duplicates (with a counter)
class Solution:
    def reorganizeString(self, s: str) -> str:
        m = {}
        pq = [(-i, k) for k, i in Counter(s).items()]
        a = []
        heapify(pq)
        while pq:
            first_count, first_chr = heappop(pq)
            if not a or a[-1] != first_chr:
                a.append(first_chr)
                if first_count + 1 != 0:
                    heappush(pq, (first_count + 1, first_chr))
            else:
                if not pq:
                    return ""
                second_count, second_chr = heappop(pq)
                a.append(second_chr)
                if second_count + 1 != 0:
                    heappush(pq, (second_count + 1, second_chr))
                heappush(pq, (first_count, first_chr))
        return ''.join(a)

# Analysis:
# Runtime: O(n*log(k))
#          Where n is the total number of characters, and each heapify takes
#          O(log(k)).     
# Memory: O(k) - Where k is the total number of unique character in pq.
# Takeaway - In heapq, the first item in array is the highest priority.
#            You can use this knowledge to perform a peek in a list.
