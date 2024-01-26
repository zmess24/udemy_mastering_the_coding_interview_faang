class Solution:
    # Define a method named characterReplacement that takes a string 's' and an integer 'k' as parameters
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize a dictionary 'alphabets' to store the count of each character in the current window
        alphabets = {}
        
        # Initialize variables for the answer, left pointer, right pointer, and the maximum length
        ans = 0
        left = 0
        right = 0
        max_len = 0

        # Iterate through the string using the right pointer
        for right in range(len(s)):
            # Update the count of the current character in the 'alphabets' dictionary
            alphabets[s[right]] = 1 + alphabets.get(s[right], 0)
            
            # Update 'max_len' with the maximum count of any character in the current window
            max_len = max(max_len, alphabets[s[right]])

            # Check if the current window size minus 'max_len' is greater than 'k'
            if (right - left + 1) - max_len > k:
                # If so, move the left pointer and decrease the count of the character at the left
                alphabets[s[left]] -= 1
                left += 1
            else:
                # If not, update the answer with the maximum window size
                ans = max(ans, (right - left + 1))

        # Return the final answer
        return ans