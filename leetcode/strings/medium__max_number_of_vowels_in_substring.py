class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_window, curr_window = 0, 0

        while right < len(s):
            char = s[right]
            
            if char in 'aeiou':
                curr_window += 1
            
            if (right - left + 1) > k:
                if s[left] in 'aeiou':
                    curr_window -= 1
                left += 1

            max_window = max(max_window, curr_window)
            right +=1

        return max_window