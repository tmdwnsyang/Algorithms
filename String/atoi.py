# Problem: XXX. <title>
# Link: https://leetcode.com/problems/string-to-integer-atoi/description/

# My Solution 1:

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        index, sign, n, res = 0, 1, len(s), 0
        MAX_INT = (2 ** 31) - 1
        MIN_INT = -(2 ** 31)
        if s[0] == "-":
            sign = -1
            index += 1
        elif s[0] == "+":
            index += 1
        
        while index < n and s[index].isdigit():
            d = int(s[index])
            if res > (MAX_INT // 10) or (res == (MAX_INT // 10) and d > MAX_INT % 10):
                return MAX_INT if sign == 1 else MIN_INT
            res = (res * 10) + d
            index += 1
        return res * sign
        

# Analysis:
# Runtime: O(n) - The total length of the string that is processed
# Memory: O(1) 