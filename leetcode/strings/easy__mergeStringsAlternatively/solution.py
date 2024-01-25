# 1768 Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longest = word1 if len(word1) > len(word2) else word2
        shortest = word1 if len(word1) < len(word2) else word2
        
        mergedWord = ""
        pointer = 0

        while pointer < len(shortest):
            mergedWord += word1[pointer]
            mergedWord += word2[pointer]
            pointer += 1
        

        while pointer < len(longest):
            mergedWord += longest[pointer]
            pointer += 1

        return mergedWord 

        