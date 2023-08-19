class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()])
        s = s.lower()
                k = 1
        palindrome = False
        substr = s
        
        while (substr[j+i] == substr[-1 * (k+i)]):
            substr = substr[k+i:-1 * (k+i)]
            if len(substr) < 2:
                return True
            
        return palindrome
