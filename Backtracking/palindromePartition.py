# Problem: 131. Palindrome Partitioning
# Link: https://leetcode.com/problems/palindrome-partitioning/description/

# My Solution 1 - DFS traversal with backtracking 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr_str = []
        n = len(s)
        def is_palindrome(p:str):
            i = 0
            j = len(p)-1
            while j > i:
                if p[i] != p[j]:
                    return False
                j -= 1
                i += 1
            return True
        def trav(i: int):
            if i == n:
                ans.append(curr_str[:])
                return
            for x in range(i, n):
                s_str = s[i:x+1]
                if is_palindrome(s_str):
                    curr_str.append(s_str)
                    trav(i+len(s_str))
                    curr_str.pop()
        trav(0)
        return ans
# Analysis:
# Runtime: O(n*2^n) - The DFS traversal generates 2^n number of substrings
#                     and for each substrings, determining whether it is
#                     a palindrome takes O(n) time complexity.
# Memory: O(n) - Where n is the length of the string, which is equivalent
#                to the recursion stack (depth) 


# My Solution 2 - Dynamic Programming
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr_str = []
        n = len(s)
        dp = [[0 for _ in s] for _ in s]

        def trav(start: int):
            if start == n:
                ans.append(curr_str[:])
                return
            for end in range(start, n):
                s_str = s[start:end+1]
                if s[start] == s[end] and (end-start < 2 or dp[start+1][end-1]): 
                    dp[start][end] = 1
                    curr_str.append(s_str)
                    trav(start+len(s_str))
                    curr_str.pop()
        trav(0)
        return ans

# Analysis:
# Runtime: O(n * 2^n) - The DP approach still generates 2^n number of nodes
#                       but eliminates the need to iteratively check if it's
#                       a palindrome or not.
# Memory: O(n^2) - 2d n x n matrix to store the previous palindrome result,
#         plus O(n) recursive stack. O(n^2 + n) = O(n^2)