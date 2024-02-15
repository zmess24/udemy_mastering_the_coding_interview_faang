class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" and t == "": return True
        if t == "": return False
        if s == "": return True

        sPointer = 0
        tPointer = 0

        while tPointer < len(t):
            if t[tPointer] == s[sPointer]:
                sPointer += 1
                if sPointer == len(s):
                    return True

            tPointer += 1
        
        return False

