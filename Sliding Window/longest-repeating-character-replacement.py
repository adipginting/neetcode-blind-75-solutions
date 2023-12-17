class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        left = 0
        result = 0
        mostChar = 0
        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0) + 1
            mostChar = max(mostChar, chars[s[right]])
            while (right - left + 1) - mostChar > k:
                chars[s[left]] = chars[s[left]] - 1
                left += 1
            result = max(result, right - left + 1)
        return result
