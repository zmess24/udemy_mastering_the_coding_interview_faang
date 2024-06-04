from collections import Counter

def minimumCharactersForWords(words):
    if len(words) == 0: return []
    # Create hashmap every character count
    hashMap = {}
    # Loop over every word in words list:
    for word in words:
        # Get character count of current word using defaultDict
        charCounts  = Counter(list(word))
        # Loop through dict of current word:
        for char in charCounts:
            # If char in hashMap and count is <= hashMap[char]
            if char in hashMap and charCounts[char] <= hashMap[char]:
                # continue
                continue
            # If char in hashMap and count is > hashMap[char]
            elif char in hashMap and charCounts[char] > hashMap[char]:
                # Add the difference between count and hashMap[char] to hashMap[char]
                hashMap[char] += (charCounts[char] - hashMap[char])
            # If not in hashMap
            else:
                # Add to hashMap[char] = count
                hashMap[char] = charCounts[char]

        # Create ans array
        ans = []
        # Loop through hashMap:
        for char, count in hashMap.items():
            # For each char, add char * the count to ans array
            for i in range(count): ans.append(char)
    # Return ans array
    return ans