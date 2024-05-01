# Problem: 287. Find the Duplicate Number
# Link: https://leetcode.com/problems/find-the-duplicate-number/description/

# My Solution 1 - Array as Hashmap:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def trav(prev: int):
            if prev == nums[prev]:
                return prev
            t = nums[prev]
            nums[prev] = prev
            return trav(t)
        return trav(nums[0])

# Analysis:
# Runtime: O(n) - Each index is visited at most once, with single recursive
#                call at every instance
# Memory: O(n) - There can be up to n function calls in memory as this is a 
#                recursive function, along with some overhead due to its recursive
#                nature of the problem.
