class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Get length of string
        length = len(s)
        # Initialize set to store characters in (python sets can only contain one of each unique value)
        charSet = set()
        # Initialize sliding window variables (e.g left, right, & maxCount, currentCount)
        left = 0
        right = 0
        maxCount = 0
        currentCount = 0
        # Start 'while' loop (right < length of string)
        while right < length:
            # If current char DOES NOT exist in character set:
            if s[right] not in charSet:
                # Add it to set, 
                charSet.add(s[right])
                # Move right varible forward by 1.
                right += 1
                # Increment currentCount by 1.
                currentCount += 1
            # If current char DOES exist in character set:
            else:
                # Remove char from char set at left index
                charSet.remove(s[left])
                # Move left variable foward by 1
                left += 1
                # Decrement current count by 1
                curentCount -= 1
            # Assign MaxCount to max between currentCount and maxCount
            maxCount = max(maxCount, currentCount)
        
        # Return maxCount
        return maxCount