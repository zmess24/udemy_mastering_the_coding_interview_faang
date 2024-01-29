class Solution:
    def countSubstrings(self, s: str) -> int:
        # Get lenght of string
        n = len(s) + 1
        # Create set to store Palindromes
        palindromes = set()
        # Create count of Palindromes
        count = 0
        # Iterate through first iteration
        for left in range(n):
            # Create second iteration
            for right in range(left+1, n):
                substring = s[left:right]
                # If right - left = 0:
                if right - left == 1:
                    # Check if already palindrome exists:
                    if substring in palindromes:
                    # If it does, Increase count by 1
                        count += 1
                    # else:
                    else: 
                        # Increase count by 1
                        count += 1
                        # Store Palindrome
                        palindromes.add(substring)
                # else:
                else:
                    # Check if palindrome already exists:
                    if substring in palindromes:
                        # If it does, Increase count by 1
                        count += 1
                    # else:
                    else:
                        palindrome = self.checkPalindrome(substring)
                        if palindrome:
                            # Increase count by 1
                            count += 1
                            # Store Palindrome
                            palindromes.add(substring)
        # Return count
        return count

    def checkPalindrome(self, s):
        left = 0
        right = len(s) -1

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True