# 90. Subsets II
# Link: https://leetcode.com/problems/subsets-ii/description/

# My Solution 1 - Backtracking
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        a = []
        s = set()
        nums.sort()
        def trav(h:int):
            nonlocal a
            nonlocal s
            if h == len(nums):
                s.add(tuple(a))
                return
            trav(h+1)
            a.append(nums[h])
            trav(h+1)
            a.pop()
        trav(0)
        return s

# Analysis:
# Runtime: O(nlog(n)) + O(n*2^n) = O(n*2^n) 
#          Where n is the total number of items in nums.
#          Before the subset is placed into the answer, deep copy is performed
#          when casting array to a tuple. Hence, we have n * 2^n.
# Memory: O(n) - Linear memory for storing items in the set