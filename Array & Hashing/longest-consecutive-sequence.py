class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        longest = 0
        for i in newSet:
            if (i - 1) not in newSet:
                long = 0
                while (i + long) in newSet:
                    long += 1
                    longest = max(longest, long)
        return longest
