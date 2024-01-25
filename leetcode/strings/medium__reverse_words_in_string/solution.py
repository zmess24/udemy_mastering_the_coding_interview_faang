class Solution:
    def reverseWords(self, s: str) -> str:
        reversedWord = ""
        split = s.split(' ')[::-1]

        for word in split:
            if word != "":
                reversedWord += word + " "

        return reversedWord.strip()