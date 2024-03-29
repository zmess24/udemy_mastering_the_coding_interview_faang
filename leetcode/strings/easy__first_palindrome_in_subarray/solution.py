class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        
        return ""

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
        
            left += 1
            right -= 1

        return True