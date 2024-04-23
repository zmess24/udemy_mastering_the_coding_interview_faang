#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def alternatingCharacters(s):
    deletions = 0
    index = 1
    
    while index < len(s):
        if s[index] == s[index-1]:
            deletions += 1
            
        index += 1
    
    return deletions