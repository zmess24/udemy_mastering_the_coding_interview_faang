class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        newString = ""

        for char in s: 
            if char in "aeiou" or char in "AEIOU": vowels.append(char)
        
        for char in s:
            if char in "aeiou" or char in "AEIOU":
                newString += vowels.pop()
            else: 
                newString += char

        return newString