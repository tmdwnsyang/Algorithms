# Problem: XXX. <title>
# Link: <link>

# My Solution 1 - Using Queue (beats 18%)
class Solution:
    def countSubstrings(self, s: str) -> int:
        q = deque()
        n = len(s)
        count = n
        for i in range(n-1):
            if s[i] == s[i+1]:
                q.append((i, i+1))
                count += 1
        for i in range(n-2):
            if s[i] == s[i+2]:
                q.append((i, i+2))
                count += 1
        while len(q) > 0:
            x, y = q.popleft()
            if x == 0 or y == n-1:
                continue
            substr = s[x-1:y+2]
            if s[x-1] == s[y+1]:
                count += 1
                q.append((x-1, y+1))
        return count


# Analysis:
# Runtime: O(X) - <Desc>
# Memory: O(X) - <Desc>