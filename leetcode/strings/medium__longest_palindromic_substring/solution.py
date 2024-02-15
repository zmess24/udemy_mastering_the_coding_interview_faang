def longestPalindromicSubstring(string):
    if string == string[::-1]: return string

    n = len(string)
    maxLongest = [0,1]

    for i in range(1,n):
        odd = checkPalindrome(i-1, i+1, string)
        even = checkPalindrome(i-1, i, string)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        maxLongest = max(maxLongest, longest, key = lambda x: x[1] - x[0])
        
    return string[maxLongest[0]:maxLongest[1]]

def checkPalindrome(left, right, s):
    while 0 <= left and right <= len(s)-1:
        if s[left] != s[right]:
            break
        
        left -= 1
        right += 1

    return [left+1, right]
        