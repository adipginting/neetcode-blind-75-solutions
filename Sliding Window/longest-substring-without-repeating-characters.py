class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        left = 0
        right = 0
        maxLength = 0


        for right in range(len(s)):
            while s[right] in stringSet:
                stringSet.remove(s[left]) # remove duplicate value that is in stringSet. So, there's potentially some characters removed up until the value of s[left] == s[right]
                left += 1 # update left index value until s[left] != s[right]
            stringSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength
