class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if target length > s length: return ""
        if len(t) > len(s): return ""
        # if s == t: return s
        if s == t: return s
        # Initiate start index, end index, answer
        startIndex = 0
        endIndex = 0
        ans = ""
        # Create charsToGo list, index queue, target length
        charsToGo = list(s)
        charQueue = []
        n = len(t)
        # Begin first iteration;
        for index, char in enumerate(s):
            # If char in target string:
            if char in t:
                # Add index to index queue
                charQueue.append(index)
                # if charsToGo length == target legnth:
                if len(charsToGo) == n:
                    # StartIndex = index
                    startIndex = index
                # pop char from charsToGo list
                charsToGo.pop(char)
                # if 'charsToGo' list == 0:
                if len(charsToGo) == 0:
                    # End index = index
                    endIndex = index
                    # break loop
                    break

        
        # answer = s[startIndex:endIndex]

        # Iterate through indexQueue:

            # Reset start index, end index, charsToGo

             # Begin iteration through string starting at current index;

                # If char in charsToGo:

                    # if charsToGo length == target legnth:

                        # startIndex = index

                    # pop char from charsToGo list

                    # if 'charsToGo' list == 0:

                        # endIndex = index

                        # s[startIndex:endIndex] length < ans length:

                            # answer = s[startIndex:endIndex]

                        # break loop
        
        # Return ans