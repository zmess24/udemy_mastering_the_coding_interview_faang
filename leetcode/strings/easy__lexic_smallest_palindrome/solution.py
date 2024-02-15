class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        alpha ='abcdefghijklmnopqrstuvwxyz'
        word = list(s)

        while (left < right):
            if word[left] != word[right]:
                if alpha.index(word[left]) < alpha.index(word[right]):
                    word[right] = word[left]
                else:
                    word[left] = word[right]

            left += 1
            right -= 1

        return "".join(word)
