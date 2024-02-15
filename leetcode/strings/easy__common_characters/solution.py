def commonCharacters(strings):
    if len(strings) == 1: return list(strings)
    hashMap = {}
    ans = []
    
    for string in strings:
        for char in set(string): # Convert string to set to get only unique characters and ignore multiplicty
            if char in hashMap:
                hashMap[char] += 1
                if hashMap[char] == len(strings):
                    ans.append(char)
            else:
                hashMap[char] = 1

    return ans
